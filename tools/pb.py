# 칼럼 본문 빌더: 이미 있는 칼럼 페이지(셸)의 본문을 dict 내용으로 바꿔 쓴다.
# 사용법은 tools/content/example_chest_pain.py 참고.
import re, json, html
E=lambda x: html.escape(x,quote=True)
import os,sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from _common import COL, TODAY
CSS=open(COL+"insomnia.html",encoding="utf-8").read()
CSS=CSS[CSS.index("  .toc {"):CSS.index("  .notice {")]
def P(t): return f"<p>{t}</p>"
def UL(items,cls=None): 
    c=f' class="{cls}"' if cls else ""
    return f"<ul{c}>\n"+"\n".join(f"  <li>{i}</li>" for i in items)+"\n</ul>"
def OL(items): return "<ol>\n"+"\n".join(f"  <li>{i}</li>" for i in items)+"\n</ol>"
def B(k,v): return f"<b>{k}:</b> {v}"
def CHECK(items,note="이 체크리스트는 진단 도구가 아니라 상담이 필요한지 가늠해 보는 참고용입니다."):
    return UL(items,"checklist")+f'\n<p class="hint">{note}</p>'
def CARDS(types,intro=None,outro=None):
    out=[]
    if intro: out.append(P(intro))
    out.append('<div class="types">')
    for i,t in enumerate(types,1):
        rows="\n".join(f"      <dt>{E(k)}</dt><dd>{E(v)}</dd>" for k,v in t["rows"])
        out.append(f'''  <div class="type-card">
    <h3>{i}. {E(t["name"])} <span>{E(t["sub"])}</span></h3>
    <dl>
{rows}
    </dl>
  </div>''')
    out.append("</div>")
    if outro: out.append(P(outro))
    return "\n".join(out)
def ROAD(steps,note="기간과 횟수는 증상이 얼마나 오래되었는지, 동반 증상이 무엇인지에 따라 달라지며, 진찰 후 개인별로 안내합니다."):
    return '<ol class="road">\n'+"\n".join(f"  <li><b>{a}</b> {b}</li>" for a,b in steps)+f'\n</ol>\n<p class="hint">{note}</p>'
def H3(t): return f"<h3>{t}</h3>"
def build(slug,d):
    p=COL+slug+".html"; s=open(p,encoding="utf-8").read()
    s=re.sub(r'(<div class="answer">\s*<b>핵심 답변</b>\s*).*?(\s*</div>)',lambda m:m.group(1)+E(d["answer"])+m.group(2),s,count=1,flags=re.S)
    toc="\n".join(f'    <li><a href="#{sid}">{E(t)}</a></li>' for sid,t,_ in d["sections"])
    secs="\n\n".join(f'<h2 id="{sid}">{E(t)}</h2>\n{h}' for sid,t,h in d["sections"])
    body=f'''
<nav class="toc" aria-label="목차">
  <b>이 글의 순서</b>
  <ol>
{toc}
    <li><a href="#faq">자주 묻는 질문</a></li>
  </ol>
</nav>

{secs}
'''
    a=s.index('</div>',s.index('<div class="answer">'))+len('</div>')
    b=s.index('  <h2',a); b=s.index('  <h2 id="faq">',a) if '<h2 id="faq">' in s else s.index('  <h2>자주 묻는 질문',a)
    s=s[:a]+"\n"+body+"\n"+s[b:]
    s=s.replace('  <h2>자주 묻는 질문 Q&amp;A</h2>','  <h2 id="faq">자주 묻는 질문 Q&amp;A</h2>',1)
    F="\n".join(f"    <dt>Q{i}. {E(q)}</dt>\n    <dd>{E(x)}</dd>" for i,(q,x) in enumerate(d["faq"],1))
    s=re.sub(r'(<dl class="faq">\n).*?(\n  </dl>)',lambda m:m.group(1)+F+m.group(2),s,count=1,flags=re.S)
    R="\n".join((f'    <li>{E(t)} — <a href="{E(u)}" target="_blank" rel="noopener">원문</a></li>' if u else f'    <li>{E(t)}</li>') for t,u in d["refs"])
    s=re.sub(r'(<ul class="refs">\n).*?(\n  </ul>)',lambda m:m.group(1)+R+m.group(2),s,count=1,flags=re.S)
    s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{E(d["desc"])}">',s,count=1)
    s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{E(d["desc"])}">',s,count=1)
    m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
    for n in ld["@graph"]:
        if n["@type"]=="FAQPage": n["mainEntity"]=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":x}} for q,x in d["faq"]]
        if n["@type"]=="Article": n["description"]=d["desc"]; n["dateModified"]=TODAY
    s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
    if '.type-card' not in s: s=s.replace('  .notice {',CSS+'  .notice {',1)
    open(p,"w",encoding="utf-8").write(s)
    t=s[s.index('<div class="answer">'):s.index('<div class="cta">')]
    n=len(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',t))).strip())
    print(slug,n)
