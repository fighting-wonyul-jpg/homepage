# 원장 소개(column/doctor.html)의 본문과 구조화 데이터를 다시 쓴다. 헤더·진료 안내·버튼 등 나머지 틀은 그대로 둔다.
# 원장님이 준 소개 글(2026-10-15)을 바탕으로 하며, 의료광고 기준에 맞게 "최고", "효과적" 같은 표현은 다듬었다.
import re,json,html
from _common import COL, BASE, site, column_slugs
p=COL+'doctor.html'; s=open(p,encoding='utf-8').read()
DOC=BASE+'column/doctor.html'
cats=site()['categories']; total=len(column_slugs())
areas="\n".join(f'    <li><a href="./#cat-{i}">{html.escape(n)}</a></li>' for i,(n,_) in enumerate(cats,1))
CAREER=['임상 경력 15년','현재 한의원(인천 서구 가정동)에서 개원 후 10년째 진료','FCST 턱관절학회','연부조직학회','침도학회','복지학회','동의방약학회']
GROUPS=[('소화기',[('만성 소화불량','chronic-dyspepsia'),('위염','gastritis'),('담적병','damjeok'),('역류성 식도염','reflux-esophagitis'),('과민성대장증후군','ibs')]),
 ('신경정신계',[('두통','headache'),('어지럼증','dizziness'),('메니에르병','meniere'),('불면증','insomnia'),('화병','hwabyung'),('공황장애','panic-disorder'),('불안장애','anxiety-disorder'),('틱장애','tic-disorder')]),
 ('안면',[('안면마비(구안와사)','facial-palsy'),('삼차신경통','trigeminal-neuralgia'),('얼굴 떨림','hemifacial-spasm')]),
 ('피부',[('여드름','acne'),('두드러기','urticaria'),('습진','eczema'),('지루성피부염','seborrheic-dermatitis'),('아토피','atopic-dermatitis')]),
 ('여성·전신',[('생리통','menstrual-pain'),('무월경','amenorrhea'),('갱년기 홍조','menopause'),('다한증','hyperhidrosis'),('부정맥','arrhythmia')])]
HERB_ROWS="\n".join(f'    <tr><th>{g}</th><td>'+', '.join(f'<a href="{u}.html">{n}</a>' for n,u in xs)+'</td></tr>' for g,xs in GROUPS)
BODY=f'''<article>
  <p class="crumb"><a href="./">건강 칼럼</a> · 원장 소개</p>
  <h1>문원열 대표원장 소개</h1>
  <p class="meta">365스마일한의원 · 인천 서구 가정동</p>

  <img class="doc-photo" src="../images/doctor.jpg" alt="진료실에서 경혈 인체 모형을 보고 있는 문원열 대표원장" width="801" height="497">

  <blockquote class="quote">
    <p>좋은 의사는 질병을 치료하고,<br>최선의 의사는 질병을 가진 환자를 치료한다.</p>
    <cite>윌리엄 오슬러</cite>
  </blockquote>

  <div class="profile">
    <p class="lead">환자 한 분 한 분의 아픔을 깊이 들여다보고, 근본적인 원인을 찾아 치료합니다.</p>
    <p>안녕하세요. 인천 가정동 365스마일한의원 대표원장 문원열입니다. 평일 저녁은 물론 주말과 공휴일에도 진료합니다. 저는 어릴 때 몸이 약해 한의원에서 자주 치료를 받으며 건강해졌고, 친척 가운데 계신 한의사 선생님들께 치료받으러 다니며 자연스럽게 한의사의 꿈을 키웠습니다.</p>
    <p>한의사가 된 뒤에도 부정맥과 두드러기로 일상생활이 힘들 만큼 아팠던 적이 있습니다. 아무리 쉬어도 몸이 회복되지 않던 그 시절, 저를 다시 일으켜 세운 것은 체질에 맞춘 한약이었습니다. "나도 아파 봤기에, 그 간절함을 잘 압니다." 그래서 환자 한 분 한 분의 간절함을 가볍게 여기지 않습니다.</p>
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

  <h2>초음파로 보며 하는 통증 치료</h2>
  <p>수개월 이상 이어지는 디스크, 척추관협착증, 만성 요통, 팔·다리 저림은 겉으로 드러난 통증만의 문제가 아닌 경우가 많습니다. 통증이 시작되는 깊은 곳의 유착이나 신경이 눌린 부위를 정확히 파악하는 것이 중요합니다.</p>
  <p>그래서 초음파로 근육, 힘줄, 관절, 신경의 상태를 실시간으로 보면서 문제가 생긴 위치에 약침(초음파 가이드 약침)을 놓고, 추나 요법으로 뭉치고 틀어진 부위를 풀어 줍니다. "아픈 부위만 보지 않고, 통증의 원인을 눈으로 직접 확인합니다."</p>

  <h2>원장이 직접 달이는 10일 맞춤 한약</h2>
  <p>담적병, 역류성 식도염, 두통, 불면증처럼 오래가는 만성 질환일수록 약재의 품질과 세심한 경과 확인이 중요하다고 생각합니다. 그래서 약재 선별부터 추출까지 탕전의 전 과정을 외부에 맡기지 않고, 원장이 원내 탕전실에서 직접 관리하고 달입니다.</p>
  <p>한 번에 한 달 치를 드리지 않고 10일분씩 처방합니다. 10일마다 복용 경과를 확인해 약재의 구성과 용량을 조절하며, 약을 드시는 동안 생기는 몸의 변화를 꼼꼼히 살핍니다.</p>

  <h2>겉과 속을 함께 치료합니다</h2>
  <blockquote class="quote">
    <p>관절과 척추 속은 초음파로 정확하게 확인하고,<br>지친 몸의 속은 맞춤 한약으로 깊이 있게 치료합니다.</p>
    <cite>365스마일한의원 진료 철학</cite>
  </blockquote>
  <p>겉의 통증만 잡으면 몸속 원인 때문에 다시 아프기 쉽고, 속만 치료해서는 당장의 구조적인 통증을 빨리 덜기 어렵습니다. 그래서 초음파 가이드 약침과 추나로 관절·척추·신경의 압박과 염증을 다스리는 <b>겉 치료</b>와, 체질에 맞춘 한약으로 장부의 균형을 바로잡고 스스로 회복하는 힘을 돕는 <b>속 치료</b>를 함께 합니다.</p>
  <p>체질에 맞춘 한약은 아래와 같은 질환에 처방합니다. 급성 질환이나 단순 소화불량은 짧은 기간 안에 경과를 보고, 담적병·오래된 피부염·만성 신경계 질환은 2~3개월 이상 단계를 나눠 진행합니다.</p>
  <table class="herb-table">
    <tr><th>진료 구분</th><th>맞춤 한약 처방 대상 질환</th></tr>
{HERB_ROWS}
  </table>

  <h2>이렇게 진료합니다</h2>
  <ul class="how">
    <li><b>원인을 찾는 진료:</b> 아픈 부위만 치료하지 않고, 불편한 증상이 왜 생겼는지 원인을 찾아 진료합니다. 그래서 첫 진료 때는 상담에 시간이 조금 더 걸릴 수 있으니 양해 부탁드립니다.</li>
    <li><b>필요한 검사:</b> 자율신경 검사, 체성분 검사, 혈액 검사, 초음파 등 진단 기기로 필요한 검사를 진행합니다.</li>
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
  .doc-photo { display: block; width: 100%; height: auto; border-radius: 14px; margin: 14px 0 4px; }
</style>'''
if '.career {' not in s: s=s.replace('</style>',CSS,1)
if '.herb-table {' not in s: s=s.replace('</style>','  .herb-table { width: 100%; border-collapse: collapse; margin: 12px 0 4px; font-size: .95rem; }\n  .herb-table th, .herb-table td { padding: 10px 8px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }\n  .herb-table tr:first-child th { background: var(--bg-soft); }\n  .herb-table th { white-space: nowrap; color: var(--brand); }\n</style>',1)
if '.doc-photo {' not in s: s=s.replace('</style>','  .doc-photo { display: block; width: 100%; height: auto; border-radius: 14px; margin: 14px 0 4px; }\n</style>',1)
DESC='인천 서구 가정동 365스마일한의원 문원열 대표원장 소개. 임상 15년, 개원 후 10년째 진료하며 턱관절·연부조직·침도 학회에서 활동하고, 통증 관리(추나·약침), 갱년기 다이어트, 난치성 질환을 주로 진료합니다.'
s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(DESC,quote=True)}">',s)
s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{html.escape(DESC,quote=True)}">',s)
m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
for n in ld['@graph']:
    if n.get('@type')=='ProfilePage':
        per=n['mainEntity']
        per['memberOf']=[{"@type":"Organization","name":x} for x in CAREER[2:]]
        per['image']=BASE+'images/doctor.jpg'
        per['knowsAbout']=['통증 관리','추나 요법','약침','초음파 가이드 약침','갱년기 다이어트','한약']
        per['description']=DESC
        n['dateModified']='2026-10-15'
s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
open(p,'w',encoding='utf-8').write(s); print('doctor.html 갱신')
