# 칼럼 본문 중간(치료 섹션 뒤)의 블로그 안내 상자를 네이버 블로그 링크 카드(썸네일·제목·요약·주소)로 바꾼다.
# 원장님 요청(2026-10-20): 블로그 목록 링크를 카드 모양으로. 썸네일은 블로그 대표 사진과 같은 원장 사진(images/doctor.jpg). 원장님이 이 카드에 한해 칼럼 안 원장 사진을 허용함.
# 여러 번 실행해도 같은 결과. 사용: python3 tools/apply_blogcard.py
import re
from _common import column_slugs, read, write

URL='https://m.blog.naver.com/PostList.naver?blogId=kimyiho8787&amp;tab=1'
CARD=f'''<div class="blogbox">
  <a class="bcard" href="{URL}" target="_blank" rel="noopener"><img src="../images/doctor.jpg" alt="365스마일한의원 문원열 원장 네이버 블로그" width="966" height="598" loading="lazy"><span class="bc-t">잘 낫지 않는 증상, 원인을 끝까지 묻는 365스마일한의원 원장님 블로그</span><span class="bc-d">초음파로 원인을 보고, 10일 한약으로 경과를 잡습니다. 진료 이야기와 건강 정보를 블로그에서 더 보실 수 있습니다.</span><span class="bc-u">m.blog.naver.com</span></a>
</div>
'''
CSS='''  .blogbox:has(.bcard) { display: block; padding: 0; border: 0; background: none; margin: 30px 0; }
  .blogbox a.bcard { display: block; padding: 0; border: 1px solid var(--line); border-radius: 12px; overflow: hidden; background: var(--bg); color: var(--text); font-weight: 400; text-decoration: none; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
  .bcard img { display: block; width: 100%; height: auto; aspect-ratio: 5 / 3; object-fit: cover; object-position: center 30%; }
  .bcard span { display: block; padding: 0 16px; }
  .bcard .bc-t { padding-top: 12px; font-weight: 700; font-size: 1rem; line-height: 1.45; }
  .bcard .bc-d { margin-top: 4px; color: var(--muted); font-size: .9rem; line-height: 1.5; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
  .bcard .bc-u { padding-bottom: 12px; margin-top: 6px; color: #03c75a; font-size: .85rem; }
'''
def apply(s):
    s=re.sub(r'<div class="blogbox">\n.*?\n</div>\n',CARD.replace('\\','\\\\'),s,count=1,flags=re.S)
    if '.bcard .bc-t' not in s: s=s.replace('</style>',CSS+'</style>',1)
    return s
if __name__=='__main__':
    n=0
    for slug in column_slugs():
        s=read(slug); o=s; s=apply(s)
        if s!=o: write(slug,s); n+=1
    print(n,'편 수정')
