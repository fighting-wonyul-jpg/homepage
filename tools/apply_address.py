# 행정구역 개편(2026-07-01 인천 서구 → 서해구·검단구)에 맞춰 주소를 고친다. 원장님 요청 2026-11-27.
# 구조화 데이터 MedicalClinic의 address를 서해구로, areaServed(아래 AREAS)와 hasMap을 맞추고, 화면 주소에 "(구 서구)"를 붙인다.
# 2026-11-27 원장님 요청으로 루원시티·청라국제도시·신현동·석남동, 부평구·계양구 추가. 지역을 바꾸려면 AREAS만 고치고 실행.
# 여러 번 실행해도 같은 결과. 사용: python3 tools/apply_address.py
import os,re,json,glob
from _common import ROOT
OLD_TXT='인천광역시 서구 가경주로 46, 2층 (가정동)'
NEW_TXT='인천광역시 서해구(구 서구) 가경주로 46, 2층 (가정동)'
MAP='https://map.naver.com/p/search/365%EC%8A%A4%EB%A7%88%EC%9D%BC%ED%95%9C%EC%9D%98%EC%9B%90/place/34838451'
ADDRESS={"@type":"PostalAddress","streetAddress":"가경주로 46, 2층 (가정동)","addressLocality":"서해구","addressRegion":"인천광역시","addressCountry":"KR"}
AREAS=[('AdministrativeArea','인천광역시 서해구'),('AdministrativeArea','인천광역시 서구'),('AdministrativeArea','인천광역시 검단구'),
       ('AdministrativeArea','인천광역시 부평구'),('AdministrativeArea','인천광역시 계양구'),
       ('Place','인천광역시 서해구 가정동'),('Place','루원시티'),('Place','청라국제도시'),('Place','인천광역시 서해구 신현동'),('Place','인천광역시 서해구 석남동')]
LD=re.compile(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',re.S)
def nodes(o):
    if isinstance(o,dict):
        yield o
        for v in o.values(): yield from nodes(v)
    elif isinstance(o,list):
        for v in o: yield from nodes(v)
def fix(ld):
    for n in nodes(ld):
        if n.get('@type')=='MedicalClinic' and 'address' in n:
            items=list(n.items()); n.clear()
            for k,v in items:
                if k in ('areaServed','hasMap'): continue
                n[k]=ADDRESS if k=='address' else v
                if k=='address':
                    n['areaServed']=[{"@type":t,"name":x} for t,x in AREAS]; n['hasMap']=MAP
def apply(s):
    s=s.replace(OLD_TXT,NEW_TXT)
    def rep(m):
        ld=json.loads(m.group(2)); fix(ld)
        return m.group(1)+json.dumps(ld,ensure_ascii=False,indent=2)+m.group(3)
    return LD.sub(rep,s)
if __name__=='__main__':
    n=0
    for p in glob.glob(os.path.join(ROOT,'column','*.html')):
        s=open(p,encoding='utf-8').read(); o=apply(s)
        if o!=s: open(p,'w',encoding='utf-8').write(o); n+=1
    print(n,'개 파일 수정')
