import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import test from "node:test";

const root = new URL("../", import.meta.url);
const load = (path) => readFileSync(new URL(path, root), "utf8");

// All 158 blog/*.html + en/blog/*.html articles (minus the two hub pages)
// have now been through scripts/unify_articles.py, same discovery as
// tests/blog-chrome.test.mjs.
function discoverArticles() {
  const list = (dir) => readdirSync(new URL(dir, root), { withFileTypes: true })
    .filter((entry) => entry.isFile() && entry.name.endsWith(".html"))
    .map((entry) => `${dir}${entry.name}`);
  const paths = [...list("blog/"), ...list("en/blog/")];
  return paths
    .filter((path) => path !== "blog/index.html" && path !== "en/blog/index.html")
    .sort();
}

// Plus the legacy (non-article) pages converted in this same round: 6 from
// the previous batch, plus the 5 that needed the apply_blog_chrome.py fixes
// (english = rel.startsWith("en/"), and the Kira page_credits footer
// verdict) landed before they could go through either script.
const CONVERTED_LEGACY_PAGES = [
  "privacy.html",
  "terms.html",
  "disclaimer.html",
  "404.html",
  "downloads/index.html",
  "downloads/ai-tools-guide-2026.html",
  "en/privacy.html",
  "en/terms.html",
  "en/disclaimer.html",
  "kira/index.html",
  "en/kira/index.html",
];

// TASK site-unify-20260927 batch U3: the 4 content-type tools/*.html pages
// (no calculator of their own) get the exact same full treatment as an
// article, plus the wider `v2c-tool` main modifier.
const CONTENT_TOOL_PAGES = [
  "tools/index.html",
  "en/tools/index.html",
  "tools/hyperframes-heygen-html-to-video-2026.html",
  "tools/postfast-mcp-social-scheduler-review-2026.html",
];

// 158 articles + 11 legacy pages + 4 content-type tool pages = 173.
const CONVERTED_ARTICLES = [
  ...discoverArticles(),
  ...CONVERTED_LEGACY_PAGES,
  ...CONTENT_TOOL_PAGES,
];

// The remaining 20 tools/*.html + en/tools/*.html pages are script-bound
// calculators/filters/quizzes: they went through unify_articles.py's
// --keep-functional-css mode (auto-detected by path), so they may still
// carry one <style data-v2c-functional> block and functional-looking
// style="" attributes -- see the separate, lighter test suite below.
const INTERACTIVE_TOOL_PAGES = [
  "tools/aeo-geo-checker-2026.html",
  "tools/ai-agent-memory-tools-comparison-2026.html",
  "tools/ai-calendar-tools-compare.html",
  "tools/ai-coding-cost-calculator.html",
  "tools/ai-coding-tools-pricing-calculator-2026.html",
  "tools/ai-cost-calculator.html",
  "tools/ai-subscription-calculator.html",
  "tools/ai-token-cost-calculator.html",
  "tools/ai-video-ad-comparison-2026.html",
  "tools/ai-video-tool-comparison-2026.html",
  "tools/clickup-vs-notion-ai-2026.html",
  "tools/geo-aeo-tools-comparison-2026.html",
  "tools/line-bot-calculator.html",
  "tools/omniroute-vs-openrouter-2026.html",
  "tools/token-cost-calculator.html",
  "tools/vps-compare.html",
  "tools/webflow-vs-framer-vs-squarespace-2026.html",
  "en/tools/line-bot-calculator.html",
  "en/tools/token-cost-calculator.html",
  "en/tools/vps-compare.html",
];

const TOOL_PATH_RE = /^(?:en\/)?tools\//;

// A JS mirror of scripts/unify_articles.py's FUNCTIONAL_CSS_MARKER_RE, used
// only to sanity-check that every statement kept in a <style
// data-v2c-functional> block looks load-bearing. The byte-exact "is this
// really a subset of the *original* <style>" check is done on the Python
// side (verify_one(), and tests/test_unify_articles.py's
// KeepFunctionalCssTests), which has git access to that original; this is
// deliberately a lighter, git-independent structural check.
const FUNCTIONAL_CSS_MARKER_RE = new RegExp(
  [
    "\\.hidden\\b", "\\.active\\b", "\\.show\\b", "\\.open\\b", "\\.selected\\b", "\\.is-", ":checked",
    "\\[hidden\\]", "\\[aria-selected", "\\[aria-expanded",
    "display\\s*:\\s*none", "visibility", "opacity\\s*:\\s*0(?!\\.)", "hidden",
  ].join("|"),
  "i",
);

function splitTopLevelCssStatements(css) {
  const statements = [];
  let i = 0;
  const n = css.length;
  while (i < n) {
    while (i < n && " \t\r\n".includes(css[i])) i += 1;
    if (i >= n) break;
    const start = i;
    let depth = 0;
    while (i < n) {
      if (css[i] === "{") depth += 1;
      else if (css[i] === "}") {
        depth -= 1;
        if (depth === 0) { i += 1; break; }
      }
      i += 1;
    }
    statements.push(css.slice(start, i));
  }
  return statements;
}

const HEADER_START = "<!-- v2-chrome:header -->";
const HEADER_END = "<!-- /v2-chrome:header -->";
const FOOTER_START = "<!-- v2-chrome:footer -->";
const FOOTER_END = "<!-- /v2-chrome:footer -->";
const DISCLOSURE_START = "<!-- v2-chrome:disclosure -->";
const DISCLOSURE_END = "<!-- /v2-chrome:disclosure -->";

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

function headSpan(html) {
  const m = /<head(\s[^>]*)?>/i.exec(html);
  assert.ok(m, "expected a <head> tag");
  const end = html.toLowerCase().indexOf("</head>");
  assert.ok(end !== -1, "expected a </head> tag");
  return html.slice(m.index + m[0].length, end);
}

function bodyOpenTag(html) {
  const m = /<body(\s[^>]*)?>/i.exec(html);
  assert.ok(m, "expected a <body> tag");
  return m[0];
}

function classListOf(tagHtml) {
  const m = /\bclass\s*=\s*"([^"]*)"/i.exec(tagHtml) || /\bclass\s*=\s*'([^']*)'/i.exec(tagHtml);
  return m ? m[1].split(/\s+/).filter(Boolean) : [];
}

function stylesheetHrefs(html) {
  const head = headSpan(html);
  const hrefs = [];
  for (const m of head.matchAll(/<link\b[^>]*>/gi)) {
    const tag = m[0];
    const rel = /\brel\s*=\s*"([^"]*)"/i.exec(tag) || /\brel\s*=\s*'([^']*)'/i.exec(tag);
    if (rel && rel[1].toLowerCase() === "stylesheet") {
      const href = /\bhref\s*=\s*"([^"]*)"/i.exec(tag) || /\bhref\s*=\s*'([^']*)'/i.exec(tag);
      hrefs.push(href ? href[1] : "");
    }
  }
  return hrefs;
}

// Minimal balanced <tag>...</tag> scanner mirroring
// scripts/apply_blog_chrome.py's find_balanced(), used here only to find
// the top-level <main> in the content region.
function findBalanced(html, tag) {
  const openRe = new RegExp(`<${tag}(\\s[^>]*)?>`, "gi");
  const closeRe = new RegExp(`</${tag}\\s*>`, "gi");
  const spans = [];
  let pos = 0;
  while (true) {
    openRe.lastIndex = pos;
    const m = openRe.exec(html);
    if (!m) break;
    let depth = 1;
    let scanPos = m.index + m[0].length;
    let end = -1;
    while (depth > 0) {
      openRe.lastIndex = scanPos;
      closeRe.lastIndex = scanPos;
      const nm = openRe.exec(html);
      const cm = closeRe.exec(html);
      if (!cm) { depth = -1; break; }
      if (nm && nm.index < cm.index) {
        depth += 1;
        scanPos = nm.index + nm[0].length;
      } else {
        depth -= 1;
        scanPos = cm.index + cm[0].length;
        end = scanPos;
      }
    }
    if (depth === 0) {
      spans.push([m.index, end, m.index + m[0].length, end - `</${tag}>`.length]);
      pos = end;
    } else {
      pos = m.index + m[0].length;
    }
  }
  return spans;
}

for (const path of CONVERTED_ARTICLES) {
  test(`${path}: body carries v2c-page`, () => {
    const html = load(path);
    const bodyTag = bodyOpenTag(html);
    assert.ok(classListOf(bodyTag).includes("v2c-page"), "body should have class v2c-page");
  });

  test(`${path}: head has no <style> element`, () => {
    const head = headSpan(load(path));
    assert.ok(!/<style\b/i.test(head), "head should not contain a <style> element");
  });

  test(`${path}: only /assets/v2-chrome.css remains as a stylesheet link`, () => {
    const hrefs = stylesheetHrefs(load(path));
    assert.deepEqual(hrefs, ["/assets/v2-chrome.css"]);
  });

  test(`${path}: body has no <style> element outside the frame markers`, () => {
    const html = load(path);
    // The whole document should have zero <style> elements at all -- head
    // was already checked above; this asserts none survive anywhere.
    assert.ok(!/<style\b/i.test(html), "document should not contain any <style> element");
  });

  test(`${path}: v2-chrome frame markers each appear exactly once`, () => {
    const html = load(path);
    assert.equal(countAll(html, HEADER_START), 1);
    assert.equal(countAll(html, HEADER_END), 1);
    assert.equal(countAll(html, FOOTER_START), 1);
    assert.equal(countAll(html, FOOTER_END), 1);
    const discStart = countAll(html, DISCLOSURE_START);
    const discEnd = countAll(html, DISCLOSURE_END);
    assert.ok(discStart === 0 || discStart === 1, "disclosure marker should appear at most once");
    assert.equal(discStart, discEnd);
  });

  test(`${path}: content region is wrapped in <main class="v2c-article">`, () => {
    const html = load(path);
    const headerEndIdx = html.indexOf(HEADER_END);
    assert.ok(headerEndIdx !== -1);
    const contentStart = headerEndIdx + HEADER_END.length;
    const discStart = html.indexOf(DISCLOSURE_START);
    const footerStart = html.indexOf(FOOTER_START);
    assert.ok(footerStart !== -1);
    const contentEnd = discStart !== -1 ? discStart : footerStart;
    const content = html.slice(contentStart, contentEnd);

    const requiredClasses = TOOL_PATH_RE.test(path) ? ["v2c-article", "v2c-tool"] : ["v2c-article"];
    const hasRequired = (tagHtml) => {
      const classes = classListOf(tagHtml);
      return requiredClasses.every((c) => classes.includes(c));
    };

    const mainSpans = findBalanced(content, "main");
    const fullSpan = mainSpans.find(
      ([s, e]) => content.slice(0, s).trim() === "" && content.slice(e).trim() === "",
    );
    if (fullSpan) {
      const tagStart = fullSpan[0];
      const tagHtml = content.slice(tagStart, content.indexOf(">", tagStart) + 1);
      assert.ok(hasRequired(tagHtml), `the <main> should carry class ${requiredClasses.join(" ")}`);
      return;
    }
    // Same unclosed-<main> shape scripts/unify_articles.py's wrap_main()
    // handles: the region opens with a <main ...> whose matching </main>
    // sits past contentEnd (e.g. Kira's page_credits disclosure block sits
    // *inside* its own top-level <main class="kira-page">). The class was
    // added to that opening tag in place, with no synthetic </main> here.
    const lead = content.length - content.trimStart().length;
    const openMatch = /^<main(\s[^>]*)?>/i.exec(content.slice(lead));
    assert.ok(openMatch, "content region should open with a <main> if it is not a full balanced span");
    assert.ok(!/<\/main\s*>/i.test(content), "an unclosed <main> here should have no </main> anywhere in the region");
    const tagHtml = content.slice(lead, lead + openMatch[0].length);
    assert.ok(hasRequired(tagHtml), `the unclosed <main> should carry class ${requiredClasses.join(" ")}`);
  });

  test(`${path}: content region has no style="" attributes outside <script>`, () => {
    const html = load(path);
    const headerEndIdx = html.indexOf(HEADER_END);
    const contentStart = headerEndIdx + HEADER_END.length;
    const discStart = html.indexOf(DISCLOSURE_START);
    const footerStart = html.indexOf(FOOTER_START);
    const contentEnd = discStart !== -1 ? discStart : footerStart;
    const content = html.slice(contentStart, contentEnd);

    const scriptSpans = findBalanced(content, "script");
    const inScript = (pos) => scriptSpans.some(([s, e]) => s <= pos && pos < e);

    // Only look for style="..." inside an actual opening tag's own text
    // (bounded by < and >), never in the plain text between tags -- a
    // <pre><code> example that shows `const { style = 'x' } = ...` as
    // sample code is not an HTML attribute and must not be flagged.
    for (const m of content.matchAll(/<[a-zA-Z][a-zA-Z0-9-]*(?:\s[^<>]*)?\/?>/g)) {
      if (inScript(m.index)) continue;
      assert.ok(
        !/\sstyle\s*=\s*("[^"]*"|'[^']*')/i.test(m[0]),
        `content region should have no style attributes outside <script> (found in: ${m[0].slice(0, 80)})`,
      );
    }
  });
}

// The 20 interactive tools/*.html pages: lighter checks that account for
// unify_articles.py's --keep-functional-css mode (at most one <style
// data-v2c-functional>, functional-looking style="" attributes allowed).
for (const path of INTERACTIVE_TOOL_PAGES) {
  test(`${path}: body carries v2c-page`, () => {
    const html = load(path);
    assert.ok(classListOf(bodyOpenTag(html)).includes("v2c-page"));
  });

  test(`${path}: only /assets/v2-chrome.css remains as a stylesheet link`, () => {
    assert.deepEqual(stylesheetHrefs(load(path)), ["/assets/v2-chrome.css"]);
  });

  test(`${path}: v2-chrome frame markers each appear exactly once`, () => {
    const html = load(path);
    assert.equal(countAll(html, HEADER_START), 1);
    assert.equal(countAll(html, HEADER_END), 1);
    assert.equal(countAll(html, FOOTER_START), 1);
    assert.equal(countAll(html, FOOTER_END), 1);
  });

  test(`${path}: content region's <main> carries v2c-article and v2c-tool`, () => {
    const html = load(path);
    const headerEndIdx = html.indexOf(HEADER_END);
    const contentStart = headerEndIdx + HEADER_END.length;
    const footerStart = html.indexOf(FOOTER_START);
    const content = html.slice(contentStart, footerStart);
    const mainMatch = /<main(\s[^>]*)?>/i.exec(content);
    assert.ok(mainMatch, "content region should contain a <main>");
    const classes = classListOf(mainMatch[0]);
    assert.ok(classes.includes("v2c-article") && classes.includes("v2c-tool"));
  });

  test(`${path}: at most one <style data-v2c-functional>, and every kept rule looks functional`, () => {
    const html = load(path);
    const styleTags = [...html.matchAll(/<style\b[^>]*>/gi)];
    assert.ok(styleTags.length <= 1, `expected 0 or 1 <style> tag, found ${styleTags.length}`);
    if (styleTags.length === 0) return;
    assert.ok(
      /data-v2c-functional/i.test(styleTags[0][0]),
      "the one remaining <style> tag must be the functional block",
    );
    const blockMatch = /<style\b[^>]*data-v2c-functional[^>]*>([\s\S]*?)<\/style>/i.exec(html);
    assert.ok(blockMatch, "expected a closing </style> for the functional block");
    const statements = splitTopLevelCssStatements(blockMatch[1]);
    assert.ok(statements.length > 0, "the functional block should not be empty if it exists");
    for (const stmt of statements) {
      assert.ok(
        FUNCTIONAL_CSS_MARKER_RE.test(stmt),
        `kept statement does not look functional: ${stmt.slice(0, 120)}`,
      );
    }
  });
}
