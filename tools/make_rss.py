# 네이버 서치어드바이저 RSS 제출용 rss.xml(루트)을 만든다. 최근에 쓰거나 고친 칼럼 50편을 새 소식으로 알린다.
# build_index.py가 마지막에 자동으로 부른다. 따로 실행: python3 tools/make_rss.py
# 제출 주소: https://column.smileclinics.net/rss.xml (서치어드바이저 → 요청 → RSS 제출)
import os,re,html,datetime,email.utils
from _common import ROOT, BASE, column_slugs, read

N=50
def info(slug):
    s=read(slug)
    t=re.search(r'<h1>(.*?)</h1>',s,re.S).group(1); t=html.unescape(re.sub(r'<[^>]+>|\s+',' ',t)).strip()
    d=html.unescape(re.search(r'<meta name="description" content="(.*?)"',s).group(1))
    pub=re.search(r'"datePublished": "(\d{4}-\d{2}-\d{2})"',s); mod=re.search(r'"dateModified": "(\d{4}-\d{2}-\d{2})"',s)
    day=(mod or pub).group(1)
    return day,(pub.group(1) if pub else day),t,d
def rfc(day):
    y,m,d=map(int,day.split('-'))
    return email.utils.format_datetime(datetime.datetime(y,m,d,9,0,tzinfo=datetime.timezone(datetime.timedelta(hours=9))))
def build():
    rows=sorted(((info(x),x) for x in column_slugs()),key=lambda r:(r[0][0],r[0][1],r[1]),reverse=True)[:N]
    items="\n".join(f'''  <item>
    <title>{html.escape(t)}</title>
    <link>{BASE}column/{x}.html</link>
    <guid isPermaLink="true">{BASE}column/{x}.html</guid>
    <description>{html.escape(d)}</description>
    <pubDate>{rfc(day)}</pubDate>
  </item>''' for (day,_,t,d),x in rows)
    last=rfc(rows[0][0][0])
    xml=f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>365스마일한의원 건강 칼럼</title>
  <link>{BASE}column/</link>
  <atom:link href="{BASE}rss.xml" rel="self" type="application/rss+xml"/>
  <description>인천 서구 가정동 365스마일한의원 문원열 대표원장이 증상별 원인과 한방 치료, 생활 관리법을 정리한 건강 칼럼입니다.</description>
  <language>ko</language>
  <lastBuildDate>{last}</lastBuildDate>
{items}
</channel>
</rss>
'''
    p=os.path.join(ROOT,'rss.xml')
    if not os.path.exists(p) or open(p,encoding='utf-8').read()!=xml: open(p,'w',encoding='utf-8').write(xml)
    return len(rows)
if __name__=='__main__': print('rss.xml',build(),'편')
