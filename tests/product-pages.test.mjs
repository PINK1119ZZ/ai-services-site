import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';

const root = new URL('../', import.meta.url);
const load = (path) => readFileSync(new URL(path, root), 'utf8');
const fixture = JSON.parse(load('tests/fixtures/product-pages-links.json'));

const between = (html, startMarker, endMarker) => {
  const start = html.indexOf(startMarker);
  assert.notEqual(start, -1, `missing marker ${startMarker}`);
  const end = html.indexOf(endMarker, start) + endMarker.length;
  return html.slice(start, end);
};

const jsonLd = (html) => [...html.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)]
  .map((match) => JSON.parse(match[1]));

// Pages redesigned in batch U4. `active` names the nav link text that should
// carry aria-current="page" on that page's own nav (none for pages absent
// from the top nav: bot-cloud, line-bot-saas, demo).
const pages = [
  {
    path: 'bot-cloud.html', commercialNav: 'index.html', commercialFooter: 'index.html', active: null,
    canonical: 'https://autodev-ai.com/bot-cloud.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/bot-cloud.html'], ['x-default', 'https://autodev-ai.com/bot-cloud.html']],
    prices: ['NT$1,500', 'NT$2,800', 'NT$4,500', 'NT$6,800+'],
    ctas: ['/contact.html?plan=bot-trial', '/contact.html?plan=bot-service', '/contact.html?plan=bot-marketing', '/contact.html?plan=bot-monitor', '/contact.html?plan=bot-enterprise'],
  },
  {
    path: 'ai-model.html', commercialNav: 'index.html', commercialFooter: 'index.html', active: 'AI 模特',
    canonical: 'https://autodev-ai.com/ai-model.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/ai-model.html'], ['x-default', 'https://autodev-ai.com/ai-model.html']],
    prices: ['NT$1,200', 'NT$3,800', 'NT$8,800', 'NT$18,000'],
    ctas: ['https://liff.line.me/2009694545-LJmZCiEX', '/contact.html?ref=prompt-pack'],
  },
  {
    path: 'line-bot-saas.html', commercialNav: 'index.html', commercialFooter: 'index.html', active: null,
    canonical: 'https://autodev-ai.com/line-bot-saas.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/line-bot-saas.html'], ['x-default', 'https://autodev-ai.com/line-bot-saas.html']],
    prices: ['NT$1,500', 'NT$3,500', 'NT$6,800'],
    ctas: ['/contact.html?plan=saas-trial', '/contact.html?plan=saas-basic', '/contact.html?plan=saas-pro', '/contact.html?plan=saas-enterprise'],
  },
  {
    path: 'demo.html', commercialNav: 'index.html', commercialFooter: 'index.html', active: null,
    canonical: 'https://autodev-ai.com/demo.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/demo.html'], ['en', 'https://autodev-ai.com/en/demo.html'], ['x-default', 'https://autodev-ai.com/demo.html']],
    prices: [],
    ctas: ['/contact.html', '/pricing.html', 'https://line.me/ti/p/@882vhisc'],
  },
  {
    path: 'en/bot-cloud.html', commercialNav: 'en/index.html', commercialFooter: 'en/index.html', active: null,
    canonical: 'https://autodev-ai.com/en/bot-cloud.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/bot-cloud.html'], ['en', 'https://autodev-ai.com/en/bot-cloud.html'], ['x-default', 'https://autodev-ai.com/bot-cloud.html']],
    prices: ['$50', '$95', '$180'],
    ctas: ['/en/contact.html?plan=bot-trial', '/en/contact.html?plan=starter', '/en/contact.html?plan=pro', '/en/contact.html?plan=business'],
  },
  {
    path: 'en/ai-model.html', commercialNav: 'en/index.html', commercialFooter: 'en/index.html', active: 'AI Model',
    canonical: 'https://autodev-ai.com/en/ai-model.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/ai-model.html'], ['en', 'https://autodev-ai.com/en/ai-model.html'], ['x-default', 'https://autodev-ai.com/ai-model.html']],
    prices: ['$40', '$125', '$285', '$580'],
    ctas: ['/en/contact.html'],
  },
  {
    path: 'en/demo.html', commercialNav: 'en/index.html', commercialFooter: 'en/index.html', active: null,
    canonical: 'https://autodev-ai.com/en/demo.html',
    hreflang: [['zh-Hant', 'https://autodev-ai.com/demo.html'], ['en', 'https://autodev-ai.com/en/demo.html'], ['x-default', 'https://autodev-ai.com/demo.html']],
    prices: [],
    ctas: ['/en/contact.html', '/en/pricing.html', 'https://line.me/ti/p/@882vhisc'],
  },
];

test('every U4 product page is v2-site with exactly one h1', () => {
  for (const { path } of pages) {
    const html = load(path);
    assert.match(html, /<body\s+class=["']v2-site["']>/i, `${path} body.v2-site`);
    assert.equal((html.match(/<h1\b/gi) || []).length, 1, `${path} single h1`);
  }
});

test('nav matches the paired commercial page nav aside from aria-current', () => {
  for (const { path, commercialNav, active } of pages) {
    const pageNav = between(load(path), '<nav class="nav"', '</nav>');
    const commercialNavHtml = between(load(commercialNav), '<nav class="nav"', '</nav>');
    if (active) {
      assert.match(pageNav, new RegExp(`href=["'][^"']*["']\\s+aria-current=["']page["']>${active}<`), `${path} marks ${active} current`);
    } else {
      assert.doesNotMatch(pageNav, /aria-current=["']page["']/, `${path} nav should not mark any item current`);
    }
    const stripped = pageNav.replace(/\s+aria-current=["']page["']/, '');
    assert.equal(stripped, commercialNavHtml, `${path} nav should equal ${commercialNav} nav once aria-current is removed`);
  }
});

test('footer matches the paired commercial page footer verbatim', () => {
  for (const { path, commercialFooter } of pages) {
    const pageFooter = between(load(path), '<footer class="v2-footer"', '</footer>');
    const commercialFooterHtml = between(load(commercialFooter), '<footer class="v2-footer"', '</footer>');
    assert.equal(pageFooter, commercialFooterHtml, `${path} footer should equal ${commercialFooter} footer`);
  }
});

test('body end loads chat-widget, lang and autodev-v2 scripts in order', () => {
  for (const { path } of pages) {
    const html = load(path);
    assert.match(html, /<script defer src=["']\/chat-widget\.js\?v=20260502e["']><\/script>\s*<script defer src=["']\/lang\.js\?v=20260505["']><\/script>\s*<script defer src=["']\/assets\/autodev-v2\.js["']><\/script>\s*<\/body>/, `${path} script order`);
  }
});

test('canonical and hreflang stay at their pre-migration values', () => {
  for (const { path, canonical, hreflang } of pages) {
    const html = load(path);
    const links = [...html.matchAll(/<link\b[^>]*>/gi)].map((m) => m[0]);
    const tagAttr = (tag, key) => tag?.match(new RegExp(`${key}=(["'])([\\s\\S]*?)\\1`, 'i'))?.[2];
    const canonicalTag = links.find((tag) => (tagAttr(tag, 'rel') || '').split(/\s+/).includes('canonical'));
    assert.equal(tagAttr(canonicalTag, 'href'), canonical, `${path} canonical`);
    for (const [lang, href] of hreflang) {
      const tag = links.find((candidate) => (tagAttr(candidate, 'rel') || '').split(/\s+/).includes('alternate') && tagAttr(candidate, 'hreflang') === lang);
      assert.equal(tagAttr(tag, 'href'), href, `${path} hreflang ${lang}`);
    }
  }
});

test('JSON-LD parses and the GA4 tag is preserved', () => {
  for (const { path } of pages) {
    const html = load(path);
    assert.ok(jsonLd(html).length > 0, `${path} JSON-LD`);
    assert.match(html, /G-4ZWDT650BM/, `${path} GA4`);
  }
});

test('original prices and CTA destinations remain present', () => {
  for (const { path, prices, ctas } of pages) {
    const html = load(path);
    for (const price of prices) assert.ok(html.includes(price), `${path} keeps price ${price}`);
    for (const cta of ctas) assert.ok(html.includes(`href="${cta}"`), `${path} keeps CTA ${cta}`);
  }
});

test('every pre-migration href, src and data-src is still present on the page', () => {
  for (const { path } of pages) {
    const html = load(path);
    const entry = fixture[path];
    assert.ok(entry, `${path} has a link fixture`);
    for (const href of entry.hrefs) assert.ok(html.includes(href), `${path} keeps href ${href}`);
    for (const src of entry.srcs) assert.ok(html.includes(src), `${path} keeps src ${src}`);
    for (const src of entry.data_srcs) assert.ok(html.includes(src), `${path} keeps data-src ${src}`);
  }
});

test('ai-model.html Kira reel and editorial lightbox keep their required ids and classes', () => {
  const zh = load('ai-model.html');
  assert.match(zh, /<section class=["']editorial-series["'] id=["']editorial-series["']>/);
  for (const cls of ['lazy-video', 'reel-caption', 'editorial-card']) {
    assert.match(zh, new RegExp(`class=["'][^"']*\\b${cls}\\b`), `ai-model.html keeps .${cls}`);
  }
  for (const id of ['editorialLightbox', 'lightboxImg', 'lightboxCaption', 'lightboxClose']) {
    assert.match(zh, new RegExp(`id=["']${id}["']`), `ai-model.html keeps #${id}`);
  }
  assert.match(zh, /document\.getElementById\(['"]editorialLightbox['"]\)/);
  assert.match(zh, /querySelectorAll\(['"]\.lazy-video['"]\)/);
  assert.match(zh, /querySelectorAll\(['"]\.editorial-card['"]\)/);

  const en = load('en/ai-model.html');
  assert.match(en, /<section class=["']scenes-section["'] id=["']editorial-series["']>/);
});

test('demo.html keeps the chat-widget trigger button behavior', () => {
  for (const path of ['demo.html', 'en/demo.html']) {
    const html = load(path);
    assert.match(html, /document\.getElementById\(['"]chat-widget-btn['"]\)\.click\(\)/);
  }
});
