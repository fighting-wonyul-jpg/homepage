# 공통 경로와 작은 도우미
import os, re, json, html, datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COL=os.path.join(ROOT,'column')+os.sep
BASE='https://fighting-wonyul-jpg.github.io/homepage/'
TODAY=datetime.date.today().isoformat()
NON_COLUMN={'index','doctor'}
def site(): return json.load(open(os.path.join(ROOT,'tools','site.json'),encoding='utf-8'))
def column_slugs(): return sorted(f[:-5] for f in os.listdir(COL) if f.endswith('.html') and f[:-5] not in NON_COLUMN)
def read(slug): return open(COL+slug+'.html',encoding='utf-8').read()
def write(slug,s): open(COL+slug+'.html','w',encoding='utf-8').write(s)
def touch(s,date=None):
    """dateModified를 오늘 날짜로."""
    return re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"',f'"dateModified": "{date or TODAY}"',s)
def touch_sitemap(slugs,date=None):
    p=os.path.join(ROOT,'sitemap.xml'); sm=open(p,encoding='utf-8').read()
    for slug in slugs:
        u=f'{BASE}column/{slug}.html'
        if u in sm: sm=re.sub(re.escape(u)+r'</loc><lastmod>[^<]*',u+f'</loc><lastmod>{date or TODAY}',sm)
        else: sm=sm.replace('</urlset>',f'  <url><loc>{u}</loc><lastmod>{date or TODAY}</lastmod></url>\n</urlset>')
    open(p,'w',encoding='utf-8').write(sm)
