# 카카오톡 채널 문의 링크를 모든 칼럼·목록·원장 소개 페이지에 넣는다 (여러 번 실행해도 한 번만 들어감).
# 위치: 휴대폰 하단 고정 버튼(블로그 자리 → 카톡 문의), 진료 안내의 "문의" 줄, 글 아래 버튼 줄.
import os,re
from _common import COL, touch
KAKAO='https://pf.kakao.com/_YUqxjG/chat'
A=f'href="{KAKAO}" target="_blank" rel="noopener"'
CSS='''  .btn-kakao { background: #fee500; color: #191919; }
  .mbar a.m-kakao { background: #fee500; border-color: #fee500; color: #191919; }
</style>'''
n=0
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    p=COL+f; s=open(p,encoding='utf-8').read()
    if 'pf.kakao.com' in s: continue
    s=s.replace('</style>',CSS,1)
    # 하단 고정 버튼: 블로그 → 카톡 문의
    m=re.search(r'(<nav class="mbar" aria-label="빠른 연결">\n.*?)(  <a href="https://m\.blog\.naver\.com/kimyiho8787" target="_blank" rel="noopener">블로그</a>\n)(</nav>)',s,re.S)
    assert m,f
    s=s[:m.start(2)]+f'  <a class="m-kakao" {A}>카톡 문의</a>\n'+s[m.end(2):]
    # 진료 안내: 예약 줄 다음에 문의 줄
    t=re.search(r'      <div><dt>예약</dt>.*?</div>\n',s); assert t,f
    s=s[:t.end()]+f'      <div><dt>문의</dt><dd><a {A}>카카오톡 채널로 문의하기</a></dd></div>\n'+s[t.end():]
    # 글 아래 버튼 줄: 네이버 예약 다음
    c=re.search(r'    <a class="btn btn-primary" href="https://m\.booking\.naver\.com[^\n]*\n',s); assert c,f
    s=s[:c.end()]+f'    <a class="btn btn-kakao" {A}>카카오톡 문의</a>\n'+s[c.end():]
    open(p,'w',encoding='utf-8').write(touch(s) if f!='index.html' else s); n+=1
print(n,'페이지')
