# 365스마일한의원 건강 칼럼

인천광역시 서구 가경주로 46, 2층 (가정동) · 대표원장 문원열

GitHub Pages로 배포되는 정적 칼럼 사이트입니다: https://fighting-wonyul-jpg.github.io/homepage/column/

- `column/` : 칼럼 페이지와 칼럼 목록(`column/index.html`)
- `images/col-*.jpg` : 칼럼 대표 이미지
- `sitemap.xml` : 검색엔진 제출용 사이트맵
- `google465fb42647d81226.html` : 구글 서치콘솔 소유 확인 파일 (지우지 마세요)
- `index.html`, `install.html` : 예전 홈페이지·앱 설치 주소(QR 포함)를 칼럼 목록으로 넘겨 주는 이동 페이지
- `sw.js` : 예전에 앱으로 설치한 휴대폰의 캐시를 정리하고 스스로 해제하는 파일 (지우지 마세요)

`main` 브랜치에 push하면 GitHub Pages가 자동으로 반영합니다.
- `CLAUDE.md` : 칼럼 작성 규칙(원장님 확인 사항), 새 칼럼 만드는 순서, 병원 정보
- `tools/` : 칼럼 셸 생성·본문 빌더·목록 재생성·점검 스크립트 (`python3 tools/check.py`로 전체 점검)
