# 행정구역 개편(2026-07-01 인천 서구 → 서해구·검단구)에 맞춰 주소를 고친다. 원장님 요청 2026-11-27.
# 구조화 데이터 address를 서해구로, areaServed(서해구·서구·검단구·가정동)와 hasMap을 넣고, 화면 주소에 "(구 서구)"를 붙인다.
# 여러 번 실행해도 같은 결과. 사용: python3 tools/apply_address.py
import os,re,glob
from _common import ROOT
OLD_TXT='인천광역시 서구 가경주로 46, 2층 (가정동)'
NEW_TXT='인천광역시 서해구(구 서구) 가경주로 46, 2층 (가정동)'
MAP='https://map.naver.com/p/search/365%EC%8A%A4%EB%A7%88%EC%9D%BC%ED%95%9C%EC%9D%98%EC%9B%90/place/34838451'
AREAS=[('AdministrativeArea','인천광역시 서해구'),('AdministrativeArea','인천광역시 서구'),('AdministrativeArea','인천광역시 검단구'),('Place','인천광역시 서해구 가정동')]
def block(ind):
    i=' '*ind; j=' '*(ind+2)
    areas=',\n'.join(f'{j}{{"@type": "{t}", "name": "{n}"}}' for t,n in AREAS)
    return (f'"address": {{\n{j}"@type": "PostalAddress",\n{j}"streetAddress": "가경주로 46, 2층 (가정동)",\n'
            f'{j}"addressLocality": "서해구",\n{j}"addressRegion": "인천광역시",\n{j}"addressCountry": "KR"\n{i}}},\n'
            f'{i}"areaServed": [\n{areas}\n{i}],\n{i}"hasMap": "{MAP}"')
PAT=re.compile(r'"address": \{\n( *)"@type": "PostalAddress",\n *"streetAddress": "가경주로 46, 2층",\n *"addressLocality": "인천광역시 서구",\n *"addressCountry": "KR"\n( *)\}')
def apply(s):
    s=PAT.sub(lambda m: block(len(m.group(2))),s)
    return s.replace(OLD_TXT,NEW_TXT)
if __name__=='__main__':
    n=0
    for p in glob.glob(os.path.join(ROOT,'column','*.html'))+glob.glob(os.path.join(ROOT,'tools','*.py'))+glob.glob(os.path.join(ROOT,'tools','*','*.py')):
        if p.endswith('apply_address.py'): continue
        s=open(p,encoding='utf-8').read(); o=apply(s)
        if o!=s: open(p,'w',encoding='utf-8').write(o); n+=1
    print(n,'개 파일 수정')
