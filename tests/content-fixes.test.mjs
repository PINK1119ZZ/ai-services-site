// Regression tests for the 2026-09-28 content-fixes batch (TASK content-fixes-20260928).
// node:test only, no dependencies. Run with:
//   node --test tests/content-fixes.test.mjs
import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (rel) => readFileSync(join(ROOT, rel), "utf8");

const MONEY_RE = /(?:NT\$|\$)[0-9]+(?:,[0-9]+)*/g;
function extractMoney(text) {
  return (text.match(MONEY_RE) || []).sort();
}

const PRICE_FILES = ["ai-model.html", "en/ai-model.html"];
const baselinePrices = JSON.parse(
  readFileSync(join(ROOT, "tests/fixtures/content-fixes-prices.json"), "utf8")
);

test("AI model pricing copy: NT$/$ amount multiset is unchanged vs. the pre-fix baseline", () => {
  for (const rel of PRICE_FILES) {
    const current = extractMoney(read(rel));
    const before = baselinePrices[rel];
    assert.ok(Array.isArray(before) && before.length > 0, `missing baseline fixture for ${rel}`);
    assert.deepEqual(current, before, `money-string multiset changed in ${rel}`);
  }
});

test('AI model pricing copy: paid single-image plan is renamed off "試做包" / "Trial Pack"', () => {
  const zh = read("ai-model.html");
  const en = read("en/ai-model.html");

  assert.ok(!zh.includes("試做包"), "ai-model.html still contains 試做包");
  assert.ok(!en.includes("Trial Pack"), "en/ai-model.html still contains Trial Pack");

  assert.ok(zh.includes("單張"), "ai-model.html missing renamed plan 單張");
  assert.ok(en.includes("Single Image"), "en/ai-model.html missing renamed plan Single Image");

  // Free trial copy/CTA must be untouched.
  assert.ok(zh.includes("免費試做 1 張"), "ai-model.html free-trial copy changed");
  assert.ok(en.includes("Free Trial 1 Image"), "en/ai-model.html free-trial copy changed");
});

test("AI model comparison table: per-shoot-cost image count reads 1- not 5-", () => {
  const zh = read("ai-model.html");
  const en = read("en/ai-model.html");

  assert.ok(zh.includes("NT$1,200-8,800（1-15 張）"), "zh per-shoot-cost line not updated");
  assert.ok(!zh.includes("含 5-15 張"), "zh per-shoot-cost line still says 含 5-15 張");

  assert.ok(en.includes("$40-$285 (1-15 images)"), "en per-shoot-cost line not updated");
  assert.ok(!en.includes("(5-15 images)"), "en per-shoot-cost line still says (5-15 images)");
});

test("AI model comparison table: quarterly-assets line reads as a quarter of usage, not a monthly fee", () => {
  const zh = read("ai-model.html");
  const en = read("en/ai-model.html");

  assert.ok(
    zh.includes("一季用量的品牌素材（30 張 + 3 影片）：") && zh.includes("一個月度合作即可交付"),
    "zh AI-side quarterly-assets line not reworded"
  );
  assert.ok(
    zh.includes("一季用量的品牌素材：") && zh.includes("NT$100,000-180,000"),
    "zh human-side quarterly-assets label not updated"
  );

  assert.ok(
    en.includes("A quarter's worth of brand assets (30 images + 3 reels):") &&
      en.includes("delivered within one monthly plan"),
    "en AI-side quarterly-assets line not reworded"
  );
  assert.ok(
    en.includes("A quarter's worth of brand assets:") && en.includes("$3,000-$6,000"),
    "en human-side quarterly-assets label not updated"
  );
});

test("en/demo.html: JSON-LD name/url match the English page, hreflang has no duplicates", () => {
  const html = read("en/demo.html");

  const ldMatch = html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
  assert.ok(ldMatch, "en/demo.html missing JSON-LD block");
  const data = JSON.parse(ldMatch[1]);

  const canonicalMatch = html.match(/<link href="([^"]+)" rel="canonical"\/>/);
  assert.ok(canonicalMatch, "en/demo.html missing canonical link");
  const canonical = canonicalMatch[1];

  assert.equal(data.url, canonical, "JSON-LD url does not match canonical URL");
  assert.ok(!/^https:\/\/autodev-ai\.com\/demo\.html$/.test(data.url), "JSON-LD url is still the zh page");
  assert.ok(!/[一-鿿]/.test(data.name), "JSON-LD name still contains Chinese text");
  assert.ok(data.name.length > 0, "JSON-LD name is empty");

  const hreflangs = [...html.matchAll(/hreflang="([^"]+)"/g)].map((m) => m[1]);
  assert.equal(hreflangs.length, new Set(hreflangs).size, "duplicate hreflang values found");
  assert.deepEqual(
    new Set(hreflangs),
    new Set(["zh-Hant", "en", "x-default"]),
    "hreflang set changed unexpectedly"
  );
});

test("ai-model.html: editorial cards are keyboard-focusable and Enter/Space open the lightbox", () => {
  const html = read("ai-model.html");

  const cardOpenTags = [...html.matchAll(/<figure class="editorial-card"[^>]*>/g)];
  assert.equal(cardOpenTags.length, 8, "expected 8 .editorial-card figures");
  for (const m of cardOpenTags) {
    const tag = m[0];
    assert.match(tag, /tabindex="0"/, `missing tabindex on: ${tag}`);
    assert.match(tag, /role="button"/, `missing role="button" on: ${tag}`);
    assert.match(tag, /aria-label="[^"]+"/, `missing aria-label on: ${tag}`);
  }

  // The lightbox script must bind a keydown handler alongside the existing
  // click handler that reacts to Enter/Space and prevents the page from
  // scrolling on Space.
  const scriptMatch = html.match(
    /document\.querySelectorAll\('\.editorial-card'\)\.forEach\(function\(card\)\{([\s\S]*?)\}\);\s*closeBtn/
  );
  assert.ok(scriptMatch, "could not find the .editorial-card binding block");
  const block = scriptMatch[1];
  assert.match(block, /addEventListener\('keydown'/, "no keydown listener bound on editorial cards");
  assert.match(block, /e\.key === 'Enter'/, "keydown handler does not check Enter");
  assert.match(block, /e\.key === ' '/, "keydown handler does not check Space");
  assert.match(block, /preventDefault\(\)/, "keydown handler does not call preventDefault (Space would scroll)");

  // Escape must still close the lightbox.
  assert.match(html, /e\.key === 'Escape'/, "Escape-to-close handler missing");
});

test("style.css: .v2-site scope has a focus-visible outline for .editorial-card", () => {
  const css = read("style.css");
  assert.match(
    css,
    /\.v2-site \.editorial-card:focus-visible\s*\{[^}]*outline[^}]*\}/,
    "missing .v2-site .editorial-card:focus-visible rule"
  );
});

test("tools/vps-compare.html: CPU/RAM/storage/sort selects are wired to a change-driven filter", () => {
  const html = read("tools/vps-compare.html");

  for (const id of ["cpu", "ram", "storage", "sort"]) {
    assert.ok(html.includes(`id="${id}"`), `missing <select id="${id}">`);
    assert.ok(html.includes(`getElementById('${id}')`), `render logic never reads #${id}`);
  }

  assert.match(html, /addEventListener\('change',\s*render\)/, "no change listener wired to a render function");
  assert.ok(html.includes("querySelectorAll('select')"), "filters are not bound via querySelectorAll('select')");
  assert.ok(html.includes("getElementById('vpsGrid')"), "render function never writes into #vpsGrid");
  assert.ok(html.includes("var providers ="), "no provider dataset found");

  // Filter must actually be gating, not a no-op: cpu/ram/storage thresholds
  // and at least one sort mode besides price should be present.
  assert.match(html, /p\.cpu >= minCpu/);
  assert.match(html, /p\.ram >= minRam/);
  assert.match(html, /minStorage/);
  assert.match(html, /sortBy === 'cpu'/);
  assert.match(html, /sortBy === 'ram'/);
});
