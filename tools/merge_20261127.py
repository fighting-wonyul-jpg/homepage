# 원장님 요청(2026-11-27): 두통 4편, 교통사고 4편을 각각 한 칼럼으로 합친다.
# - 군발두통·생리 편두통·소아 두통 → headache (섹션 #cluster #menstrual #child)
# - 편타손상·사고 후 두통 어지럼·사고 후 불면 불안 → traffic-accident (섹션 #neck #head #sleep)
# 옛 주소는 site.json redirects로 이동 페이지가 되고(build_index.py), 분류·짧은 이름·검색어·구글 주력·관련 칼럼 카드에서 정리한다.
# 한 번만 실행하는 작업 기록용 스크립트입니다.
import json,os,re
from _common import ROOT, COL, read, write, touch, touch_sitemap, column_slugs
MERGE={'cluster-headache':'headache','menstrual-migraine':'headache','child-headache':'headache',
       'whiplash':'traffic-accident','accident-headache':'traffic-accident','accident-insomnia':'traffic-accident'}

HEAD_SEC='''<h2 id="cluster">눈 뒤를 찌르는 두통이 몇 주씩 몰려온다면, 군발두통</h2>
<p>늘 같은 쪽 눈 안쪽이나 관자놀이가 송곳으로 쑤시듯 아프고, 그쪽 눈이 붉어지며 눈물과 콧물이 흐른다면 군발두통을 생각합니다. 한 번 오면 15분에서 세 시간쯤 이어지고, 몇 주에서 몇 달 동안 거의 매일 비슷한 시각에, 특히 잠든 지 한두 시간 뒤에 찾아왔다가 한동안 잠잠해집니다. 너무 아파 누워 있지 못하고 방 안을 서성이게 되는 점이 편두통과 다릅니다.</p>
<ul>
  <li><b>신경과 진단이 먼저:</b> 발작을 끊는 산소 흡입과 트립탄, 몰려오는 기간을 줄이는 예방약은 모두 처방이 필요한 치료입니다. 처음 의심될 때는 신경과에서 진단과 MRI를 받으세요. 50세 넘어 처음 생겼거나, 시야가 흐려지면서 눈이 단단하게 아프다면(급성 녹내장) 곧바로 진료를 받아야 합니다.</li>
  <li><b>몰려오는 기간에는 술을 끊기:</b> 이 기간에는 맥주 한 잔으로도 한 시간 안팎에 발작이 오는 일이 많습니다. 기간이 끝날 때까지 술을 멀리하고, 낮잠과 들쭉날쭉한 수면, 담배도 피하세요.</li>
  <li><b>한의원의 역할:</b> 발작과 발작 사이에 아픈 쪽 뒷목과 어깨의 굳은 근육을 침과 약침으로 풀고, 탕약으로 흐트러진 잠과 지친 몸을 돌봅니다. 베라파밀 같은 예방약을 드신다면 알려 주시면 확인해 처방하며, 한약이 예방약을 대신하지는 않습니다. 군발두통에 대한 침 연구는 아직 규모가 작습니다.</li>
</ul>

<h2 id="menstrual">생리 무렵마다 되풀이되는 편두통, 월경 편두통</h2>
<p>생리 시작 이틀 전부터 생리 셋째 날 사이에 편두통이 오고, 세 번의 주기 가운데 두 번 이상 이 무렵에 맞춰 온다면 월경 관련 편두통으로 봅니다(국제두통질환분류 ICHD-3). 생리 직전 에스트로겐이 갑자기 떨어지는 것이 방아쇠가 되며, 평소 편두통보다 오래가고 진통제가 덜 듣는 일이 많습니다.</p>
<ul>
  <li><b>생리일과 두통을 한 달력에:</b> 생리 시작일, 두통이 온 날, 세기(0~10), 먹은 약을 두세 주기 적어 오시면 생리와의 관계를 분명하게 볼 수 있습니다.</li>
  <li><b>한의학의 경행두통(經行頭痛):</b> 생리 직전 기운이 위로 치솟아 관자놀이가 터질 듯 욱신거리는 경우와, 생리가 끝날 무렵 혈이 비어 머리가 띵하고 은은하게 아픈 경우를 나누어 다스립니다.</li>
  <li><b>주기에 맞춘 치료:</b> 두통이 예상되는 생리 일주일 전후부터 침을 시작하고, 탕약은 생리 전에는 치솟는 기운을 가라앉히는 쪽으로, 생리 뒤에는 빠져나간 혈을 채우는 쪽으로 무게를 옮깁니다. 임신을 준비 중이라면 진료 때 꼭 알려 주세요. 확인 후 안전한 약재로 처방합니다.</li>
  <li><b>피임약을 쓰는 분:</b> 눈앞이 번쩍이는 조짐이 있는 편두통이라면 에스트로겐이 든 경구피임약이 뇌졸중 위험을 높일 수 있습니다. 피임약을 시작하거나 바꿀 때 처방한 곳에 편두통 조짐이 있다는 사실을 꼭 알리세요.</li>
</ul>

<h2 id="child">아이가 머리가 자주 아프다고 할 때, 소아 두통</h2>
<p>아이가 되풀이해서 머리가 아프다고 할 때도 대부분은 편두통이나 긴장성 두통입니다. 아이의 편두통은 어른과 달리 이마 양쪽이나 관자놀이가 함께 아프고, 배가 아프거나 토하는 일이 많으며 지속 시간이 짧은 편입니다. 어릴 때 멀미가 심했거나 부모 중에 편두통이 있는 아이에게 흔합니다.</p>
<ul>
  <li><b>검사부터 받아야 하는 아이:</b> 아침에 눈뜨자마자 머리가 아프며 토할 때, 두통 때문에 자다가 깰 때, 몇 주에 걸쳐 점점 잦아지고 세질 때, 걸음이 비틀거리거나 물체가 둘로 보일 때, 갑자기 멍해지거나 성격이 달라졌을 때는 소아청소년과·소아신경과에서 영상 검사를 먼저 받으세요.</li>
  <li><b>생활 리듬부터:</b> 주말에도 잠드는 시각을 크게 바꾸지 않고, 아침을 거르지 않으며 학교에 물병을 챙겨 줍니다. 자기 전 한 시간은 휴대폰과 태블릿을 멀리하게 해 주세요. 4주쯤 아픈 날과 그날의 잠·끼니·화면 시간을 적어 오시면 원인을 찾는 데 도움이 됩니다.</li>
  <li><b>아이 치료는 어른과 다릅니다:</b> 어린이에게는 약침을 쓰지 않습니다. 초등학생까지는 피부에 붙이는 소아 스티커침을 쓰고, 탕약은 쓴맛이 덜한 약재 위주로 지으며, 아이가 넘기기 힘들어하면 집에서 단것을 조금 타서 먹여도 됩니다.</li>
</ul>

'''
ACC_SEC='''<h2 id="neck">사고 뒤 목이 뻣뻣하고 고개가 안 돌아간다면, 편타손상</h2>
<p>뒤에서 받히는 순간 몸통은 좌석에 밀려 앞으로 나가고 머리는 잠깐 뒤에 남았다가 튕겨 나갑니다. 이때 목의 근육과 인대, 목뼈 뒤쪽의 작은 관절이 늘어나는 것이 편타손상(목 염좌)이며, 사고 당일보다 다음 날이나 이틀 뒤에 고개 돌리기가 더 힘들어지는 일이 흔합니다.</p>
<ul>
  <li><b>얼마나 다쳤는지 나누기:</b> 1995년 캐나다 퀘벡 특별위원회 분류(WAD)는 목 통증만 있는 1단계, 움직임이 줄고 압통이 뚜렷한 2단계, 팔 저림·힘 빠짐 같은 신경 증상이 있는 3단계, 골절이나 탈구가 있는 4단계로 나눕니다. 한의원은 주로 1~2단계를 치료하고, 3단계는 신경 검사와 함께 보며, 4단계는 정형외과·신경외과 치료가 먼저입니다.</li>
  <li><b>CT가 먼저인 경우:</b> 목뼈 한가운데를 누르면 몹시 아프거나 고개를 좌우로 거의 돌리지 못할 때, 65세 이상이거나 차가 뒤집힐 만큼 큰 사고였을 때는 응급실에서 영상 검사부터 받으세요.</li>
  <li><b>목 치료:</b> 초음파로 다친 근육과 인대의 붓기와 깊이를 확인하며 약침·초음파 가이드 약침을 놓고, 침을 꽂은 채 고개를 천천히 돌려 보는 운동침도 씁니다. 붓기가 가라앉는 시기부터는 진찰 후 추나 요법을 시행합니다.</li>
  <li><b>집에서:</b> 목 보조기는 병원에서 권한 기간만 차고, 아프지 않은 범위에서 고개를 조금씩 움직이는 편이 오래 고정하는 것보다 낫습니다. 벽에 등을 대고 턱을 살짝 뒤로 당긴 채 5초 버티기를 하루 두세 번 해 보세요.</li>
</ul>

<h2 id="head">사고 뒤 두통과 어지럼이 계속된다면</h2>
<p>사고 뒤 일주일 안에 시작된 두통은 외상 후 두통으로 따로 분류하며(국제두통질환분류 ICHD-3), 석 달 넘게 이어지면 지속성으로 봅니다. 원인은 한 가지보다 몇 가지가 겹치는 경우가 많습니다.</p>
<ul>
  <li><b>목에서 올라오는 두통:</b> 뒤통수에서 시작해 눈 뒤나 관자놀이로 뻗치고, 고개를 돌리거나 오래 숙이면 심해집니다. 뒤통수 아래 근육과 목 위쪽 관절을 눌러 두통이 재현되는지 보고, 그 자리를 침·약침으로 풉니다.</li>
  <li><b>뇌진탕 뒤 증상:</b> 머리를 직접 부딪치지 않아도 크게 흔들리면 두통, 멍함, 빛과 소리에 대한 예민함이 몇 주 갈 수 있습니다. 첫 하루 이틀은 푹 쉬고, 그 뒤에는 증상이 심해지지 않는 범위에서 짧은 산책부터 활동을 늘립니다.</li>
  <li><b>고개를 돌릴 때만 빙글 돈다면:</b> 누웠다 일어나거나 돌아누울 때 1분이 안 되게 천장이 도는 어지럼은 충격으로 귀 속 돌가루가 제자리를 벗어난 이석증일 수 있습니다. 이비인후과에서 돌가루를 되돌리는 치료를 받으세요.</li>
  <li><b>다시 검사가 필요한 신호:</b> 어르신이나 혈액을 묽게 하는 약을 드시는 분은 몇 주 뒤 머리 안에 피가 고이는 만성 경막하 출혈이 드러나기도 합니다. 처음 CT가 정상이었어도 두통이 새로 심해지거나 걸음이 이상해지고 멍해지면 다시 검사를 받으세요.</li>
</ul>

<h2 id="sleep">사고 뒤 잠을 못 자고 차 타기가 무섭다면</h2>
<p>누우면 사고 장면이 떠올라 잠들기 어렵고, 경적이나 급정거 소리에 심장이 내려앉고, 조수석에서도 발에 힘이 들어가는 것은 큰 충격을 겪은 뒤 흔한 반응이며 대개 몇 주에 걸쳐 줄어듭니다. 한의학은 『황제내경』의 '놀라면 기가 어지러워진다(驚則氣亂)'는 말로 이를 설명하고, 작은 일에도 깜짝 놀라는 상태(심담허겁)와 사고 처리 과정의 억울함으로 가슴이 꽉 막힌 상태(간기울결)를 나누어 다스립니다.</p>
<ul>
  <li><b>진찰:</b> 잠드는 시각과 밤중에 깨는 횟수, 악몽을 여쭙고 자율신경 검사로 긴장 정도를 확인합니다. 수면제나 항불안제를 드신다면 알려 주시면 확인해 처방합니다.</li>
  <li><b>치료:</b> 손목의 신문·내관처럼 마음을 가라앉히는 혈에 침을 놓고, 긴장으로 굳은 뒷목과 날개뼈 사이에는 약침과 온열 요법을 합니다. 증상이 가벼운 경우 한약 치료를 중심으로 관리하기도 합니다. 증상이 깊으면 정신건강의학과 치료를 함께 받으세요.</li>
  <li><b>운전은 한 단계씩:</b> 조수석, 익숙한 짧은 길, 낮 시간 운전 순서로 다시 익숙해지고, 사고가 난 길은 맨 마지막에 가 보세요.</li>
  <li><b>바로 도움을 받아야 할 때:</b> 한 달이 지나도 악몽과 회피, 놀람이 줄지 않으면 정신건강의학과에서 외상 후 스트레스 장애 평가를 받으세요. 스스로를 해칠 것 같은 생각이 들면 자살예방 상담전화 109에 바로 연락하세요.</li>
</ul>

'''
def add(slug,sec,toc,kw):
    s=read(slug)
    assert 'id="'+toc[0][0]+'"' not in s
    s=s.replace('<h2 id="home">',sec+'<h2 id="home">',1)
    li=''.join(f'    <li><a href="#{i}">{t}</a></li>\n' for i,t in toc)
    s=s.replace('    <li><a href="#home">',li+'    <li><a href="#home">',1)
    s=re.sub(r'(<meta name="keywords" content="[^"]*?), 인천 서구 한의원',lambda m:m.group(1)+', '+kw+', 인천 서구 한의원',s,count=1)
    write(slug,touch(s))
if not os.environ.get("CARDS"): add("headache",HEAD_SEC,[('cluster','눈 뒤를 찌르는 두통, 군발두통'),('menstrual','생리 무렵마다 오는 월경 편두통'),('child','아이가 머리가 자주 아플 때, 소아 두통')],'군발두통, 생리 두통, 월경 편두통, 소아 두통')
if not os.environ.get("CARDS"): add("traffic-accident",ACC_SEC,[('neck','사고 뒤 목 통증, 편타손상'),('head','사고 뒤 두통·어지럼'),('sleep','사고 뒤 불면·불안')],'교통사고 두통, 교통사고 어지럼, 교통사고 불면')

def tidy_site():
    # site.json 정리
    p=os.path.join(ROOT,'tools','site.json'); S=json.load(open(p,encoding='utf-8'))
    S['categories']=[[n,[x for x in ss if x not in MERGE]] for n,ss in S['categories']]
    for k in ('popular','google_core'):
        if k in S: S[k]=[x for x in S[k] if x not in MERGE]
    if 'seasonal' in S:
        for k,v in S['seasonal'].items(): S['seasonal'][k]=[x for x in v if x not in MERGE]
    syn=S.get('synonyms',{})
    for old,new in MERGE.items():
        S['labels'].pop(old,None)
        if old in syn:
            v=syn.pop(old); syn.setdefault(new,[])
            for w in v:
                if w not in syn[new]: syn[new].append(w)
    extra={'headache':['군발두통','생리 두통','월경 편두통','소아 두통','아이 두통'],'traffic-accident':['목 염좌','편타손상','교통사고 두통','교통사고 어지럼','교통사고 불면','교통사고 불안','자보']}
    for new,ws in extra.items():
        syn.setdefault(new,[])
        for w in ws:
            if w not in syn[new]: syn[new].append(w)
    S['redirects'].update(MERGE)
    json.dump(S,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); open(p,'a',encoding='utf-8').write('\n')
    print('site.json 정리')
if not os.environ.get('CARDS'): tidy_site()

# 관련 칼럼 카드에서 합쳐진 칼럼을 새 칼럼(이미 있으면 같은 분류의 다른 칼럼)으로 바꾼다. build_index.py 실행 뒤 다시 실행해도 됨.
def fix_cards():
    S=json.load(open(os.path.join(ROOT,'tools','site.json'),encoding='utf-8')); cat_of={s:n for n,ss in S['categories'] for s in ss}
    idx=open(COL+'index.html',encoding='utf-8').read()
    item={m.group(1):m.group(2) for m in re.finditer(r'<a class="item" href="([a-z0-9-]+)\.html"[^>]*>(.*?)</a>',idx)}
    changed=[]
    for f in column_slugs():
        s=read(f); m=re.search(r'(<div class="rel-grid">\n)(.*?)(\n    </div>)',s,re.S)
        if not m: continue
        rel=re.findall(r'href="([a-z0-9-]+)\.html"',m.group(2))
        if not any(r in MERGE for r in rel): continue
        new=[]
        for r in rel:
            if r not in MERGE: new.append(r); continue
            c=MERGE[r]
            if c==f or c in rel or c in new:
                c=next(t for t in S['categories'][[n for n,_ in S['categories']].index(cat_of[f])][1]+column_slugs() if t!=f and t not in rel and t not in new and t not in MERGE)
            new.append(c)
        cards="\n".join(f'      <a class="rel-card" href="{r}.html">{item[r]}</a>' for r in new)
        s=s[:m.start(2)]+cards+s[m.end(2):]
        write(f,touch(s)); changed.append(f); print(f,rel,'→',new)
    touch_sitemap(changed)
if __name__=='__main__' and os.environ.get('CARDS'): fix_cards()
