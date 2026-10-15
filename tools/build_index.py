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
nav=[f'    <li><a href="./" data-cat="all" aria-current="true">전체<small>{len(allslugs)}</small></a></li>']
nav+=[f'    <li><a href="#cat-{i}" data-cat="cat-{i}">{html.escape(n)}<small>{len(ss)}</small></a></li>' for i,(n,ss) in enumerate(CAT,1)]
import datetime
_m=datetime.date.today().month
NOW='spring' if 3<=_m<=5 else 'summer' if 6<=_m<=8 else 'autumn' if 9<=_m<=11 else 'winter'
pop="\n".join(f'    <li><a href="{x}.html">{html.escape(LABEL[x])}</a></li>' for x in POP)
for sea,xs in S.get('seasonal',{}).items():
    for x in xs:
        if x in POP: continue
        pop+="\n"+f'    <li data-season="{sea}"'+('' if sea==NOW else ' hidden')+f'><a href="{x}.html">{html.escape(LABEL[x])}</a></li>'

secs="\n".join(f'''  <section class="cat" id="cat-{i}">
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
  <ul class="cat-nav">
'''+"\n".join(nav)+'''
  </ul>
'''+secs+'''
<script>
(function(){
  var links=document.querySelectorAll('.cat-nav a'), secs=document.querySelectorAll('.cat'), items=document.querySelectorAll('.cat .item');
  var q=document.getElementById('q'), msg=document.getElementById('qmsg');
  function norm(t){ return (t||'').toLowerCase().replace(/[\\s·()（）,.]/g,''); }
  items.forEach(function(a){ a._k=norm(a.textContent+' '+(a.dataset.k||'')); });
  function show(id){
    items.forEach(function(a){ a.hidden=false; });
    secs.forEach(function(s){ s.hidden = !(id==='all' || s.id===id); });
    links.forEach(function(a){ a.setAttribute('aria-current', a.dataset.cat===id ? 'true' : 'false'); });
  }
  function search(){
    var t=norm(q.value);
    document.body.classList.toggle('searching', !!t);
    if(!t){ msg.textContent=''; fromHash(); return; }
    var n=0;
    links.forEach(function(a){ a.setAttribute('aria-current', a.dataset.cat==='all' ? 'true' : 'false'); });
    secs.forEach(function(s){
      var c=0; s.querySelectorAll('.item').forEach(function(a){ var ok=a._k.indexOf(t)>-1; a.hidden=!ok; if(ok) c++; });
      s.hidden = c===0; n+=c;
    });
    msg.textContent = n ? '검색 결과 '+n+'편' : '찾는 칼럼이 없습니다. 증상이 궁금하시면 0507-1495-4600으로 전화 주세요.';
  }
  links.forEach(function(a){
    a.addEventListener('click', function(ev){
      ev.preventDefault(); var id=a.dataset.cat; q.value=''; msg.textContent=''; document.body.classList.remove('searching'); show(id);
      history.replaceState(null,'', id==='all' ? location.pathname : '#'+id);
    });
  });
  q.addEventListener('input', search);
  function fromHash(){ var h=location.hash.slice(1); show(h && document.getElementById(h) ? h : 'all'); }
  window.addEventListener('hashchange', function(){ q.value=''; msg.textContent=''; fromHash(); });
  fromHash();
})();
</script>
'''
s=re.sub(r'  <div class="search">.*?</div>\n','',s,count=1,flags=re.S)
a=s.index('  <p class="cat-label">')
b=s.index('</script>',s.index('<script>',s.index('<section class="cat"')))+len('</script>\n')
s=s[:a]+TOP+s[b:]
bb=s.index('  <div class="blogbox">'); s=s[:bb]+SEARCH+s[bb:]
m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
def fix(o):
    if isinstance(o,dict):
        if o.get('@type')=='ItemList':
            o['itemListElement']=[{"@type":"ListItem","position":i,"url":f"{BASE}column/{x}.html","name":html.unescape(page(x)[0])} for i,x in enumerate(allslugs,1)]
        for v in o.values(): fix(v)
    elif isinstance(o,list):
        for v in o: fix(v)
fix(ld); s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
open(COL+'index.html','w',encoding='utf-8').write(s)
print(len(allslugs),'편,',len(CAT),'분류')
