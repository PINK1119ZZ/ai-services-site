import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';

const source = readFileSync(new URL('../chat-widget.js', import.meta.url), 'utf8');

class FakeClassList {
  constructor(element) { this.element = element; }
  add(name) { if (!this.contains(name)) this.element.className = `${this.element.className} ${name}`.trim(); }
  contains(name) { return this.element.className.split(/\s+/).includes(name); }
  toggle(name, force) {
    const add = force === undefined ? !this.contains(name) : force;
    const names = this.element.className.split(/\s+/).filter(Boolean).filter((item) => item !== name);
    if (add) names.push(name);
    this.element.className = names.join(' ');
    return add;
  }
}

class FakeText {
  constructor(text) { this.nodeType = 3; this.data = text; this.parentElement = null; }
  get textContent() { return this.data; }
  set textContent(value) { this.data = String(value); }
}

class FakeElement {
  constructor(tagName, document) {
    this.nodeType = 1;
    this.tagName = tagName.toUpperCase();
    this.ownerDocument = document;
    this.childNodes = [];
    this.parentElement = null;
    this.attributes = new Map();
    this.dataset = {};
    this.style = {};
    this.className = '';
    this.value = '';
    this.disabled = false;
    this._listeners = new Map();
  }
  get children() { return this.childNodes.filter((node) => node.nodeType === 1); }
  get classList() { return new FakeClassList(this); }
  get id() { return this.getAttribute('id') || ''; }
  set id(value) { this.setAttribute('id', value); }
  get textContent() { return this.childNodes.map((node) => node.textContent).join(''); }
  set textContent(value) { this.childNodes = [new FakeText(String(value))]; this.childNodes[0].parentElement = this; }
  set innerHTML(value) { this.childNodes = []; parseHtml(String(value), this, this.ownerDocument); }
  get innerHTML() { return this.textContent; }
  set href(value) { this.setAttribute('href', value); }
  get href() { return this.getAttribute('href'); }
  set target(value) { this.setAttribute('target', value); }
  set rel(value) { this.setAttribute('rel', value); }
  appendChild(node) { node.parentElement = this; this.childNodes.push(node); return node; }
  remove() { if (this.parentElement) this.parentElement.childNodes = this.parentElement.childNodes.filter((node) => node !== this); }
  setAttribute(name, value) {
    const stringValue = String(value);
    this.attributes.set(name, stringValue);
    if (name === 'class') this.className = stringValue;
    if (name === 'id') this.ownerDocument.ids.set(stringValue, this);
    if (name.startsWith('data-')) this.dataset[name.slice(5).replace(/-([a-z])/g, (_, c) => c.toUpperCase())] = stringValue;
  }
  getAttribute(name) { return this.attributes.get(name) ?? null; }
  addEventListener(type, listener) {
    const listeners = this._listeners.get(type) || [];
    listeners.push(listener);
    this._listeners.set(type, listeners);
  }
  dispatchEvent(event) {
    event.target = this;
    for (const listener of this._listeners.get(event.type) || []) listener(event);
  }
  click() { this.dispatchEvent(event('click')); }
  focus() { this.ownerDocument.activeElement = this; }
  querySelectorAll(selector) {
    const matches = [];
    const match = selector.startsWith('.')
      ? (node) => node.classList.contains(selector.slice(1))
      : selector.startsWith('#')
        ? (node) => node.id === selector.slice(1)
        : (node) => node.tagName === selector.toUpperCase();
    for (const child of this.children) {
      if (match(child)) matches.push(child);
      matches.push(...child.querySelectorAll(selector));
    }
    return matches;
  }
  querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  get scrollHeight() { return this.childNodes.length; }
}

class FakeDocument {
  constructor() {
    this.ids = new Map();
    this.activeElement = null;
    this._listeners = new Map();
    this.head = new FakeElement('head', this);
    this.body = new FakeElement('body', this);
  }
  createElement(tag) { return new FakeElement(tag, this); }
  createTextNode(text) { return new FakeText(text); }
  getElementById(id) { return this.ids.get(id) || null; }
  querySelector(selector) { return this.body.querySelector(selector) || this.head.querySelector(selector); }
  addEventListener(type, listener) {
    const listeners = this._listeners.get(type) || [];
    listeners.push(listener);
    this._listeners.set(type, listeners);
  }
  dispatchEvent(event) { for (const listener of this._listeners.get(event.type) || []) listener(event); }
}

function parseHtml(html, root, document) {
  const stack = [root];
  const voidTags = new Set(['input', 'path']);
  for (const token of html.match(/<[^>]+>|[^<]+/g) || []) {
    if (token.startsWith('</')) { stack.pop(); continue; }
    if (!token.startsWith('<')) { stack.at(-1).appendChild(document.createTextNode(token)); continue; }
    const tag = token.match(/^<\s*([\w-]+)/)?.[1];
    if (!tag) continue;
    const node = document.createElement(tag);
    for (const match of token.matchAll(/([:\w-]+)(?:=(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?/g)) {
      if (match[1] !== tag) node.setAttribute(match[1], match[2] ?? match[3] ?? match[4] ?? '');
    }
    stack.at(-1).appendChild(node);
    if (!voidTags.has(tag) && !token.endsWith('/>')) stack.push(node);
  }
}

function event(type, values = {}) {
  return { type, defaultPrevented: false, preventDefault() { this.defaultPrevented = true; }, ...values };
}

function boot({ pathname = '/', fetchImpl } = {}) {
  const document = new FakeDocument();
  const fetchCalls = [];
  const fetch = (...args) => {
    fetchCalls.push(args);
    return fetchImpl ? fetchImpl(...args) : Promise.resolve({ ok: true, json: async () => ({ reply: 'Ready' }) });
  };
  let timerId = 0;
  vm.runInNewContext(source, {
    document,
    location: { pathname },
    fetch,
    AbortController,
    URL,
    Math,
    Promise,
    setTimeout(callback, delay) { if (delay <= 800) queueMicrotask(callback); return ++timerId; },
    clearTimeout() {},
  });
  return { document, fetchCalls };
}

async function settle() {
  for (let count = 0; count < 8; count += 1) await Promise.resolve();
}

async function waitFor(predicate) {
  for (let count = 0; count < 50; count += 1) {
    if (predicate()) return;
    await new Promise((resolve) => setImmediate(resolve));
  }
  assert.fail('condition did not become observable');
}

test('bot replies render hostile markup as text and create only safe URL links', async () => {
  const reply = '<img src=x onerror=globalThis.pwned=true>\nAvoid https://user:pass@example.com and use https://example.com/help, then https://example.com/docs?q=a,b.';
  const { document } = boot({ fetchImpl: async () => ({ ok: true, json: async () => ({ reply }) }) });
  document.getElementById('chat-widget-btn').click();
  const input = document.getElementById('chatInput');
  input.value = 'Show details';
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: false }));
  await settle();

  const botReply = document.getElementById('chatMessages').querySelectorAll('.bot').at(-1);
  assert.match(botReply.textContent, /<img src=x onerror=/);
  assert.equal(botReply.querySelector('img'), null);
  const links = botReply.querySelectorAll('a');
  assert.equal(links.length, 2);
  assert.equal(links[0].getAttribute('href'), 'https://example.com/help');
  assert.equal(links[0].getAttribute('rel'), 'noopener noreferrer');
  assert.equal(links[1].getAttribute('href'), 'https://example.com/docs?q=a,b');
});

test('Traditional Chinese fallback keeps prose and creates two exact contact links', async () => {
  const { document } = boot({ pathname: '/contact.html', fetchImpl: async () => { throw new Error('offline'); } });
  document.getElementById('chat-widget-btn').click();
  const input = document.getElementById('chatInput');
  input.value = '需要協助';
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: false }));
  await waitFor(() => document.getElementById('chat-widget-box').getAttribute('aria-busy') === 'false');

  const fallback = document.getElementById('chatMessages').querySelectorAll('.bot').at(-1);
  assert.match(fallback.textContent, /，或開啟需求諮詢：/);
  assert.deepEqual(fallback.querySelectorAll('a').map((link) => link.getAttribute('href')), [
    'https://t.me/AUTO_DEV_AI_BOT',
    'https://chat.autodev-ai.com/form',
  ]);
});

test('locale, controls, Escape focus return, and reduced motion are exposed in the DOM', async () => {
  const { document } = boot({ pathname: '/en/contact.html' });
  const button = document.getElementById('chat-widget-btn');
  const box = document.getElementById('chat-widget-box');
  assert.equal(button.getAttribute('aria-controls'), 'chat-widget-box');
  assert.equal(button.getAttribute('aria-expanded'), 'false');
  assert.match(button.getAttribute('aria-label'), /chat/i);
  assert.match(document.getElementById('chatInput').getAttribute('aria-label'), /question/i);
  assert.deepEqual(document.getElementById('chatQuickBtns').querySelectorAll('button').map((item) => item.textContent.trim()), ['Services', 'Budget', 'Scope', 'Enquiry']);
  assert.match(box.textContent, /AI-assisted/);
  assert.doesNotMatch(box.textContent, /免費|幾秒|free consultation/i);
  assert.match(document.head.querySelector('style').textContent, /prefers-reduced-motion:\s*reduce/);

  button.click();
  assert.equal(button.getAttribute('aria-expanded'), 'true');
  document.dispatchEvent(event('keydown', { key: 'Escape' }));
  assert.equal(button.getAttribute('aria-expanded'), 'false');
  assert.equal(document.activeElement === button, true);
  await settle();

  const { document: zhDocument } = boot({ pathname: '/contact.html' });
  assert.deepEqual(zhDocument.getElementById('chatQuickBtns').querySelectorAll('button').map((item) => item.textContent.trim()), ['服務', '預算', '範圍', '諮詢']);
  assert.match(zhDocument.getElementById('chat-widget-box').textContent, /AI 輔助/);
  assert.doesNotMatch(zhDocument.getElementById('chat-widget-box').textContent, /免費|幾秒/);
});

test('busy state blocks duplicate Enter, click, and quick-button requests', async () => {
  let resolveFetch;
  const pending = new Promise((resolve) => { resolveFetch = resolve; });
  const { document, fetchCalls } = boot({ fetchImpl: () => pending });
  document.getElementById('chat-widget-btn').click();
  const input = document.getElementById('chatInput');
  input.value = 'One request';
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: false }));
  input.value = 'Duplicate';
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: false }));
  document.getElementById('chatSend').click();
  document.getElementById('chatQuickBtns').querySelector('button').click();
  assert.equal(fetchCalls.length, 1);
  assert.equal(document.getElementById('chat-widget-box').getAttribute('aria-busy'), 'true');
  document.dispatchEvent(event('keydown', { key: 'Escape' }));
  assert.equal(document.activeElement === document.getElementById('chat-widget-btn'), true);

  resolveFetch({ ok: true, json: async () => ({ reply: 'Done' }) });
  await settle();
  assert.equal(document.getElementById('chat-widget-box').getAttribute('aria-busy'), 'false');
  assert.equal(document.activeElement === document.getElementById('chat-widget-btn'), true);
});

test('IME, 500-character input, session payload, and two-domain failover stay intact', async () => {
  let attempt = 0;
  const { document, fetchCalls } = boot({
    fetchImpl: async () => {
      attempt += 1;
      if (attempt === 1) throw new Error('offline');
      return { ok: true, json: async () => ({ reply: 'Recovered' }) };
    },
  });
  const input = document.getElementById('chatInput');
  assert.equal(input.getAttribute('maxlength'), '500');
  input.value = 'Composed question';
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: true }));
  assert.equal(fetchCalls.length, 0);
  input.dispatchEvent(event('keydown', { key: 'Enter', isComposing: false }));
  await waitFor(() => fetchCalls.length === 2 && document.getElementById('chat-widget-box').getAttribute('aria-busy') === 'false');

  assert.deepEqual(fetchCalls.map(([url]) => url), [
    'https://chat.autodev-ai.com/api/chat',
    'https://line-bot.76.13.219.163.nip.io/api/chat',
  ]);
  const payloads = fetchCalls.map(([, options]) => JSON.parse(options.body));
  assert.equal(payloads[0].message, 'Composed question');
  assert.match(payloads[0].session_id, /^web_/);
  assert.equal(payloads[1].session_id, payloads[0].session_id);
});
