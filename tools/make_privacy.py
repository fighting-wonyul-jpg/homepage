# column/privacy.html (개인정보 처리 안내) 생성. 원장 소개 페이지의 틀을 그대로 쓴다.
import re,json
from _common import COL, BASE
t=open(COL+'doctor.html',encoding='utf-8').read()
URL=BASE+'column/privacy.html'
TITLE='개인정보 처리 안내 | 365스마일한의원 건강 칼럼'
DESC='365스마일한의원 건강 칼럼 사이트의 방문 통계(구글 애널리틱스) 사용과 개인정보 처리에 대한 안내입니다.'
h=t[:t.index('<script type="application/ld+json">')]
h=re.sub(r'<title>.*?</title>',f'<title>{TITLE}</title>',h)
h=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{DESC}">',h)
h=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{DESC}">',h)
h=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{TITLE}">',h)
h=re.sub(r'<meta name="keywords" content="[^"]*">\n','',h)
h=re.sub(r'<meta name="robots" content="[^"]*">','<meta name="robots" content="noindex, follow">',h)
h=h.replace(BASE+'column/doctor.html',URL).replace('<meta property="og:type" content="profile">','<meta property="og:type" content="website">')
ld={"@context":"https://schema.org","@type":"WebPage","name":TITLE,"url":URL,"inLanguage":"ko","dateModified":"2026-10-15"}
rest=t[t.index('</script>',t.index('<script type="application/ld+json">'))+len('</script>'):]
head_rest=rest[:rest.index('<article>')]
tail=rest[rest.index('  <section class="visit">'):]
body='''<article>
  <p class="crumb"><a href="./">건강 칼럼</a> · 개인정보 처리 안내</p>
  <h1>개인정보 처리 안내</h1>
  <p class="meta">365스마일한의원 · 시행일 2026년 10월 15일</p>

  <h2>1. 직접 받는 개인정보는 없습니다</h2>
  <p>이 칼럼 사이트에는 회원가입이나 상담 신청 양식이 없으며, 이름·연락처 같은 개인정보를 직접 받거나 저장하지 않습니다.</p>

  <h2>2. 방문 통계(구글 애널리틱스)</h2>
  <p>더 도움이 되는 칼럼을 만들기 위해 Google LLC의 방문 통계 도구인 구글 애널리틱스를 사용합니다. 쿠키를 통해 아래 정보가 수집됩니다.</p>
  <ul>
    <li>읽은 페이지, 머문 시간, 들어온 경로(검색, 블로그 등)</li>
    <li>기기와 브라우저 종류, 대략적인 지역(도시 단위)</li>
    <li>사이트 안의 예약·문의·전화·길찾기·블로그 버튼을 누른 횟수, 칼럼 검색창에 입력한 검색어</li>
  </ul>
  <p>이 정보로 방문자 개인을 알아보지 않으며, 칼럼 개선과 방문 통계 목적으로만 씁니다. 정보는 구글의 서버(미국 등)에서 처리되고, 구글 애널리틱스의 데이터 보관 설정 기간 동안 보관된 뒤 삭제됩니다. 검색창에는 이름이나 연락처 같은 개인정보를 입력하지 마세요.</p>

  <h2>3. 수집을 원하지 않으시면</h2>
  <ul>
    <li>브라우저 설정에서 쿠키를 차단할 수 있습니다.</li>
    <li>구글이 제공하는 <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">구글 애널리틱스 차단 부가 기능</a>을 설치하면 수집되지 않습니다.</li>
  </ul>

  <h2>4. 외부 서비스로 이동할 때</h2>
  <p>네이버 예약, 카카오톡 채널, 네이버 블로그·지도, 유튜브로 이동하면 해당 서비스의 개인정보 처리방침이 적용됩니다. 원장 소개 페이지의 유튜브 영상은 개인정보 보호 강화 모드로 넣었습니다.</p>

  <h2>5. 문의</h2>
  <p>개인정보와 관련한 문의는 365스마일한의원(<a href="tel:0507-1495-4600">0507-1495-4600</a>)으로 연락해 주세요.</p>

'''
page=h+'<script type="application/ld+json">\n'+json.dumps(ld,ensure_ascii=False,indent=2)+'\n</script>'+head_rest+body+tail
open(COL+'privacy.html','w',encoding='utf-8').write(page); print('privacy.html',len(page))
