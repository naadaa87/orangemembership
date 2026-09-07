# -*- coding: utf-8 -*-
"""HMK 오렌지 멤버십 홈페이지 생성기"""
import os, re, datetime

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://orangemembership.pages.dev"
TODAY = "2026-08-28"

NAV = [
    ("benefits.html", "혜택"),
    ("tiers.html", "등급 · 회비"),
    ("points.html", "오렌지 포인트"),
    ("partners.html", "제휴 혜택"),
    ("community.html", "커뮤니티"),
    ("guide.html", "이용안내"),
]

TOPBAR = '2027년 1월 오픈 예정 — <b>사전 알림 신청</b>하시면 오픈 일정을 가장 먼저 알려 드립니다'


def head(title, desc, page):
    canon = SITE + "/" + ("" if page == "index.html" else page)
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="HMK 홀딩스그룹 총괄기획본부">
<meta name="theme-color" content="#E76D27">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="HMK 오렌지 멤버십">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og.jpg">
<meta property="og:locale" content="ko_KR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
'''


def header(page):
    menu = "".join(
        f'<a href="{h}"{" class=\"on\"" if h == page else ""}>{t}</a>' for h, t in NAV
    )
    mmenu = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<div class="topbar">{TOPBAR}</div>
<header>
  <div class="wrap nav">
    <a href="index.html" class="logo" aria-label="HMK 오렌지 멤버십 홈">
      <img src="assets/img/logo.png" alt="HMK 홀딩스그룹">
      <span>오렌지 멤버십</span>
    </a>
    <nav class="menu">{menu}</nav>
    <a href="join.html" class="btn btn-p btn-sm nav-cta">사전 알림 신청</a>
    <button class="burger" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
  <div class="mnav"><div class="wrap">{mmenu}<a href="join.html" class="btn btn-p">사전 알림 신청</a></div></div>
</header>
'''


FOOTER = '''<footer>
  <div class="wrap">
    <div class="f-top">
      <div class="f-brand">
        <img src="assets/img/logo.png" alt="HMK 홀딩스그룹">
        <p>HMK 홀딩스그룹은 저평가된 상업용 부동산을 매입해 공유창고 · 창고형 할인매장 · 라이브커머스로 공간을 다시 씁니다. 오렌지 멤버십은 그 네 가지 사업을 한 장의 카드로 잇는 회원제입니다.</p>
      </div>
      <div class="f-col">
        <h4>멤버십</h4>
        <a href="benefits.html">혜택 안내</a>
        <a href="tiers.html">등급 · 회비</a>
        <a href="points.html">오렌지 포인트</a>
        <a href="partners.html">제휴 혜택</a>
      </div>
      <div class="f-col">
        <h4>이용</h4>
        <a href="community.html">커뮤니티</a>
        <a href="guide.html">이용 안내</a>
        <a href="guide.html#faq">자주 묻는 질문</a>
        <a href="join.html">사전 알림 신청</a>
      </div>
      <div class="f-col">
        <h4>회사</h4>
        <a href="https://hmkholdings.com" target="_blank" rel="noopener">HMK 홀딩스그룹</a>
        <a href="https://storage-orange.com" target="_blank" rel="noopener">오렌지 공유창고</a>
        <a href="terms.html">회원 약관</a>
        <a href="terms.html#privacy">개인정보 처리방침</a>
      </div>
    </div>
    <div class="f-bot">
      <div>&copy; <span id="yr">2026</span> HMK HOLDINGS GROUP. All rights reserved.</div>
      <div class="lg"><a href="terms.html">이용약관</a><a href="terms.html#privacy">개인정보 처리방침</a><a href="join.html">문의</a></div>
    </div>
    <p class="f-disc">본 사이트에 안내된 회비 · 혜택 · 등급 조건 · 제휴 내용은 2027년 1월 시행을 목표로 준비 중인 계획안이며, 시행 시점의 사업 여건과 관계 법령 검토 결과에 따라 변경될 수 있습니다. 확정된 조건은 서비스 개시 시점에 회원 약관과 함께 공지합니다. 제휴 혜택은 제휴사의 사정에 따라 변경되거나 종료될 수 있습니다.</p>
  </div>
</footer>
<div class="mcta">
  <div class="px"><div class="k">오렌지 멤버십 연회비</div><div class="v">39,000원</div></div>
  <a href="join.html" class="btn btn-p btn-sm">사전 알림 신청</a>
</div>
<script src="assets/js/config.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>'''


def page(fname, title, desc, body):
    html = head(title, desc, fname) + header(fname) + body + FOOTER
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return fname


def phead(eyebrow, h1, lead, img=None):
    """서브페이지 상단"""
    v = f'<div class="hero-visual rv"><img src="assets/img/{img}" alt="" loading="eager" width="1500" height="844"></div>' if img else ""
    grid = "hero-grid" if img else ""
    return f'''<section class="hero">
  <div class="wrap {grid}">
    <div class="rv">
      <span class="eyebrow">{eyebrow}</span>
      <h1 class="h1">{h1}</h1>
      <p class="lead" style="margin-top:18px">{lead}</p>
    </div>
    {v}
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# index.html
# ══════════════════════════════════════════════════════════
IDX = '''<section class="hero">
  <div class="wrap hero-grid">
    <div class="rv">
      <span class="badge"><i>OPEN 예정</i> 2027년 1월 서비스 개시</span>
      <h1 class="h1">한 장의 카드로<br>사고, <span class="o">보관하고</span>, 팔기까지</h1>
      <p class="lead">창고형 할인매장에서 사고, 지하 공유창고에 두고, 2층 스튜디오에서 팝니다.<br>오렌지 멤버십은 HMK 홀딩스그룹의 네 가지 사업과 제휴사 혜택을 하나로 묶은 생활 회원제입니다.</p>
      <div class="hero-price">
        <span class="lab">연회비</span>
        <span class="val">39,000원</span>
        <span class="sub">월 3,250원 · 하루 107원</span>
      </div>
      <div class="btn-row">
        <a href="join.html" class="btn btn-p btn-lg">사전 알림 신청하기</a>
        <a href="#calc-sec" class="btn btn-g btn-lg">내 혜택 계산해 보기</a>
      </div>
    </div>
    <div class="hero-visual rv">
      <img src="assets/img/hero-card.jpg" alt="HMK 오렌지 멤버십 카드" width="1500" height="844" fetchpriority="high">
      <div class="hero-float">
        <div class="k">가입 첫날 받는 혜택</div>
        <div class="v">114,000원<em>회비의 2.9배</em></div>
      </div>
    </div>
  </div>
</section>

<section class="sec-sm">
  <div class="wrap">
    <div class="statbar rv">
      <div><div class="k">연회비</div><div class="v">39,000원</div><div class="s">월 3,250원</div></div>
      <div><div class="k">가입 첫날 혜택</div><div class="v">114,000원</div><div class="s">회비의 2.9배</div></div>
      <div><div class="k">이용 가능한 사업</div><div class="v">3 + 1</div><div class="s">매장 · 창고 · 방송 · 온라인</div></div>
      <div><div class="k">제휴 카테고리</div><div class="v">13개</div><div class="s">자동차 · 이사 · 생활</div></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head center rv">
      <span class="eyebrow">Why Orange</span>
      <h2 class="h2">다른 멤버십과 무엇이 다른가</h2>
      <p class="lead">보통의 멤버십은 상품 마진을 깎아 할인을 만듭니다. 오렌지 멤버십은 직접 소유한 공간에서 혜택이 나옵니다.</p>
    </div>
    <div class="grid g3">
      <div class="card rv"><div class="ic">🏬</div>
        <span class="tag">SPACE</span>
        <h3>공간을 소유해서 줄 수 있는 혜택</h3>
        <p>비어 있는 창고 유닛과 예약이 없는 스튜디오 시간을 회원에게 내드립니다. 상품을 할인하는 방식으로는 만들 수 없는 크기의 혜택입니다.</p></div>
      <div class="card rv"><div class="ic">🔁</div>
        <span class="tag">CONNECTED</span>
        <h3>사는 사람이 파는 사람이 됩니다</h3>
        <p>1층에서 사고, 지하에 두고, 2층에서 방송으로 팝니다. 세 사업이 같은 건물 안에 있어서 가능한 동선입니다.</p></div>
      <div class="card rv"><div class="ic">🤝</div>
        <span class="tag">PARTNERS</span>
        <h3>제휴사에게 공간을 먼저 내드립니다</h3>
        <p>매장과 물류, 방송 채널을 제휴사에 제공하고 그 대가로 회원 혜택을 받아옵니다. 그래서 조건이 다릅니다.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">Benefits</span>
      <h2 class="h2">네 가지 사업, 하나의 회원증</h2>
      <p class="lead">회원증 한 장이 매장 할인, 창고 보관, 방송 판매, 온라인 주문을 모두 엽니다.</p>
    </div>
    <div class="grid g2">
      <article class="bizcard rv">
        <div class="ph"><img src="assets/img/biz-market.jpg" alt="오렌지 창고마켓 계산대" loading="lazy" width="1500" height="844"></div>
        <div class="bd">
          <span class="fl">1F</span>
          <h3>오렌지 창고마켓</h3>
          <p>창고형 할인매장. 팔레트 단위로 진열하고 회원가와 비회원가를 나란히 표시합니다.</p>
          <ul>
            <li>대표 품목 회원가 평균 7% 인하</li>
            <li>구매액 2% 오렌지 포인트 적립</li>
            <li>매장 당일 픽업 · 벌크 상품 회원 전용 단가</li>
          </ul>
        </div>
      </article>
      <article class="bizcard rv">
        <div class="ph"><img src="assets/img/biz-storage.jpg" alt="오렌지 공유창고" loading="lazy" width="1500" height="844"></div>
        <div class="bd">
          <span class="fl">B1</span>
          <h3>오렌지 공유창고</h3>
          <p>24시간 무인 운영 공유창고. 가입하면 첫 달을 무료로 써 보실 수 있습니다.</p>
          <ul>
            <li>가입 시 첫 달 무료 이용권</li>
            <li>등급별 이용료 요율 8~15% 인하</li>
            <li>매장에서 산 물건 3일 무료 보관</li>
          </ul>
        </div>
      </article>
      <article class="bizcard rv">
        <div class="ph"><img src="assets/img/biz-live.jpg" alt="오렌지 라이브쇼핑 스튜디오" loading="lazy" width="1500" height="844"></div>
        <div class="bd">
          <span class="fl">2F</span>
          <h3>오렌지 라이브쇼핑</h3>
          <p>라이브커머스 스튜디오. 촬영 장비 없이도 방송을 시작할 수 있습니다.</p>
          <ul>
            <li>회원 전용 방송 특가</li>
            <li>스튜디오 대관료 10~20% 인하</li>
            <li>프라임 회원 월 2시간 무료 이용</li>
          </ul>
        </div>
      </article>
      <article class="bizcard rv">
        <div class="ph"><img src="assets/img/card-app.jpg" alt="오렌지 멤버십 앱" loading="lazy" width="1500" height="844"></div>
        <div class="bd">
          <span class="fl">ONLINE</span>
          <h3>오렌지 온라인몰</h3>
          <p>매장과 같은 재고, 같은 가격. 주문하고 매장에서 바로 받으실 수 있습니다.</p>
          <ul>
            <li>오프라인과 동일한 회원가 적용</li>
            <li>무료배송 기준 금액 인하</li>
            <li>매장 픽업 시 1% 추가 적립</li>
          </ul>
        </div>
      </article>
    </div>
    <div class="btn-row rv" style="margin-top:36px; justify-content:center">
      <a href="benefits.html" class="btn btn-n">혜택 전체 보기</a>
    </div>
  </div>
</section>

<section class="sec warm" id="calc-sec">
  <div class="wrap">
    <div class="sec-head center rv">
      <span class="eyebrow">Calculator</span>
      <h2 class="h2">내가 받을 혜택을 계산해 보세요</h2>
      <p class="lead">평소 장보는 금액과 이용 계획을 넣으면 연간 예상 혜택 금액이 나옵니다.</p>
    </div>
    <div class="calc rv" id="calc">
      <div class="calc-in">
        <div class="fgrp">
          <label for="cShop">한 달 장보기 금액 <output id="oShop">12만원</output></label>
          <input type="range" id="cShop" min="0" max="50" step="1" value="12">
          <p class="small" style="margin-top:8px">오렌지 창고마켓과 온라인몰에서 쓰시는 금액을 합쳐서 넣어 주세요.</p>
        </div>
        <div class="fgrp">
          <label for="cStore">공유창고 월 이용료 <output id="oStore">8만원</output></label>
          <input type="range" id="cStore" min="0" max="30" step="1" value="8">
          <p class="small" style="margin-top:8px">이용 계획이 없으시면 0으로 두시면 됩니다.</p>
        </div>
        <div class="fgrp" style="margin-bottom:0">
          <label>이용하실 것 같은 제휴 서비스</label>
          <div class="chips">
            <label class="chip"><input type="checkbox" class="cP" value="car" checked><span>자동차 정비 · 타이어</span></label>
            <label class="chip"><input type="checkbox" class="cP" value="move"><span>이사 · 정리수납</span></label>
            <label class="chip"><input type="checkbox" class="cP" value="interior"><span>인테리어 · 가구</span></label>
            <label class="chip"><input type="checkbox" class="cP" value="health"><span>건강검진</span></label>
            <label class="chip"><input type="checkbox" class="cP" value="edu"><span>교육 · 학원</span></label>
            <label class="chip"><input type="checkbox" class="cP" value="telecom"><span>통신 요금</span></label>
          </div>
        </div>
      </div>
      <div class="calc-out">
        <div class="rlab">연간 예상 혜택 금액 <span style="opacity:.65">(첫해 기준)</span></div>
        <div class="rbig" id="rTotal">0원</div>
        <div class="rsub" id="rMult">연회비 39,000원의 0.0배</div>
        <div class="rrow"><span>회원가 절감</span><span id="rDisc">0원</span></div>
        <div class="rrow"><span>오렌지 포인트 적립</span><span id="rPoint">0P</span></div>
        <div class="rrow"><span>창고 이용료 인하</span><span id="rStore">0원</span></div>
        <div class="rrow"><span>제휴 혜택</span><span id="rPartner">0원</span></div>
        <div class="rrow"><span>웰컴 패키지 · 라운지</span><span id="rWelcome">0원</span></div>
        <div class="rtier" id="rTier">예상 등급 <b>오렌지</b></div>
      </div>
    </div>
    <p class="tbl-note rv" style="text-align:center; max-width:760px; margin:20px auto 0">계산 결과는 계획 중인 혜택 기준의 예상값입니다. 회원가 평균 인하율 7%, 등급별 적립률, 제휴 카테고리별 평균 절감액을 적용해 산정했으며, 웰컴 패키지 114,000원은 가입 첫해에만 지급됩니다. 실제 금액은 이용 내역과 상품에 따라 달라집니다.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center rv">
      <span class="eyebrow">Welcome Package</span>
      <h2 class="h2">가입한 날, 회비는 이미 돌아옵니다</h2>
      <p class="lead">39,000원을 결제하시면 그 자리에서 114,000원어치의 혜택을 받으십니다.</p>
    </div>
    <div class="split rv" style="margin-bottom:44px">
      <div class="sp-txt">
        <div class="tbl-wrap">
          <table>
            <thead><tr><th>구성</th><th>내용</th><th>가치</th></tr></thead>
            <tbody>
              <tr><td>오렌지 포인트</td><td>20,000P 즉시 지급</td><td class="hl">20,000원</td></tr>
              <tr><td>공유창고 첫 달 무료</td><td>미니 유닛 1개월</td><td class="hl">50,000원</td></tr>
              <tr><td>웰컴 쿠폰</td><td>5,000원 쿠폰 4매</td><td class="hl">20,000원</td></tr>
              <tr><td>무인카페 음료권</td><td>3개월간 월 4잔</td><td class="hl">24,000원</td></tr>
              <tr><td>합계</td><td>가입 즉시 지급</td><td class="hl">114,000원</td></tr>
            </tbody>
          </table>
        </div>
        <p class="tbl-note">쿠폰을 5,000원짜리 네 장으로 나눈 이유가 있습니다. 한 장이면 한 번 오시지만 네 장이면 네 번 오시게 됩니다. 오시는 동안 매장 동선에 익숙해지고, 지하 창고를 구경하시게 됩니다.</p>
      </div>
      <div><img src="assets/img/card-box.jpg" alt="오렌지 멤버십 웰컴 키트" loading="lazy" width="1500" height="844"></div>
    </div>
    <div class="note rv"><b>중도에 해지하셔도 손해 보지 않으십니다.</b> 가입 후 14일 이내에 혜택을 쓰지 않으셨다면 전액 환불해 드립니다. 그 이후에 해지하셔도 남은 기간만큼 일할로 계산해 돌려 드리며, 별도의 위약금은 없습니다.</div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head center rv">
      <span class="eyebrow">Membership Tiers</span>
      <h2 class="h2">회비는 하나, 등급은 쓰실수록 올라갑니다</h2>
      <p class="lead">등급을 올리려고 더 내실 필요가 없습니다. 이용 실적에 따라 자동으로 승급됩니다.</p>
    </div>
    <div class="tiers rv">
      <div class="tier">
        <div class="nm">오렌지</div>
        <div class="cond">연회비 39,000원 결제 시</div>
        <div class="rate">2.0<small>% 적립</small></div>
        <ul><li>회원가 적용</li><li>웰컴 패키지</li><li>무인카페 월 2잔</li><li>창고 첫 달 무료</li></ul>
      </div>
      <div class="tier feat">
        <div class="rib">가장 많이 도달하는 등급</div>
        <div class="nm">오렌지 플러스</div>
        <div class="cond">연 구매 120만원 또는<br>창고 3개월 이용</div>
        <div class="rate">2.5<small>% 적립</small></div>
        <ul><li>창고 요율 8% 인하</li><li>무인카페 월 4잔</li><li>오렌지 데이 선행 입장</li><li>무료배송 기준 인하</li></ul>
      </div>
      <div class="tier">
        <div class="nm">오렌지 프라임</div>
        <div class="cond">연 구매 360만원 또는<br>창고 12개월 이용</div>
        <div class="rate">3.0<small>% 적립</small></div>
        <ul><li>창고 요율 15% 인하</li><li>스튜디오 월 2시간 무료</li><li>무료배송 기준 없음</li><li>전용 상담창구</li></ul>
      </div>
      <div class="tier">
        <div class="nm">오렌지 비즈</div>
        <div class="cond">사업자등록증 인증 시<br>다른 등급과 함께 적용</div>
        <div class="rate">사입가<small>적용</small></div>
        <ul><li>사입 전용가</li><li>세금계산서 자동발행</li><li>창고 요율 10% 인하</li><li>셀러클럽 자동 가입</li></ul>
      </div>
    </div>
    <div class="btn-row rv" style="margin-top:34px; justify-content:center">
      <a href="tiers.html" class="btn btn-n">등급 자세히 보기</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split rv">
    <div class="sp-txt">
      <span class="eyebrow">Partners</span>
      <h2 class="h2">자동차부터 이사까지,<br>큰돈 쓰는 곳에서 아낍니다</h2>
      <p class="lead" style="margin:18px 0 24px">13개 카테고리의 제휴사가 오렌지 회원에게 별도 조건을 제공합니다. 장 보시는 동안 타이어를 교체하고, 이사하실 때 창고를 무료로 연장해 드립니다.</p>
      <ul class="chk">
        <li>타이어 교체 공임 면제 · 정비 회원가</li>
        <li>이사 견적 회원가 · 이사 기간 창고 무료 연장</li>
        <li>인테리어 시공 회원가 · 가구 배송 전 무료 보관</li>
        <li>건강검진 · 교육 · 통신 요금 회원 전용 조건</li>
      </ul>
      <div class="btn-row" style="margin-top:28px"><a href="partners.html" class="btn btn-p">제휴 혜택 전체 보기</a></div>
    </div>
    <div><img src="assets/img/card-tap.jpg" alt="오렌지 멤버십 카드 결제" loading="lazy" width="1500" height="844"></div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head center rv">
      <span class="eyebrow">How to use</span>
      <h2 class="h2">쓰는 방법은 간단합니다</h2>
    </div>
    <div class="steps rv">
      <div class="step"><h3>가입하고 카드를 받습니다</h3><p>앱이나 매장 안내 데스크에서 가입하시면 실물 카드를 드립니다. 앱이 익숙하지 않으셔도 휴대폰 번호만으로 이용하실 수 있습니다.</p></div>
      <div class="step"><h3>계산대에서 보여 주십니다</h3><p>카드나 앱 바코드를 보여 주시면 회원가가 자동으로 적용되고 포인트가 쌓입니다. 따로 쿠폰을 찾으실 필요가 없습니다.</p></div>
      <div class="step"><h3>쌓인 포인트로 다음 회비를 냅니다</h3><p>오렌지 포인트는 1원 단위로 쓰실 수 있고, 다음 해 연회비로도 쓰실 수 있습니다. 연 120만원 정도 구매하시면 회비가 거의 채워집니다.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split rev rv">
    <div><img src="assets/img/biz-reception.jpg" alt="오렌지 라운지 안내 데스크" loading="lazy" width="1500" height="844"></div>
    <div class="sp-txt">
      <span class="eyebrow">Community</span>
      <h2 class="h2">할인이 아니라 관계로 남는<br>멤버십을 만들고 있습니다</h2>
      <p class="lead" style="margin:18px 0 24px">공유창고 라운지와 24시간 무인카페를 회원 공간으로 씁니다. 사업자 회원은 오렌지 셀러클럽에 자동으로 가입되어 사입 정보와 방송 노하우를 나눕니다.</p>
      <ul class="chk">
        <li>오렌지 라운지 — 무인카페 무료 음료, 모임 공간 예약</li>
        <li>오렌지 셀러클럽 — 정기모임, 합동 라이브, 실무 세미나</li>
        <li>오렌지 크루 — 후기 · 방송 참여로 등급 승급</li>
      </ul>
      <div class="btn-row" style="margin-top:28px"><a href="community.html" class="btn btn-g">커뮤니티 살펴보기</a></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap-n">
    <div class="sec-head center rv"><span class="eyebrow">FAQ</span><h2 class="h2">자주 묻는 질문</h2></div>
    <div class="acc rv">
      <div class="acc-i"><button class="acc-q">회원이 아니면 매장에 들어갈 수 없나요?</button>
        <div class="acc-a"><div>아닙니다. 오렌지 창고마켓은 누구나 들어오실 수 있습니다. 회원이 되시면 같은 상품을 회원가로 사시고 포인트가 쌓입니다. 매대에는 회원가와 비회원가를 나란히 표시합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">연회비 39,000원은 언제 내나요?</button>
        <div class="acc-a"><div>가입하실 때 1년치를 한 번에 결제하십니다. 이용 기간은 결제일부터 365일이며, 해지하지 않으시면 자동으로 갱신됩니다. 갱신 30일 전과 7일 전에 두 번 알려 드리고, 자동갱신은 언제든 해제하실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">중간에 해지하면 환불되나요?</button>
        <div class="acc-a"><div>가입 후 14일 이내이고 혜택을 쓰지 않으셨다면 전액 환불해 드립니다. 그 이후에는 남은 기간만큼 일할로 계산해 돌려 드리며, 이미 쓰신 웰컴 혜택의 실비만 차감합니다. <strong>위약금은 없습니다.</strong> 해지는 앱 마이페이지, 고객센터, 매장 안내 데스크 어디서나 가능합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">가족도 같이 쓸 수 있나요?</button>
        <div class="acc-a"><div>같은 세대의 가족 3명까지 추가 비용 없이 등록하실 수 있습니다. 가족 회원도 회원가로 구매하시고, 쌓인 포인트는 대표 회원 계정으로 합산되어 함께 쓰실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">스마트폰이 익숙하지 않아도 쓸 수 있나요?</button>
        <div class="acc-a"><div>네. 실물 회원카드를 드리고, 카드가 없으셔도 휴대폰 번호만 말씀하시면 회원 확인이 됩니다. 매장 안내 데스크에서 가입과 조회를 도와 드립니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">언제부터 가입할 수 있나요?</button>
        <div class="acc-a"><div>2027년 1월 서비스 개시를 목표로 준비하고 있습니다. 사전 알림을 신청해 주시면 오픈 일정이 확정되는 대로 문자로 알려 드립니다.</div></div></div>
    </div>
    <div class="btn-row rv" style="margin-top:28px; justify-content:center"><a href="guide.html#faq" class="btn btn-g">질문 더 보기</a></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cta rv">
      <h2 class="h2">오픈 소식을 가장 먼저 받아 보세요</h2>
      <p>사전 알림을 신청하신 분께는 오픈 일정과 초기 가입 안내를 문자로 보내 드립니다. 신청에 비용이 들지 않으며, 가입 의무도 없습니다.</p>
      <div class="btn-row"><a href="join.html" class="btn btn-p btn-lg">사전 알림 신청하기</a><a href="benefits.html" class="btn btn-g btn-lg">혜택 다시 보기</a></div>
    </div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# benefits.html
# ══════════════════════════════════════════════════════════
BEN = phead("Benefits", "혜택 안내", "오렌지 멤버십 회원이 네 가지 사업에서 받으시는 혜택을 한곳에 모았습니다. 등급이 올라가면 혜택도 함께 늘어납니다.", "card-duo.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Welcome</span><h2 class="h2">가입하시면 바로 받는 것</h2>
      <p class="lead">연회비 39,000원을 결제하신 그 자리에서 드립니다.</p></div>
    <div class="grid g4 rv">
      <div class="card"><div class="ic">🎁</div><h3>오렌지 포인트 20,000P</h3><p>가입 즉시 지급합니다. 매장, 온라인몰, 창고 이용료에 1원 단위로 쓰실 수 있습니다. 지급일부터 90일간 유효합니다.</p></div>
      <div class="card"><div class="ic">📦</div><h3>공유창고 첫 달 무료</h3><p>미니 유닛 한 칸을 한 달간 무료로 쓰실 수 있습니다. 계절 옷, 캠핑 장비, 아이 물건을 넣어 보시면 됩니다.</p></div>
      <div class="card"><div class="ic">🎟️</div><h3>웰컴 쿠폰 4매</h3><p>3만원 이상 구매 시 쓰실 수 있는 5,000원 쿠폰 네 장. 지급일부터 90일간 유효합니다.</p></div>
      <div class="card"><div class="ic">☕</div><h3>무인카페 음료 12잔</h3><p>3개월간 매달 네 잔씩 드립니다. 창고에 들르시거나 라운지에 앉으실 때 쓰시면 됩니다.</p></div>
    </div>
    <div class="note rv" style="margin-top:30px"><b>합계 114,000원.</b> 연회비 39,000원의 2.9배입니다. 가입 후 14일 안에 혜택을 쓰지 않으셨다면 전액 환불해 드립니다.</div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">1F · Warehouse Market</span><h2 class="h2">오렌지 창고마켓</h2>
      <p class="lead">팔레트 단위로 진열하는 창고형 할인매장입니다. 회원가와 비회원가를 매대에 나란히 표시합니다.</p></div>
    <div class="split rv">
      <div class="sp-txt">
        <ul class="chk">
          <li><b>회원가 적용</b> — 대표 품목 평균 7% 인하, 계산대에서 자동 적용</li>
          <li><b>구매액 2% 적립</b> — 등급이 오르면 2.5%, 3.0%로 올라갑니다</li>
          <li><b>오렌지 데이</b> — 매월 셋째 주 토요일, 추가 2% 적립</li>
          <li><b>매장 당일 픽업</b> — 온라인으로 주문하고 매장에서 바로 수령</li>
          <li><b>벌크 상품 회원 전용 단가</b> — 대량 구매 시 고정 게시 가격</li>
          <li><b>구매 후 3일 무료 보관</b> — 많이 사셔도 지하에 맡기고 가시면 됩니다</li>
        </ul>
      </div>
      <div><img src="assets/img/biz-market.jpg" alt="오렌지 창고마켓" loading="lazy" width="1500" height="844"></div>
    </div>
    <div class="note nv rv" style="margin-top:34px"><b>집에 둘 곳이 없어 못 사시던 물건.</b> 창고형 매장에서 가장 큰 벽은 가격이 아니라 보관입니다. 지하에 창고가 있으면 이 벽이 사라집니다. 사시고 3일간 맡겨 두셨다가 편하실 때 가져가시면 됩니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">B1 · Shared Storage</span><h2 class="h2">오렌지 공유창고</h2>
      <p class="lead">24시간 무인으로 운영합니다. 출입은 QR과 얼굴 인식으로 하시고, 라운지와 무인카페가 함께 있습니다.</p></div>
    <div class="split rev rv">
      <div><img src="assets/img/biz-storage.jpg" alt="오렌지 공유창고" loading="lazy" width="1500" height="844"></div>
      <div class="sp-txt">
        <ul class="chk">
          <li><b>가입 시 첫 달 무료</b> — 미니 유닛 한 칸, 계약 의무 없음</li>
          <li><b>이용료 요율 인하</b> — 플러스 8%, 프라임 15%, 비즈 10%</li>
          <li><b>이용료 2% 적립</b> — 창고 이용료에도 포인트가 쌓입니다</li>
          <li><b>계약 연장 시 매달 5,000P</b> — 오래 쓰실수록 돌려받습니다</li>
          <li><b>포장재 회원가</b> — 박스, 완충재, 자물쇠를 1층에서 회원가로</li>
          <li><b>라운지 · 무인카페 이용</b> — 등급별 월 2~4잔 무료</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">2F · Live Commerce</span><h2 class="h2">오렌지 라이브쇼핑</h2>
      <p class="lead">라이브커머스 스튜디오입니다. 조명과 카메라, 송출 장비가 갖춰져 있어 몸만 오시면 됩니다.</p></div>
    <div class="split rv">
      <div class="sp-txt">
        <ul class="chk">
          <li><b>회원 전용 방송 특가</b> — 방송 중에만 열리는 회원가</li>
          <li><b>시청 후 구매 시 1% 추가 적립</b></li>
          <li><b>스튜디오 대관료 인하</b> — 일반 10%, 오렌지 비즈 20%</li>
          <li><b>프라임 회원 월 2시간 무료</b></li>
          <li><b>촬영 · 편집 대행 회원가</b> — 처음이시면 제작을 도와 드립니다</li>
          <li><b>비즈 회원 방송 편성 우선 배정</b></li>
        </ul>
      </div>
      <div><img src="assets/img/biz-live.jpg" alt="오렌지 라이브쇼핑 스튜디오" loading="lazy" width="1500" height="844"></div>
    </div>
    <div class="note rv" style="margin-top:34px"><b>사시던 분이 파시는 분이 되실 수 있습니다.</b> 1층에서 사입하시고, 지하에 재고를 두시고, 2층에서 방송으로 파십니다. 사업자등록증을 인증하시면 오렌지 비즈 조건이 적용됩니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Online</span><h2 class="h2">오렌지 온라인몰</h2>
      <p class="lead">매장과 같은 재고, 같은 가격입니다. 온라인으로 주문하시고 매장에서 받으시면 배송비가 들지 않습니다.</p></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">🛒</div><h3>동일 회원가</h3><p>오프라인 매장과 같은 회원가가 적용됩니다. 온라인이라고 다르지 않습니다.</p></div>
      <div class="card"><div class="ic">🚚</div><h3>무료배송 기준 인하</h3><p>플러스는 더 낮아지고, 프라임은 금액 제한이 없습니다.</p></div>
      <div class="card"><div class="ic">📍</div><h3>매장 당일 픽업</h3><p>주문하시고 당일 매장에서 수령하실 수 있습니다. 픽업하시면 1% 추가 적립됩니다.</p></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">All Benefits</span><h2 class="h2">등급별 혜택 한눈에 보기</h2></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>구분</th><th>혜택</th><th>오렌지</th><th>플러스</th><th>프라임</th><th>비즈</th></tr></thead>
        <tbody>
          <tr><td rowspan="3">적립</td><td style="text-align:left">구매 적립률</td><td class="hl">2.0%</td><td class="hl">2.5%</td><td class="hl">3.0%</td><td>등급 적용</td></tr>
          <tr><td style="text-align:left">오렌지 데이 추가</td><td>+2%</td><td>+2%</td><td>+2%</td><td>+2%</td></tr>
          <tr><td style="text-align:left">방송 시청 후 구매 · 픽업</td><td>+1%</td><td>+1%</td><td>+1%</td><td>+1%</td></tr>
          <tr><td rowspan="3">창고마켓</td><td style="text-align:left">회원가 적용</td><td>○</td><td>○</td><td>○</td><td class="hl">사입가</td></tr>
          <tr><td style="text-align:left">오렌지 데이 선행 입장</td><td>—</td><td>1시간</td><td>1시간</td><td>1시간</td></tr>
          <tr><td style="text-align:left">세금계산서 자동발행</td><td>—</td><td>—</td><td>—</td><td>○</td></tr>
          <tr><td rowspan="3">공유창고</td><td style="text-align:left">첫 달 무료 이용권</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td style="text-align:left">이용료 요율 인하</td><td>—</td><td class="hl">8%</td><td class="hl">15%</td><td class="hl">10%</td></tr>
          <tr><td style="text-align:left">구매 후 3일 무료 보관</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td rowspan="3">라이브쇼핑</td><td style="text-align:left">회원 전용 방송 특가</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td style="text-align:left">스튜디오 대관료 인하</td><td>10%</td><td>10%</td><td>10%</td><td class="hl">20%</td></tr>
          <tr><td style="text-align:left">스튜디오 무료 이용</td><td>—</td><td>—</td><td class="hl">월 2시간</td><td>—</td></tr>
          <tr><td rowspan="3">온라인몰</td><td style="text-align:left">동일 회원가</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td style="text-align:left">무료배송 기준</td><td>인하</td><td>추가 인하</td><td class="hl">제한 없음</td><td>별도 견적</td></tr>
          <tr><td style="text-align:left">매장 당일 픽업</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td rowspan="2">라운지</td><td style="text-align:left">무인카페 무료 음료</td><td>월 2잔</td><td>월 4잔</td><td>월 4잔</td><td>월 4잔</td></tr>
          <tr><td style="text-align:left">모임 공간 예약</td><td>○</td><td>○</td><td class="hl">우선</td><td>○</td></tr>
          <tr><td rowspan="3">기타</td><td style="text-align:left">제휴 13개 카테고리</td><td>○</td><td>○</td><td class="hl">상위 혜택</td><td>사업자 전용</td></tr>
          <tr><td style="text-align:left">가족 회원 3인 공유</td><td>○</td><td>○</td><td>○</td><td>○</td></tr>
          <tr><td style="text-align:left">전용 상담창구</td><td>—</td><td>—</td><td>○</td><td>○</td></tr>
        </tbody>
      </table>
    </div>
    <p class="tbl-note rv">위 내용은 2027년 1월 시행을 목표로 준비 중인 계획안입니다. 혜택의 이용 조건과 횟수는 시행 시점에 회원 약관과 함께 확정 공지합니다.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap"><div class="cta rv">
    <h2 class="h2">혜택을 직접 계산해 보세요</h2>
    <p>평소 장보는 금액을 넣으시면 연간 예상 혜택 금액이 바로 나옵니다.</p>
    <div class="btn-row"><a href="index.html#calc-sec" class="btn btn-p btn-lg">혜택 계산해 보기</a><a href="join.html" class="btn btn-g btn-lg">사전 알림 신청</a></div>
  </div></div>
</section>'''


# ══════════════════════════════════════════════════════════
# tiers.html
# ══════════════════════════════════════════════════════════
TIER = phead("Tiers &amp; Fee", "등급 · 회비", "연회비는 39,000원 하나입니다. 등급을 올리려고 더 내실 필요가 없고, 쓰시는 만큼 자동으로 올라갑니다.", "card-hand.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="statbar rv">
      <div><div class="k">연회비</div><div class="v">39,000원</div><div class="s">부가세 포함</div></div>
      <div><div class="k">월 환산</div><div class="v">3,250원</div><div class="s">커피 한 잔 값</div></div>
      <div><div class="k">유료 등급</div><div class="v">1개</div><div class="s">나머지는 무상 승급</div></div>
      <div><div class="k">가족 공유</div><div class="v">3인</div><div class="s">추가 비용 없음</div></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head center rv"><span class="eyebrow">Tiers</span><h2 class="h2">네 개의 등급</h2>
      <p class="lead">가입하시면 오렌지 등급으로 시작합니다. 이용 실적이 쌓이면 요건을 채우신 날 바로 승급되고, 신청하실 필요가 없습니다.</p></div>
    <div class="tiers rv">
      <div class="tier">
        <div class="nm">오렌지</div>
        <div class="cond">연회비 39,000원 결제</div>
        <div class="rate">2.0<small>% 적립</small></div>
        <ul><li>회원가 적용</li><li>웰컴 패키지 114,000원</li><li>공유창고 첫 달 무료</li><li>무인카페 월 2잔</li><li>구매 후 3일 무료 보관</li><li>가족 회원 3인 공유</li></ul>
      </div>
      <div class="tier feat">
        <div class="rib">가장 많이 도달하는 등급</div>
        <div class="nm">오렌지 플러스</div>
        <div class="cond">연 누적 구매 120만원<br>또는 창고 3개월 이용<br>또는 커뮤니티 300점</div>
        <div class="rate">2.5<small>% 적립</small></div>
        <ul><li>창고 이용료 8% 인하</li><li>무인카페 월 4잔</li><li>오렌지 데이 1시간 선행 입장</li><li>무료배송 기준 추가 인하</li><li>오렌지 등급 혜택 전부 포함</li></ul>
      </div>
      <div class="tier">
        <div class="nm">오렌지 프라임</div>
        <div class="cond">연 누적 구매 360만원<br>또는 창고 12개월 이용<br>또는 커뮤니티 800점</div>
        <div class="rate">3.0<small>% 적립</small></div>
        <ul><li>창고 이용료 15% 인하</li><li>스튜디오 월 2시간 무료</li><li>유닛 사이즈 무상 변경 연 1회</li><li>무료배송 금액 제한 없음</li><li>라운지 우선 예약 · 전용 상담창구</li></ul>
      </div>
      <div class="tier">
        <div class="nm">오렌지 비즈</div>
        <div class="cond">사업자등록증 인증<br>다른 등급과 함께 적용<br>회비는 동일</div>
        <div class="rate">사입가<small>적용</small></div>
        <ul><li>사입 전용가</li><li>세금계산서 자동발행</li><li>창고 요율 10% 인하</li><li>스튜디오 대관료 20% 인하</li><li>방송 편성 우선 배정</li><li>셀러클럽 자동 가입</li></ul>
      </div>
    </div>
    <div class="note rv" style="margin-top:34px"><b>오렌지 비즈는 등급이 아니라 트랙입니다.</b> 사업자등록증을 인증하시면 기존 등급과 함께 적용되어 &lsquo;오렌지 프라임 · 비즈&rsquo;처럼 표시됩니다. 회비는 39,000원으로 같고, 혜택 구성만 사업자에게 맞게 바뀝니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Rules</span><h2 class="h2">등급 운영 규칙</h2></div>
    <div class="grid g2 rv">
      <div class="card"><div class="ic">⬆️</div><h3>승급은 요건을 채우신 날 바로</h3><p>세 가지 요건 중 하나만 채우시면 됩니다. 회사가 자동으로 확인해 승급 처리하고 앱으로 알려 드립니다. 따로 신청하실 필요가 없습니다.</p></div>
      <div class="card"><div class="ic">⬇️</div><h3>강등은 갱신 시점에만</h3><p>이용 기간 중에는 등급이 내려가지 않습니다. 갱신 시점에만 조정되며, 3개월 전에 미리 알려 드리고 등급을 유지하실 방법도 함께 안내합니다.</p></div>
      <div class="card"><div class="ic">💾</div><h3>이미 쌓인 것은 그대로</h3><p>등급이 내려가도 이미 적립하신 포인트와 이미 발급된 혜택은 그대로 유지됩니다. 소급해서 회수하지 않습니다.</p></div>
      <div class="card"><div class="ic">🏆</div><h3>커뮤니티 활동으로도 올라갑니다</h3><p>구매 금액이 크지 않으셔도 후기 작성, 라운지 프로그램 참여, 회원 추천으로 점수를 쌓으시면 승급하실 수 있습니다.</p></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Fee</span><h2 class="h2">회비와 결제 조건</h2></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>항목</th><th>조건</th></tr></thead>
        <tbody>
          <tr><td>연회비</td><td style="text-align:left">39,000원 (부가가치세 포함)</td></tr>
          <tr><td>결제 방식</td><td style="text-align:left">가입 시 1년치 일시 결제. 이용 기간은 결제일부터 365일</td></tr>
          <tr><td>자동갱신</td><td style="text-align:left">해지하지 않으시면 자동 갱신. 이용 기간 중 언제든 해제 가능</td></tr>
          <tr><td>갱신 고지</td><td style="text-align:left">갱신 30일 전과 7일 전 두 번, 앱 · 문자 · 이메일로 안내</td></tr>
          <tr><td>전액 환불</td><td style="text-align:left">가입 후 14일 이내 · 혜택 미사용 시 전액 환불</td></tr>
          <tr><td>중도 해지</td><td style="text-align:left">언제든 가능. 남은 기간만큼 일할 환급. 위약금 없음</td></tr>
          <tr><td>웰컴 혜택 정산</td><td style="text-align:left">이미 쓰신 웰컴 혜택의 실비만 환급액에서 차감</td></tr>
          <tr><td>가족 회원</td><td style="text-align:left">같은 세대 3인까지 추가 비용 없이 등록. 포인트 합산 사용</td></tr>
          <tr><td>회비 인상</td><td style="text-align:left">초기 3년간 39,000원 유지 계획. 인상 시 3개월 전 고지 · 별도 동의 확인</td></tr>
        </tbody>
      </table>
    </div>
    <div class="note rv" style="margin-top:30px"><b>해지는 가입만큼 쉬워야 한다고 봅니다.</b> 앱 마이페이지에서 세 번 안에 해지하실 수 있고, 고객센터와 매장 안내 데스크에서도 됩니다. 해지 화면에서 환급 예정 금액과 차감 내역을 미리 보여 드립니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Break-even</span><h2 class="h2">얼마나 쓰면 회비를 넘길까요</h2>
      <p class="lead">회원가 절감과 적립만 놓고 계산하면 이렇게 나옵니다. 웰컴 패키지 114,000원은 여기 포함하지 않았습니다.</p></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>월 장보기 금액</th><th>연간 구매액</th><th>도달 등급</th><th>회원가 절감</th><th>포인트 적립</th><th>합계</th></tr></thead>
        <tbody>
          <tr><td>5만원</td><td>60만원</td><td>오렌지</td><td>42,000원</td><td>12,000P</td><td class="hl">54,000원</td></tr>
          <tr><td>8만원</td><td>96만원</td><td>오렌지</td><td>67,200원</td><td>19,200P</td><td class="hl">86,400원</td></tr>
          <tr><td>12만원</td><td>144만원</td><td>플러스</td><td>100,800원</td><td>36,000P</td><td class="hl">136,800원</td></tr>
          <tr><td>20만원</td><td>240만원</td><td>플러스</td><td>168,000원</td><td>60,000P</td><td class="hl">228,000원</td></tr>
          <tr><td>30만원</td><td>360만원</td><td>프라임</td><td>252,000원</td><td>108,000P</td><td class="hl">360,000원</td></tr>
        </tbody>
      </table>
    </div>
    <p class="tbl-note rv">회원가 평균 인하율 7% 기준으로 산정한 예상값입니다. 상품과 시기에 따라 적용 폭이 달라지며 모든 상품에 회원가가 적용되지는 않습니다.</p>
    <div class="note nv rv" style="margin-top:26px"><b>장을 다섯 번 보시면 회비만큼 아끼십니다.</b> 한 번에 8만원어치 장을 보시면 회원가로 5,600원, 적립으로 1,600원, 합쳐서 7,200원이 돌아옵니다. 다섯 번이면 36,000원, 여섯 번이면 회비를 넘습니다.</div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap"><div class="cta rv">
    <h2 class="h2">아직 가입은 시작되지 않았습니다</h2>
    <p>2027년 1월 서비스 개시를 목표로 준비하고 있습니다. 사전 알림을 신청하시면 오픈 일정을 가장 먼저 알려 드립니다.</p>
    <div class="btn-row"><a href="join.html" class="btn btn-p btn-lg">사전 알림 신청하기</a></div>
  </div></div>
</section>'''


# ══════════════════════════════════════════════════════════
# points.html
# ══════════════════════════════════════════════════════════
PTS = phead("Orange Point", "오렌지 포인트", "1포인트가 1원입니다. 매장, 온라인몰, 창고 이용료, 스튜디오 대관료에 1원 단위로 쓰실 수 있고, 다음 해 연회비로도 쓰실 수 있습니다.", "app-mockup.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">How to earn</span><h2 class="h2">이렇게 쌓입니다</h2></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>적립 항목</th><th>오렌지</th><th>플러스</th><th>프라임</th><th>설명</th></tr></thead>
        <tbody>
          <tr><td>구매 적립</td><td class="hl">2.0%</td><td class="hl">2.5%</td><td class="hl">3.0%</td><td style="text-align:left">매장 · 온라인몰 · 창고 이용료 · 스튜디오 대관료</td></tr>
          <tr><td>오렌지 데이</td><td>+2%</td><td>+2%</td><td>+2%</td><td style="text-align:left">매월 셋째 주 토요일</td></tr>
          <tr><td>방송 시청 후 구매</td><td>+1%</td><td>+1%</td><td>+1%</td><td style="text-align:left">라이브쇼핑 시청 후 당일 구매</td></tr>
          <tr><td>매장 픽업</td><td>+1%</td><td>+1%</td><td>+1%</td><td style="text-align:left">온라인 주문을 매장에서 수령</td></tr>
          <tr><td>후기 작성</td><td colspan="3">500P (사진 포함 시 1,000P)</td><td style="text-align:left">구매하신 상품에 대한 후기</td></tr>
          <tr><td>창고 계약 연장</td><td colspan="3">월 5,000P</td><td style="text-align:left">공유창고 계약을 유지하실 때마다</td></tr>
          <tr><td>회원 추천</td><td colspan="3">추천인 5,000P · 신규 3,000P</td><td style="text-align:left">추천으로 가입이 완료된 경우</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Fee coverage</span><h2 class="h2">쌓인 포인트로 다음 회비를 내실 수 있습니다</h2>
      <p class="lead">갱신할 때 새로 돈을 내시는 게 아니라 이미 가지고 계신 것을 쓰시게 됩니다.</p></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>연간 구매액</th><th>기본 적립</th><th>행사 · 활동 적립</th><th>연간 누적</th><th>회비 충당률</th></tr></thead>
        <tbody>
          <tr><td>60만원</td><td>12,000P</td><td>4,000P</td><td>16,000P</td><td>41%</td></tr>
          <tr><td>120만원</td><td>24,000~30,000P</td><td>8,000P</td><td>32,000~38,000P</td><td class="hl">82~97%</td></tr>
          <tr><td>240만원</td><td>48,000~60,000P</td><td>14,000P</td><td>62,000~74,000P</td><td class="hl">159~190%</td></tr>
          <tr><td>360만원 이상</td><td>72,000~108,000P</td><td>20,000P</td><td>92,000~128,000P</td><td class="hl">236~328%</td></tr>
        </tbody>
      </table>
    </div>
    <p class="tbl-note rv">행사·활동 적립은 오렌지 데이 4회 참여, 후기 6건 작성, 픽업 8회 이용을 가정한 값입니다. 실제 적립액은 이용 내역에 따라 달라집니다.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Rules</span><h2 class="h2">포인트 이용 규칙</h2></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">1️⃣</div><h3>1포인트부터 사용</h3><p>최소 사용 금액 제한이 없습니다. 1원 단위로 쓰시면 됩니다.</p></div>
      <div class="card"><div class="ic">📅</div><h3>유효기간 24개월</h3><p>적립일부터 24개월간 유효합니다. 소멸 30일 전에 앱과 문자로 알려 드리며, 알려 드리지 않은 포인트는 소멸시키지 않습니다.</p></div>
      <div class="card"><div class="ic">👨‍👩‍👧</div><h3>가족 합산 사용</h3><p>가족 회원이 적립한 포인트는 대표 회원 계정으로 합산되어 함께 쓰실 수 있습니다.</p></div>
      <div class="card"><div class="ic">🚫</div><h3>현금 충전은 하지 않습니다</h3><p>구매와 활동으로만 쌓이는 적립형입니다. 현금으로 충전하시거나 현금으로 돌려받으실 수는 없습니다.</p></div>
      <div class="card"><div class="ic">↩️</div><h3>취소 시 회수</h3><p>구매를 취소하거나 반품하시면 해당 거래로 적립된 포인트는 회수됩니다.</p></div>
      <div class="card"><div class="ic">💳</div><h3>연회비 결제 가능</h3><p>다음 이용 기간의 연회비를 포인트로 결제하실 수 있습니다.</p></div>
    </div>
    <div class="note nv rv" style="margin-top:30px"><b>현금 충전을 만들지 않은 이유.</b> 현금을 넣어 여러 곳에서 쓰는 수단은 관련 법령상 별도의 등록 의무가 생길 수 있습니다. 오렌지 포인트는 구매와 활동으로만 쌓이는 적립형으로 운영하고, 사용처는 HMK 홀딩스그룹 사업으로 한정합니다.</div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap split rv">
    <div class="sp-txt">
      <span class="eyebrow">Transparency</span>
      <h2 class="h2">얼마나 아끼셨는지<br>계속 보여 드리겠습니다</h2>
      <p class="lead" style="margin:18px 0 24px">멤버십의 가장 흔한 문제는 실제로 많이 받으셨는데도 그걸 모르신다는 점입니다. 영수증과 앱에서 누적 절감액을 계속 보여 드리려고 합니다.</p>
      <ul class="chk">
        <li>영수증에 이번 구매 절감액과 올해 누적 절감액 표시</li>
        <li>앱 첫 화면에 연회비 회수율을 진행률로 표시</li>
        <li>갱신 60일 전에 &lsquo;올해 아낀 금액&rsquo; 리포트 발송</li>
        <li>소멸 예정 포인트는 30일 전에 개별 안내</li>
      </ul>
    </div>
    <div><img src="assets/img/card-app.jpg" alt="오렌지 멤버십 앱 화면" loading="lazy" width="1500" height="844"></div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# partners.html
# ══════════════════════════════════════════════════════════
PTN = phead("Partners", "제휴 혜택", "13개 카테고리의 제휴사가 오렌지 회원에게 별도 조건을 제공합니다. 큰돈이 나가는 곳에서 크게 아끼시도록 구성했습니다.", "card-wallet.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Anchor</span><h2 class="h2">매장에서 바로 이용하시는 제휴</h2>
      <p class="lead">매장 안과 주차장에 제휴사 서비스를 놓습니다. 장 보시는 동안 일이 끝나 있게 만드는 것이 목표입니다.</p></div>
    <div class="grid g2 rv">
      <div class="card"><div class="ic">🚗</div><span class="tag">01 · 자동차</span><h3>정비 · 타이어 · 중고차 · 렌터카 · 충전</h3>
        <p>매장 옆 부스에서 타이어를 교체하고, 주차장에서 중고차를 보시고, 전기차를 충전하십니다.</p>
        <ul style="margin-top:16px; border-top:1px solid var(--line-2); padding-top:14px">
          <li style="font-size:14.8px; padding:5px 0">· 타이어 교체 공임 면제 · 엔진오일 회원가</li>
          <li style="font-size:14.8px; padding:5px 0">· 중고차 회원 전용가 · 성능점검 무료</li>
          <li style="font-size:14.8px; padding:5px 0">· 장기렌트 선수금 인하 · 충전 요금 회원가</li>
          <li style="font-size:14.8px; padding:5px 0">· 신차 회원 전용 견적 · 출고 지원</li>
        </ul></div>
      <div class="card"><div class="ic">📦</div><span class="tag">02 · 이사 · 보관</span><h3>포장이사 · 정리수납 · 용달</h3>
        <p>이사는 공유창고와 가장 잘 맞는 제휴입니다. 짐을 맡기시고 여유 있게 이사하십니다.</p>
        <ul style="margin-top:16px; border-top:1px solid var(--line-2); padding-top:14px">
          <li style="font-size:14.8px; padding:5px 0">· 이사 견적 회원가</li>
          <li style="font-size:14.8px; padding:5px 0">· 이사 기간 창고 무료 연장</li>
          <li style="font-size:14.8px; padding:5px 0">· 정리수납 첫 상담 무료</li>
        </ul></div>
      <div class="card"><div class="ic">🛋️</div><span class="tag">03 · 인테리어 · 가구</span><h3>시공 · 가구 · 조명 · 홈퍼니싱</h3>
        <p>1층 리빙존에서 실물을 보시고, 시공 전까지 자재와 가구를 지하에 보관하십니다.</p>
        <ul style="margin-top:16px; border-top:1px solid var(--line-2); padding-top:14px">
          <li style="font-size:14.8px; padding:5px 0">· 시공 견적 회원가</li>
          <li style="font-size:14.8px; padding:5px 0">· 가구 배송 전 무료 보관</li>
          <li style="font-size:14.8px; padding:5px 0">· 샘플 상담 우선 예약</li>
        </ul></div>
      <div class="card"><div class="ic">🔌</div><span class="tag">04 · 가전 · 렌탈</span><h3>정수기 · 안마의자 · 매트리스 · 대형가전</h3>
        <p>1층 체험존에서 직접 써 보시고 결정하십니다.</p>
        <ul style="margin-top:16px; border-top:1px solid var(--line-2); padding-top:14px">
          <li style="font-size:14.8px; padding:5px 0">· 렌탈 등록비 면제</li>
          <li style="font-size:14.8px; padding:5px 0">· 의무 사용기간 단축</li>
          <li style="font-size:14.8px; padding:5px 0">· 회원 전용 렌탈료</li>
        </ul></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Everyday</span><h2 class="h2">생활에서 자주 쓰시는 제휴</h2></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">📱</div><span class="tag">05 · 통신</span><h3>알뜰폰 · 인터넷 · IPTV</h3><p>매장 안 개통 카운터에서 바로 처리하십니다. 회원 전용 요금제와 개통 시 포인트를 드립니다.</p></div>
      <div class="card"><div class="ic">⛽</div><span class="tag">06 · 주유 · 충전</span><h3>주유소 · 전기차 충전</h3><p>리터당 할인과 충전 요금 회원가. 충전하시는 동안 라운지를 무료로 쓰실 수 있습니다.</p></div>
      <div class="card"><div class="ic">🍽️</div><span class="tag">07 · 식음료 · 외식</span><h3>지역 프랜차이즈 · 베이커리 · 커피</h3><p>매장에 입점한 브랜드와 지역 가맹점에서 회원 할인이 적용됩니다.</p></div>
      <div class="card"><div class="ic">🐾</div><span class="tag">08 · 반려동물</span><h3>사료 · 용품 · 동물병원 · 미용</h3><p>사료는 대량 구매가 이득입니다. 사시고 지하에 두셨다가 필요할 때 가져가십니다.</p></div>
      <div class="card"><div class="ic">🩺</div><span class="tag">09 · 건강 · 의료</span><h3>건강검진 · 치과 · 안과 · 건강기능식품</h3><p>검진 패키지 회원가와 건강기능식품 회원 전용 구성을 준비합니다.</p></div>
      <div class="card"><div class="ic">📚</div><span class="tag">10 · 교육 · 문화</span><h3>학원 · 온라인 교육 · 키즈카페 · 문화</h3><p>수강료 할인과 회원 전용 문화 이용권. 아이 픽업 대기 시간에 라운지를 쓰십니다.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">For Business</span><h2 class="h2">사업자 회원을 위한 제휴</h2>
      <p class="lead">오렌지 비즈 회원께만 적용되는 제휴입니다. 사업을 하시는 데 실제로 드는 비용을 줄이는 쪽으로 골랐습니다.</p></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">🧾</div><span class="tag">11 · 사업자 금융 · 세무</span><h3>세무 · 회계 · 사업자 카드</h3><p>기장료 회원가와 창업 초기 세무 상담을 지원합니다.</p></div>
      <div class="card"><div class="ic">📮</div><span class="tag">12 · 셀러 인프라</span><h3>택배 · 포장재 · 촬영 · 상세페이지</h3><p>택배 계약 요율 우대, 포장재 회원가, 상세페이지 제작 할인. 2층 스튜디오와 함께 쓰시면 됩니다.</p></div>
      <div class="card"><div class="ic">🛡️</div><span class="tag">13 · 보험</span><h3>보관물 · 사업자 배상책임 · 자동차</h3><p>창고에 맡기신 물건의 화재보험을 단체요율로 가입하실 수 있습니다.</p></div>
    </div>
    <div class="note warnbox rv" style="margin-top:30px">멤버십 혜택에는 대부업 관련 상품을 포함하지 않습니다. 금융 관련 안내가 필요한 경우 별도의 메뉴와 별도의 동의 절차로 분리해 제공하며, 관계 법령이 정한 표기 사항을 함께 안내합니다.</div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap split rv">
    <div class="sp-txt">
      <span class="eyebrow">For Partners</span>
      <h2 class="h2">제휴를 검토하고 계신<br>기업이시라면</h2>
      <p class="lead" style="margin:18px 0 24px">저희는 &lsquo;회원에게 할인해 주세요&rsquo;라고 부탁드리지 않습니다. 매장 공간과 물류, 방송 채널을 먼저 내드리고 그 대가로 회원 혜택을 받아옵니다.</p>
      <ul class="chk">
        <li><b>공간</b> — 매장 내 팝업존 · 전시존 · 서비스 카운터 · 옥외 주차장</li>
        <li><b>보관 · 물류</b> — 지하 공유창고 유닛과 통합 물류 코어</li>
        <li><b>미디어</b> — 2층 라이브커머스 스튜디오와 방송 슬롯</li>
        <li><b>고객</b> — 오프라인 방문객 · 온라인 회원 · 입점 셀러</li>
      </ul>
      <div class="btn-row" style="margin-top:28px"><a href="join.html#partner" class="btn btn-p">제휴 문의하기</a></div>
    </div>
    <div><img src="assets/img/biz-counter.jpg" alt="HMK 스토리지 상담 카운터" loading="lazy" width="1500" height="844"></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="tbl-note rv" style="max-width:900px; margin:0 auto; text-align:center">제휴 카테고리와 혜택 내용은 2027년 1월 시행을 목표로 준비 중인 계획안입니다. 제휴사와의 협의 결과에 따라 카테고리 구성과 혜택 조건이 달라질 수 있으며, 확정된 내용은 서비스 개시 시점에 안내합니다. 제휴 서비스의 제공 주체는 제휴사이며, 상품과 서비스의 내용 및 이행에 관한 책임은 제휴사에 있습니다.</p>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# community.html
# ══════════════════════════════════════════════════════════
COM = phead("Community", "오렌지 커뮤니티", "혜택은 다른 곳이 더 크게 줄 수 있지만, 사람은 옮겨 갈 수 없습니다. 오렌지 멤버십이 커뮤니티에 공을 들이는 이유입니다.", "biz-reception.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="sec-head center rv"><span class="eyebrow">Three Communities</span><h2 class="h2">세 개의 모임</h2></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">☕</div><span class="tag">LOUNGE</span><h3>오렌지 라운지</h3><p>공유창고에 있는 라운지와 24시간 무인카페를 회원 공간으로 씁니다. 창고를 쓰러 오신 분, 장을 보러 오신 분, 방송을 하러 오신 셀러가 자연스럽게 지나는 자리입니다.</p></div>
      <div class="card"><div class="ic">🏪</div><span class="tag">SELLER CLUB</span><h3>오렌지 셀러클럽</h3><p>사업자 회원이 자동으로 가입되는 모임입니다. 어디서 싸게 떼오는지, 재고를 어떻게 두는지, 어떻게 파는지를 서로 나눕니다.</p></div>
      <div class="card"><div class="ic">🎬</div><span class="tag">CREW</span><h3>오렌지 크루</h3><p>후기를 쓰시고, 창고 활용법을 공유하시고, 직접 방송을 진행하시는 회원입니다. 활동 점수가 쌓이면 등급이 올라갑니다.</p></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap split rv">
    <div class="sp-txt">
      <span class="eyebrow">Orange Lounge</span>
      <h2 class="h2">동네 사랑방처럼<br>쓰셔도 됩니다</h2>
      <p class="lead" style="margin:18px 0 24px">창고 옆 라운지는 24시간 열려 있습니다. 무인카페에서 음료를 드시고, 모임 공간을 예약해 쓰시고, 온라인으로 주문하신 물건을 픽업 락커에서 찾아가십니다.</p>
      <ul class="chk">
        <li><b>무인카페</b> — 오렌지 월 2잔, 플러스 이상 월 4잔 무료</li>
        <li><b>오픈 테이블</b> — 작업하시거나 기다리실 때 자유롭게</li>
        <li><b>모임 공간</b> — 10인 내외 규모, 앱으로 예약</li>
        <li><b>픽업 락커</b> — 온라인 주문 무인 수령, 24시간</li>
        <li><b>셀러 데스크</b> — 상품 검수와 포장, 오렌지 비즈 전용</li>
      </ul>
    </div>
    <div><img src="assets/img/biz-storage.jpg" alt="오렌지 라운지" loading="lazy" width="1500" height="844"></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Seller Club</span><h2 class="h2">셀러클럽 — 같은 고민을 하는 분들</h2>
      <p class="lead">소상공인과 온라인 셀러는 늘 같은 문제를 안고 계십니다. 저희는 그 문제의 답을 세 층에 나눠 갖고 있습니다.</p></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>셀러의 고민</th><th>HMK가 드리는 답</th><th>모임이 더하는 것</th></tr></thead>
        <tbody>
          <tr><td>사입처가 없다</td><td style="text-align:left">1층 창고마켓 사입 전용가</td><td style="text-align:left">어떤 상품이 잘 나가는지 서로 공유</td></tr>
          <tr><td>재고 둘 데가 없다</td><td style="text-align:left">지하 공유창고 회원 요율</td><td style="text-align:left">유닛 크기 선택 경험 공유</td></tr>
          <tr><td>팔 채널이 없다</td><td style="text-align:left">2층 스튜디오와 방송 편성</td><td style="text-align:left">방송 노하우 · 합동 라이브</td></tr>
          <tr><td>촬영 · 편집을 못 한다</td><td style="text-align:left">제작 대행 회원가</td><td style="text-align:left">서로 촬영 도와주기 · 장비 공유</td></tr>
          <tr><td>세무 · 정산이 어렵다</td><td style="text-align:left">세무 파트너 연계</td><td style="text-align:left">실무 경험 공유 · 정기 세미나</td></tr>
        </tbody>
      </table>
    </div>
    <div class="grid g3 rv" style="margin-top:36px">
      <div class="card"><div class="ic">📅</div><h3>셀러 정기모임 · 월 1회</h3><p>라운지에서 진행합니다. 새로 오신 분 소개하고 상품 정보를 나눕니다.</p></div>
      <div class="card"><div class="ic">📺</div><h3>합동 라이브 · 월 2회</h3><p>셀러 서너 분이 함께 방송하십니다. 스튜디오는 무료로 드립니다.</p></div>
      <div class="card"><div class="ic">🤝</div><h3>셀러 멘토링 · 분기</h3><p>경력 있으신 셀러가 처음 시작하시는 분을 1:1로 도와 드립니다.</p></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Crew</span><h2 class="h2">활동하시면 등급이 올라갑니다</h2>
      <p class="lead">구매 금액이 크지 않으셔도 됩니다. 활동으로 쌓은 점수만으로도 승급하실 수 있습니다.</p></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>활동</th><th>내용</th><th>포인트</th><th>활동 점수</th></tr></thead>
        <tbody>
          <tr><td>상품 후기</td><td style="text-align:left">구매하신 상품의 사진과 후기</td><td>500~1,000P</td><td>10점</td></tr>
          <tr><td>창고 활용기</td><td style="text-align:left">유닛 정리 방법과 활용 사례</td><td>3,000P</td><td>40점</td></tr>
          <tr><td>오렌지 크루 방송</td><td style="text-align:left">회원이 직접 진행하는 라이브</td><td>판매액의 3%</td><td>80점</td></tr>
          <tr><td>매장 제안</td><td style="text-align:left">상품 · 진열 · 운영 개선 제안</td><td>채택 시 5,000P</td><td>30점</td></tr>
          <tr><td>회원 추천</td><td style="text-align:left">새 회원을 추천해 주실 때</td><td>5,000P</td><td>20점</td></tr>
          <tr><td>모임 개설</td><td style="text-align:left">라운지에서 직접 모임을 여실 때</td><td>공간 무료 · 음료 지원</td><td>60점</td></tr>
        </tbody>
      </table>
    </div>
    <p class="tbl-note rv">활동 점수 300점이면 오렌지 플러스, 800점이면 오렌지 프라임으로 승급하십니다. 1,500점을 넘기시면 오렌지 크루로 인증해 드립니다.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="note nv rv"><b>회사가 다 짜 놓으면 행사가 되고, 회원이 만드시면 모임이 됩니다.</b> 저희는 공간과 도구와 규칙만 준비하고, 운영에는 되도록 끼어들지 않으려고 합니다. 라운지 예약 시스템과 모임 신청 양식, 활동 점수 반영까지만 저희가 하고 나머지는 회원께 맡깁니다. 오래가는 모임은 대부분 그렇게 굴러갑니다.</div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# guide.html
# ══════════════════════════════════════════════════════════
GUIDE = phead("Guide", "이용 안내", "가입부터 사용, 해지까지 알아 두셔야 할 내용을 정리했습니다.", "card-tap.jpg") + '''
<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Join</span><h2 class="h2">가입 방법</h2></div>
    <div class="steps rv">
      <div class="step"><h3>앱 또는 매장에서 가입</h3><p>오렌지 멤버십 앱이나 매장 안내 데스크에서 가입하십니다. 만 19세 이상이면 가입하실 수 있고, 14세 이상 19세 미만이시면 법정대리인의 동의가 필요합니다.</p></div>
      <div class="step"><h3>연회비 39,000원 결제</h3><p>1년치를 한 번에 결제하십니다. 결제하신 날부터 365일간 이용하십니다. 결제 화면에서 자동갱신 여부와 해지 방법을 함께 안내해 드립니다.</p></div>
      <div class="step"><h3>실물 카드와 웰컴 패키지 수령</h3><p>실물 회원카드를 드리고 웰컴 패키지가 바로 지급됩니다. 포인트는 즉시 계정에 들어오고, 쿠폰과 이용권은 앱에서 확인하십니다.</p></div>
    </div>
  </div>
</section>

<section class="sec warm">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Use</span><h2 class="h2">사용 방법</h2></div>
    <div class="grid g2 rv">
      <div class="card"><div class="ic">🏷️</div><h3>매장에서</h3><p>계산대에서 실물 카드나 앱 바코드를 보여 주십니다. 회원가가 자동으로 적용되고 포인트가 쌓입니다. 카드를 안 가져오셨어도 휴대폰 번호만 말씀하시면 됩니다.</p></div>
      <div class="card"><div class="ic">🔑</div><h3>공유창고에서</h3><p>QR이나 얼굴 인식으로 출입하십니다. 이용료는 등록하신 결제 수단으로 자동 청구되고, 등급 요율이 자동 적용됩니다.</p></div>
      <div class="card"><div class="ic">🎥</div><h3>스튜디오에서</h3><p>앱에서 예약하십니다. 오렌지 비즈 회원은 편성이 우선 배정되고, 프라임 회원은 월 2시간을 무료로 쓰십니다.</p></div>
      <div class="card"><div class="ic">💻</div><h3>온라인몰에서</h3><p>같은 계정으로 로그인하시면 회원가가 적용됩니다. 매장 픽업을 고르시면 배송비 없이 당일 받으시고 1% 추가 적립됩니다.</p></div>
    </div>
    <div class="note rv" style="margin-top:30px"><b>앱이 익숙하지 않으셔도 괜찮습니다.</b> 실물 회원카드를 드리고, 카드가 없으셔도 휴대폰 번호만으로 회원 확인이 됩니다. 앱 글자 크기를 키울 수 있고, 매장 안내 데스크에서 가입과 조회를 도와 드립니다.</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">Renewal &amp; Cancel</span><h2 class="h2">갱신 · 해지 · 환불</h2></div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>구분</th><th>내용</th></tr></thead>
        <tbody>
          <tr><td>자동갱신</td><td style="text-align:left">해지하지 않으시면 이용 기간 만료일에 자동 갱신됩니다. 갱신 30일 전과 7일 전, 두 번에 걸쳐 갱신 예정 사실과 결제 금액, 해지 방법을 앱 · 문자 · 이메일로 알려 드립니다.</td></tr>
          <tr><td>자동갱신 해제</td><td style="text-align:left">이용 기간 중 언제든 앱에서 해제하실 수 있습니다. 해제하셔도 남은 기간의 혜택은 그대로 유지됩니다.</td></tr>
          <tr><td>해지 방법</td><td style="text-align:left">앱 마이페이지, 고객센터 전화, 매장 안내 데스크에서 하실 수 있습니다. 가입하실 때보다 복잡한 절차를 요구하지 않습니다.</td></tr>
          <tr><td>14일 전액 환불</td><td style="text-align:left">가입 후 14일 이내이고 웰컴 패키지를 포함해 어떤 혜택도 쓰지 않으셨다면 연회비 전액을 돌려 드립니다.</td></tr>
          <tr><td>중도 해지 환급</td><td style="text-align:left">환급액 = 39,000원 × (잔여일수 ÷ 365) − 이미 쓰신 웰컴 혜택 실비. 산정 결과가 0원 미만이어도 추가로 청구하지 않습니다.</td></tr>
          <tr><td>환급 처리</td><td style="text-align:left">해지 신청일부터 3영업일 이내에 처리합니다. 원칙적으로 결제하신 수단으로 돌려 드립니다.</td></tr>
          <tr><td>위약금</td><td style="text-align:left">없습니다.</td></tr>
          <tr><td>잔여 포인트</td><td style="text-align:left">해지하시면 남은 포인트는 소멸합니다. 해지 화면에서 잔액을 미리 보여 드립니다.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="note rv" style="margin-top:26px">
      <b>환급 계산 예시</b><br>
      가입 후 100일에 해지하시고 포인트 12,000P와 쿠폰 2매, 음료 6잔을 쓰셨다면 —<br>
      일할 환급액 39,000원 × (265 ÷ 365) = 28,315원, 웰컴 혜택 정산 28,000원을 빼면 환급액은 315원입니다.
    </div>
  </div>
</section>

<section class="sec warm" id="faq">
  <div class="wrap-n">
    <div class="sec-head center rv"><span class="eyebrow">FAQ</span><h2 class="h2">자주 묻는 질문</h2></div>
    <div class="acc rv">
      <div class="acc-i"><button class="acc-q">회원이 아니면 매장에 들어갈 수 없나요?</button><div class="acc-a"><div>아닙니다. 오렌지 창고마켓은 누구나 들어오실 수 있습니다. 회원이 되시면 같은 상품을 회원가로 사시고 포인트가 쌓입니다. 매대에 회원가와 비회원가를 나란히 표시합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">코스트코 회원인데 굳이 또 가입할 이유가 있나요?</button><div class="acc-a"><div>오렌지 멤버십은 상품 구색으로 경쟁하는 회원제가 아닙니다. 사시는 것에 더해 <strong>보관하고 파실 수 있다는 점</strong>이 다릅니다. 지하에 공유창고가 있고 2층에 방송 스튜디오가 있어서, 집이 좁아도 대량으로 사실 수 있고 안 쓰는 물건을 방송으로 파실 수도 있습니다. 그리고 매장 반경 3km 생활 상권을 목표로 하기 때문에 자주 오시기 편합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">등급을 올리려면 돈을 더 내야 하나요?</button><div class="acc-a"><div>아닙니다. 유료 등급은 39,000원 하나뿐입니다. 플러스와 프라임은 이용 실적에 따라 추가 비용 없이 자동으로 올라갑니다. 구매 금액이 크지 않으셔도 창고를 이용하시거나 커뮤니티 활동을 하시면 승급하실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">오렌지 비즈는 어떻게 신청하나요?</button><div class="acc-a"><div>사업자등록증을 앱이나 매장에서 제출하시고 인증을 마치시면 됩니다. 회비는 39,000원으로 같고 혜택 구성만 사업자에게 맞게 바뀝니다. 기존 등급과 함께 적용되어 &lsquo;오렌지 플러스 · 비즈&rsquo;처럼 표시됩니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">포인트를 현금으로 충전할 수 있나요?</button><div class="acc-a"><div>충전은 하지 않습니다. 오렌지 포인트는 구매와 활동으로만 쌓이는 적립형입니다. 현금으로 돌려받으시거나 다른 분께 양도하실 수도 없습니다. 다만 가족 회원끼리는 합산해서 쓰실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">포인트 유효기간이 지나면 어떻게 되나요?</button><div class="acc-a"><div>적립일부터 24개월이 지나면 소멸합니다. 소멸 30일 전에 금액과 소멸 예정일을 앱과 문자로 알려 드리며, <strong>저희가 알려 드리지 않은 포인트는 소멸시키지 않습니다.</strong></div></div></div>
      <div class="acc-i"><button class="acc-q">가족은 몇 명까지 등록되나요?</button><div class="acc-a"><div>같은 세대의 가족 3명까지 추가 비용 없이 등록하실 수 있습니다. 가족 회원도 회원가로 구매하시고, 적립하신 포인트는 대표 회원 계정으로 합산되어 함께 쓰실 수 있습니다. 등록 변경은 이용 기간 중 두 번까지 가능합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">공유창고 첫 달 무료는 아무 유닛이나 되나요?</button><div class="acc-a"><div>공실 상태인 미니 유닛에 한해 드립니다. 원하시는 크기가 이미 차 있으면 다른 크기를 안내해 드리거나 대기 신청을 받습니다. 이용권은 지급일부터 6개월 안에 개시하셔야 합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제휴 혜택은 어디서 확인하나요?</button><div class="acc-a"><div>앱 혜택 메뉴에서 지금 쓰실 수 있는 것부터 보여 드립니다. 제휴 서비스의 제공 주체는 제휴사이며, 제휴사의 사정으로 조건이 바뀌거나 종료될 수 있습니다. 변경이 있을 경우 30일 전에 알려 드립니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">회비가 오를 수도 있나요?</button><div class="acc-a"><div>초기 3년간은 39,000원을 유지할 계획입니다. 이후 인상이 필요해지면 적용일 3개월 전에 개별 고지하고 동의 의사를 별도로 확인합니다. 동의하지 않으시면 종전 회비로 한 번 더 갱신하실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">언제부터 가입할 수 있나요?</button><div class="acc-a"><div>2027년 1월 서비스 개시를 목표로 준비하고 있습니다. 사전 알림을 신청해 주시면 오픈 일정이 확정되는 대로 문자로 알려 드립니다. 신청에 비용이 들지 않고 가입 의무도 없습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">어느 지역에서 이용할 수 있나요?</button><div class="acc-a"><div>1호점 개점 지역부터 순차적으로 넓혀 갑니다. 매장이 아직 없는 지역에서는 온라인몰 중심으로 이용하실 수 있도록 준비 중입니다. 사전 알림 신청 시 지역을 남겨 주시면 개점 계획을 세울 때 참고합니다.</div></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap"><div class="cta rv">
    <h2 class="h2">더 궁금하신 점이 있으신가요</h2>
    <p>사전 알림 신청 화면에서 문의 내용을 함께 남기실 수 있습니다.</p>
    <div class="btn-row"><a href="join.html" class="btn btn-p btn-lg">문의 남기기</a></div>
  </div></div>
</section>'''


# ══════════════════════════════════════════════════════════
# join.html
# ══════════════════════════════════════════════════════════
JOIN = '''<section class="hero">
  <div class="wrap hero-grid">
    <div class="rv">
      <span class="badge"><i>OPEN 예정</i> 2027년 1월 서비스 개시</span>
      <h1 class="h1">오픈 소식을<br>가장 먼저 받아 보세요</h1>
      <p class="lead" style="margin-top:18px">사전 알림을 신청하신 분께 오픈 일정과 초기 가입 안내를 문자로 보내 드립니다. 신청에 비용이 들지 않고, 가입 의무도 없습니다.</p>
      <ul class="chk" style="margin-top:24px">
        <li>오픈 일정 확정 시 문자 안내</li>
        <li>1호점 개점 지역 우선 안내</li>
        <li>초기 가입 혜택 안내</li>
      </ul>
    </div>
    <div class="hero-visual rv"><img src="assets/img/mascot-card.jpg" alt="HMK 오렌지 멤버십" loading="eager" width="1448" height="1086"></div>
  </div>
</section>

<section class="sec">
  <div class="wrap-n">
    <form class="form rv" id="alertForm" novalidate>
      <h2 class="h3" style="margin-bottom:8px">사전 알림 신청</h2>
      <p class="small" style="margin-bottom:28px">아래 정보를 남겨 주시면 오픈 일정이 확정되는 대로 알려 드리겠습니다.</p>

      <input type="text" name="_hp" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">

      <div class="field">
        <label for="f-name">이름 <em>*</em></label>
        <input type="text" id="f-name" name="name_" placeholder="홍길동" autocomplete="name" required>
      </div>
      <div class="field">
        <label for="f-phone">휴대폰 번호 <em>*</em></label>
        <input type="tel" id="f-phone" name="phone" placeholder="010-0000-0000" autocomplete="tel" inputmode="numeric" required>
        <p class="hint">오픈 안내 문자를 받으실 번호입니다.</p>
      </div>
      <div class="field">
        <label for="f-region">관심 지역</label>
        <select id="f-region" name="region">
          <option value="">선택해 주세요</option>
          <option>서울</option><option>경기 북부</option><option>경기 남부</option><option>인천</option>
          <option>강원</option><option>대전 · 세종 · 충청</option><option>대구 · 경북</option>
          <option>부산 · 울산 · 경남</option><option>광주 · 전라</option><option>제주</option>
        </select>
        <p class="hint">개점 계획을 세울 때 참고합니다.</p>
      </div>
      <div class="field">
        <label>관심 있으신 서비스 (복수 선택 가능)</label>
        <div class="chips">
          <label class="chip"><input type="checkbox" name="interest" value="market"><span>오렌지 창고마켓</span></label>
          <label class="chip"><input type="checkbox" name="interest" value="storage"><span>오렌지 공유창고</span></label>
          <label class="chip"><input type="checkbox" name="interest" value="live"><span>오렌지 라이브쇼핑</span></label>
          <label class="chip"><input type="checkbox" name="interest" value="biz"><span>오렌지 비즈 (사업자)</span></label>
          <label class="chip"><input type="checkbox" name="interest" value="partner"><span>제휴 문의</span></label>
        </div>
      </div>
      <div class="field" id="partner">
        <label for="f-memo">문의 내용 (선택)</label>
        <textarea id="f-memo" name="memo" rows="4" placeholder="궁금하신 점이나 제휴 문의 내용을 남겨 주세요."></textarea>
      </div>

      <div class="field" style="margin-bottom:16px">
        <label class="agree">
          <input type="checkbox" name="agree" required>
          <span><b>[필수]</b> 사전 알림 발송을 위한 개인정보 수집 · 이용에 동의합니다.<br>
          <span class="small">수집 항목: 이름, 휴대폰 번호, 관심 지역 · 서비스, 문의 내용 / 이용 목적: 오픈 안내 및 문의 응대 / 보유 기간: 서비스 개시 후 6개월 또는 삭제 요청 시까지. 동의를 거부하실 수 있으나 이 경우 사전 알림을 받으실 수 없습니다. <a href="terms.html#privacy">자세히 보기</a></span></span>
        </label>
      </div>
      <div class="field" style="margin-bottom:26px">
        <label class="agree">
          <input type="checkbox" name="marketing">
          <span><b>[선택]</b> 오렌지 멤버십 관련 소식과 혜택 안내 수신에 동의합니다. 동의하지 않으셔도 사전 알림 신청에는 영향이 없습니다.</span>
        </label>
      </div>

      <button type="submit" class="btn btn-p btn-lg" style="width:100%">사전 알림 신청하기</button>
      <div class="formmsg" id="formMsg" role="status" aria-live="polite"></div>
    </form>

    <div class="note nv rv" style="margin-top:30px">
      <b>남겨 주신 정보는 오픈 안내와 문의 응대에만 씁니다.</b> 제휴사를 포함한 제3자에게 제공하지 않으며, 삭제를 요청하시면 지체 없이 파기합니다. 자세한 내용은 <a href="terms.html#privacy" style="color:var(--o)">개인정보 처리방침</a>을 확인해 주세요.
    </div>
  </div>
</section>

<section class="sec-sm warm">
  <div class="wrap">
    <div class="sec-head center rv"><h2 class="h3">신청 전에 확인해 보세요</h2></div>
    <div class="grid g3 rv">
      <div class="card"><div class="ic">🎁</div><h3>혜택 안내</h3><p>네 가지 사업에서 받으시는 혜택을 한곳에 정리했습니다.</p><div class="btn-row" style="margin-top:18px"><a href="benefits.html" class="btn btn-g btn-sm">보러 가기</a></div></div>
      <div class="card"><div class="ic">🧮</div><h3>혜택 계산기</h3><p>평소 장보는 금액을 넣으시면 연간 예상 혜택이 나옵니다.</p><div class="btn-row" style="margin-top:18px"><a href="index.html#calc-sec" class="btn btn-g btn-sm">계산해 보기</a></div></div>
      <div class="card"><div class="ic">❓</div><h3>자주 묻는 질문</h3><p>가입, 등급, 포인트, 해지에 관한 질문을 모았습니다.</p><div class="btn-row" style="margin-top:18px"><a href="guide.html#faq" class="btn btn-g btn-sm">확인하기</a></div></div>
    </div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# terms.html
# ══════════════════════════════════════════════════════════
TERMS = phead("Terms &amp; Privacy", "약관 · 개인정보 처리방침", "회원 약관의 주요 내용과 사전 알림 신청에 적용되는 개인정보 처리방침을 안내합니다.") + '''
<section class="sec">
  <div class="wrap-n">
    <div class="note warnbox rv" style="margin-bottom:36px">
      <b>안내</b><br>오렌지 멤버십 회원 약관은 2027년 1월 시행을 목표로 준비 중이며, 아래는 주요 내용을 요약한 것입니다. 최종 약관은 법무 검토를 거쳐 서비스 개시 시점에 전문으로 공지합니다. 아래 개인정보 처리방침은 현재 이 사이트의 사전 알림 신청에 적용되는 내용입니다.
    </div>

    <h2 class="h2 rv" style="margin-bottom:24px">회원 약관 주요 내용</h2>
    <div class="acc rv">
      <div class="acc-i"><button class="acc-q">제1장 총칙 — 목적과 용어</button><div class="acc-a"><div>이 약관은 HMK 홀딩스그룹 및 계열회사가 운영하는 유료 회원제 &lsquo;오렌지 멤버십&rsquo;의 이용 조건과 절차, 회사와 회원의 권리 · 의무를 정합니다. 약관을 개정할 때는 적용일 30일 전(회원에게 불리한 내용은 60일 전)에 알려 드리며, 동의하지 않으시면 해지하고 남은 기간의 회비를 돌려받으실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제2장 회원 가입 — 자격과 등급</button><div class="acc-a"><div>만 19세 이상이면 가입하실 수 있고, 14세 이상 19세 미만이시면 법정대리인 동의가 필요합니다. 등급은 이용 실적에 따라 추가 비용 없이 자동 승급되며, 강등은 갱신 시점에만 적용하고 3개월 전에 미리 알려 드립니다. 사업자등록증을 인증하시면 오렌지 비즈 트랙이 함께 적용됩니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제3장 회비 — 결제와 자동갱신</button><div class="acc-a"><div>연회비는 39,000원(부가세 포함)이며 가입 시 1년치를 결제하십니다. 해지하지 않으시면 자동 갱신되고, 갱신 30일 전과 7일 전 두 번에 걸쳐 갱신 예정 사실 · 결제 금액 · 해지 방법을 앱 · 문자 · 이메일로 알려 드립니다. 자동갱신은 이용 기간 중 언제든 해제하실 수 있습니다. 회비를 인상할 때는 3개월 전에 개별 고지하고 동의 의사를 별도로 확인합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제4장 혜택 — 제공과 변경</button><div class="acc-a"><div>혜택의 이용 조건과 횟수는 회사가 정해 앱과 매장에 게시합니다. 회원에게 불리하게 혜택을 바꿀 때는 적용일 60일 전에 알려 드리고 가능한 범위에서 대체 혜택을 함께 제시합니다. 이 변경에 동의하지 않으시면 30일 안에 해지하실 수 있으며, 이 경우 웰컴 혜택 정산 없이 남은 기간의 회비를 전부 돌려 드립니다. 제휴 서비스의 제공 주체는 제휴사이며 상품과 서비스의 이행 책임은 제휴사에 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제5장 오렌지 포인트</button><div class="acc-a"><div>1포인트는 1원에 상당하며 1포인트부터 쓰실 수 있습니다. 유효기간은 적립일부터 24개월이고, 소멸 30일 전에 개별 고지합니다. 고지하지 않은 포인트는 소멸시키지 않습니다. 현금 충전 · 양도 · 환금은 되지 않으며, 가족 회원 간에는 합산해 쓰실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제6장 해지 및 환불</button><div class="acc-a"><div>이용 기간 중 언제든 해지하실 수 있고, 가입하실 때보다 복잡한 절차를 요구하지 않습니다. 가입 후 14일 이내이고 혜택을 쓰지 않으셨다면 전액 환불합니다. 그 밖의 경우 <strong>환급액 = 연회비 × (잔여일수 ÷ 365) − 사용한 웰컴 혜택 실비</strong>로 계산하며, 결과가 0원 미만이어도 추가로 청구하지 않습니다. 별도의 위약금은 없습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제7장 의무와 책임</button><div class="acc-a"><div>회원 자격과 혜택을 타인에게 양도하거나 거래의 대상으로 삼으실 수 없습니다. 회원가로 사신 물건을 영리 목적으로 되파는 것도 제한됩니다. 다만 오렌지 비즈 회원이 정해진 조건에 따라 사입하시는 경우는 여기에 해당하지 않습니다. 공유창고 이용 시에는 별도의 보관 금지 물품 기준이 함께 적용됩니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">제8장 기타 — 개인정보와 분쟁</button><div class="acc-a"><div>회원의 개인정보는 관계 법령에 따라 처리하며 자세한 내용은 개인정보 처리방침에 따릅니다. 마케팅 수신과 제휴사 제공 동의는 각각 별도 항목으로 받고, 동의하지 않으셔도 가입에는 영향이 없습니다. 분쟁이 생기면 협의로 해결하도록 노력하며, 한국소비자원이나 전자거래분쟁조정위원회에 조정을 신청하실 수 있습니다.</div></div></div>
    </div>
  </div>
</section>

<section class="sec warm" id="privacy">
  <div class="wrap-n">
    <h2 class="h2 rv" style="margin-bottom:10px">개인정보 처리방침</h2>
    <p class="small rv" style="margin-bottom:28px">사전 알림 신청에 적용되는 내용입니다. 시행일 2026년 8월 28일</p>
    <div class="acc rv">
      <div class="acc-i"><button class="acc-q">1. 수집하는 개인정보 항목</button><div class="acc-a"><div><strong>필수</strong> — 이름, 휴대폰 번호<br><strong>선택</strong> — 관심 지역, 관심 서비스, 문의 내용, 마케팅 수신 동의 여부<br><strong>자동 수집</strong> — 접속 로그, 브라우저 정보 (서비스 안정성 확인 목적)</div></div></div>
      <div class="acc-i"><button class="acc-q">2. 수집 · 이용 목적</button><div class="acc-a"><div>오렌지 멤버십 서비스 개시 안내, 개점 지역 안내, 문의 응대에만 사용합니다. 마케팅 수신에 동의하신 경우에 한해 멤버십 관련 소식과 혜택 안내를 보내 드립니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">3. 보유 및 이용 기간</button><div class="acc-a"><div>서비스 개시 후 6개월까지 보유하며, 그 전이라도 삭제를 요청하시면 지체 없이 파기합니다. 관계 법령에 따라 보존해야 하는 기록은 해당 법령이 정한 기간 동안 분리 보관합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">4. 제3자 제공</button><div class="acc-a"><div>남겨 주신 정보를 제휴사를 포함한 제3자에게 제공하지 않습니다. 법령에 따라 제공 의무가 있는 경우에만 예외로 하며, 이 경우에도 최소한의 범위에서만 제공합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">5. 처리 위탁</button><div class="acc-a"><div>문자 발송과 데이터 보관을 위해 국내 전문 사업자에게 처리를 위탁할 수 있습니다. 위탁 시에는 계약을 통해 개인정보 보호 의무를 부과하고 관리 · 감독합니다. 위탁 사업자가 확정되면 이 항목에 상호와 위탁 업무를 기재해 공개합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">6. 정보주체의 권리</button><div class="acc-a"><div>언제든지 자신의 개인정보에 대한 열람, 정정, 삭제, 처리 정지를 요청하실 수 있습니다. 아래 연락처로 요청하시면 지체 없이 처리하고 결과를 알려 드립니다. 마케팅 수신 동의는 언제든 철회하실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">7. 파기 절차와 방법</button><div class="acc-a"><div>보유 기간이 끝나거나 처리 목적이 달성되면 지체 없이 파기합니다. 전자적 파일은 복구할 수 없는 방법으로 삭제하고, 출력물은 분쇄하거나 소각합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">8. 안전성 확보 조치</button><div class="acc-a"><div>개인정보 접근 권한을 최소한으로 제한하고, 전송 구간을 암호화하며, 접근 기록을 보관합니다. 개인정보를 취급하는 담당자를 지정해 관리합니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">9. 개인정보 보호책임자</button><div class="acc-a"><div>부서: HMK 홀딩스그룹 총괄기획본부<br>문의: 사전 알림 신청 화면의 문의란 또는 회사 대표 연락처<br>보호책임자와 연락처는 서비스 개시 시점에 확정해 이 항목에 기재합니다.<br><br>개인정보 침해와 관련해 도움이 필요하시면 개인정보침해신고센터(privacy.kisa.or.kr, 118), 개인정보 분쟁조정위원회(kopico.go.kr, 1833-6972)에 문의하실 수 있습니다.</div></div></div>
      <div class="acc-i"><button class="acc-q">10. 처리방침의 변경</button><div class="acc-a"><div>이 처리방침을 변경할 때는 변경 내용과 시행일을 이 페이지에 공지합니다. 회원에게 중대한 영향을 미치는 변경은 시행 7일 전에 공지합니다.</div></div></div>
    </div>
  </div>
</section>'''


# ══════════════════════════════════════════════════════════
# 404
# ══════════════════════════════════════════════════════════
NF = '''<section class="hero" style="padding:110px 0 120px">
  <div class="wrap" style="text-align:center">
    <span class="eyebrow" style="display:block">ERROR 404</span>
    <h1 class="h1" style="margin-bottom:18px">찾으시는 페이지가 없습니다</h1>
    <p class="lead" style="max-width:520px; margin:0 auto 32px">주소가 바뀌었거나 삭제된 페이지일 수 있습니다. 아래 메뉴에서 다시 찾아 주세요.</p>
    <div class="btn-row" style="justify-content:center">
      <a href="index.html" class="btn btn-p btn-lg">홈으로 가기</a>
      <a href="benefits.html" class="btn btn-g btn-lg">혜택 보기</a>
    </div>
  </div>
</section>'''


PAGES = [
    ("index.html", "HMK 오렌지 멤버십 — 한 장의 카드로 사고, 보관하고, 팔기까지",
     "연 39,000원으로 오렌지 창고마켓·공유창고·라이브쇼핑·온라인몰과 13개 제휴 혜택을 한 번에. 가입 첫날 114,000원 상당의 웰컴 패키지를 드립니다. 2027년 1월 오픈 예정.", IDX),
    ("benefits.html", "혜택 안내 — HMK 오렌지 멤버십",
     "회원가 평균 7% 인하, 구매액 2~3% 적립, 공유창고 첫 달 무료, 스튜디오 대관료 인하까지. 오렌지 멤버십 혜택을 사업별·등급별로 정리했습니다.", BEN),
    ("tiers.html", "등급 · 회비 — HMK 오렌지 멤버십",
     "연회비 39,000원 하나. 오렌지·플러스·프라임 등급은 이용 실적에 따라 추가 비용 없이 자동 승급됩니다. 사업자는 오렌지 비즈 트랙이 함께 적용됩니다.", TIER),
    ("points.html", "오렌지 포인트 — HMK 오렌지 멤버십",
     "1포인트 1원. 매장·온라인몰·창고 이용료·스튜디오 대관료에 1원 단위로 쓰시고, 다음 해 연회비로도 쓰실 수 있습니다. 유효기간 24개월.", PTS),
    ("partners.html", "제휴 혜택 — HMK 오렌지 멤버십",
     "자동차 정비·타이어, 이사·보관, 인테리어, 가전 렌탈부터 통신·건강·교육까지 13개 카테고리. 매장 안에서 바로 이용하시는 제휴를 준비합니다.", PTN),
    ("community.html", "오렌지 커뮤니티 — HMK 오렌지 멤버십",
     "오렌지 라운지, 셀러클럽, 오렌지 크루. 무인카페와 모임 공간을 회원 공간으로 쓰고, 사업자 회원은 셀러클럽에서 사입과 방송 노하우를 나눕니다.", COM),
    ("guide.html", "이용 안내 · 자주 묻는 질문 — HMK 오렌지 멤버십",
     "가입부터 사용, 갱신, 해지, 환불까지. 오렌지 멤버십 이용에 필요한 내용과 자주 묻는 질문 12가지를 정리했습니다.", GUIDE),
    ("join.html", "사전 알림 신청 — HMK 오렌지 멤버십",
     "2027년 1월 오픈 예정. 사전 알림을 신청하시면 오픈 일정과 초기 가입 안내를 문자로 보내 드립니다. 신청에 비용이 들지 않습니다.", JOIN),
    ("terms.html", "약관 · 개인정보 처리방침 — HMK 오렌지 멤버십",
     "오렌지 멤버십 회원 약관의 주요 내용과 사전 알림 신청에 적용되는 개인정보 처리방침을 안내합니다.", TERMS),
    ("404.html", "페이지를 찾을 수 없습니다 — HMK 오렌지 멤버십",
     "요청하신 페이지를 찾을 수 없습니다.", NF),
]

for fn, t, d, b in PAGES:
    page(fn, t, d, b)
    print("+", fn)

# ── robots.txt ──
with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nDisallow: /admin.html\n\nSitemap: {SITE}/sitemap.xml\n")

# ── sitemap.xml ──
urls = []
prio = {"index.html": "1.0", "benefits.html": "0.9", "tiers.html": "0.9",
        "join.html": "0.9", "partners.html": "0.8", "points.html": "0.8",
        "community.html": "0.7", "guide.html": "0.7", "terms.html": "0.4"}
for fn, *_ in PAGES:
    if fn == "404.html":
        continue
    loc = SITE + "/" + ("" if fn == "index.html" else fn)
    urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{prio.get(fn,'0.6')}</priority>\n  </url>")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(urls) + "\n</urlset>\n")

# ── _headers (Cloudflare Pages) ──
with open(os.path.join(OUT, "_headers"), "w", encoding="utf-8") as f:
    f.write("""/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()

/assets/img/*
  Cache-Control: public, max-age=31536000, immutable

/assets/css/*
  Cache-Control: public, max-age=604800

/assets/js/*
  Cache-Control: public, max-age=604800

/*.html
  Cache-Control: public, max-age=0, must-revalidate

/admin.html
  X-Robots-Tag: noindex, nofollow, noarchive
  Cache-Control: no-store
""")

print("+ robots.txt / sitemap.xml / _headers")
