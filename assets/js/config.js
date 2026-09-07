/* ═══════════════════════════════════════════════════════════
   HMK 오렌지 멤버십 — Supabase 연결 설정

   아래 두 값을 채우시면 사전 알림 신청 폼과 관리자 페이지가
   바로 동작합니다.

   값을 찾는 곳
     Supabase 대시보드 → Project Settings → API
       Project URL      →  SUPABASE_URL
       Project API keys → anon public →  SUPABASE_ANON_KEY

   anon 키는 브라우저에 노출되는 것이 정상입니다.
   실제 보안은 schema.sql 의 행 수준 보안(RLS)이 담당합니다.
   service_role 키는 절대 이 파일에 넣지 마십시오.
   ═══════════════════════════════════════════════════════════ */

window.HMK_CONFIG = {
  SUPABASE_URL: '',        // 예) https://abcdefghijk.supabase.co
  SUPABASE_ANON_KEY: '',   // 예) eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  TABLE: 'membership_leads'
};
