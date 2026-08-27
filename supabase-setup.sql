-- ============================================================
-- HMK 오렌지 멤버십 — 오픈 알림 신청 접수 표
--
-- 쓰는 곳: Supabase 대시보드 > SQL Editor > New query > 붙여넣고 Run
-- 다 돌린 뒤 Project Settings > API에서 Project URL과 anon public 키를
-- assets/js/main.js 상단의 SUPABASE_URL / SUPABASE_ANON_KEY에 넣습니다.
--
-- anon 키는 브라우저에 그대로 노출되는 값입니다. 아래 RLS 설정을
-- 반드시 함께 적용해서 "신청은 되지만 남의 신청 내역은 못 보는" 상태로
-- 두어야 합니다.
-- ============================================================

-- 1. 표 만들기 -------------------------------------------------
create table if not exists public.membership_leads (
  id          bigint generated always as identity primary key,
  created_at  timestamptz not null default now(),
  name        text        not null,
  phone       text        not null,
  interest    text,
  agreed_at   timestamptz,
  source      text,
  memo        text,
  status      text        not null default 'new'
);

comment on table  public.membership_leads is '오렌지 멤버십 오픈 알림 신청';
comment on column public.membership_leads.interest  is '가장 관심 있는 것 (1F 매장 / B1 창고 / 2F 스튜디오 / 사업자)';
comment on column public.membership_leads.agreed_at is '개인정보 수집·이용 동의 시각';
comment on column public.membership_leads.source    is '신청이 들어온 페이지';
comment on column public.membership_leads.status    is 'new / contacted / joined / closed';

create index if not exists membership_leads_created_at_idx
  on public.membership_leads (created_at desc);


-- 2. 값 검사 ---------------------------------------------------
-- 이름·연락처 길이와 형식을 데이터베이스 쪽에서도 한 번 더 거릅니다.
alter table public.membership_leads
  drop constraint if exists membership_leads_name_len;
alter table public.membership_leads
  add constraint membership_leads_name_len
  check (char_length(name) between 1 and 40);

alter table public.membership_leads
  drop constraint if exists membership_leads_phone_fmt;
alter table public.membership_leads
  add constraint membership_leads_phone_fmt
  check (phone ~ '^[0-9]{9,13}$');

alter table public.membership_leads
  drop constraint if exists membership_leads_interest_len;
alter table public.membership_leads
  add constraint membership_leads_interest_len
  check (interest is null or char_length(interest) <= 60);


-- 3. 접근 권한 (여기가 중요합니다) --------------------------------
alter table public.membership_leads enable row level security;

-- 기존 정책이 있으면 지우고 다시 만듭니다.
drop policy if exists "anon can insert lead"  on public.membership_leads;
drop policy if exists "staff can read leads"  on public.membership_leads;

-- (1) 홈페이지 방문자: 신청만 가능. 조회·수정·삭제는 불가.
create policy "anon can insert lead"
  on public.membership_leads
  for insert
  to anon
  with check (true);

-- (2) 로그인한 직원 계정: 조회 가능.
--     CRM(hmkmngsystem)과 같은 프로젝트를 쓰신다면 직원 계정이 곧 authenticated 입니다.
create policy "staff can read leads"
  on public.membership_leads
  for select
  to authenticated
  using (true);

-- anon 역할에서 조회 권한을 확실히 떼어 둡니다.
revoke select, update, delete on public.membership_leads from anon;
grant  insert                 on public.membership_leads to   anon;


-- 4. 같은 번호 중복 신청 막기 (선택) ------------------------------
-- 하루 안에 같은 번호로 여러 번 신청하는 것을 막고 싶을 때만 쓰세요.
-- create unique index if not exists membership_leads_phone_day_uniq
--   on public.membership_leads (phone, (created_at::date));


-- 5. 확인용 조회 -----------------------------------------------
-- select created_at, name, phone, interest, status
--   from public.membership_leads
--  order by created_at desc
--  limit 50;
