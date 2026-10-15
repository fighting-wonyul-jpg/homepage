# 칼럼 공통 기능(column/site.js)을 모든 페이지에 연결하고, 칼럼에는 "가족에게 보내기" 상자를 글쓴이 소개 앞에 넣는다.
# 체크리스트 클릭·상담 안내, 공유 버튼, 계절별 많이 찾는 칼럼은 site.js가 처리한다. 여러 번 실행해도 한 번만 들어감.
import os
from _common import COL, NON_COLUMN, touch
CSS='''  .checklist li { cursor: pointer; border-radius: 8px; transition: background .15s; user-select: none; }
  .checklist li:hover { background: var(--bg-soft); }
  .checklist li.on { font-weight: 600; }
  .checklist li.on::before { background: var(--brand); box-shadow: inset 0 0 0 2px var(--bg); }
  .check-tip { margin: 0 0 6px; font-size: .9rem; font-weight: 700; color: var(--brand); }
  .check-result { margin: 10px 0 4px; padding: 14px 16px; border-radius: 12px; background: var(--bg-soft); border: 1px solid var(--line); }
  .check-result p { margin: 0; }
  .check-btns { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
  .check-btns a { padding: 9px 14px; border-radius: 10px; font-weight: 700; font-size: .92rem; text-decoration: none; border: 1.5px solid var(--brand); color: var(--brand); }
  .check-btns a.cb-book { background: var(--brand); color: var(--on-brand); }
  .check-btns a.cb-kakao { background: #fee500; border-color: #fee500; color: #191919; }
  .share { margin-top: 32px; padding: 16px 18px; border-radius: 14px; border: 1px dashed var(--line); text-align: center; }
  .share p { margin: 0 0 10px; font-weight: 700; }
  .share .sh-btns { display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; }
  .share button { font: inherit; font-weight: 700; font-size: .92rem; padding: 9px 16px; border-radius: 10px; cursor: pointer; border: 1.5px solid var(--brand); background: var(--bg); color: var(--brand); }
  .share button.sh-native { background: var(--brand); color: var(--on-brand); }
  .share .sh-msg { margin: 8px 0 0; font-size: .85rem; font-weight: 400; color: var(--muted); min-height: 1em; }
</style>'''
SHARE='''  <section class="share" aria-label="공유">
    <p>이 글이 도움이 될 가족이나 지인에게 보내 주세요</p>
    <div class="sh-btns">
      <button type="button" class="sh-native" hidden>카카오톡·문자로 보내기</button>
      <button type="button" class="sh-copy">링크 복사</button>
    </div>
    <p class="sh-msg" aria-live="polite"></p>
  </section>

  <section class="author"'''
n=0
for f in sorted(os.listdir(COL)):
    if not f.endswith('.html'): continue
    p=COL+f; s=open(p,encoding='utf-8').read(); o=s
    if 'src="site.js"' not in s: s=s.replace('<script src="ga.js" defer></script>','<script src="ga.js" defer></script>\n<script src="site.js" defer></script>',1)
    if '.check-result {' not in s: s=s.replace('</style>',CSS,1)
    if f[:-5] not in NON_COLUMN and 'class="share"' not in s:
        assert s.count('  <section class="author"')==1,f
        s=s.replace('  <section class="author"',SHARE,1)
    if s!=o: open(p,'w',encoding='utf-8').write(touch(s) if f[:-5] not in NON_COLUMN else s); n+=1
print(n,'페이지')
