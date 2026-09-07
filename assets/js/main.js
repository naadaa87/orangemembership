/* HMK 오렌지 멤버십 — 공통 스크립트 */
(function () {
  'use strict';

  /* ── 모바일 메뉴 ───────────────────────────── */
  var burger = document.querySelector('.burger');
  var mnav = document.querySelector('.mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = mnav.classList.toggle('on');
      burger.classList.toggle('on', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ── 헤더 그림자 ───────────────────────────── */
  var hd = document.querySelector('header');
  if (hd) {
    var onScroll = function () { hd.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── 스크롤 리빌 ───────────────────────────── */
  var rvs = document.querySelectorAll('.rv');
  if (rvs.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
      rvs.forEach(function (el, i) {
        el.style.transitionDelay = (Math.min(i % 4, 3) * 70) + 'ms';
        io.observe(el);
      });
    } else {
      rvs.forEach(function (el) { el.classList.add('in'); });
    }
  }

  /* ── 아코디언 ──────────────────────────────── */
  document.querySelectorAll('.acc-q').forEach(function (q) {
    q.setAttribute('aria-expanded', 'false');
    q.addEventListener('click', function () {
      var item = q.parentElement;
      var panel = item.querySelector('.acc-a');
      var open = item.classList.toggle('on');
      q.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.style.maxHeight = open ? panel.scrollHeight + 'px' : 0;
    });
  });

  /* ── 회비 회수 계산기 ──────────────────────── */
  var calc = document.getElementById('calc');
  if (calc) {
    var FEE = 39000;
    var WELCOME = 114000;          // 웰컴 패키지 체감 가치
    var DISC = 0.07;               // 회원가 평균 인하율
    var PARTNER = {                // 제휴 카테고리별 연간 절감 추정 (원)
      car: 80000, move: 50000, interior: 120000,
      health: 150000, edu: 120000, telecom: 96000
    };
    var $ = function (id) { return document.getElementById(id); };
    var won = function (n) { return Math.round(n).toLocaleString('ko-KR'); };

    function run() {
      var mShop = +$('cShop').value;                  // 월 장보기 (만원)
      var mStore = +$('cStore').value;                // 월 창고 이용료 (만원)
      var yShop = mShop * 10000 * 12;
      var yStore = mStore * 10000 * 12;

      // 등급 판정
      var tier = '오렌지', rate = 0.02, cut = 0, cafe = 24000;
      if (yShop >= 3600000 || mStore >= 15) { tier = '오렌지 프라임'; rate = 0.03; cut = 0.15; cafe = 48000; }
      else if (yShop >= 1200000 || mStore > 0) { tier = '오렌지 플러스'; rate = 0.025; cut = 0.08; cafe = 48000; }

      var vDisc = yShop * DISC;                       // 회원가 절감
      var vPoint = yShop * rate;                      // 포인트 적립
      var vStore = yStore * cut;                      // 창고 요율 인하
      var vPartner = 0;
      document.querySelectorAll('.cP:checked').forEach(function (c) { vPartner += PARTNER[c.value] || 0; });

      var total = vDisc + vPoint + vStore + vPartner + WELCOME + cafe;
      var mult = total / FEE;

      $('rTotal').textContent = won(total) + '원';
      $('rMult').textContent = '연회비 39,000원의 ' + mult.toFixed(1) + '배';
      $('rDisc').textContent = won(vDisc) + '원';
      $('rPoint').textContent = won(vPoint) + 'P';
      $('rStore').textContent = won(vStore) + '원';
      $('rPartner').textContent = won(vPartner) + '원';
      $('rWelcome').textContent = won(WELCOME + cafe) + '원';
      $('rTier').innerHTML = '예상 등급 <b>' + tier + '</b> · 적립률 <b>' + (rate * 100).toFixed(1) + '%</b>';

      $('oShop').textContent = mShop + '만원';
      $('oStore').textContent = mStore === 0 ? '이용 안 함' : mStore + '만원';
    }

    calc.addEventListener('input', run);
    calc.addEventListener('change', run);
    run();
  }

  /* ── 사전 알림 신청 폼 ─────────────────────── */
  var form = document.getElementById('alertForm');
  if (form) {
    var msg = document.getElementById('formMsg');
    var btn = form.querySelector('button[type=submit]');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('input[name=_hp]').value) return;   // 허니팟

      var name = form.name_.value.trim();
      var phone = form.phone.value.replace(/[^0-9]/g, '');
      var agree = form.agree.checked;

      function show(type, text) {
        msg.className = 'formmsg ' + type;
        msg.textContent = text;
      }
      if (name.length < 2) { show('err', '이름을 두 글자 이상 입력해 주세요.'); form.name_.focus(); return; }
      if (phone.length < 10 || phone.length > 11) { show('err', '휴대폰 번호를 다시 확인해 주세요.'); form.phone.focus(); return; }
      if (!agree) { show('err', '개인정보 수집·이용에 동의해 주셔야 신청이 접수됩니다.'); return; }

      btn.disabled = true;
      btn.textContent = '접수 중…';

      var payload = {
        name: name,
        phone: phone,
        region: form.region.value || null,
        interest: Array.prototype.map.call(
          form.querySelectorAll('input[name=interest]:checked'),
          function (c) { return c.value; }
        ).join(',') || null,
        memo: form.memo.value.trim().slice(0, 1000) || null,
        marketing: form.marketing.checked,
        status: 'new',
        source: 'web'
      };

      var reset = function () { btn.disabled = false; btn.textContent = '사전 알림 신청하기'; };
      var done = function () {
        show('ok', '사전 알림 신청이 접수되었습니다. 오픈 일정이 확정되면 문자로 알려 드리겠습니다.');
        form.reset();
        reset();
      };
      var fail = function (m) { show('err', m || '일시적인 오류로 접수되지 않았습니다. 잠시 후 다시 시도해 주세요.'); reset(); };

      var cfg = window.HMK_CONFIG || {};
      if (!cfg.SUPABASE_URL || !cfg.SUPABASE_ANON_KEY) {
        // 연동 전 미리보기 모드
        console.warn('[HMK] assets/js/config.js 에 Supabase 정보가 비어 있어 실제 전송을 건너뜁니다.');
        setTimeout(done, 400);
        return;
      }

      fetch(cfg.SUPABASE_URL + '/rest/v1/' + (cfg.TABLE || 'membership_leads'), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'apikey': cfg.SUPABASE_ANON_KEY,
          'Authorization': 'Bearer ' + cfg.SUPABASE_ANON_KEY,
          // 같은 번호로 다시 신청하면 새 행 대신 최신 내용으로 갱신합니다
          'Prefer': 'return=minimal,resolution=merge-duplicates'
        },
        body: JSON.stringify(payload)
      }).then(function (r) {
        if (r.ok) { done(); return; }
        return r.text().then(function (t) {
          console.error('[HMK] 접수 실패', r.status, t);
          fail(r.status === 409
            ? '이미 신청하신 번호입니다. 접수된 내용을 최신으로 갱신했습니다.'
            : null);
        });
      }).catch(function (e) { console.error(e); fail(); });
    });

    // 휴대폰 자동 하이픈
    var tel = form.querySelector('input[name=phone]');
    if (tel) {
      tel.addEventListener('input', function () {
        var v = tel.value.replace(/[^0-9]/g, '').slice(0, 11);
        if (v.length > 7) v = v.slice(0, 3) + '-' + v.slice(3, 7) + '-' + v.slice(7);
        else if (v.length > 3) v = v.slice(0, 3) + '-' + v.slice(3);
        tel.value = v;
      });
    }
  }

  /* ── 현재 연도 ─────────────────────────────── */
  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();
})();
