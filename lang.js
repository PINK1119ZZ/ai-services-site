/* lang.js — Bilingual (zh/en) toggle for AutoDev AI site
   Usage: add data-en="English text" to any element.
   Nav links are auto-translated via NAV dict.
   Toggle button is auto-injected into nav. */
(function(){
var NAV={
  '服務':'Services','作品':'Portfolio','方案':'Pricing',
  '部落格':'Blog','關於':'About','體驗 Demo':'Try Demo','免費諮詢':'Consult'
};

function getLang(){return localStorage.getItem('site-lang')||'zh'}

function applyLang(lang){
  // Nav links
  document.querySelectorAll('#navLinks a:not(#langToggle)').forEach(function(a){
    if(!a.dataset.zh)a.dataset.zh=a.textContent.trim();
    a.textContent=lang==='en'?(NAV[a.dataset.zh]||a.dataset.zh):a.dataset.zh;
  });
  // Page content
  document.querySelectorAll('[data-en]').forEach(function(el){
    if(!el.getAttribute('data-zh'))el.setAttribute('data-zh',el.innerHTML);
    el.innerHTML=lang==='en'?el.getAttribute('data-en'):el.getAttribute('data-zh');
  });
  document.documentElement.lang=lang==='zh'?'zh-Hant':'en';
  var btn=document.getElementById('langToggle');
  if(btn)btn.textContent=lang==='zh'?'EN':'中文';
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
    btn.href='javascript:void(0)';
    btn.addEventListener('click',function(e){
      e.preventDefault();
      localStorage.setItem('site-lang',getLang()==='zh'?'en':'zh');
      applyLang(getLang());
    });
    if(cta)navLinks.insertBefore(btn,cta);
    else navLinks.appendChild(btn);
  }
  applyLang(getLang());
}

if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
else init();
})();
