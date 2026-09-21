import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';

const html = readFileSync(new URL('../tools/line-bot-calculator.html', import.meta.url), 'utf8');

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

function fixture() {
  const channels = [
    element({ dataset: { channel: 'Telegram' }, classList: new Classes(['active']) }),
    element({ dataset: { channel: 'LINE' } }),
    element({ dataset: { channel: 'Messenger' } }),
  ];
  const names = [
    '關鍵字自動回覆', '圖文訊息／選單', 'Rich Menu 圖文選單', 'AI 客服',
    '客製知識庫', '多語言支援', '預約／報名流程', '金流整合',
    '會員等級／點數', '訂單通知', 'GA4／流程分析', '客戶管理後台',
  ];
  const features = names.map((name) => {
    const input = element({ dataset: { feature: name } });
    input.label = element();
    return input;
  });
  const nodes = {
    selectedChannel: element(), featureCount: element(), selectedFeatures: element(), clearFeatures: element(),
  };
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

function runScopeScript() {
  const script = html.match(/<script id="bot-scope-script">([\s\S]*?)<\/script>/)?.[1];
  assert.ok(script, 'bot scope script');
  assert.doesNotMatch(script, /innerHTML/);
  const dom = fixture();
  const networkCalls = { count: 0 };
  vm.runInNewContext(script, {
    document: dom.document,
    fetch() { networkCalls.count += 1; },
    XMLHttpRequest() { networkCalls.count += 1; },
    localStorage: new Proxy({}, { get() { throw new Error('storage accessed'); } }),
  });
  return { ...dom, networkCalls };
}

test('Bot scope tool defaults to Telegram and renders selections without prices or network', () => {
  const { channels, features, nodes, networkCalls } = runScopeScript();
  assert.equal(nodes.selectedChannel.textContent, 'Telegram');
  assert.equal(channels[0].attributes['aria-pressed'], 'true');
  assert.equal(nodes.featureCount.textContent, '0 項');
  assert.equal(nodes.selectedFeatures.children[0].textContent, '尚未選擇功能');

  features[0].checked = true;
  features[0].dispatch('change');
  assert.equal(nodes.featureCount.textContent, '1 項');
  assert.deepEqual(nodes.selectedFeatures.children.map((item) => item.textContent), ['關鍵字自動回覆']);
  assert.equal(features[0].label.classList.contains('selected'), true);
  assert.equal(networkCalls.count, 0);
});

test('Bot scope tool changes channel and clears every selected feature', () => {
  const { channels, features, nodes, networkCalls } = runScopeScript();
  features[0].checked = true;
  features[5].checked = true;
  features[0].dispatch('change');
  channels[1].dispatch('click');
  assert.equal(nodes.selectedChannel.textContent, 'LINE');
  assert.equal(channels[1].attributes['aria-pressed'], 'true');
  assert.equal(nodes.featureCount.textContent, '2 項');

  nodes.clearFeatures.dispatch('click');
  assert.ok(features.every((feature) => feature.checked === false));
  assert.equal(nodes.featureCount.textContent, '0 項');
  assert.equal(nodes.selectedFeatures.children[0].textContent, '尚未選擇功能');
  assert.equal(networkCalls.count, 0);
});

test('Bot scope page keeps scope guidance and removes pseudo-cost behavior', () => {
  assert.match(html, /NT\$50,000/);
  assert.match(html, /NT\$100,000/);
  assert.match(html, /NT\$200,000\+/);
  assert.match(html, /href="\/contact\.html\?from=calculator"/);
  assert.match(html, /href="\/bot-cloud\.html"/);
  assert.match(html, /aria-live="polite"/);
  assert.equal((html.match(/type="checkbox"/g) || []).length, 12);
  assert.doesNotMatch(html, /data-cost|data-maintain|NT\$8,000|台灣市場.*中位值|月維護費|首年總成本|50%|gumroad\.com|m\.do\.co/);
});
