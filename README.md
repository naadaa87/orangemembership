# HMK 오렌지 멤버십 — 고객용 홈페이지

정적 HTML 사이트입니다. 빌드 도구나 서버가 필요 없고, 폴더를 그대로 올리면 동작합니다.

---

## 1. 파일 구성

```
orange-membership/
├── index.html          메인
├── membership.html     멤버십 소개 · 등급 · 회비 회수 계산기 · 결제/해지 조건
├── benefits.html       혜택 (장소별 + 등급별 전체표)
├── points.html         오렌지 포인트
├── partners.html       제휴 혜택 13개 분야
├── lounge.html         라운지 · 셀러클럽 · 오렌지 크루 · 연간 프로그램
├── biz.html            사업자 회원 (오렌지 비즈)
├── join.html           가입 안내 · 해지/환불 · 오픈 알림 신청
├── faq.html            자주 묻는 질문
├── terms.html          회원 약관 전문 (8장 39조 + 별표 2종)
├── privacy.html        개인정보 처리방침
├── 404.html            없는 주소로 들어왔을 때 (Cloudflare Pages가 자동으로 씁니다)
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/            로고 2종 + 파비콘 + 공유 미리보기 이미지
├── supabase-setup.sql  오픈 알림 접수 표 만드는 SQL
├── _headers            Cloudflare Pages 캐시·보안 헤더
├── robots.txt
└── sitemap.xml
```

---

## 2. GitHub 업로드

1. GitHub에서 새 저장소를 만듭니다 (예: `hmk-orange-membership`).
2. `Add file` → `Upload files` 화면에서 **`orange-membership` 폴더 안의 내용물**을 통째로 드래그 앤 드롭합니다.
   - 파일 선택 버튼을 쓰면 폴더 경로가 사라져 `assets` 구조가 깨집니다. 반드시 드래그 앤 드롭으로 올려주세요.
   - `index.html`이 저장소 최상단에 있어야 합니다.
3. `Commit changes`를 누릅니다.

---

## 3. Cloudflare Pages 배포

1. Cloudflare 대시보드 → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. 위에서 만든 저장소를 선택합니다.
3. 빌드 설정:

   | 항목 | 값 |
   |---|---|
   | Framework preset | `None` |
   | Build command | *(비워 둠)* |
   | Build output directory | `/` |

4. **Save and Deploy**를 누르면 1분 안에 `프로젝트명.pages.dev` 주소가 생깁니다.
5. 도메인을 붙이려면 **Custom domains** 탭에서 연결합니다.

---

## 4. 배포 전에 반드시 교체할 항목

아래 값은 임시로 넣어 둔 것입니다. 실제 값으로 바꾼 뒤 공개해 주세요.

| 항목 | 현재 값 | 들어 있는 위치 |
|---|---|---|
| 고객센터 번호 | `1600-0000` | 모든 페이지 푸터, `join.html`, `faq.html`, `privacy.html` |
| 대표 이메일 | `membership@hmkholdings.com` | 푸터, `join.html`, `faq.html` |
| 개인정보 문의 | `privacy@hmkholdings.com` | `privacy.html` |
| 개인정보 보호책임자 | 미지정 (안내 문구만 있음) | `privacy.html` 9번 항목 |
| 약관 시행일 | 부칙에 "확정 시 게시" | `terms.html` 부칙 |
| 사이트 주소 | `https://example.pages.dev` | `robots.txt`, `sitemap.xml`, 모든 페이지의 `og:url` · `canonical` |

### 오픈 알림 신청 폼 연결

`assets/js/main.js` 맨 위 세 줄 중 필요한 것만 채우면 폼이 실제로 동작합니다.

**방법 1 — Supabase (권장)**

CRM에서 이미 쓰고 계신 Supabase에 그대로 쌓습니다. 추가 비용이 없고, 나중에 CRM 고객 명단으로 옮기기도 쉽습니다.

1. Supabase 대시보드 → SQL Editor → `supabase-setup.sql` 내용을 붙여넣고 Run
2. Project Settings → API에서 Project URL과 anon public 키를 복사
3. `assets/js/main.js` 상단에 넣기

```js
var SUPABASE_URL = "https://xxxxxxxx.supabase.co";
var SUPABASE_ANON_KEY = "eyJhbGciOi...";
```

신청 내역은 `membership_leads` 표에 쌓이고, Table Editor에서 바로 보실 수 있습니다.

**방법 2 — Formspree, Google Forms 등**

```js
var NOTIFY_ENDPOINT = "https://formspree.io/f/xxxxxxxx";
```

셋 다 비워 두면 "온라인 접수 채널 준비 중, 매장·고객센터로 신청" 안내가 뜨고 데이터는 전송되지 않습니다.

**스팸에 대해 알아두실 것**

폼에는 사람 눈에 보이지 않는 칸을 하나 넣어 두었습니다. 자동 프로그램이 이 칸을 채우면 접수하지 않습니다. 다만 anon 키는 브라우저에 노출되는 값이라, 마음먹은 사람은 홈페이지를 거치지 않고 Supabase 주소로 바로 넣을 수도 있습니다. `supabase-setup.sql`의 RLS 설정과 값 검사가 1차 방어선이고, 실제로 스팸이 들어오기 시작하면 Cloudflare Pages Functions에 접수 경로를 하나 만들어 Turnstile을 붙이는 방식으로 막습니다. 오픈 전 기간에는 지금 구성으로 충분합니다.

---

## 5. 카카오톡·문자로 링크를 보낼 때

`assets/img/og-cover.png`가 미리보기 이미지로 뜹니다. 이미지를 바꾸시려면 같은 이름, 같은 크기(1200 × 630)로 덮어쓰시면 됩니다.

한 번 공유된 링크는 카카오가 미리보기를 저장해 둡니다. 이미지를 바꾸고도 예전 것이 계속 보이면 [카카오 디벨로퍼스 도구](https://developers.kakao.com/tool/clear/og)에서 주소를 넣고 캐시를 지워 주세요.

---

## 6. 법적 고지 관련 (수정 시 주의)

기획서 PART 9의 법률 검토 결과가 화면에 반영되어 있습니다. 문구를 손볼 때 아래는 유지해 주세요.

- **표시광고법** — `114,000원`이 나오는 모든 자리에는 산정 근거 링크(`membership.html#welcome-basis`)가 붙어 있습니다. 근거 표를 지우면 실증 자료 없이 광고하는 상태가 됩니다.
- 회원가 `평균 7%`는 대표 품목 기준 목표값이라는 단서가 항상 함께 있어야 합니다.
- `업계 최저가`, `국내 최초` 같은 표현은 넣지 않습니다.
- **전자상거래법** — 자동갱신 고지(30일 전·7일 전), 14일 전액 환불, 간편 해지 안내가 `join.html` 상단 박스에 들어 있습니다.
- **대부업법** — 대부 상품과 금리 관련 표현은 이 사이트 어디에도 넣지 않습니다. 금융·보험 안내는 별도 메뉴·별도 화면·별도 동의로 분리합니다.
- **자본시장법** — 토큰증권, 지분투자, 배당 관련 표현은 넣지 않습니다.
- **전자금융거래법** — 오렌지 포인트는 충전·양도·환금 불가라는 설명이 `points.html`과 `terms.html` 제25조에 있습니다.

---

## 7. 내용을 고칠 때

각 페이지는 독립된 HTML이라 원하는 파일만 열어 수정하면 됩니다. 다만 아래 내용은 여러 페이지에 걸쳐 있으니 함께 고쳐야 합니다.

| 고치는 내용 | 함께 확인할 파일 |
|---|---|
| 연회비 금액 | `index.html`, `membership.html`, `benefits.html`, `join.html`, `faq.html`, `terms.html`, `assets/js/main.js`(`FEE`) |
| 등급별 적립률·요율 | `membership.html`, `benefits.html`, `terms.html`(별표 1), `assets/js/main.js`(`tierOf`) |
| 웰컴 패키지 구성 | `index.html`, `membership.html`, `join.html`, `terms.html`(제30조·별표 1) |
| 상단 메뉴 | 11개 HTML 파일의 `<div class="nav-links">` 블록 |
| 푸터·고지사항 | 11개 HTML 파일의 `<footer class="site-footer">` 블록 |

---

## 8. 디자인 기준

| 항목 | 값 |
|---|---|
| 포인트 컬러 | `#E76D27` (오렌지) |
| 보조 컬러 | `#1C2A4F` (네이비) |
| 배경 | `#FFFFFF` / `#F1F2F3` (연한 무채색) |
| 본문 서체 | Pretendard (CDN), 대체 Noto Sans KR |
| 숫자·라벨 서체 | IBM Plex Mono (Google Fonts) |
| 기본 글자 크기 | 17px / 행간 1.78 — 고령 회원을 고려해 일반 사이트보다 크게 잡았습니다 |

`B1` `1F` `2F` `온라인` 층 태그가 사이트 전체에서 "이 혜택을 어디서 쓰는가"를 표시하는 공통 장치입니다. 새 혜택을 추가할 때도 같은 태그를 붙여 주세요.
