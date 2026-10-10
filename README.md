# 365스마일한의원 홈페이지

인천광역시 서구 가경주로 46, 2층 (가정동) · 대표원장 문원열

GitHub Pages로 배포되는 정적 홈페이지입니다. 빌드 과정 없이 `index.html` 한 파일로 구성되어 있습니다.

## 수정해야 할 항목

`index.html`에서 아래 자리표시자를 찾아 실제 내용으로 바꿔 주세요.

- `000-0000-0000` : 실제 전화번호 (여러 곳)
- `[ ]` 표시가 있는 부분 : 원장 이력, 자격, 진료 철학, 일요일·공휴일 진료, 주차 안내
- 원장 사진 영역 (`.photo`)

## 배포

`main` 브랜치에 push하면 GitHub Pages가 자동으로 반영합니다. 저장소 Settings → Pages에서 Source를 `Deploy from a branch`, Branch를 `main` / `/ (root)`로 설정해 주세요.

## 앱(PWA) 설치

홈페이지는 휴대폰 홈 화면에 앱처럼 설치할 수 있는 PWA입니다.

- 설치 안내 페이지: `install.html` (https://fighting-wonyul-jpg.github.io/homepage/install.html)
- QR 코드: `icons/qr-install.png`, `icons/qr-install.svg` → 위 설치 페이지로 연결됩니다. 설치 페이지의 **QR 안내문 인쇄** 버튼으로 진료실에 붙일 안내문을 바로 출력할 수 있습니다.
- 안드로이드(Chrome)는 "앱 설치하기" 버튼, 아이폰(Safari)은 "공유 → 홈 화면에 추가" 안내가 자동으로 표시됩니다. 카카오톡 등 인앱 브라우저에서는 기본 브라우저로 열도록 안내합니다.

관련 파일: `manifest.webmanifest`(앱 이름·아이콘·색상), `sw.js`(오프라인 캐시), `install.js`(설치 버튼), `offline.html`, `icons/`

**주의**
- 페이지 내용을 수정한 뒤에는 `sw.js`의 `VERSION` 값(`v1` → `v2` …)을 올려야 설치된 앱에도 새 내용이 반영됩니다.
- 전화번호를 바꿀 때 `offline.html`, `install.html`의 `000-0000-0000`도 함께 바꿔 주세요.
- 사이트 주소(도메인)가 바뀌면 QR 코드를 새 주소로 다시 만들어야 합니다.
