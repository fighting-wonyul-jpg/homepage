# 구글에 보여 줄 칼럼을 주력 칼럼(site.json의 google_core)으로 줄인다. (원장님 결정 2026-11-16)
# 배경: 구글이 220편 대부분을 "크롤링됨 - 색인 생성되지 않음"으로 뺐다. 주력 40편만 구글에 남기고 품질을 올린 뒤 차츰 다시 연다.
# - 주력이 아닌 칼럼: <meta name="googlebot" content="noindex, follow"> 를 넣는다. 구글에만 적용되고 네이버·사이트 안 목록은 그대로다.
# - sitemap-google.xml: 구글 서치콘솔 제출용(첫 화면·원장 소개·분류 페이지·주력 칼럼). sitemap.xml은 네이버용으로 전체를 유지한다.
# build_index.py가 마지막에 부른다. 다시 열려면 google_core에 slug를 더하고 build_index.py를 실행한다.
import os,re
from _common import ROOT, BASE, site, column_slugs, read, write
TAG='<meta name="googlebot" content="noindex, follow">\n'
def apply():
    core=set(site().get('google_core',[])); slugs=column_slugs()
    assert core<=set(slugs),('google_core에 없는 칼럼',core-set(slugs))
    for x in slugs:
        s=read(x); o=s
        s=s.replace(TAG,'')
        if core and x not in core:
            a='<meta name="robots" content="index, follow">\n'
            assert a in s,x
            s=s.replace(a,a+TAG,1)
        if s!=o: write(x,s)
    sm=open(os.path.join(ROOT,'sitemap.xml'),encoding='utf-8').read()
    keep=[]
    for m in re.finditer(r'  <url><loc>([^<]+)</loc>.*?</url>\n',sm):
        name=m.group(1).rsplit('/',1)[-1][:-5]
        if not core or name=='' or name=='doctor' or name.startswith('cat-') or name in core: keep.append(m.group(0))
    head=sm[:sm.index('  <url>')]
    open(os.path.join(ROOT,'sitemap-google.xml'),'w',encoding='utf-8').write(head+''.join(keep)+'</urlset>\n')
    return len(core),len(keep)
if __name__=='__main__': print('주력 %d편, 구글 사이트맵 %d개 주소'%apply())
