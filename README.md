# HMK 오렌지 멤버십 홈페이지

HMK 홀딩스그룹 오렌지 멤버십 소개 사이트. 정적 HTML/CSS/JS로만 구성되어 있어 빌드 도구 없이 그대로 배포됩니다.

- 저장소 · `naadaa87/orangemembership`
- 배포 · Cloudflare Pages
- 기획 · 총괄기획본부

---

## 폴더 구조

```
/
├── index.html          메인
├── benefits.html       혜택 안내
├── tiers.html          등급 · 회비
├── points.html         오렌지 포인트
├── partners.html       제휴 혜택
├── community.html      커뮤니티
├── guide.html          이용 안내 · FAQ
├── join.html           사전 알림 신청
├── terms.html          약관 · 개인정보 처리방침
├── admin.html          사전 알림 신청 관리 (검색 노출 차단)
├── 404.html
├── robots.txt
├── sitemap.xml
├── _headers            Cloudflare 캐시 · 보안 헤더
├── build.py            페이지 생성 스크립트 (배포에는 불필요)
├── supabase/
│   └── schema.sql      테이블 · 보안정책 SQL
└── assets/
    ├── css/style.css
    ├── js/config.js    ★ Supabase 주소 · 키를 넣는 곳
    ├── js/main.js
    └── img/            이미지 19개
```

---

## GitHub 업로드

> **반드시 폴더 안의 내용물을 드래그해서 올리십시오.**
> `om` 폴더 자체를 올리거나 `choose your files` 버튼으로 개별 선택하면 `assets/` 하위 경로가 평평해지면서 파일이 서로 덮어써집니다.

1. https://github.com/naadaa87/orangemembership 접속
2. `Add file` → `Upload files`
3. 탐색기에서 이 폴더를 열고 **안의 항목 전체를 선택해 드래그**
   (`index.html`, `assets` 폴더, `_headers`, `robots.txt` 등)
4. `assets/css/style.css` 처럼 경로가 살아 있는지 목록에서 확인
5. Commit

---

## Cloudflare Pages 설정

| 항목 | 값 |
|---|---|
| Framework preset | **None** |
| Build command | *(비워 둠)* |
| Build output directory | **/** |
| Root directory | *(비워 둠)* |

`_headers` 파일이 있으면 캐시와 보안 헤더가 자동 적용됩니다.

---

## 배포 후 해야 할 일

### 1. 도메인 치환

현재 코드에는 `https://orangemembership.pages.dev` 가 임시로 들어가 있습니다.
실제 도메인이 정해지면 아래 네 곳을 모두 바꿔 주십시오.

- 각 HTML의 `<link rel="canonical">`
- 각 HTML의 `og:url`, `og:image`
- `robots.txt` 의 Sitemap 주소
- `sitemap.xml` 의 모든 `<loc>`

`build.py` 상단의 `SITE` 값만 바꾸고 `python3 build.py` 를 다시 돌리면 전부 한 번에 반영됩니다.

### 2. Supabase 연동 (사전 알림 폼 · 관리자 페이지)

**① 프로젝트 생성** — Supabase에서 새 프로젝트를 만듭니다. 리전은 `Northeast Asia (Seoul)` 를 고르십시오.

**② 테이블 생성** — SQL Editor 를 열고 `supabase/schema.sql` 전체를 붙여넣어 실행합니다.
테이블, 인덱스, 행 수준 보안(RLS) 정책이 한 번에 만들어집니다.

**③ 키 입력** — Project Settings → API 에서 두 값을 복사해 `assets/js/config.js` 에 넣습니다.

```js
window.HMK_CONFIG = {
  SUPABASE_URL: 'https://abcdefghijk.supabase.co',
  SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
  TABLE: 'membership_leads'
};
```

anon 키는 브라우저에 노출되는 것이 정상입니다. 실제 보안은 RLS가 담당합니다.
**`service_role` 키는 절대 넣지 마십시오.**

**④ 관리자 계정 추가** — Authentication → Users → Add user 에서 이메일과 비밀번호를 만들고
`Auto Confirm User` 를 체크합니다. 이어서 Authentication → Providers → Email 에서
**Enable Sign Ups 를 꺼 두십시오.** 켜져 있으면 누구나 계정을 만들어 신청자 명단을 볼 수 있습니다.

**⑤ 확인** — `join.html` 에서 신청을 넣어 보고 `admin.html` 에서 목록에 뜨는지 확인합니다.

`config.js` 가 비어 있으면 폼은 실제 전송 없이 성공 메시지만 띄우는 미리보기 모드로 동작합니다.

#### 데이터 구조

| 컬럼 | 내용 |
|---|---|
| `name` | 이름 (2~40자) |
| `phone` | 휴대폰 번호, 하이픈 없이 저장. 중복 신청 시 최신 내용으로 갱신 |
| `region` | 관심 지역 |
| `interest` | `market,storage,live,biz,partner` 쉼표 구분 |
| `memo` | 문의 내용 |
| `marketing` | 마케팅 수신 동의 여부 |
| `status` | `new` / `contacted` / `hold` / `done` / `spam` |

익명 사용자는 **INSERT만** 가능하고 조회는 차단됩니다. 스팸 방지용 허니팟 필드(`_hp`)도 들어가 있습니다.

### 2-1. 관리자 페이지

`https://<도메인>/admin.html` 로 접속합니다.

- 신청 현황 요약 (전체 · 오늘 · 미처리 · 마케팅 동의율)
- 이름 · 연락처 검색, 상태 · 지역 · 관심 서비스 필터
- 상태 변경 (신규 → 연락완료 → 처리완료)
- CSV 내려받기 (Excel 한글 깨짐 방지 BOM 포함)

`robots.txt` 와 `_headers` 에서 검색 노출을 막아 두었으나 주소를 아는 사람은 접근할 수 있습니다.
로그인 없이는 아무 데이터도 조회되지 않지만, 계정 관리는 신중히 하십시오.
CSV에는 신청자 연락처가 그대로 들어가므로 파일 취급에 주의가 필요합니다.

### 3. 개인정보 처리방침 보완

`terms.html` 의 아래 두 항목은 확정 정보를 채워야 합니다.

- 5번 처리 위탁 — 문자 발송·데이터 보관 위탁사 상호와 위탁 업무
- 9번 개인정보 보호책임자 — 성명, 직위, 연락처

---

## 콘텐츠 수정 방법

모든 페이지는 `build.py` 안에 문자열로 들어 있습니다.
헤더·푸터·메뉴는 공통 함수에서 생성되므로 한 곳만 고치면 전 페이지에 반영됩니다.

```bash
python3 build.py
```

CSS와 JS는 `assets/` 안에서 직접 수정하시면 됩니다.

---

## 디자인 토큰

| 항목 | 값 |
|---|---|
| 오렌지 | `#E76D27` |
| 네이비 | `#1C2A4F` |
| 본문 폰트 | Pretendard Variable |
| 숫자 폰트 | IBM Plex Mono |
| 모서리 | 16px (큰 카드 24px) |
| 배경 | 흰색 / 웜화이트 `#FAF7F3` |

---

## 표기 관련 주의

사이트에 적힌 회비·혜택·등급 조건은 2027년 1월 시행 목표의 계획안입니다.
아래 원칙을 지켜 작성했으므로 수정하실 때도 유지해 주십시오.

- 대부업 관련 상품은 멤버십 혜택에 포함하지 않음
- 토큰증권·지분투자 관련 표현 사용하지 않음
- "최대" 금액 표기 시 산정 근거 병기
- 자동갱신·해지·환불 조건을 명시하고 해지 경로를 숨기지 않음
- 제휴 혜택은 제휴사 사정으로 변경될 수 있음을 고지
