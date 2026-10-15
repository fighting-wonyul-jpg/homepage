# 다른 칼럼에서 한 번도 연결되지 않은 칼럼을 찾아, 관련 칼럼 2곳의 "함께 읽으면 좋은 칼럼"에 넣는다.
# 바뀐 칼럼은 dateModified를 오늘로 바꾼다. 사용: python3 tools/link_orphans.py
import re,collections
from _common import COL, site, column_slugs, read, write, touch, touch_sitemap
S=site(); cat_of={s:n for n,ss in S['categories'] for s in ss}
idx=open(COL+'index.html',encoding='utf-8').read()
item={m.group(1):m.group(2) for m in re.finditer(r'<a class="item" href="([a-z0-9-]+)\.html"[^>]*>(.*?)</a>',idx)}
fs=column_slugs()
def rel(slug):
    blk=re.search(r'<div class="rel-grid">(.*?)</div>',read(slug),re.S).group(1)
    return re.findall(r'href="([a-z0-9-]+)\.html"',blk)
R={f:rel(f) for f in fs}
inb=collections.Counter(r for f in fs for r in R[f])
orph=sorted(f for f in fs if inb[f]==0)
used=set(); changed=set()
for o in orph:
    cands=list(R[o])+[t for t in fs if cat_of.get(t)==cat_of.get(o) and t not in R[o]]
    got=0
    for t in cands:
        if got==2: break
        if t==o or t in used or o in R[t]: continue
        i=max(range(len(R[t])),key=lambda i:inb[R[t][i]]); old=R[t][i]
        if inb[old]<3: continue
        R[t][i]=o; inb[old]-=1; inb[o]+=1; used.add(t); changed.add(t); got+=1
    print(o,'→',got,'곳에 연결')
for t in sorted(changed):
    s=read(t)
    cards="\n".join(f'      <a class="rel-card" href="{r}.html">{item[r]}</a>' for r in R[t])
    s=re.sub(r'(<div class="rel-grid">\n).*?(\n    </div>)',lambda m:m.group(1)+cards+m.group(2),s,count=1,flags=re.S)
    write(t,touch(s))
touch_sitemap(sorted(changed))
print('연결 없는 칼럼',len(orph),'/ 수정한 칼럼',len(changed))
