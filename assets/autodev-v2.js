(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.AutoDevV2 = api;
  if (root.document) {
    const start = () => api.mount(root.document, root);
    root.document.readyState === 'loading' ? root.document.addEventListener('DOMContentLoaded', start) : start();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  function initNavigation(doc) {
    const button = doc.querySelector('[data-nav-toggle]');
    const menu = doc.querySelector('[data-nav-links]');
    if (!button || !menu) return;
    const setOpen = (open) => {
      menu.classList.toggle('show', open);
      button.setAttribute('aria-expanded', String(open));
      button.setAttribute('aria-label', open ? button.dataset?.closeLabel || 'Close menu' : button.dataset?.openLabel || 'Open menu');
    };
    button.addEventListener('click', (event) => { event.stopPropagation(); setOpen(!menu.classList.contains('show')); });
    doc.addEventListener('keydown', (event) => { if (event.key === 'Escape') setOpen(false); });
    doc.addEventListener('click', (event) => {
      if (menu.classList.contains('show') && !menu.contains(event.target) && !button.contains(event.target)) setOpen(false);
    });
    menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setOpen(false)));
  }
  function initReveal(doc, win) {
    const elements = doc.querySelectorAll('[data-reveal]');
    if (!elements.length || !('IntersectionObserver' in win) || win.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    doc.documentElement.classList.add('v2-reveal-ready');
    const observer = new win.IntersectionObserver((entries) => entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add('is-visible'); observer.unobserve(entry.target); }
    }), { rootMargin: '0px 0px -48px' });
    elements.forEach((element) => observer.observe(element));
  }
  function initAnalytics(doc, win) {
    doc.querySelectorAll('[data-analytics]').forEach((element) => element.addEventListener('click', () => {
      if (typeof win.gtag === 'function') win.gtag('event', 'select_content', { content_type: 'commercial_site', item_id: element.dataset.analytics });
    }));
  }
  function mount(doc, win) { initNavigation(doc); initReveal(doc, win); initAnalytics(doc, win); }
  return { initNavigation, initReveal, initAnalytics, mount };
});
