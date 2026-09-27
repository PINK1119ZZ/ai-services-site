import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const root = new URL('../', import.meta.url);
const load = (path) => readFileSync(new URL(path, root), 'utf8');
const listArticles = (dir) => readdirSync(fileURLToPath(new URL(dir, root)))
  .filter((name) => name.endsWith('.html') && name !== 'index.html')
  .sort();

const tagAttr = (tag, key) => tag?.match(new RegExp(`${key}=(["'])([\\s\\S]*?)\\1`, 'i'))?.[2];
const attr = (html, rel, key = 'href') => {
  const tag = [...html.matchAll(/<link\b[^>]*>/gi)]
    .map((match) => match[0])
    .find((candidate) => (tagAttr(candidate, 'rel') || '').split(/\s+/).includes(rel));
  return tagAttr(tag, key);
};
const between = (html, startMarker, endMarker) => {
  const start = html.indexOf(startMarker);
  assert.notEqual(start, -1, `missing marker ${startMarker}`);
  const end = html.indexOf(endMarker, start) + endMarker.length;
  return html.slice(start, end);
};
const jsonLd = (html) => [...html.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)]
  .map((match) => JSON.parse(match[1]));

const pages = [
  {
    blog: 'blog/index.html',
    commercial: 'index.html',
    dir: 'blog/',
    canonical: 'https://autodev-ai.com/blog/',
    hreflangZh: 'https://autodev-ai.com/blog/',
    hreflangEn: 'https://autodev-ai.com/en/blog/index.html',
    hreflangDefault: 'https://autodev-ai.com/blog/',
    linkPrefix: '/blog/',
    currentLinkText: '洞察',
    adsenseClient: 'ca-pub-7482625906579389',
  },
  {
    blog: 'en/blog/index.html',
    commercial: 'en/index.html',
    dir: 'en/blog/',
    canonical: 'https://autodev-ai.com/en/blog/',
    hreflangZh: 'https://autodev-ai.com/blog/',
    hreflangEn: 'https://autodev-ai.com/en/blog/',
    hreflangDefault: 'https://autodev-ai.com/blog/',
    linkPrefix: '/en/blog/',
    currentLinkText: 'Insights',
    adsenseClient: null,
  },
];

test('both blog hub pages use the v2 shell with exactly one h1', () => {
  for (const { blog } of pages) {
    const html = load(blog);
    assert.match(html, /<body\s+class=["']v2-site["']>/i, `${blog} body.v2-site`);
    assert.equal((html.match(/<h1\b/gi) || []).length, 1, `${blog} single h1`);
  }
});

test('blog hub nav matches its commercial page nav aside from the active-page marker', () => {
  for (const { blog, commercial, currentLinkText } of pages) {
    const blogNav = between(load(blog), '<nav class="nav"', '</nav>');
    const commercialNav = between(load(commercial), '<nav class="nav"', '</nav>');
    assert.match(blogNav, new RegExp(`aria-current=["']page["'][^>]*>${currentLinkText}<|>${currentLinkText}<\\/a>`));
    const stripped = blogNav.replace(/\s+aria-current=["']page["']/, '');
    assert.equal(stripped, commercialNav, `${blog} nav should equal ${commercial} nav once aria-current is removed`);
  }
});

test('blog hub footer matches its commercial page footer verbatim', () => {
  for (const { blog, commercial } of pages) {
    const blogFooter = between(load(blog), '<footer class="v2-footer"', '</footer>');
    const commercialFooter = between(load(commercial), '<footer class="v2-footer"', '</footer>');
    assert.equal(blogFooter, commercialFooter, `${blog} footer should equal ${commercial} footer`);
  }
});

test('every published article is linked at least once from its language hub', () => {
  for (const { blog, dir, linkPrefix } of pages) {
    const html = load(blog);
    const articles = listArticles(dir);
    assert.ok(articles.length > 0, `${dir} has articles`);
    for (const name of articles) {
      const href = `${linkPrefix}${name}`;
      assert.ok(html.includes(`href="${href}"`), `${blog} links ${href}`);
    }
  }
});

test('canonical and hreflang stay at their existing values', () => {
  for (const { blog, canonical, hreflangZh, hreflangEn, hreflangDefault } of pages) {
    const html = load(blog);
    assert.equal(attr(html, 'canonical'), canonical, `${blog} canonical`);
    const zhTag = [...html.matchAll(/<link\b[^>]*>/gi)].map((m) => m[0]).find((t) => tagAttr(t, 'hreflang') === 'zh-Hant');
    const enTag = [...html.matchAll(/<link\b[^>]*>/gi)].map((m) => m[0]).find((t) => tagAttr(t, 'hreflang') === 'en');
    const defaultTag = [...html.matchAll(/<link\b[^>]*>/gi)].map((m) => m[0]).find((t) => tagAttr(t, 'hreflang') === 'x-default');
    assert.equal(tagAttr(zhTag, 'href'), hreflangZh, `${blog} hreflang zh-Hant`);
    assert.equal(tagAttr(enTag, 'href'), hreflangEn, `${blog} hreflang en`);
    assert.equal(tagAttr(defaultTag, 'href'), hreflangDefault, `${blog} hreflang x-default`);
  }
});

test('JSON-LD parses and analytics/ads tags are preserved', () => {
  for (const { blog, adsenseClient } of pages) {
    const html = load(blog);
    assert.ok(jsonLd(html).length, `${blog} JSON-LD`);
    assert.match(html, /G-4ZWDT650BM/, `${blog} GA4`);
    if (adsenseClient) assert.match(html, new RegExp(adsenseClient.replace('.', '\\.')), `${blog} AdSense client`);
  }
});

test('the AGENT insertion marker is inside the post grid immediately above the newest card', () => {
  const zh = load('blog/index.html');
  const en = load('en/blog/index.html');
  for (const page of [zh, en]) {
    assert.equal(page.match(/AGENT-NEW-POST-CARDS/g)?.length, 1);
    assert.match(page, /<div class="v2-post-grid">\s*<!--\s*AGENT-NEW-POST-CARDS:[^>]*-->\s*<(div|a)\b[^>]*class="v2-post-card/);
  }
});

test('scripts load the shared v2 chrome and chat/lang helpers once', () => {
  for (const { blog } of pages) {
    const html = load(blog);
    assert.match(html, /chat-widget\.js\?v=20260502e/, `${blog} chat widget`);
    assert.match(html, /lang\.js\?v=20260505/, `${blog} lang.js`);
    assert.match(html, /assets\/autodev-v2\.js/, `${blog} autodev-v2.js`);
    assert.equal((html.match(/chat-widget\.js\?v=20260502e/g) || []).length, 1, `${blog} chat widget loaded once`);
    assert.equal((html.match(/lang\.js\?v=20260505/g) || []).length, 1, `${blog} lang.js loaded once`);
  }
});

test("every post card has a title and an article link", () => {
  for (const [file, prefix] of [["blog/index.html", "/blog/"], ["en/blog/index.html", "/en/blog/"]]) {
    const html = readFileSync(new URL(file, root), "utf8");
    const grid = html.slice(html.indexOf('<div class="v2-post-grid">'));
    const opens = [...grid.matchAll(/<(div|a)\b[^>]*class="[^"]*v2-post-card[^"]*"[^>]*>/g)];
    assert.ok(opens.length > 0, `${file} has cards`);
    for (let n = 0; n < opens.length; n += 1) {
      const card = grid.slice(opens[n].index, n + 1 < opens.length ? opens[n + 1].index : undefined);
      assert.match(card, /<h3\b[^>]*>[^<\s][\s\S]*?<\/h3>|<h3\b[^>]*><a\b[^>]*>[^<\s]/, `${file} card ${n} title`);
      assert.ok(card.includes(`href="${prefix}`), `${file} card ${n} article link`);
    }
  }
});

test("post grids have balanced div tags so no card is nested in another", () => {
  for (const file of ["blog/index.html", "en/blog/index.html"]) {
    const html = readFileSync(new URL(file, root), "utf8");
    const start = html.indexOf('<div class="v2-post-grid">');
    const end = html.indexOf("</section>", start);
    const grid = html.slice(start, end);
    let depth = 0;
    let cards = 0;
    for (const tag of grid.matchAll(/<\/?div\b[^>]*>/g)) {
      depth += tag[0].startsWith("</") ? -1 : 1;
      if (/class="v2-post-card/.test(tag[0])) { cards += 1; assert.equal(depth, 2, `${file} post card opened inside another element`); }
      if (depth === 0) break;
    }
    assert.equal(depth, 0, `${file} post grid closes`);
    assert.equal(cards, (grid.match(/<div\b[^>]*class="v2-post-card/g) || []).length, `${file} every div card sits directly in the grid`);
  }
});

