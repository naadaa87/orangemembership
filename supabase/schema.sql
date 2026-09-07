-- ═══════════════════════════════════════════════════════════
--  HMK 오렌지 멤버십 — 사전 알림 신청 백엔드
--  Supabase SQL Editor 에 그대로 붙여넣고 실행하십시오.
--  프로젝트 리전은 Northeast Asia (Seoul) 을 권장합니다.
-- ═══════════════════════════════════════════════════════════

-- ── 1. 신청 테이블 ─────────────────────────────────────────
create table if not exists public.membership_leads (
  id          bigint generated always as identity primary key,
  name        text        not null,
  phone       text        not null,
  region      text,
  interest    text,
  memo        text,
  marketing   boolean     not null default false,
  status      text        not null default 'new',
  source      text        not null default 'web',
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now(),

  -- 입력값 방어 (프런트 검증만 믿지 않습니다)
  constraint  chk_name     check (char_length(name)  between 2 and 40),
  constraint  chk_phone    check (phone ~ '^01[0-9]{8,9}$'),
  constraint  chk_region   check (region   is null or char_length(region)   <= 40),
  constraint  chk_interest check (interest is null or char_length(interest) <= 200),
  constraint  chk_memo     check (memo     is null or char_length(memo)     <= 1000),
  constraint  chk_status   check (status in ('new','contacted','hold','done','spam'))
);

comment on table  public.membership_leads is 'HMK 오렌지 멤버십 사전 알림 신청';
comment on column public.membership_leads.status   is 'new 신규 / contacted 연락완료 / hold 보류 / done 처리완료 / spam 스팸';
comment on column public.membership_leads.interest is '쉼표 구분: market,storage,live,biz,partner';

create index if not exists idx_leads_created on public.membership_leads (created_at desc);
create index if not exists idx_leads_status  on public.membership_leads (status);
create index if not exists idx_leads_region  on public.membership_leads (region);
create unique index if not exists uq_leads_phone on public.membership_leads (phone);


-- ── 2. updated_at 자동 갱신 ────────────────────────────────
create or replace function public.touch_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_leads_touch on public.membership_leads;
create trigger trg_leads_touch
  before update on public.membership_leads
  for each row execute function public.touch_updated_at();


-- ── 3. 행 수준 보안 ────────────────────────────────────────
alter table public.membership_leads enable row level security;

-- 홈페이지 방문자(anon)는 "쓰기만" 가능합니다. 조회는 안 됩니다.
drop policy if exists "anon can insert" on public.membership_leads;
create policy "anon can insert"
  on public.membership_leads
  for insert to anon
  with check (
    status = 'new'
    and source = 'web'
    and char_length(name)  between 2 and 40
    and phone ~ '^01[0-9]{8,9}$'
  );

-- 로그인한 관리자만 조회·수정할 수 있습니다.
drop policy if exists "auth can select" on public.membership_leads;
create policy "auth can select"
  on public.membership_leads
  for select to authenticated
  using (true);

drop policy if exists "auth can update" on public.membership_leads;
create policy "auth can update"
  on public.membership_leads
  for update to authenticated
  using (true) with check (true);

drop policy if exists "auth can delete" on public.membership_leads;
create policy "auth can delete"
  on public.membership_leads
  for delete to authenticated
  using (true);


-- ── 4. 중복 신청 처리 ──────────────────────────────────────
-- 같은 번호로 다시 신청하면 새 행을 만들지 않고 최신 내용으로 갱신합니다.
-- 프런트에서 Prefer: resolution=merge-duplicates 헤더와 함께 호출합니다.
-- (uq_leads_phone 유니크 인덱스가 위에서 생성되어 있어야 동작합니다)


-- ── 5. 관리자 계정 만들기 ──────────────────────────────────
-- SQL 로 만들지 않습니다. 아래 경로에서 직접 추가하십시오.
--   Supabase 대시보드 → Authentication → Users → Add user
--   Email / Password 입력 후 "Auto Confirm User" 체크
--
-- 회원가입 화면을 열어 두지 않도록 아래도 함께 확인하십시오.
--   Authentication → Providers → Email → "Enable Sign Ups" 를 끔


-- ── 6. 확인용 조회 ─────────────────────────────────────────
-- select count(*) as 전체,
--        count(*) filter (where created_at >= current_date) as 오늘,
--        count(*) filter (where marketing)                  as 마케팅동의
--   from public.membership_leads;
