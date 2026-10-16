# 칼럼 목록(column/index.html)의 검색창·많이 찾는 칼럼·분류·목록·ItemList를 tools/site.json 기준으로 다시 만든다.
# 칼럼을 추가·삭제하거나 분류를 바꾼 뒤 실행: python3 tools/build_index.py
import re,os,json,html
from _common import COL, BASE, site, column_slugs, read
S=site(); CAT=S['categories']; LABEL=S['labels']; POP=S['popular']; SYN=S['synonyms']
allslugs=[s for _,ss in CAT for s in ss]; assert len(allslugs)==len(set(allslugs)),'중복 slug'
files=set(column_slugs())
assert set(allslugs)==files,('site.json 분류와 칼럼 파일이 다릅니다',set(allslugs)^files)
s=open(COL+'index.html',encoding='utf-8').read()
GEN={'인천 서구 한의원','가정동 한의원','침치료','약침','한약','인천 서구','추나','온열 요법'}
def page(slug):
    p=read(slug)
    h1=re.sub(r'\s*<br\s*/?>\s*',' ',re.search(r'<h1>(.*?)</h1>',p).group(1)); img=re.search(r'<img class="cover" src="\.\./images/([^"]+)"',p).group(1)
    kw=re.search(r'<meta name="keywords" content="([^"]*)"',p).group(1)
    ks=[k.strip() for k in html.unescape(kw).split(',') if k.strip() and k.strip() not in GEN and not k.strip().startswith('인천 ')]
    return h1,img,ks
def card(x):
    h1,img,ks=page(x); ks=ks+SYN.get(x,[])
    return f'      <a class="item" href="{x}.html" data-k="{html.escape(" ".join(ks),quote=True)}"><img src="../images/{img}" alt="" loading="lazy"><span><small>{html.escape(LABEL[x])}</small>{h1}</span></a>'
CP=S['cat_pages']
def catcard(n,ss):
    sample=' · '.join(html.escape(LABEL[x].split('(')[0]) for x in ss[:3])
    return f'    <a class="catcard" href="{CP[n][0]}.html"><b>{html.escape(n)}</b><small>{len(ss)}편</small><span>{sample}</span></a>'
grid="\n".join(catcard(n,ss) for n,ss in CAT)
import datetime
_m=datetime.date.today().month
NOW='spring' if 3<=_m<=5 else 'summer' if 6<=_m<=8 else 'autumn' if 9<=_m<=11 else 'winter'
pop="\n".join(f'    <li><a href="{x}.html">{html.escape(LABEL[x])}</a></li>' for x in POP)
for sea,xs in S.get('seasonal',{}).items():
    for x in xs:
        if x in POP: continue
        pop+="\n"+f'    <li data-season="{sea}"'+('' if sea==NOW else ' hidden')+f'><a href="{x}.html">{html.escape(LABEL[x])}</a></li>'

secs="\n".join(f'''  <section class="cat" id="cat-{i}" hidden>
    <h2>{html.escape(n)} <small>{len(ss)}편</small></h2>
    <div class="grid2">
'''+"\n".join(card(x) for x in ss)+'''
    </div>
  </section>''' for i,(n,ss) in enumerate(CAT,1))
SEARCH='''  <div class="search">
    <label for="q">질환명으로 찾기</label>
    <input id="q" type="search" placeholder="예: 이석증, 허리디스크, 생리통" autocomplete="off">
    <p class="search-msg" id="qmsg" aria-live="polite"></p>
  </div>
'''
TOP=f'''  <p class="cat-label">요즘 많이 찾는 칼럼</p>
  <ul class="pop">
{pop}
  </ul>
  <p class="cat-label">분류별로 보기</p>
  <div class="catgrid">
{grid}
  </div>
'''+secs+'''
<script>
(function(){
  var MAP={CATMAP};
  var h=location.hash.slice(1); if(MAP[h]){ location.replace(MAP[h]); return; }
  var secs=document.querySelectorAll('.cat'), items=document.querySelectorAll('.cat .item');
  var q=document.getElementById('q'), msg=document.getElementById('qmsg');
  function norm(t){ return (t||'').toLowerCase().replace(/[\\s·()（）,.]/g,''); }
  items.forEach(function(a){ a._k=norm(a.textContent+' '+(a.dataset.k||'')); });
  function search(){
    var t=norm(q.value);
    document.body.classList.toggle('searching', !!t);
    if(!t){ msg.textContent=''; secs.forEach(function(s){ s.hidden=true; }); return; }
    var n=0;
    secs.forEach(function(s){
      var c=0; s.querySelectorAll('.item').forEach(function(a){ var ok=a._k.indexOf(t)>-1; a.hidden=!ok; if(ok) c++; });
      s.hidden = c===0; n+=c;
    });
    msg.textContent = n ? '검색 결과 '+n+'편' : '찾는 칼럼이 없습니다. 증상이 궁금하시면 0507-1495-4600으로 전화 주세요.';
  }
  q.addEventListener('input', search);
})();
</script>
'''.replace('{CATMAP}',json.dumps({f'cat-{i}':CP[n][0]+'.html' for i,(n,_) in enumerate(CAT,1)}))
CSS='''  .catgrid { display: grid; gap: 10px; grid-template-columns: repeat(2, 1fr); margin: 0 0 8px; }
  @media (min-width: 640px) { .catgrid { grid-template-columns: repeat(3, 1fr); } }
  .catcard { display: block; padding: 14px 14px 12px; border: 1px solid var(--line); border-left: 4px solid var(--brand); border-radius: 14px; background: var(--bg); color: var(--text); text-decoration: none; line-height: 1.45; }
  .catcard:hover { border-color: var(--brand); }
  .catcard b { display: block; font-size: 1rem; }
  .catcard small { display: inline-block; margin-top: 2px; color: var(--brand); font-weight: 700; font-size: .82rem; }
  .catcard span { display: block; margin-top: 4px; color: var(--muted); font-size: .8rem; }
  .searching .catgrid { display: none; }
  .cat-chips { display: flex; flex-wrap: wrap; gap: 6px; margin: 6px 0 4px; padding: 0; list-style: none; }
  .cat-chips a { display: inline-block; padding: 6px 12px; border: 1px solid var(--line); border-radius: 999px; color: var(--text); text-decoration: none; font-size: .85rem; font-weight: 600; background: var(--bg); }
  .cat-chips a[aria-current="page"] { background: var(--brand); border-color: var(--brand); color: var(--on-brand); }
  .back { display: inline-block; margin: 4px 0 18px; font-weight: 700; text-decoration: none; }
'''
s=re.sub(r'  <div class="search">.*?</div>\n','',s,count=1,flags=re.S)
a=s.index('  <p class="cat-label">')
b=s.index('</script>',s.index('<script>',s.index('<section class="cat"')))+len('</script>\n')
s=s[:a]+TOP+s[b:]
mb=re.search(r'  <div class="blogbox">.*?</div>\n',s,re.S); BLOG=mb.group(0); s=s[:mb.start()]+s[mb.end():]
cl=s.index('  <p class="cat-label">'); s=s[:cl]+SEARCH+s[cl:]
vv=s.index('  <section class="visit">'); s=s[:vv]+BLOG+s[vv:]
m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
def fix(o):
    if isinstance(o,dict):
        if o.get('@type')=='ItemList':
            o['itemListElement']=[{"@type":"ListItem","position":i,"url":f"{BASE}column/{x}.html","name":html.unescape(page(x)[0])} for i,x in enumerate(allslugs,1)]
        for v in o.values(): fix(v)
    elif isinstance(o,list):
        for v in o: fix(v)
fix(ld); s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
if '.catgrid {' not in s: s=s.replace('</style>',CSS+'</style>',1)
open(COL+'index.html','w',encoding='utf-8').write(s)
INDEX=s

# ---- 분류 페이지 (column/cat-*.html): 칼럼 목록을 틀로 써서 분류별 목록을 만든다
from _common import touch_sitemap
def catpage(i,n,ss):
    slug,intro=CP[n]; url=f'{BASE}column/{slug}.html'
    title=f'인천 {n} 한의원 칼럼 | 365스마일한의원'; h1=f'{n} 칼럼'
    desc=intro if len(intro)<=155 else intro[:intro.rfind('.',0,155)+1]
    t=INDEX
    t=re.sub(r'<title>.*?</title>',f'<title>{html.escape(title)}</title>',t,count=1)
    for k in ['name="description"','property="og:description"']:
        t=re.sub(r'(<meta '+k+r' content=")[^"]*',lambda m:m.group(1)+html.escape(desc,quote=True),t,count=1)
    t=re.sub(r'(<meta property="og:title" content=")[^"]*',lambda m:m.group(1)+html.escape(h1,quote=True),t,count=1)
    t=re.sub(r'(<link rel="canonical" href=")[^"]*',lambda m:m.group(1)+url,t,count=1)
    t=re.sub(r'(<meta property="og:url" content=")[^"]*',lambda m:m.group(1)+url,t,count=1)
    t=re.sub(r'(<meta property="og:image" content=")[^"]*',lambda m:m.group(1)+BASE+'images/'+page(ss[0])[1],t,count=1)
    m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',t,re.S); ld=json.loads(m.group(2))
    ld['name']=h1; ld['url']=url; ld['description']=desc
    ld['breadcrumb']={"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"건강 칼럼","item":f"{BASE}column/"},{"@type":"ListItem","position":2,"name":n,"item":url}]}
    ld['mainEntity']={"@type":"ItemList","itemListElement":[{"@type":"ListItem","position":j,"url":f"{BASE}column/{x}.html","name":html.unescape(page(x)[0])} for j,x in enumerate(ss,1)]}
    t=t[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+t[m.end(2):]
    chips="\n".join(f'    <li><a href="{CP[nn][0]}.html"'+(' aria-current="page"' if nn==n else '')+f'>{html.escape(nn)}</a></li>' for nn,_ in CAT)
    body=f'''  <p class="crumb"><a href="./">건강 칼럼</a> · {html.escape(n)}</p>
  <h1>{html.escape(h1)} <small style="font-size:.55em;color:var(--muted)">{len(ss)}편</small></h1>
  <p class="lead-p">{html.escape(intro)}</p>
  <a class="back" href="./">← 전체 분류 보기</a>
  <div class="grid2">
'''+"\n".join(card(x) for x in ss)+f'''
  </div>
  <p class="cat-label">다른 분류 보기</p>
  <ul class="cat-chips">
{chips}
  </ul>
'''
    a=t.index('  <p class="crumb">'); b=t.index('</script>',t.index('<script>',t.index('<section class="cat"')))+len('</script>\n')
    t=t[:a]+body+t[b:]
    t=re.sub(r'  <div class="search">.*?</div>\n','',t,count=1,flags=re.S)
    t=t.replace(' aria-label="365스마일한의원 건강 칼럼 홈"',' aria-label="365스마일한의원 건강 칼럼 홈"',1)
    open(COL+slug+'.html','w',encoding='utf-8').write(t)
    return slug
made=[catpage(i,n,ss) for i,(n,ss) in enumerate(CAT,1)]
for f in os.listdir(COL):
    if f.startswith('cat-') and f[:-5] not in made: os.remove(COL+f)
sm=open(os.path.join(os.path.dirname(COL.rstrip(os.sep)),'sitemap.xml'),encoding='utf-8').read()
touch_sitemap([x for x in made if f'column/{x}.html' not in sm])

# ---- 칼럼 위치 표시: 건강 칼럼 · 분류 · 칼럼
CATOF={x:n for n,ss in CAT for x in ss}
from _common import write
for x in allslugs:
    p0=read(x); n=CATOF[x]; cs=CP[n][0]
    p1=re.sub(r'<p class="crumb"><a href="\./">건강 칼럼</a> · (?:<a href="cat-[a-z-]+\.html">[^<]*</a> · )?',f'<p class="crumb"><a href="./">건강 칼럼</a> · <a href="{cs}.html">{html.escape(n)}</a> · ',p0,count=1)
    def bc(m):
        o=json.loads(m.group(2)); ch=[False]
        def walk(v):
            if isinstance(v,dict):
                if v.get('@type')=='BreadcrumbList':
                    it=[e for e in v['itemListElement'] if '/cat-' not in str(e.get('item',''))]
                    it.insert(1,{"@type":"ListItem","position":2,"name":n,"item":f"{BASE}column/{cs}.html"})
                    for k,e in enumerate(it,1): e['position']=k
                    v['itemListElement']=it; ch[0]=True
                for vv in v.values(): walk(vv)
            elif isinstance(v,list):
                for vv in v: walk(vv)
        walk(o)
        return m.group(1)+json.dumps(o,ensure_ascii=False,indent=2)+m.group(3) if ch[0] else m.group(0)
    p1=re.sub(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',bc,p1,flags=re.S)
    if p1!=p0: write(x,p1)
print(len(allslugs),'편,',len(CAT),'분류, 분류 페이지',len(made),'개')
