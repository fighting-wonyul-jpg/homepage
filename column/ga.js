/* 방문자 분석 (Google Analytics 4) + 버튼 클릭·검색어 기록 */
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }
gtag('js', new Date());
gtag('config', 'G-650CYRNZYH');

(function(){
  var TYPES = [
    [/booking\.naver\.com/, 'click_booking'],
    [/pf\.kakao\.com/, 'click_kakao'],
    [/^tel:/, 'click_call'],
    [/map\.naver\.com/, 'click_map'],
    [/blog\.naver\.com/, 'click_blog'],
    [/youtu/, 'click_youtube']
  ];
  var PLACES = [
    ['.mbar', 'mobile_bar'], ['.quick', 'pc_quick'], ['header', 'header'], ['.visit', 'visit_info'],
    ['.cta', 'bottom_buttons'], ['.blogbox', 'blog_box'], ['.author', 'author_box'], ['.links', 'doctor_links']
  ];
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '', name = null;
    for (var i = 0; i < TYPES.length; i++) if (TYPES[i][0].test(href)) { name = TYPES[i][1]; break; }
    if (!name) return;
    var where = 'body';
    for (var j = 0; j < PLACES.length; j++) if (a.closest(PLACES[j][0])) { where = PLACES[j][1]; break; }
    gtag('event', name, { link_location: where, link_text: (a.textContent || '').trim().slice(0, 30), transport_type: 'beacon' });
  }, true);

  var q = document.getElementById('q'), timer = null, last = '';
  if (q) q.addEventListener('input', function(){
    clearTimeout(timer);
    timer = setTimeout(function(){
      var t = q.value.trim();
      if (t.length >= 2 && t !== last) { last = t; gtag('event', 'search', { search_term: t }); }
    }, 1500);
  });
})();
