# 구조화 데이터에서 원장(Person)과 한의원(MedicalClinic)을 하나의 대상으로 묶는다. (2026-11-27)
# - 한의원: @id = column/#clinic. 칼럼의 MedicalClinic, publisher, 원장 소개의 worksFor가 모두 같은 한의원을 가리킨다.
# - 원장: @id = column/doctor.html#doctor. 칼럼 작성자(author)에 worksFor(365스마일한의원)를 넣는다.
# - 원장 소개의 worksFor에는 주소·전화·진료시간·지도·진료 지역까지 한의원 정보를 모두 넣는다(칼럼의 MedicalClinic에서 복사).
# build_index.py가 마지막에 부른다. 따로 실행: python3 tools/apply_entity_links.py
import os,re,json,glob
from _common import ROOT, BASE
CLINIC_ID=BASE+'column/#clinic'; DOC_ID=BASE+'column/doctor.html#doctor'
LD=re.compile(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)',re.S)
def nodes(o):
    if isinstance(o,dict):
        yield o
        for v in o.values(): yield from nodes(v)
    elif isinstance(o,list):
        for v in o: yield from nodes(v)
def clinic_full():
    s=open(os.path.join(ROOT,'column','lumbar-disc.html'),encoding='utf-8').read()
    for m in LD.finditer(s):
        for n in nodes(json.loads(m.group(2))):
            if n.get('@type')=='MedicalClinic' and 'address' in n:
                c={'@type':'MedicalClinic','@id':CLINIC_ID}
                c.update({k:v for k,v in n.items() if k not in ('@type','@id')}); return c
def fix(ld,full):
    for n in nodes(ld):
        t=n.get('@type')
        if t=='MedicalClinic' and n.get('name')=='365스마일한의원' and n.get('@id')!=CLINIC_ID:
            items=list(n.items()); n.clear(); n['@type']=t; n['@id']=CLINIC_ID
            n.update((k,v) for k,v in items if k not in ('@type','@id'))
        if t=='Person' and n.get('name')=='문원열':
            if n.get('@id')!=DOC_ID:
                items=list(n.items()); n.clear(); n['@type']=t; n['@id']=DOC_ID
                n.update((k,v) for k,v in items if k not in ('@type','@id'))
            n['worksFor']=full if n.get('url')==n.get('@id','').split('#')[0] and 'memberOf' in n else {'@type':'MedicalClinic','@id':CLINIC_ID,'name':'365스마일한의원'}
def apply():
    full=clinic_full(); cnt=0
    for p in sorted(glob.glob(os.path.join(ROOT,'column','*.html'))):
        s=open(p,encoding='utf-8').read(); o=s
        def rep(m):
            ld=json.loads(m.group(2)); fix(ld,full)
            return m.group(1)+json.dumps(ld,ensure_ascii=False,indent=2)+m.group(3)
        s=LD.sub(rep,s)
        if s!=o: open(p,'w',encoding='utf-8').write(s); cnt+=1
    return cnt
if __name__=='__main__': print(apply(),'개 파일 수정')
