import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import test from "node:test";

const root = new URL("../", import.meta.url);
const load = (path) => readFileSync(new URL(path, root), "utf8");

const HEADER_START = "<!-- v2-chrome:header -->";
const HEADER_END = "<!-- /v2-chrome:header -->";
const FOOTER_START = "<!-- v2-chrome:footer -->";
const FOOTER_END = "<!-- /v2-chrome:footer -->";
const DISCLOSURE_START = "<!-- v2-chrome:disclosure -->";
const DISCLOSURE_END = "<!-- /v2-chrome:disclosure -->";

function discoverArticles() {
  const list = (dir) => readdirSync(new URL(dir, root), { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".html"))
    .map((entry) => `${dir}${entry.name}`);
  const paths = [...list("blog/"), ...list("en/blog/")];
  return paths
    .filter((path) => path !== "blog/index.html" && path !== "en/blog/index.html")
    .sort();
}

const articles = discoverArticles();

const contentNavFixture = JSON.parse(readFileSync(new URL("fixtures/blog-content-navs.json", import.meta.url), "utf8"));
const disclosureFixture = new Set(
  JSON.parse(readFileSync(new URL("fixtures/blog-disclosure-footers.json", import.meta.url), "utf8")),
);

function countAll(haystack, needle) {
  let count = 0;
  let idx = 0;
  while (true) {
    idx = haystack.indexOf(needle, idx);
    if (idx === -1) break;
    count += 1;
    idx += needle.length;
  }
  return count;
}

function markerSpan(html, startMarker, endMarker) {
  const s = html.indexOf(startMarker);
  if (s === -1) return null;
  const e = html.indexOf(endMarker, s);
  if (e === -1) return null;
  return [s, e + endMarker.length];
}

// Minimal balanced <nav>...</nav> scanner mirroring scripts/apply_blog_chrome.py's
// find_balanced(), used only to count content (toc/breadcrumb) navs for the
// fixture cross-check below.
function findNavSpans(html) {
  const openRe = /<nav(\s[^>]*)?>/gi;
  const closeRe = /<\/nav\s*>/gi;
  const spans = [];
  let pos = 0;
  while (true) {
    openRe.lastIndex = pos;
    const m = openRe.exec(html);
    if (!m) break;
    let depth = 1;
    let scanPos = m.index + m[0].length;
    while (depth > 0) {
      openRe.lastIndex = scanPos;
      closeRe.lastIndex = scanPos;
      const nm = openRe.exec(html);
      const cm = closeRe.exec(html);
      if (!cm) { depth = -1; break; }
      if (nm && nm.index < cm.index) { depth += 1; scanPos = nm.index + nm[0].length; }
      else { depth -= 1; scanPos = cm.index + cm[0].length; }
    }
    if (depth === 0) { spans.push([m.index, scanPos]); pos = scanPos; }
    else pos = m.index + m[0].length;
  }
  return spans;
}

function tagAttr(tag, name) {
  const m = tag.match(new RegExp(`${name}=["']([^"']*)["']`, "i"));
  return m ? m[1] : "";
}

function countContentNavs(html, headerSpan) {
  let count = 0;
  for (const [s, e] of findNavSpans(html)) {
    if (headerSpan && s >= headerSpan[0] && s < headerSpan[1]) continue;
    const tag = html.slice(s, html.indexOf(">", s) + 1);
    const cls = tagAttr(tag, "class");
    const aria = tagAttr(tag, "aria-label");
    if (/toc|breadcrumb|目錄/i.test(cls) || /toc|breadcrumb|目錄/i.test(aria)) count += 1;
  }
  return count;
}

test("blog-chrome fixture covers exactly the migrated article set", () => {
  assert.deepEqual(Object.keys(contentNavFixture).sort(), articles);
});

test("every article has exactly one v2-chrome header block and one footer block", () => {
  for (const path of articles) {
    const html = load(path);
    assert.equal(countAll(html, HEADER_START), 1, `${path} header start marker`);
    assert.equal(countAll(html, HEADER_END), 1, `${path} header end marker`);
    assert.equal(countAll(html, FOOTER_START), 1, `${path} footer start marker`);
    assert.equal(countAll(html, FOOTER_END), 1, `${path} footer end marker`);
    const [hs, he] = markerSpan(html, HEADER_START, HEADER_END);
    const [fs] = markerSpan(html, FOOTER_START, FOOTER_END);
    assert.ok(hs < he, `${path} header span order`);
    assert.ok(he <= fs, `${path} header comes before footer`);
  }
});

test("id nav / navLinks / mobileMenuBtn each appear exactly once, inside the v2 header block", () => {
  for (const path of articles) {
    const html = load(path);
    const [hs, he] = markerSpan(html, HEADER_START, HEADER_END);
    for (const idName of ['id="nav"', 'id="navLinks"', 'id="mobileMenuBtn"']) {
      const occurrences = [];
      let idx = html.indexOf(idName);
      while (idx !== -1) { occurrences.push(idx); idx = html.indexOf(idName, idx + 1); }
      assert.equal(occurrences.length, 1, `${path} ${idName} occurrence count`);
      assert.ok(occurrences[0] >= hs && occurrences[0] < he, `${path} ${idName} inside header block`);
    }
  }
});

test("v2-chrome.css appears exactly once, right before </head> and after every other head style/link", () => {
  for (const path of articles) {
    const html = load(path);
    assert.equal(countAll(html, "/assets/v2-chrome.css"), 1, `${path} css link count`);
    const headEnd = html.indexOf("</head>");
    const cssIdx = html.indexOf("v2-chrome.css");
    assert.ok(cssIdx !== -1 && cssIdx < headEnd, `${path} css link before </head>`);
    const linkTagEnd = html.indexOf(">", cssIdx) + 1;
    const between = html.slice(linkTagEnd, headEnd);
    assert.doesNotMatch(between, /<style|<link/i, `${path} css link is the last head style/link`);
  }
});

test("autodev-v2.js is referenced exactly once", () => {
  for (const path of articles) {
    const html = load(path);
    assert.equal(countAll(html, "/assets/autodev-v2.js"), 1, `${path} autodev-v2.js reference count`);
  }
});

test("no element outside the v2 chrome carries the legacy nav-logo class", () => {
  const navLogoClassRe = /class=["'][^"']*\bnav-logo\b[^"']*["']/;
  for (const path of articles) {
    const html = load(path);
    assert.doesNotMatch(html, navLogoClassRe, `${path} legacy nav-logo class`);
  }
});

test("content navigation (toc/breadcrumb/series/related) counts match the pre-migration baseline", () => {
  for (const path of articles) {
    const html = load(path);
    const [hs, he] = markerSpan(html, HEADER_START, HEADER_END);
    const count = countContentNavs(html, [hs, he]);
    assert.equal(count, contentNavFixture[path], `${path} content nav count`);
  }
});

test("no <footer appears anywhere outside the v2-chrome footer marker block", () => {
  for (const path of articles) {
    const html = load(path);
    const [fs, fe] = markerSpan(html, FOOTER_START, FOOTER_END);
    for (const m of html.matchAll(/<footer\b/gi)) {
      assert.ok(m.index >= fs && m.index < fe, `${path} stray <footer at ${m.index}`);
    }
  }
});

test("only the baseline disclosure-footer articles carry a non-empty v2c-disclosure aside", () => {
  for (const path of articles) {
    const html = load(path);
    const disclosureCount = countAll(html, DISCLOSURE_START);
    if (disclosureFixture.has(path)) {
      assert.equal(disclosureCount, 1, `${path} expected exactly one disclosure block`);
      const [ds, de] = markerSpan(html, DISCLOSURE_START, DISCLOSURE_END);
      const block = html.slice(ds, de);
      const pMatch = block.match(/<p>([\s\S]*?)<\/p>/);
      assert.ok(pMatch, `${path} disclosure block has a <p>`);
      assert.ok(pMatch[1].trim().length > 0, `${path} disclosure <p> is non-empty`);
      assert.match(block, /class="v2c-disclosure"/, `${path} disclosure aside class`);
    } else {
      assert.equal(disclosureCount, 0, `${path} should have no disclosure block`);
    }
  }
});

test("English articles use the English v2 chrome, Traditional-Chinese articles use the zh chrome", () => {
  for (const path of articles) {
    const html = load(path);
    const [hs, he] = markerSpan(html, HEADER_START, HEADER_END);
    const header = html.slice(hs, he);
    const [fs, fe] = markerSpan(html, FOOTER_START, FOOTER_END);
    const footer = html.slice(fs, fe);
    if (path.startsWith("en/")) {
      assert.match(header, /href="\/en\/services\.html">Services</, `${path} en nav`);
      assert.match(header, /href="\/en\/blog\/" aria-current="page">Insights</, `${path} en nav current`);
      assert.match(footer, /href="\/en\/privacy\.html">Privacy</, `${path} en footer`);
    } else {
      assert.match(header, /href="\/services\.html">服務</, `${path} zh nav`);
      assert.match(header, /href="\/blog\/" aria-current="page">洞察</, `${path} zh nav current`);
      assert.match(footer, /href="\/privacy\.html">隱私權</, `${path} zh footer`);
    }
  }
});
