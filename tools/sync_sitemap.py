# 사이트맵(sitemap.xml)의 <lastmod>를 실제 수정 날짜에 맞춘다. build_index.py가 마지막에 부른다.
# 칼럼: 각 파일의 "dateModified". 칼럼 목록·분류 페이지·원장 소개: git에 마지막으로 바뀐 날짜(바뀐 채 아직 커밋 전이면 오늘).
import os,re,subprocess
from _common import ROOT, BASE, COL, TODAY
def file_day(rel):
    p=os.path.join(ROOT,rel)
    s=open(p,encoding='utf-8').read(); m=re.search(r'"dateModified": "(\d{4}-\d{2}-\d{2})"',s)
    if m and not rel.endswith(('index.html','doctor.html')) and '/cat-' not in rel: return m.group(1)
    dirty=subprocess.run(['git','status','--porcelain','--',rel],cwd=ROOT,capture_output=True,text=True).stdout.strip()
    if dirty: return TODAY
    d=subprocess.run(['git','log','-1','--format=%cs','--',rel],cwd=ROOT,capture_output=True,text=True).stdout.strip()
    return d or TODAY
def sync():
    p=os.path.join(ROOT,'sitemap.xml'); sm=open(p,encoding='utf-8').read()
    def fix(m):
        loc=m.group(1); rel=loc.replace(BASE,'')
        rel=rel+'index.html' if rel.endswith('/') else rel
        return f'<loc>{loc}</loc><lastmod>{file_day(rel)}</lastmod>'
    sm2=re.sub(r'<loc>([^<]+)</loc><lastmod>[^<]*</lastmod>',fix,sm)
    if sm2!=sm: open(p,'w',encoding='utf-8').write(sm2)
    return sm2.count('<loc>')
if __name__=='__main__': print('sitemap',sync(),'개 주소')
