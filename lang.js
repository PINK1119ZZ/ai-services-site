/* lang.js — Bilingual (zh/en) toggle for AutoDev AI site
   On Chinese pages (/): clicking EN redirects to /en/
   On English pages (/en/): clicking 中文 redirects back to /
   Toggle button is auto-injected into nav. */
(function(){

function isEnPage(){
  return location.pathname.startsWith('/en/') || location.pathname === '/en';
}

function getCounterpartUrl(){
  var path = location.pathname;
  if(isEnPage()){
    // /en/services.html -> /services.html
    // /en/ -> /
    // /en/blog/ -> /blog/
    var zhPath = path.replace(/^\/en\/?/, '/');
    if(zhPath === '') zhPath = '/';
    return zhPath;
  } else {
    // /services.html -> /en/services.html
    // / -> /en/
    // /blog/ -> /en/blog/
    if(path === '/' || path === '') return '/en/';
    return '/en' + path;
  }
}

function init(){
  var s=document.createElement('style');
  s.textContent='#langToggle{cursor:pointer;font-weight:600;font-size:0.85rem;letter-spacing:0.5px;opacity:0.75;transition:opacity 0.3s;white-space:nowrap;}#langToggle:hover{opacity:1;}';
  document.head.appendChild(s);
  var navLinks=document.getElementById('navLinks');
  if(navLinks){
    var cta=navLinks.querySelector('.nav-cta');
    var btn=document.createElement('a');
    btn.id='langToggle';
    btn.href=getCounterpartUrl();
    btn.textContent=isEnPage()?'中文':'EN';
    if(cta)navLinks.insertBefore(btn,cta);
    else navLinks.appendChild(btn);
  }
}

if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
else init();

// FAQ accordion (delegated — works on any page that loads lang.js)
document.addEventListener('click', function(e){
  var q = e.target && e.target.closest && e.target.closest('.faq-q');
  if(!q) return;
  var item = q.parentElement;
  if(item && item.classList.contains('faq-item')) item.classList.toggle('open');
});
})();
