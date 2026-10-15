# (보관용) 블로그 공지·영상 정보만으로 쓴 2차 버전. 다시 쓰려면: python3 tools/make_doctor_v2.py
# 원장 소개(column/doctor.html)의 본문과 구조화 데이터를 다시 쓴다. 헤더·진료 안내·버튼 등 나머지 틀은 그대로 둔다.
# 원장님 블로그 공지 두 편(2026-08-24·25)과 유튜브 영상 정보만으로 쓴 버전(2026-10-15). 1차 버전(원장님 소개 글 기반)은 make_doctor_v1.py.
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

  <img class="doc-photo" src="../images/doctor.jpg" alt="진료실에서 경혈 인체 모형을 보고 있는 문원열 대표원장" width="966" height="598">

  <blockquote class="quote">
    <p>아픈 부위만 보지 않고,<br>통증의 원인을 눈으로 직접 확인합니다.</p>
    <cite>문원열 대표원장</cite>
  </blockquote>

  <div class="profile">
    <p>안녕하세요. 인천 가정동 365스마일한의원 대표원장 문원열입니다. 15년 동안 환자분들을 진료해 왔고, 가정동 한자리에서 10년째 진료하고 있습니다.</p>
    <p>진료실에 들어오시는 분들의 첫마디에는 짙은 피로와 체념이 배어 있을 때가 많습니다. 수개월, 길게는 수년 동안 디스크와 협착증으로 다리 저림을 견뎌 오신 분, 오래된 내과·신경계 질환으로 일상이 무너진 분들입니다.</p>
  </div>

  <h2>나도 아파 봤기에</h2>
  <p>저 역시 한의사가 된 뒤 부정맥과 두드러기로 일상생활이 힘들 만큼 아팠던 적이 있습니다. 아무리 쉬어도 회복되지 않던 그때, 저를 다시 일으켜 세운 것은 체질에 맞춘 한약이었습니다. 몸이 무너지는 경험을 해 보았기에, 환자 한 분 한 분의 간절함을 가볍게 여기지 않습니다.</p>

  <h2>겉과 속을 함께 치료합니다</h2>
  <blockquote class="quote">
    <p>관절과 척추 속은 초음파로 정확하게 확인하고,<br>지친 몸의 속은 맞춤 한약으로 깊이 있게 치료합니다.</p>
    <cite>365스마일한의원 진료 철학</cite>
  </blockquote>
  <ul class="how">
    <li><b>겉 치료 – 초음파로 보며 하는 통증 치료:</b> 초음파로 근육, 힘줄, 관절, 신경을 실시간으로 보면서 문제가 생긴 자리에 약침(초음파 가이드 약침)을 놓고, 추나 요법으로 뭉치고 틀어진 부위를 풀어 줍니다.</li>
    <li><b>속 치료 – 원장이 직접 달이는 10일 맞춤 한약:</b> 약재 선별부터 달이는 과정까지 외부에 맡기지 않고 원내 탕전실에서 직접 합니다. 한 달 치를 한 번에 드리지 않고 10일분씩 처방해, 경과를 보며 약재 구성과 양을 조절합니다.</li>
  </ul>

  <h2>맞춤 한약을 처방하는 질환</h2>
  <p>급성 질환이나 단순 소화불량은 짧은 기간 안에 경과를 보고, 담적병·오래된 피부염·만성 신경계 질환은 2~3개월 이상 단계를 나눠 진행합니다.</p>
  <table class="herb-table">
    <tr><th>구분</th><th>질환</th></tr>
{HERB_ROWS}
  </table>

  <h2>첫 진료가 조금 긴 이유</h2>
  <p>통증과 질환이 시작된 원인을 찾기 위해 자율신경 검사, 초음파 진단 등 진찰 과정을 거칩니다. 첫 방문 때는 시간이 조금 더 걸리는 점 양해 부탁드립니다.</p>

  <h2>퇴근 후, 주말, 공휴일에도</h2>
  <p>평일 저녁 8시까지, 토·일·공휴일에도 진료합니다. 어디서부터 어떻게 치료해야 할지 몰라 답답하셨다면 편안한 마음으로 이야기해 주세요.</p>

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
DESC='인천 서구 가정동 365스마일한의원 문원열 대표원장 소개. 임상 15년, 가정동에서 10년째 진료하며 초음파로 통증의 원인을 보고 원장이 직접 달인 맞춤 한약으로 겉과 속을 함께 치료합니다.'
s=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{html.escape(DESC,quote=True)}">',s)
s=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="{html.escape(DESC,quote=True)}">',s)
m=re.search(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',s,re.S); ld=json.loads(m.group(2))
for n in ld['@graph']:
    if n.get('@type')=='ProfilePage':
        per=n['mainEntity']
        per.pop('memberOf',None)
        per['image']=BASE+'images/doctor.jpg'
        per['knowsAbout']=['통증 관리','추나 요법','약침','초음파 가이드 약침','한약']
        per['description']=DESC
        n['dateModified']='2026-10-15'
s=s[:m.start(2)]+json.dumps(ld,ensure_ascii=False,indent=2)+s[m.end(2):]
open(p,'w',encoding='utf-8').write(s); print('doctor.html 갱신')
