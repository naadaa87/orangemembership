/* ============================================================
   HMK 오렌지 멤버십 — 고객용 홈페이지
   ------------------------------------------------------------
   [배포 전 설정] 오픈 알림 신청 접수 경로

   방법 1 (권장) — Supabase에 바로 적재
     아래 두 값을 채우면 신청 내용이 membership_leads 표에 쌓입니다.
     표 만드는 SQL은 같은 폴더의 supabase-setup.sql에 있습니다.
     anon 키는 공개되는 값입니다. 반드시 SQL의 RLS 설정을 함께
     적용해서 "쓰기만 되고 읽기는 막힌" 상태로 두어야 합니다.

   방법 2 — Formspree, Google Forms 등 외부 접수 주소 사용
     NOTIFY_ENDPOINT에 POST 주소를 넣습니다.

   둘 다 비워 두면 전화·매장 접수 안내 문구가 대신 표시됩니다.
   ============================================================ */
var SUPABASE_URL = "";       // 예: https://xxxxxxxx.supabase.co
var SUPABASE_ANON_KEY = "";  // Project Settings > API > anon public
var NOTIFY_ENDPOINT = "";

(function () {
  "use strict";

  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  };
  var won = function (n) { return Math.round(n).toLocaleString("ko-KR"); };

  /* --------------------------------------------------------
     1. 모바일 내비게이션
     -------------------------------------------------------- */
  var toggle = $(".nav-toggle");
  var links = $(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$("a", links).forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && links.classList.contains("is-open")) {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* --------------------------------------------------------
     2. 스크롤 등장 효과
     -------------------------------------------------------- */
  var targets = $$(".rv");
  if (targets.length) {
    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      var io = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-in");
              io.unobserve(entry.target);
            }
          });
        },
        { rootMargin: "0px 0px -8% 0px", threshold: 0.06 }
      );
      targets.forEach(function (el) { io.observe(el); });
    }
  }

  /* --------------------------------------------------------
     3. 층 스택 — 클릭한 층 강조
     -------------------------------------------------------- */
  var floors = $$(".floor");
  if (floors.length) {
    floors.forEach(function (f) {
      f.addEventListener("click", function () {
        var on = f.classList.contains("is-active");
        floors.forEach(function (x) { x.classList.remove("is-active"); });
        if (!on) f.classList.add("is-active");
      });
    });
  }

  /* --------------------------------------------------------
     4. 회비 회수 계산기
     -------------------------------------------------------- */
  var calc = $("#calc");
  if (calc) {
    var FEE = 39000;          // 연회비
    var SAVE_RATE = 0.07;     // 회원가 평균 절감률(대표 품목 기준 목표값)
    var OD_POINT = 1600;      // 오렌지 데이 1회 추가 적립 (8만원 구매 × 2%)
    var REVIEW_POINT = 500;   // 후기 1건 적립
    var DRINK_VALUE = 2000;   // 무인카페 음료 1잔 상당액

    var spendEl = $("#c-spend");
    var storageEl = $("#c-storage");
    var state = { od: 4, review: 6, cafe: 0.5 };

    function tierOf(annual) {
      if (annual >= 3600000) {
        return { name: "오렌지 프라임", rate: 0.03, storage: 0.15, drinks: 4 };
      }
      if (annual >= 1200000) {
        return { name: "오렌지 플러스", rate: 0.025, storage: 0.08, drinks: 4 };
      }
      return { name: "오렌지", rate: 0.02, storage: 0, drinks: 2 };
    }

    function render() {
      var monthly = Number(spendEl.value);
      var storageFee = Number(storageEl.value);
      var annual = monthly * 12;
      var tier = tierOf(annual);

      var priceSave = annual * SAVE_RATE;
      var basePoint = annual * tier.rate;
      var odPoint = state.od * OD_POINT;
      var reviewPoint = state.review * REVIEW_POINT;
      var storageSave = storageFee * 12 * tier.storage;
      var cafeValue = tier.drinks * 12 * DRINK_VALUE * state.cafe;

      var total = priceSave + basePoint + odPoint + reviewPoint + storageSave + cafeValue;
      var ratio = total / FEE;

      $("#c-spend-val").textContent = won(monthly) + "원";
      var stEl = $("#c-storage-val");
      stEl.textContent = storageFee === 0 ? "이용 안 함" : won(storageFee) + "원";
      stEl.classList.toggle("as-text", storageFee === 0);
      $("#c-tier").textContent = tier.name;
      $("#c-tier-rate").textContent = (tier.rate * 100).toFixed(1) + "%";

      $("#o-total").firstChild.nodeValue = won(total);
      $("#o-price").textContent = won(priceSave) + "원";
      $("#o-point").textContent = won(basePoint + odPoint + reviewPoint) + "P";
      $("#o-storage").textContent =
        storageSave > 0 ? won(storageSave) + "원" : "—";
      $("#o-cafe").textContent = cafeValue > 0 ? won(cafeValue) + "원" : "—";

      var verdict;
      if (total >= FEE) {
        var months = Math.max(1, Math.ceil((FEE / total) * 12));
        verdict =
          "연회비 39,000원의 <b>약 " + ratio.toFixed(1) + "배</b>입니다. " +
          "지금 이용 패턴이면 가입 후 <b>약 " + months + "개월</b>이면 회비만큼 돌아옵니다. " +
          "가입 첫날 받는 웰컴 패키지는 여기에 포함되어 있지 않습니다.";
      } else {
        verdict =
          "지금 이용 패턴으로는 연간 <b>" + won(total) + "원</b>이 돌아옵니다. " +
          "장보기 금액을 조금 올리거나 공유창고를 함께 쓰면 회비를 넘어섭니다. " +
          "가입 첫날 받는 웰컴 패키지(114,000원 상당)는 여기에 포함되어 있지 않습니다.";
      }
      $("#o-verdict").innerHTML = verdict;
    }

    [spendEl, storageEl].forEach(function (el) {
      if (el) el.addEventListener("input", render);
    });

    $$("[data-seg]", calc).forEach(function (group) {
      var key = group.getAttribute("data-seg");
      $$("button", group).forEach(function (btn) {
        btn.addEventListener("click", function () {
          $$("button", group).forEach(function (b) {
            b.setAttribute("aria-pressed", "false");
          });
          btn.setAttribute("aria-pressed", "true");
          state[key] = Number(btn.getAttribute("data-value"));
          render();
        });
      });
    });

    render();
  }

  /* --------------------------------------------------------
     5. 오픈 알림 신청 폼
     -------------------------------------------------------- */
  var form = $("#notify-form");
  if (form) {
    var msg = $("#notify-msg");

    function say(text, kind) {
      msg.className = "form-msg is-on " + kind;
      msg.innerHTML = text;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var name = $("#nf-name").value.trim();
      var phone = $("#nf-phone").value.trim();
      var agree = $("#nf-agree").checked;

      if (!name || !phone) {
        say("이름과 연락처를 모두 입력해 주세요.", "info");
        return;
      }
      if (!agree) {
        say("개인정보 수집·이용 동의가 필요합니다.", "info");
        return;
      }
      if (!/^[0-9\-\s]{9,}$/.test(phone)) {
        say("연락처를 숫자로 다시 확인해 주세요.", "info");
        return;
      }

      // 사람 눈에 보이지 않는 칸이 채워져 있으면 자동 프로그램으로 보고 접수하지 않습니다.
      var trap = $("#nf-company");
      if (trap && trap.value) {
        say("신청이 접수되었습니다. 오픈 일정이 확정되면 문자로 안내드리겠습니다.", "ok");
        form.reset();
        return;
      }

      var useSupabase = !!(SUPABASE_URL && SUPABASE_ANON_KEY);
      if (!useSupabase && !NOTIFY_ENDPOINT) {
        say(
          "온라인 접수 채널은 준비 중입니다. 매장 안내 데스크 또는 고객센터로 신청해 주세요.<br>" +
            "입력하신 내용은 전송되지 않았습니다.",
          "info"
        );
        return;
      }

      var btn = $("#nf-submit");
      btn.disabled = true;
      btn.textContent = "신청하는 중…";

      var req;
      if (useSupabase) {
        var interestEl = $("#nf-interest");
        req = fetch(SUPABASE_URL.replace(/\/+$/, "") + "/rest/v1/membership_leads", {
          method: "POST",
          headers: {
            apikey: SUPABASE_ANON_KEY,
            Authorization: "Bearer " + SUPABASE_ANON_KEY,
            "Content-Type": "application/json",
            Prefer: "return=minimal"
          },
          body: JSON.stringify({
            name: name,
            phone: phone.replace(/[^0-9]/g, ""),
            interest: interestEl ? interestEl.value : null,
            agreed_at: new Date().toISOString(),
            source: location.pathname.replace(/^\//, "") || "index.html"
          })
        });
      } else {
        req = fetch(NOTIFY_ENDPOINT, {
          method: "POST",
          headers: { Accept: "application/json" },
          body: new FormData(form)
        });
      }

      req
        .then(function (res) {
          if (!res.ok) throw new Error("bad response");
          form.reset();
          say(
            "신청이 접수되었습니다. 오픈 일정이 확정되면 문자로 안내드리겠습니다.",
            "ok"
          );
        })
        .catch(function () {
          say(
            "지금은 접수가 되지 않습니다. 잠시 후 다시 시도하시거나 고객센터로 연락해 주세요.",
            "info"
          );
        })
        .then(function () {
          btn.disabled = false;
          btn.textContent = "오픈 알림 신청";
        });
    });
  }

  /* --------------------------------------------------------
     6. 현재 연도
     -------------------------------------------------------- */
  $$("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
