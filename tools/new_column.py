# 새 칼럼 만들기 (3단계)
# 1) 셸 만들기: 완성된 칼럼을 복제해 제목·주소·키워드만 바꾼 빈 틀을 만든다.
#    python3 tools/new_column.py shell <slug> <키워드> "<제목>" "<메타 키워드, 쉼표로>" "<표지 그림 설명>" [--from arrhythmia]
# 2) 본문 쓰기: tools/content/<slug>.py 를 example_chest_pain.py 형식으로 작성해 실행 (pb.build가 본문을 채운다).
#    표지: tools/covers/ 예시처럼 그려 images/col-<slug>.jpg 저장.
# 3) 마무리: 블로그 안내 상자·관련 칼럼 3개·날짜·사이트맵을 맞춘다. 그 뒤 tools/site.json 분류에 slug와 labels를 넣고
#    python3 tools/new_column.py finish <slug> <관련1> <관련2> <관련3>
#    python3 tools/build_index.py && python3 tools/link_orphans.py && python3 tools/check.py
import sys,re,html,json,datetime
from _common import COL, BASE, TODAY, read, write, touch, touch_sitemap
BLOG='https://m.blog.naver.com/kimyiho8787'
BOX=f'''<div class="blogbox">
  <p>원장님이 네이버 블로그에 진료 이야기와 건강 정보를 꾸준히 올리고 있습니다. 더 많은 이야기는 블로그에서 확인해 보세요.</p>
  <a href="{BLOG}" target="_blank" rel="noopener">블로그 보기</a>
</div>

'''
def shell(slug,kw,title,keys,alt,src='arrhythmia'):
    s=read(src)
    old_t=re.search(r'<h1>(.*?)</h1>',s).group(1)
    old_kw=re.search(r'<p class="crumb"><a href="\./">건강 칼럼</a> · (.*?)</p>',s).group(1)
    s=s.replace(old_t,title).replace(src+'.html',slug+'.html').replace(f'col-{src}.jpg',f'col-{slug}.jpg').replace(old_kw,f'인천 {kw} 한의원')
    s=re.sub(r'<meta name="keywords" content="[^"]*">',f'<meta name="keywords" content="{html.escape(keys,quote=True)}">',s)
    s=re.sub(r'<img class="cover" src="([^"]+)" alt="[^"]*">',lambda m:f'<img class="cover" src="{m.group(1)}" alt="{html.escape(alt,quote=True)}">',s)
    d=datetime.date.today()
    s=re.sub(r'(<p class="meta">.*?대표원장</a> · )\d{4}년 \d{1,2}월 \d{1,2}일',lambda m:m.group(1)+f'{d.year}년 {d.month}월 {d.day}일',s)
    s=re.sub(r'"datePublished": "[^"]*"',f'"datePublished": "{TODAY}"',s); s=touch(s)
    write(slug,s); print('셸 생성:',COL+slug+'.html')
def finish(slug,*rel):
    assert len(rel)==3,'관련 칼럼 3개'
    s=read(slug)
    if 'class="blogbox"' not in s:
        i=s.index('<h2 id="treat"'); j=s.index('<h2',i+5); s=s[:j]+BOX+s[j:]
    idx=open(COL+'index.html',encoding='utf-8').read()
    item={m.group(1):m.group(2) for m in re.finditer(r'<a class="item" href="([a-z0-9-]+)\.html"[^>]*>(.*?)</a>',idx)}
    cards="\n".join(f'      <a class="rel-card" href="{r}.html">{item[r]}</a>' for r in rel)
    s=re.sub(r'(<div class="rel-grid">\n).*?(\n    </div>)',lambda m:m.group(1)+cards+m.group(2),s,count=1,flags=re.S)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S): json.loads(b)
    d=html.unescape(re.search(r'<meta name="description" content="(.*?)"',s).group(1))
    write(slug,touch(s)); touch_sitemap([slug])
    print('마무리 완료. 설명 길이',len(d),'(155자 이하 권장)')
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='shell':
        src='arrhythmia'
        if '--from' in a: k=a.index('--from'); src=a[k+1]; a=a[:k]+a[k+2:]
        shell(*a[1:6],src=src)
    elif a and a[0]=='finish': finish(*a[1:])
    else: print(open(__file__,encoding='utf-8').read().split('import sys')[0])
