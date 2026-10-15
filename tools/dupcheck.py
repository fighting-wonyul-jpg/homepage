# 사용법: python3 tools/dupcheck.py slug1 slug2 ...
# 지정한 칼럼의 문장 중 다른 칼럼에도 똑같이 있는 문장을 출력한다 (8편 이상 공통인 안내문은 제외).
import re,html,collections,sys
from _common import COL, column_slugs, read
NEW=set(sys.argv[1:]); d=collections.defaultdict(set)
for n in column_slugs():
    s=read(n); body=re.search(r'<article.*?</article>',s,re.S).group(0)
    for pat in [r'<section class="related">.*?</section>',r'<div class="area">.*?</div>',r'<p class="notice">.*?</p>',r'<ul class="refs">.*?</ul>',
                r'<section class="visit">.*?</section>',r'<section class="author".*?</section>',r'<div class="blogbox">.*?</div>']:
        body=re.sub(pat,'',body,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>','\n',body))
    for x in re.split(r'[.\n?]',t):
        x=x.strip()
        if len(x)>15 and x!="-": d[x].add(n)
bad=0
for k,v in d.items():
    if len(v)>1 and v&NEW and len(v)<8: print(sorted(v),k[:110]); bad+=1
print("dups",bad)
