/* 칼럼 공통 기능: 눌러 보는 체크리스트, 가족에게 보내기, 계절별 많이 찾는 칼럼 */
(function(){
  var BOOK = 'https://m.booking.naver.com/booking/13/bizes/208486?theme=place&lang=ko&area=ple';
  var KAKAO = 'https://pf.kakao.com/_YUqxjG/chat';
  function ev(name, params){ if (window.gtag) gtag('event', name, params || {}); }

  /* 1. 체크리스트: 항목을 눌러 체크, 3개 이상이면 상담 안내 */
  document.querySelectorAll('ul.checklist').forEach(function(ul){
    var items = ul.querySelectorAll('li');
    var box = document.createElement('div');
    box.className = 'check-result'; box.hidden = true; box.setAttribute('aria-live', 'polite');
    var hint = ul.nextElementSibling && ul.nextElementSibling.classList.contains('hint') ? ul.nextElementSibling : ul;
    hint.insertAdjacentElement('afterend', box);
    var shown = false;
    function update(){
      var n = ul.querySelectorAll('li.on').length;
      var tip = ul.previousElementSibling && ul.previousElementSibling.classList.contains('check-tip') ? ul.previousElementSibling : null;
      if (n >= 3) {
        box.hidden = false;
        box.innerHTML = '<p><b>' + n + '개 항목에 해당합니다.</b> 진료로 정확한 상태를 확인해 보시길 권합니다.</p>' +
          '<div class="check-btns"><a class="cb-book" href="' + BOOK + '" target="_blank" rel="noopener">네이버 예약</a>' +
          '<a class="cb-kakao" href="' + KAKAO + '" target="_blank" rel="noopener">카톡 문의</a>' +
          '<a class="cb-call" href="tel:0507-1495-4600">전화 상담</a></div>';
        if (!shown) { shown = true; ev('checklist_result', { checked: n }); }
      } else if (n > 0) {
        box.hidden = false;
        box.innerHTML = '<p>' + n + '개 항목에 해당합니다. 3개 이상이면 진료를 받아 보시길 권합니다.</p>';
      } else { box.hidden = true; }
    }
    items.forEach(function(li){
      li.setAttribute('role', 'checkbox'); li.setAttribute('aria-checked', 'false'); li.tabIndex = 0;
      function toggle(){ li.classList.toggle('on'); li.setAttribute('aria-checked', li.classList.contains('on')); update(); }
      li.addEventListener('click', toggle);
      li.addEventListener('keydown', function(e){ if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); toggle(); } });
    });
    var tip = document.createElement('p'); tip.className = 'check-tip'; tip.textContent = '해당하는 항목을 눌러 체크해 보세요.';
    ul.insertAdjacentElement('beforebegin', tip);
  });

  /* 2. 가족에게 보내기 */
  document.querySelectorAll('.share').forEach(function(sec){
    var url = location.href.split('#')[0], title = document.title;
    var nb = sec.querySelector('.sh-native'), cb = sec.querySelector('.sh-copy'), msg = sec.querySelector('.sh-msg');
    if (navigator.share && nb) {
      nb.hidden = false;
      nb.addEventListener('click', function(){
        navigator.share({ title: title, text: '건강 칼럼을 보내 드려요: ' + title, url: url }).then(function(){ ev('share', { method: 'native' }); }).catch(function(){});
      });
    }
    if (cb) cb.addEventListener('click', function(){
      function done(){ msg.textContent = '링크를 복사했습니다. 카카오톡이나 문자에 붙여 넣어 보내 주세요.'; ev('share', { method: 'copy' }); }
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(url).then(done, fallback); else fallback();
      function fallback(){
        var t = document.createElement('textarea'); t.value = url; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
        document.body.appendChild(t); t.select(); try { document.execCommand('copy'); done(); } catch (e) { msg.textContent = url; } document.body.removeChild(t);
      }
    });
  });

  /* 3. 계절별 많이 찾는 칼럼 (목록 페이지) */
  var m = new Date().getMonth() + 1;
  var season = (m >= 3 && m <= 5) ? 'spring' : (m >= 6 && m <= 8) ? 'summer' : (m >= 9 && m <= 11) ? 'autumn' : 'winter';
  document.querySelectorAll('.pop li[data-season]').forEach(function(li){ li.hidden = li.getAttribute('data-season') !== season; });
})();
