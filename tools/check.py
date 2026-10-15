# 전체 칼럼 점검: 깨진 링크, 구조화 데이터 오류, 설명 길이, 관련 칼럼, 연결 없는 칼럼, 금지 표현, 공통 블록 누락.
# 사용: python3 tools/check.py   (문제가 없으면 "문제 없음")
import re,os,json,html,collections
from _common import ROOT, COL, site, column_slugs, read
S=site(); kids=set(dict(S['categories']).get('소아',[]))
P=collections.defaultdict(list); inb=collections.Counter()
def text(s):
    s=re.sub(r'<style.*?</style>|<script.*?</script>|<p class="notice">.*?</p>','',s,flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>',' ',s))
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    s=open(COL+f,encoding='utf-8').read(); slug=f[:-5]
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S):
        try: json.loads(b)
        except Exception as e: P['구조화 데이터 오류'].append((f,str(e)[:60]))
    for h in re.findall(r'(?:href|src)="([^"#:?]+)"',s):
        p=os.path.normpath(os.path.join(COL,h)); p=os.path.join(p,'index.html') if os.path.isdir(p) else p
        if not os.path.exists(p): P['깨진 링크'].append((f,h))
    if slug not in column_slugs(): continue
    d=html.unescape(re.search(r'<meta name="description" content="(.*?)"',s).group(1))
    if len(d)>155: P['설명 155자 초과'].append((f,len(d)))
    n=re.findall(r'href="([a-z0-9-]+)\.html"',re.search(r'<div class="rel-grid">(.*?)</div>',s,re.S).group(1))
    if len(set(n))!=3 or slug in n: P['관련 칼럼 이상'].append((f,n))
    for x in n: inb[x]+=1
    for c in ['class="visit"','class="blogbox"','class="mbar"','class="author"','class="area"']:
        if c not in s: P['블록 누락 '+c].append(f)
    t=text(s)
    for w,why in [(r'뜸(?:을|은|이|과|·| 치료| 요법)','뜸은 시행하지 않음'),(r'산부인과와 상의','임신 문구 규칙 (배란통의 피임약 안내는 예외)'),
                  (r'부작용(?:이|은)? ?(?:전혀 )?없|100% ?(?:효과|완치)|최고의 치료|특효|완치(?:시킵|됩니다)|보장합니다','의료광고 금지 표현'),
                  (r'추나[^.]{0,30}상담할 수 있습니다','추나는 "진찰 후 시행합니다"')]:
        for m in re.finditer(w,t):
            if slug=='ovulation-pain' and '피임약' in t[max(0,m.start()-60):m.start()]: continue
            P[why].append((f,re.sub(r'\s+',' ',t[max(0,m.start()-30):m.end()+20])))
    if slug in kids:
        for m in re.finditer('약침',t):
            c=t[max(0,m.start()-40):m.end()+40]
            if not re.search(r'않|성인|청소년|고려|어떻게',c): P['소아 약침 확인'].append((f,re.sub(r'\s+',' ',c)))
for f in column_slugs():
    if inb[f]==0: P['다른 칼럼에서 연결 없음 (link_orphans.py 실행)'].append(f)
if not P: print('문제 없음')
for k,v in P.items():
    print(f'## {k} ({len(v)})')
    for x in v[:15]: print('  ',x)
