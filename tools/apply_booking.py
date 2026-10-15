# 네이버 예약 링크를 모든 칼럼·목록·원장 소개 페이지에 넣는다 (여러 번 실행해도 한 번만 들어감).
# 위치: PC 헤더(전화 예약 옆), 진료 안내의 "예약" 줄, 하단 버튼 줄, 휴대폰 하단 고정 버튼.
import os,re
from _common import COL, touch
BOOK='https://m.booking.naver.com/booking/13/bizes/208486?theme=place&amp;lang=ko&amp;area=ple'
A=f'href="{BOOK}" target="_blank" rel="noopener"'
CSS='''  .nav-r { display: flex; align-items: center; gap: 8px; }
  .book { display: none; padding: 7px 14px; border-radius: 999px; border: 1.5px solid var(--brand); color: var(--brand); text-decoration: none; font-size: .9rem; font-weight: 700; }
  @media (min-width: 640px) { .book { display: inline-block; } }
</style>'''
n=0
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    p=COL+f; s=open(p,encoding='utf-8').read()
    if 'booking.naver.com' in s: continue
    call='<a class="call" href="tel:0507-1495-4600">전화 예약</a>'
    assert s.count(call)==1,f
    s=s.replace(call,f'<span class="nav-r"><a class="book" {A}>예약</a>{call}</span>')
    s=s.replace('</style>',CSS,1)
    # 진료 안내: 전화 줄 다음에 예약 줄
    t='<div><dt>전화</dt><dd><a href="tel:0507-1495-4600">0507-1495-4600</a></dd></div>'
    assert s.count(t)==1,f
    s=s.replace(t,t+f'\n      <div><dt>예약</dt><dd><a {A}>예약 바로가기</a> 또는 전화 예약</dd></div>')
    # 하단 버튼 줄
    c='    <a class="btn btn-primary" href="tel:0507-1495-4600">전화로 상담 예약 0507-1495-4600</a>\n'
    assert s.count(c)==1,f
    s=s.replace(c,c+f'    <a class="btn btn-primary" {A}>예약하기</a>\n')
    # 휴대폰 하단 고정 버튼: 전화 / 네이버 예약 / 길찾기 / 블로그
    m=re.search(r'<nav class="mbar" aria-label="빠른 연결">\n(.*?)</nav>',s,re.S)
    lines=m.group(1).strip('\n').split('\n'); call_l=[x for x in lines if 'm-call' in x][0]
    blog=[x for x in lines if 'blog.naver' in x][0]; mp=[x for x in lines if 'map.naver' in x][0]
    new='\n'.join([call_l.replace('>전화 예약<','>전화<'),f'  <a class="m-book" {A}>예약</a>',mp,blog])+'\n'
    s=s[:m.start(1)]+new+s[m.end(1):]
    s=s.replace('    .mbar a { flex: 1; text-align: center; padding: 10px 4px; border-radius: 10px; font-weight: 700; font-size: .95rem;',
                '    .mbar a { flex: 1; text-align: center; padding: 10px 2px; border-radius: 10px; font-weight: 700; font-size: .88rem; white-space: nowrap;')
    s=s.replace('    .mbar a.m-call { background: var(--brand); color: var(--on-brand); }',
                '    .mbar a.m-call, .mbar a.m-book { background: var(--brand); color: var(--on-brand); }\n    .mbar a.m-book { flex: 1.4; }')
    s=s.replace('padding: 8px 10px calc(8px + env(safe-area-inset-bottom)); gap: 8px;','padding: 8px 8px calc(8px + env(safe-area-inset-bottom)); gap: 6px;')
    open(p,'w',encoding='utf-8').write(touch(s) if f not in ('index.html',) else s); n+=1
print(n,'페이지')
