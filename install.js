// 서비스 워커 등록 + 앱 설치 버튼 처리 (index.html, install.html 공용)
(function () {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("sw.js").catch(function () {});
    });
  }

  var ua = navigator.userAgent;
  var isIOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var isKakao = /KAKAOTALK/i.test(ua);
  var isInApp = isKakao || /NAVER\(inapp|Instagram|FBAN|FBAV|Line\//i.test(ua);
  var isStandalone = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
  var deferred = null;

  function $all(sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); }
  function show(sel, on) { $all(sel).forEach(function (el) { el.hidden = !on; }); }

  function render() {
    show("[data-install-done]", isStandalone);
    show("[data-install-btn]", !isStandalone && !!deferred);
    show("[data-install-ios]", !isStandalone && isIOS && !isInApp);
    show("[data-install-inapp]", !isStandalone && isInApp);
    show("[data-install-other]", !isStandalone && !deferred && !isIOS && !isInApp);
  }

  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    render();
  });
  window.addEventListener("appinstalled", function () {
    deferred = null;
    isStandalone = true;
    render();
  });

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-install-btn]");
    if (btn && deferred) {
      deferred.prompt();
      deferred.userChoice.finally(function () { deferred = null; render(); });
      return;
    }
    var ext = e.target.closest("[data-open-external]");
    if (ext) {
      e.preventDefault();
      var url = location.href;
      if (isKakao) {
        location.href = "kakaotalk://web/openExternal?url=" + encodeURIComponent(url);
      } else if (/Android/i.test(ua)) {
        location.href = "intent://" + url.replace(/^https?:\/\//, "") + "#Intent;scheme=https;package=com.android.chrome;end";
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(function () { alert("주소를 복사했어요. Safari에 붙여넣어 열어 주세요."); });
      }
    }
  });

  document.addEventListener("DOMContentLoaded", render);
})();
