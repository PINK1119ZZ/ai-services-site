import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const root = new URL('../', import.meta.url);
const routes = [
  ['index.html', 'https://autodev-ai.com/', 'https://autodev-ai.com/en/'],
  ['services.html', 'https://autodev-ai.com/services.html', 'https://autodev-ai.com/en/services.html'],
  ['portfolio.html', 'https://autodev-ai.com/portfolio.html', 'https://autodev-ai.com/en/portfolio.html'],
  ['about.html', 'https://autodev-ai.com/about.html', 'https://autodev-ai.com/en/about.html'],
  ['contact.html', 'https://autodev-ai.com/contact.html', 'https://autodev-ai.com/en/contact.html'],
  ['pricing.html', 'https://autodev-ai.com/pricing.html', 'https://autodev-ai.com/en/pricing.html'],
];
const logo = 'https://autodev-ai.com/autodev-logo2.png';

const load = (path) => readFileSync(new URL(path, root), 'utf8');
const tagAttr = (tag, key) => tag?.match(new RegExp(`${key}=(["'])([\\s\\S]*?)\\1`, 'i'))?.[2];
const attr = (html, rel, key = 'href') => {
  const tag = [...html.matchAll(/<link\b[^>]*>/gi)]
    .map((match) => match[0])
    .find((candidate) => (tagAttr(candidate, 'rel') || '').split(/\s+/).includes(rel));
  return tagAttr(tag, key);
};
const meta = (html, key, keyAttr = 'name') => {
  const tag = [...html.matchAll(/<meta\b[^>]*>/gi)]
    .map((match) => match[0])
    .find((candidate) => tagAttr(candidate, keyAttr) === key);
  return tagAttr(tag, 'content');
};
const containsLiteralClaim = (html, claim) => html.toLowerCase().includes(claim.toLowerCase());
const jsonLd = (html) => [...html.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)]
  .map((match) => JSON.parse(match[1]));

test('all commercial routes keep paired metadata, icons, one h1 and parseable JSON-LD', () => {
  for (const [zhPath, zhUrl, enUrl] of routes) {
    for (const [path, canonical] of [[zhPath, zhUrl], [`en/${zhPath}`, enUrl]]) {
      const html = load(path);
      const title = html.match(/<title>([^<]+)<\/title>/i)?.[1];
      const description = meta(html, 'description');
      assert.equal((html.match(/<h1\b/gi) || []).length, 1, `${path} h1`);
      assert.equal(attr(html, 'canonical'), canonical, `${path} canonical`);
      assert.match(html, new RegExp(`hreflang=["']zh-Hant["'][^>]*href=["']${zhUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']|href=["']${zhUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["'][^>]*hreflang=["']zh-Hant["']`));
      assert.match(html, new RegExp(`hreflang=["']en["'][^>]*href=["']${enUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']|href=["']${enUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["'][^>]*hreflang=["']en["']`));
      assert.equal(meta(html, 'og:image', 'property'), logo, `${path} og:image`);
      assert.equal(meta(html, 'twitter:card'), 'summary_large_image', `${path} twitter card`);
      assert.equal(meta(html, 'twitter:title'), title, `${path} twitter title`);
      assert.equal(meta(html, 'twitter:description'), description, `${path} twitter description`);
      assert.equal(meta(html, 'twitter:image'), logo, `${path} twitter image`);
      for (const icon of ['/favicon.ico', '/apple-touch-icon.png', '/icon-192.png']) {
        assert.match(html, new RegExp(`href=["']${icon.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']`), `${path} ${icon}`);
      }
      assert.ok(jsonLd(html).length, `${path} JSON-LD`);
      assert.match(html, /assets\/autodev-v2\.js/);
    }
  }
  for (const path of ['index.html', 'en/index.html']) assert.match(load(path), /type=["']application\/rss\+xml["'][^>]*href=["']\/feed\.xml["']/i, `${path} RSS`);
  assert.equal(meta(load('pricing.html'), 'theme-color'), '#f7f4ee');
});

test('metadata values preserve the other quote character', () => {
  assert.equal(tagAttr(`<meta content="AutoDev's full description">`, 'content'), "AutoDev's full description");
  assert.equal(tagAttr(`<meta content='A "quoted" workflow'>`, 'content'), 'A "quoted" workflow');
});

test('Google Ads stays on the two base pages while GA4 stays on every commercial route', () => {
  const adsPages = new Set(['index.html', 'contact.html']);
  for (const [zhPath] of routes) {
    for (const path of [zhPath, `en/${zhPath}`]) {
      const html = load(path);
      assert.match(html, /G-4ZWDT650BM/, `${path} GA4`);
      assert.equal(/AW-18066037819|fireAdsConversion|gtag\(['"]config['"],\s*ADS_ID/.test(html), adsPages.has(path), `${path} Ads scope`);
    }
  }
});

test('literal claim checks recognize regex punctuation', () => {
  for (const claim of ['NT$8,000', '$250', '25+ Projects']) {
    assert.equal(containsLiteralClaim(`before ${claim} after`, claim), true, claim);
  }
});

test('commercial copy keeps the agreed truth and price boundaries', () => {
  const html = routes.flatMap(([path]) => [load(path), load(`en/${path}`)]).join('\n');
  for (const claim of ['10x', '1,300', '1300', '25+ Projects', '2 週完成', '兩週完成', '不滿意不收費', 'no satisfaction, no charge', 'full refund', 'free maintenance', 'free consultation', 'within hours', '30-min', 'NT$8,000', '$250', '14-30 days']) {
    assert.equal(containsLiteralClaim(html, claim), false, claim);
  }
  assert.match(load('portfolio.html'), /AutoDev 自用系統/);
  assert.match(load('portfolio.html'), /流程示意/);
  assert.doesNotMatch(`${load('portfolio.html')}\n${load('en/portfolio.html')}`, /已核實|\bverified\b/i);
  assert.match(load('pricing.html'), /NT\$50,000/);
  assert.match(load('pricing.html'), /NT\$100,000/);
  assert.match(load('pricing.html'), /NT\$200,000/);
  for (const page of ['contact.html', 'en/contact.html']) {
    const contact = load(page);
    for (const budget of ['NT$50K', 'NT$100K', 'NT$200K+']) assert.ok(contact.includes(budget), `${page} ${budget}`);
  }
});

test('pricing JSON-LD describes positioning as a list rather than offers', () => {
  for (const path of ['pricing.html', 'en/pricing.html']) {
    const html = load(path);
    const list = jsonLd(html).find((block) => block['@type'] === 'ItemList');
    assert.ok(list, `${path} ItemList`);
    assert.deepEqual(list.itemListElement.map((item) => item['@type']), ['ListItem', 'ListItem', 'ListItem']);
    assert.deepEqual(list.itemListElement.map((item) => item.position), [1, 2, 3]);
    assert.doesNotMatch(JSON.stringify(list), /Offer|priceCurrency|"price"/i);
  }
  assert.doesNotMatch(JSON.stringify(jsonLd(load('index.html'))), /priceRange/i);
  assert.doesNotMatch(JSON.stringify(jsonLd(load('en/index.html'))), /priceRange/i);
});

test('legacy anchors, active helpers and Chinese pricing analytics stay coherent', () => {
  for (const path of ['services.html', 'en/services.html']) assert.match(load(path), /id=["']services["']/i, `${path} #services`);
  for (const path of ['portfolio.html', 'en/portfolio.html']) assert.match(load(path), /id=["']process["']/i, `${path} #process`);
  for (const path of ['contact.html', 'en/contact.html']) {
    assert.match(load(path), /id=["']contact["']/i, `${path} #contact`);
    assert.match(load(path), /id=["']faq["']/i, `${path} #faq`);
  }
  for (const path of ['services.html', 'portfolio.html', 'about.html']) assert.doesNotMatch(load(path), /function submitNewsletter/, `${path} dead newsletter helper`);
  assert.match(load('index.html'), /function submitNewsletter/);
  assert.match(load('index.html'), /<form\b[^>]*v2-newsletter-form/i);
  assert.match(load('pricing.html'), /data-analytics=["']nav_contact["']/);
  assert.match(load('pricing.html'), /data-analytics=["']final_contact["']/);
});

test('contact routes enquiries to the owned bot with fixed source labels and no fake submission signals', () => {
  const pages = [
    ['contact.html', 'https://autodev-ai.com/contact.html', 'website_zh_contact', true, ['提出問題', '澄清範圍', '確認方案']],
    ['en/contact.html', 'https://autodev-ai.com/en/contact.html', 'website_en_contact', false, ['Describe the problem', 'Clarify the scope', 'Confirm the proposal']],
  ];
  for (const [page, canonical, source, hasAds, steps] of pages) {
    const html = load(page);
    const hrefs = [...html.matchAll(/<a\b[^>]*href=["'](https:\/\/chat\.autodev-ai\.com\/form[^"']*)["'][^>]*>/gi)];
    const primary = hrefs.map((match) => match[0]).find((tag) => /class=["'][^"']*v2-button[^"']*["']/.test(tag)) || '';
    assert.match(primary, /class=["'][^"']*v2-button[^"']*["']/);
    assert.match(primary, /data-analytics=["']contact_owned_bot["']/);
    assert.doesNotMatch(primary, /onclick=/i);
    assert.ok(hrefs.length >= 2, `${page} owned form links`);
    for (const [, href] of hrefs) {
      const url = new URL(href);
      assert.equal(url.origin, 'https://chat.autodev-ai.com');
      assert.equal(url.pathname, '/form');
      assert.deepEqual([...url.searchParams], [['src', source]], `${page} source`);
    }
    assert.doesNotMatch(html, /<form\b|<textarea\b|type=["'](?:email|submit)["']|action=["']|formsubmit\.co|[?&]sent=1|history\.replaceState|createElement\(["']div["']\)/i);
    assert.doesNotMatch(html, /href=["']\/form["']/);
    assert.doesNotMatch(html, /user_data|customer_email|customer_phone|generate_lead|form_submit|form_start/i);
    assert.match(html, /G-4ZWDT650BM/);
    assert.equal(/AW-18066037819/.test(html), hasAds, `${page} Ads`);
    assert.match(html, /chat-widget\.js\?v=20260502e/);
    assert.match(html, /lang\.js\?v=20260505/);
    for (const step of steps) assert.ok(html.includes(step), `${page} ${step}`);
    const contactPage = jsonLd(html).find((block) => block['@type'] === 'ContactPage');
    assert.equal(contactPage.url, canonical);
    assert.equal(JSON.stringify(contactPage).toLowerCase().includes('email'), false);
  }
});

test('shared v2 dark styles keep small text and newsletter controls readable', () => {
  const css = load('style.css');
  assert.match(css, /\.v2-section\.dark \.v2-kicker,\s*\.v2-section\.dark \.v2-pill,\s*\.v2-newsletter \.v2-kicker\s*\{[^}]*color:\s*#dfc29d/i);
  assert.match(css, /\.v2-newsletter \.v2-button\s*\{[^}]*background:\s*var\(--v2-white\)[^}]*color:\s*var\(--v2-ink\)[^}]*border-color:\s*var\(--v2-white\)/i);
});

test('shared navigation synchronizes aria state and closes with Escape', () => {
  const { initNavigation } = require('../assets/autodev-v2.js');
  const listeners = {};
  const buttonListeners = {};
  const classes = new Set();
  const button = {
    setAttribute(name, value) { this[name] = value; },
    addEventListener(name, fn) { buttonListeners[name] = fn; },
    contains() { return false; },
  };
  const menu = {
    classList: { toggle(name, on) { on ? classes.add(name) : classes.delete(name); }, contains(name) { return classes.has(name); } },
    querySelectorAll() { return []; },
    contains() { return false; },
  };
  const doc = {
    querySelector(selector) { return selector === '[data-nav-toggle]' ? button : menu; },
    addEventListener(name, fn) { listeners[name] = fn; },
  };
  initNavigation(doc);
  buttonListeners.click({ stopPropagation() {} });
  assert.equal(button['aria-expanded'], 'true');
  listeners.keydown({ key: 'Escape' });
  assert.equal(button['aria-expanded'], 'false');
  assert.equal(classes.has('show'), false);
});
