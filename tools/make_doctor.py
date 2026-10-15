# 원장 소개(column/doctor.html)의 본문과 구조화 데이터를 다시 쓴다. 헤더·진료 안내·버튼 등 나머지 틀은 그대로 둔다.
# 원장님이 준 소개 글(2026-10-15)을 바탕으로 하며, 의료광고 기준에 맞게 "최고", "효과적" 같은 표현은 다듬었다.
import re,json,html
from _common import COL, BASE, site, column_slugs
p=COL+'doctor.html'; s=open(p,encoding='utf-8').read()
DOC=BASE+'column/doctor.html'
cats=site()['categories']; total=len(column_slugs())
areas="\n".join(f'    <li><a href="./#cat-{i}">{html.escape(n)}</a></li>' for i,(n,_) in enumerate(cats,1))
CAREER=['현재 한의원(인천 서구 가정동)에서 개원 후 10년째 진료','FCST 턱관절학회','연부조직학회','침도학회','복지학회','동의방약학회']
BODY=f'''<article>
  <p class="crumb"><a href="./">건강 칼럼</a> · 원장 소개</p>
  <h1>문원열 대표원장 소개</h1>
  <p class="meta">365스마일한의원 · 인천 서구 가정동</p>

  <blockquote class="quote">
    <p>좋은 의사는 질병을 치료하고,<br>최선의 의사는 질병을 가진 환자를 치료한다.</p>
    <cite>윌리엄 오슬러</cite>
  </blockquote>

  <div class="profile">
    <p class="lead">환자 한 분 한 분의 아픔을 깊이 들여다보고, 근본적인 원인을 찾아 치료합니다.</p>
    <p>안녕하세요. 365스마일한의원 원장 문원열입니다. 저는 어릴 때 몸이 약해 한의원에서 자주 치료를 받으며 건강해졌고, 친척 가운데 계신 한의사 선생님들께 치료받으러 다니며 자연스럽게 한의사의 꿈을 키웠습니다.</p>
    <p>한의사가 된 뒤에도 부정맥과 두드러기로 일상생활이 힘들 만큼 몸이 안 좋았던 때가 있었습니다. 그때 한약으로 몸을 추스른 경험이 있어, 지금도 아픈 분들의 마음을 누구보다 가까이 이해하려고 합니다.</p>
  </div>

  <h2>주요 이력</h2>
  <ul class="career">
{chr(10).join(f"    <li>{html.escape(c)}</li>" for c in CAREER)}
  </ul>

  <h2>진료 철학</h2>
  <p>환자를 만날 때마다 '이분께 어떻게 하면 도움이 될 수 있을까?'를 먼저 생각합니다. 불편한 곳이 빨리 나아질 수 있도록 꾸준히 공부하고 연구하며, 좋은 기운으로 기분 좋게 치료받고 가실 수 있도록 제 컨디션 관리에도 늘 신경 씁니다.</p>
  <p>저의 꿈은 윌리엄 오슬러의 말처럼 '좋은 의사를 넘어 최선의 의사'가 되는 것입니다. 질병만 보는 것이 아니라 마음과 몸을 함께 살펴, 환자분이 더 나은 일상을 살아가도록 곁에서 함께 걷겠습니다. 환자 한 분 한 분을 소중한 가족처럼 대하겠습니다.</p>

  <h2>365스마일한의원이 지향하는 것</h2>
  <ol class="mission">
    <li>환자분이 행복해지도록 돕는 한의원</li>
    <li>환자분의 고통을 덜어 드리는 한의원</li>
    <li>진정성 있는 의료 서비스를 드리는 한의원</li>
  </ol>

  <h2>이렇게 진료합니다</h2>
  <ul class="how">
    <li><b>원인을 찾는 진료:</b> 아픈 부위만 치료하지 않고, 불편한 증상이 왜 생겼는지 원인을 찾아 진료합니다. 그래서 첫 진료 때는 상담에 시간이 조금 더 걸릴 수 있으니 양해 부탁드립니다.</li>
    <li><b>필요한 검사:</b> 자율신경 검사, 체성분 검사, 혈액 검사, 초음파 등 진단 기기로 필요한 검사를 진행합니다.</li>
    <li><b>10일씩 처방하는 한약:</b> 한약은 꼼꼼히 살피기 위해 10일분씩 처방하고, 중간 경과를 확인한 뒤 처방을 바꾸거나 약재를 더합니다.</li>
    <li><b>침·약침·추나·온열 요법:</b> 약침은 일반 약침과, 근골격계 통증에 초음파 화면으로 바늘 끝을 확인하며 놓는 초음파 가이드 약침을 모두 시행합니다. 병원 검사나 다른 진료가 먼저 필요한 경우에는 그 점을 먼저 안내합니다.</li>
  </ul>

  <h2>주요 진료 분야</h2>
  <ul class="how">
    <li><b>통증 관리 (추나·약침):</b> 손이나 도구로 뼈, 근육, 관절을 조정하는 추나와 약침으로 목·허리 같은 척추 질환과 근골격계·관절 통증을 관리합니다.</li>
    <li><b>다이어트, 특히 갱년기 다이어트:</b> 갱년기에는 몸과 마음에 변화가 많아 갑자기 체중이 늘어 힘들어하는 분이 많습니다. 체중 관리와 함께 몸과 마음이 모두 편안해지도록 돕습니다.</li>
    <li><b>오래된 난치성 질환:</b> 잘 낫지 않는 질환으로 지친 분들의 삶의 질이 나아지도록 함께 방법을 찾습니다.</li>
  </ul>

  <h2>영상으로 만나는 진료 철학</h2>
  <div class="video">
    <iframe src="https://www.youtube-nocookie.com/embed/Cr1kxTnYP_8" title="인천 가정동에서 10년째 진료하는 한의사의 진료 철학" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  <p class="video-cap">인천 가정동에서 10년째 진료하는 한의사의 진료 철학 (5분) · <a href="https://youtu.be/Cr1kxTnYP_8" target="_blank" rel="noopener">유튜브에서 보기</a></p>

  <h2>원장님 이야기 더 보기</h2>
  <ul class="links">
    <li><a href="https://m.blog.naver.com/PostView.naver?blogId=kimyiho8787&amp;logNo=224389405891" target="_blank" rel="noopener"><small>네이버 블로그</small>잘 낫지 않는 만성통증 원인을 끝까지 묻는 365스마일한의원 진료 안내</a></li>
    <li><a href="https://m.blog.naver.com/PostView.naver?blogId=kimyiho8787&amp;logNo=224388459097" target="_blank" rel="noopener"><small>네이버 블로그</small>인천 가정동 365스마일한의원 진료과목 소개</a></li>
    <li><a href="https://www.youtube.com/@365smilekmd" target="_blank" rel="noopener"><small>유튜브 채널</small>스마일 한의사 문원열</a></li>
  </ul>

  <h2>원장님이 쓴 건강 칼럼 {total}편</h2>
  <p>증상별 원인과 한방 치료, 집에서 하는 관리법을 분야별로 정리했습니다.</p>
  <ul class="areas">
{areas}
  </ul>

'''
a=s.index('<article>'); b=s.index('  <section class="visit">'); s=s[:a]+BODY+s[b:]
CSS='''  .quote { margin: 18px 0 6px; padding: 16px 18px; border-left: 4px solid var(--brand); background: var(--bg-soft); border-radius: 0 12px 12px 0; }
  .quote p { margin: 0; font-weight: 700; font-size: 1.05rem; line-height: 1.7; }
  .quote cite { display: block; margin-top: 6px; font-style: normal; font-size: .88rem; color: var(--muted); }
  .career { list-style: none; padding: 0; margin: 10px 0 0; display: grid; gap: 6px; }
  .career li { padding: 10px 14px; border-radius: 10px; background: var(--bg-soft); font-weight: 600; }
  .career li::before { content: "▸ "; color: var(--brand); }
  .mission li, .how li { margin-bottom: 8px; }
</style>'''
if '.career {' not in s: s=s.replace('</style>',CSS,1)
DESC='인천 서구 가정동 365스마일한의원 문원열 대표원장 소개. 개원 후 10년째 진료하며 턱관절·연부조직·침도 학회에서 활동하고, 통증 관리(추나·약침), 갱년기 다이어트, 난치성 질환을 주로 진료합니다.'
s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(DESC,quote=True)}">',s)
s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{html.escape(DESC,quote=True)}">',s)
m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
for n in ld['@graph']:
    if n.get('@type')=='ProfilePage':
        per=n['mainEntity']
        per['memberOf']=[{"@type":"Organization","name":x} for x in CAREER[1:]]
        per['knowsAbout']=['통증 관리','추나 요법','약침','초음파 가이드 약침','갱년기 다이어트','한약']
        per['description']=DESC
        n['dateModified']='2026-10-15'
s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
open(p,'w',encoding='utf-8').write(s); print('doctor.html 갱신')
