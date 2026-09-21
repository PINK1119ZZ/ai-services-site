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

const load = (path) => readFileSync(new URL(path, root), 'utf8');
const attr = (html, rel, key = 'href') => {
  const tag = html.match(new RegExp(`<link[^>]*rel=["']${rel}["'][^>]*>`, 'i'))?.[0];
  return tag?.match(new RegExp(`${key}=["']([^"']+)`))?.[1];
};

test('all commercial routes have paired metadata, one h1 and parseable JSON-LD', () => {
  for (const [zhPath, zhUrl, enUrl] of routes) {
    for (const [path, canonical] of [[zhPath, zhUrl], [`en/${zhPath}`, enUrl]]) {
      const html = load(path);
      assert.equal((html.match(/<h1\b/gi) || []).length, 1, `${path} h1`);
      assert.equal(attr(html, 'canonical'), canonical, `${path} canonical`);
      assert.match(html, new RegExp(`hreflang=["']zh-Hant["'][^>]*href=["']${zhUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']|href=["']${zhUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["'][^>]*hreflang=["']zh-Hant["']`));
      assert.match(html, new RegExp(`hreflang=["']en["'][^>]*href=["']${enUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["']|href=["']${enUrl.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}["'][^>]*hreflang=["']en["']`));
      const blocks = [...html.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)];
      assert.ok(blocks.length, `${path} JSON-LD`);
      blocks.forEach((block) => JSON.parse(block[1]));
      assert.match(html, /assets\/autodev-v2\.js/);
    }
  }
});

test('commercial copy keeps the agreed truth and price boundaries', () => {
  const html = routes.flatMap(([path]) => [load(path), load(`en/${path}`)]).join('\n');
  for (const claim of ['10x', '1,300', '1300', '25+ Projects', '2 週完成', '兩週完成', '不滿意不收費', 'no satisfaction, no charge', 'full refund', 'free maintenance', 'free consultation', 'within hours', '30-min', 'NT$8,000', '$250', '14-30 days']) {
    assert.doesNotMatch(html, new RegExp(claim, 'i'), claim);
  }
  assert.match(load('portfolio.html'), /AutoDev 自用系統/);
  assert.match(load('portfolio.html'), /流程示意/);
  assert.match(load('pricing.html'), /NT\$50,000/);
  assert.match(load('pricing.html'), /NT\$100,000/);
  assert.match(load('pricing.html'), /NT\$200,000/);
  for (const page of ['contact.html', 'en/contact.html']) {
    const contact = load(page);
    for (const budget of ['NT$50K', 'NT$100K', 'NT$200K+']) assert.ok(contact.includes(budget), `${page} ${budget}`);
  }
});

test('contact routes enquiries to the owned bot without fake submission signals', () => {
  const pages = [
    ['contact.html', 'https://autodev-ai.com/contact.html', ['提出問題', '澄清範圍', '確認方案']],
    ['en/contact.html', 'https://autodev-ai.com/en/contact.html', ['Describe the problem', 'Clarify the scope', 'Confirm the proposal']],
  ];
  for (const [page, canonical, steps] of pages) {
    const html = load(page);
    const primary = [...html.matchAll(/<a\b[^>]*href=["']https:\/\/chat\.autodev-ai\.com\/form["'][^>]*>/gi)]
      .map((match) => match[0])
      .find((tag) => /class=["'][^"']*v2-button[^"']*["']/.test(tag)) || '';
    assert.match(primary, /class=["'][^"']*v2-button[^"']*["']/);
    assert.match(primary, /data-analytics=["']contact_owned_bot["']/);
    assert.doesNotMatch(primary, /onclick=/i);
    assert.doesNotMatch(html, /<form\b|<textarea\b|type=["'](?:email|submit)["']|action=["']|formsubmit\.co|[?&]sent=1|history\.replaceState|createElement\(["']div["']\)/i);
    assert.doesNotMatch(html, /href=["']\/form["']/);
    assert.doesNotMatch(html, /user_data|customer_email|customer_phone|generate_lead|form_submit|form_start/i);
    assert.match(html, /G-4ZWDT650BM/);
    assert.match(html, /AW-18066037819/);
    assert.match(html, /chat-widget\.js\?v=20260502e/);
    assert.match(html, /lang\.js\?v=20260505/);
    for (const step of steps) assert.ok(html.includes(step), `${page} ${step}`);
    const blocks = [...html.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)].map((match) => JSON.parse(match[1]));
    const contactPage = blocks.find((block) => block['@type'] === 'ContactPage');
    assert.equal(contactPage.url, canonical);
    assert.equal(JSON.stringify(contactPage).toLowerCase().includes('email'), false);
  }
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
