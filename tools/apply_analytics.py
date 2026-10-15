# 모든 칼럼·목록·소개·안내 페이지에 구글 애널리틱스(column/ga.js), 네이버 애널리틱스(</body> 앞)와 "개인정보 처리 안내" 링크를 넣는다. 여러 번 실행해도 한 번만 들어감.
import os,re
from _common import COL
GA='''<script async src="https://www.googletagmanager.com/gtag/js?id=G-650CYRNZYH"></script>
<script src="ga.js" defer></script>
</head>'''
CSS='''  .policy { margin: 10px 0 0; font-size: .82rem; }
  .policy a { color: var(--muted); }
</style>'''
NAVER='''<script src="https://wcs.pstatic.net/wcslog.js"></script>
<script>
if(!wcs_add) var wcs_add = {};
wcs_add["wa"] = "1284e5d119c14b0";
if(window.wcs) { wcs_do(); }
</script>
</body>'''
n=0
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    p=COL+f; s=open(p,encoding='utf-8').read(); o=s
    if 'googletagmanager.com/gtag' not in s: s=s.replace('</head>',GA,1)
    if 'wcs_add["wa"]' not in s: s=s.replace('</body>',NAVER,1)
    if 'class="policy"' not in s:
        m=re.search(r'  <p class="notice">.*?</p>\n',s,re.S)
        if m: s=s[:m.end()]+'  <p class="policy"><a href="privacy.html">개인정보 처리 안내</a></p>\n'+s[m.end():]
        else:
            i=s.index('</article>'); s=s[:i]+'  <p class="policy"><a href="privacy.html">개인정보 처리 안내</a></p>\n'+s[i:]
        s=s.replace('</style>',CSS,1)
    if s!=o: open(p,'w',encoding='utf-8').write(s); n+=1
print(n,'페이지')
