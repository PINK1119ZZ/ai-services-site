import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';

const load = (path) => readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const pages = [
  {
    label: 'zh', html: load('tools/line-bot-calculator.html'),
    names: ['關鍵字自動回覆', '圖文訊息／選單', 'Rich Menu 圖文選單', 'AI 客服', '客製知識庫', '多語言支援', '預約／報名流程', '金流整合', '會員等級／點數', '訂單通知', 'GA4／流程分析', '客戶管理後台'],
    empty: '尚未選擇功能', zero: '0 項', one: '1 項', contact: '/contact.html?from=calculator', cloud: '/bot-cloud.html',
  },
  {
    label: 'en', html: load('en/tools/line-bot-calculator.html'),
    names: ['Keyword auto replies', 'Rich messages / menus', 'Rich Menu', 'AI support', 'Custom knowledge base', 'Multilingual support', 'Booking / registration flow', 'Payment integration', 'Membership / points', 'Order notifications', 'GA4 / flow analysis', 'Customer admin'],
    empty: 'No features selected', zero: '0 items', one: '1 item', contact: '/en/contact.html?from=calculator', cloud: '/en/bot-cloud.html',
  },
];

class Classes {
  constructor(initial = []) { this.values = new Set(initial); }
  contains(name) { return this.values.has(name); }
  toggle(name, force) { force ? this.values.add(name) : this.values.delete(name); }
}

function element(initial = {}) {
  const listeners = {};
  return {
    dataset: {}, classList: new Classes(), textContent: '', checked: false,
    children: [], attributes: {}, ...initial,
    addEventListener(name, fn) { listeners[name] = fn; },
    dispatch(name) { listeners[name]?.({ currentTarget: this }); },
    setAttribute(name, value) { this.attributes[name] = value; },
    replaceChildren(...children) { this.children = children; },
    closest() { return this.label; },
  };
}

function fixture(names) {
  const channels = [
    element({ dataset: { channel: 'Telegram' }, classList: new Classes(['active']) }),
    element({ dataset: { channel: 'LINE' } }),
    element({ dataset: { channel: 'Messenger' } }),
  ];
  const features = names.map((name) => {
    const input = element({ dataset: { feature: name } });
    input.label = element();
    return input;
  });
  const nodes = { selectedChannel: element(), featureCount: element(), selectedFeatures: element(), clearFeatures: element() };
  const document = {
    querySelectorAll(selector) {
      if (selector === '[data-channel]') return channels;
      if (selector === 'input[data-feature]') return features;
      return [];
    },
    getElementById(id) { return nodes[id]; },
    createElement() { return element(); },
  };
  return { channels, features, nodes, document };
}

function runScopeScript(page) {
  const script = page.html.match(/<script id="bot-scope-script">([\s\S]*?)<\/script>/)?.[1];
  assert.ok(script, `${page.label} bot scope script`);
  assert.doesNotMatch(script, /innerHTML/);
  const dom = fixture(page.names);
  const networkCalls = { count: 0 };
  vm.runInNewContext(script, {
    document: dom.document,
    fetch() { networkCalls.count += 1; },
    XMLHttpRequest() { networkCalls.count += 1; },
    localStorage: new Proxy({}, { get() { throw new Error('storage accessed'); } }),
  });
  return { ...dom, networkCalls };
}

test('both Bot scope tools default to Telegram and render selections without prices or network', () => {
  for (const page of pages) {
    const { channels, features, nodes, networkCalls } = runScopeScript(page);
    assert.equal(nodes.selectedChannel.textContent, 'Telegram', page.label);
    assert.equal(channels[0].attributes['aria-pressed'], 'true');
    assert.equal(nodes.featureCount.textContent, page.zero);
    assert.equal(nodes.selectedFeatures.children[0].textContent, page.empty);
    features[0].checked = true;
    features[0].dispatch('change');
    assert.equal(nodes.featureCount.textContent, page.one);
    assert.deepEqual(nodes.selectedFeatures.children.map((item) => item.textContent), [page.names[0]]);
    assert.equal(features[0].label.classList.contains('selected'), true);
    assert.equal(networkCalls.count, 0);
  }
});

test('both Bot scope tools change channel and clear every selected feature', () => {
  for (const page of pages) {
    const { channels, features, nodes, networkCalls } = runScopeScript(page);
    features[0].checked = true;
    features[5].checked = true;
    features[0].dispatch('change');
    channels[1].dispatch('click');
    assert.equal(nodes.selectedChannel.textContent, 'LINE');
    assert.equal(channels[1].attributes['aria-pressed'], 'true');
    nodes.clearFeatures.dispatch('click');
    assert.ok(features.every((feature) => feature.checked === false));
    assert.equal(nodes.featureCount.textContent, page.zero);
    assert.equal(nodes.selectedFeatures.children[0].textContent, page.empty);
    assert.equal(networkCalls.count, 0);
  }
});

test('paired Bot scope pages keep guidance, routes and hreflang without pseudo-cost behavior', () => {
  for (const page of pages) {
    assert.match(page.html, /NT\$50,000/);
    assert.match(page.html, /NT\$100,000/);
    assert.match(page.html, /NT\$200,000\+/);
    assert.ok(page.html.includes(`href="${page.contact}"`));
    assert.ok(page.html.includes(`href="${page.cloud}"`));
    assert.match(page.html, /aria-live="polite"/);
    assert.match(page.html, /<div class="channel-tabs"[^>]*role="group"/);
    assert.equal((page.html.match(/type="checkbox"/g) || []).length, 12);
    assert.doesNotMatch(page.html, /data-cost|data-maintain|50%|NT\$8,000|\$400|Free 30-Min|台灣市場.*中位值|Taiwan market|月維護費|Monthly maintenance|首年總成本|Estimated Cost|gumroad\.com|m\.do\.co/i);
  }
  assert.match(pages[0].html, /hreflang="en" href="https:\/\/autodev-ai\.com\/en\/tools\/line-bot-calculator\.html"/);
  assert.match(pages[1].html, /hreflang="zh-Hant" href="https:\/\/autodev-ai\.com\/tools\/line-bot-calculator\.html"/);
  assert.match(pages[0].html, /你的勾選[^。]*不會送出或儲存/);
  assert.match(pages[1].html, /Your selections[^.]*not sent or stored/);
  assert.doesNotMatch(pages[1].html, />Free Quote<\/a>/);
  assert.match(pages[1].html, />Discuss a project<\/a>/);
});

test('tool directories and Chinese cost article describe a scope checklist', () => {
  const zhIndex = load('tools/index.html');
  const enIndex = load('en/tools/index.html');
  const article = load('blog/line-bot-cost.html');
  const zhCard = zhIndex.match(/<a href="\/tools\/line-bot-calculator\.html"[\s\S]*?<\/a>/)?.[0] ?? '';
  const enCard = enIndex.match(/<a href="\/en\/tools\/line-bot-calculator\.html"[\s\S]*?<\/a>/)?.[0] ?? '';
  const articleCta = article.match(/<!-- Calculator CTA Banner -->\s*(<section[^>]*>[\s\S]*?href="\/tools\/line-bot-calculator\.html"[\s\S]*?<\/section>)/)?.[1] ?? '';
  assert.match(zhCard, /Bot 需求與預算準備工具/);
  assert.match(enCard, /Bot Requirements & Budget Prep/);
  assert.match(articleCta, /需求清單/);
  assert.doesNotMatch(`${zhCard}\n${articleCta}`, /即時|估價|費用計算器/);
  assert.doesNotMatch(enCard, /estimate|cost calculator|instant/i);
  assert.match(articleCta, /background:#16213e/);
  assert.match(articleCta, /color:#cbd5e1/);
  assert.match(articleCta, /href="\/tools\/line-bot-calculator\.html"[^>]*background:#334155[^>]*color:#fff/);
  const og = load('blog/og/line-bot-cost.svg');
  assert.match(og, /<svg width="1200" height="630"/);
  assert.match(og, />LINE Bot 開發費用<\/text>/);
  assert.match(og, />需求範圍與專案預算指南<\/text>/);
  assert.doesNotMatch(og, /NT\$8,000|8,000 起/);
});
