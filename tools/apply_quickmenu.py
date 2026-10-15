# PC 화면(1000px 이상) 오른쪽에 떠 있는 퀵메뉴: 카톡 문의 / 네이버 예약 / 전화 / 길찾기 / 맨 위로.
# 휴대폰에서는 숨기고 하단 고정 버튼(.mbar)을 쓴다. 여러 번 실행해도 한 번만 들어감.
import os
from _common import COL, touch
KAKAO='https://pf.kakao.com/_YUqxjG/chat'
BOOK='https://m.booking.naver.com/booking/13/bizes/208486?theme=place&amp;lang=ko&amp;area=ple'
MAP='https://map.naver.com/p/search/365%EC%8A%A4%EB%A7%88%EC%9D%BC%ED%95%9C%EC%9D%98%EC%9B%90/place/34838451'
CSS='''  .quick { display: none; }
  @media (min-width: 1000px) {
    .quick { display: flex; flex-direction: column; gap: 6px; position: fixed; right: 20px; top: 50%; transform: translateY(-50%); z-index: 40; width: 112px; padding: 8px; border: 1px solid var(--line); border-radius: 16px; background: var(--bg); box-shadow: 0 4px 16px rgba(0,0,0,.08); }
    .quick a { display: block; padding: 10px 4px; border-radius: 10px; text-align: center; text-decoration: none; font-size: .82rem; font-weight: 700; line-height: 1.35; color: var(--brand); border: 1.5px solid var(--line); }
    .quick a:hover { border-color: var(--brand); }
    .quick a.q-kakao { background: #fee500; border-color: #fee500; color: #191919; }
    .quick a.q-book { background: var(--brand); border-color: var(--brand); color: var(--on-brand); }
    .quick a.q-tel small { display: block; font-size: .72rem; font-weight: 600; color: var(--muted); white-space: nowrap; letter-spacing: -.02em; }
    .quick a.q-top { color: var(--muted); font-weight: 600; }
  }
</style>'''
MENU=f'''<nav class="quick" aria-label="빠른 상담">
  <a class="q-kakao" href="{KAKAO}" target="_blank" rel="noopener">카톡 문의</a>
  <a class="q-book" href="{BOOK}" target="_blank" rel="noopener">예약</a>
  <a class="q-tel" href="tel:0507-1495-4600">전화 예약<small>0507-1495-4600</small></a>
  <a href="{MAP}" target="_blank" rel="noopener">길찾기</a>
  <a class="q-top" href="#top">맨 위로 ↑</a>
</nav>
<nav class="mbar"'''
n=0
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    p=COL+f; s=open(p,encoding='utf-8').read()
    if 'class="quick"' in s: continue
    assert s.count('<nav class="mbar"')==1 and s.count('<body>')==1,f
    s=s.replace('</style>',CSS,1).replace('<nav class="mbar"',MENU,1).replace('<body>','<body id="top">',1)
    open(p,'w',encoding='utf-8').write(touch(s) if f!='index.html' else s); n+=1
print(n,'페이지')
