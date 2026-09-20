import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readdir, readFile, stat } from "node:fs/promises";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

async function walkHtml(dir = root) {
  const paths = [];
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    if (entry.name === ".git") continue;
    const path = join(dir, entry.name);
    if (entry.isDirectory()) paths.push(...await walkHtml(path));
    else if (entry.name.endsWith(".html")) paths.push(path);
  }
  return paths.sort();
}

function jsonLdBlocks(html) {
  return [...html.matchAll(/<script[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)]
    .map((match) => JSON.parse(match[1]));
}

function textOnly(html) {
  return html.replace(/<[^>]+>/g, "").replace(/&amp;/g, "&").replace(/&#39;/g, "'").trim();
}

const costPages = [
  {
    path: "blog/line-bot-cost.html",
    canonical: "https://autodev-ai.com/blog/line-bot-cost.html",
    tgLink: "/services.html#telegram",
    budget: ["NT$50,000", "NT$100,000", "NT$200,000+"],
    banned: ["NT$8,000", "NT$12,000", "NT$15,000", "5-10 倍", "免費維護", "全額退款"],
  },
  {
    path: "en/blog/line-bot-cost.html",
    canonical: "https://autodev-ai.com/en/blog/line-bot-cost.html",
    tgLink: "/en/services.html#telegram",
    budget: ["NT$50,000", "NT$100,000", "NT$200,000+"],
    banned: ["$250", "$400", "$500", "5-10x", "free maintenance", "full refund", "50-70%"],
  },
];

const retiredArticleLinks = [
  "/blog/ai-video-editing-tools-capcut-vs-runway-vs-premiere-ai-2026.html",
  "/blog/claude-code-complete-guide-2026.html",
  "/blog/claude-code-vs-cursor-2026.html",
  "/blog/qwen3-27b-local-deploy-2026.html",
  "/blog/scrapling-python-tutorial-2026.html",
  "superpowers-claude-code-tutorial-2026.html",
  "claude-code-complete-guide-2026.html",
  "cursor-3-review-2026.html",
  "n8n-vs-make-vs-zapier-2026.html",
];

const affectedLinkSources = [
  "blog/seedance-25-review-2026.html",
  "blog/deepseek-harness-complete-guide-2026.html",
  "blog/mastra-ai-typescript-agent-framework-2026.html",
  "blog/sandboxaq-switch-ai-agent-slack-teams-tutorial-2026.html",
  "blog/deepseek-tui-terminal-coding-agent-2026.html",
  "blog/omlx-apple-silicon-llm-server-2026.html",
  "blog/firecrawl-api-review-2026.html",
  "blog/agentmemory-claude-code-tutorial-2026.html",
  "blog/claude-video-watch-tutorial-2026.html",
  "blog/officecli-mcp-claude-code-tutorial-2026.html",
];

test("all 208 original HTML documents retain paths and parse every JSON-LD block", async () => {
  const files = await walkHtml();
  assert.equal(files.length, 208);
  const failures = [];
  for (const file of files) {
    const html = await readFile(file, "utf8");
    try { jsonLdBlocks(html); }
    catch (error) { failures.push(`${relative(root, file)}: ${error.message}`); }
  }
  assert.deepEqual(failures, []);
});

test("known broken blog links are repaired without inventing routes", async () => {
  for (const source of affectedLinkSources) {
    const html = await readFile(join(root, source), "utf8");
    for (const href of retiredArticleLinks) {
      assert.doesNotMatch(html, new RegExp(`href=["']${href.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}["']`));
    }
  }
  const replacementTargets = [
    "blog/ai-video-tools-comparison-2026.html",
    "blog/opencode-vs-cursor-vs-claude-code-2026.html",
  ];
  for (const target of replacementTargets) await stat(join(root, target));
});

test("obsolete /blog.html navigation is absent", async () => {
  for (const file of await walkHtml()) {
    assert.doesNotMatch(await readFile(file, "utf8"), /href=["'](?:\.\.\/|\/)?blog\.html(?:[?#][^"']*)?["']/);
  }
});


test("known static references resolve to real sections and the shared navigation helper", async () => {
  for (const [page, sectionClass] of [["ai-model.html", "editorial-series"], ["en/ai-model.html", "scenes-section"]]) {
    const html = await readFile(join(root, page), "utf8");
    assert.match(html, new RegExp(`<section\\b[^>]*class=["']${sectionClass}["'][^>]*id=["']editorial-series["']`));
  }

  const governmentArticle = await readFile(join(root, "blog/openai-government-stake-ai-nationalization-2026.html"), "utf8");
  assert.doesNotMatch(governmentArticle, /href=["']\.\.\/styles\.css["']/);
  const geoArticle = await readFile(join(root, "blog/best-geo-tools-comparison-2026.html"), "utf8");
  assert.doesNotMatch(geoArticle, /src=["']\/script\.js["']/);
  assert.match(geoArticle, /getElementById\(["']mobileMenuBtn["']\)/);

  for (const page of [
    "blog/claude-code-prompt-pack-guide-2026.html",
    "tools/ai-coding-cost-calculator.html",
    "tools/ai-subscription-calculator.html",
  ]) {
    const html = await readFile(join(root, page), "utf8");
    const toggle = html.match(/<button\b[^>]*id=["']mobileMenuBtn["'][^>]*>/)?.[0] ?? "";
    assert.match(html, /<div\b[^>]*id=["']navLinks["'][^>]*data-nav-links[^>]*>/);
    for (const attribute of [/data-nav-toggle/, /aria-controls=["']navLinks["']/, /aria-expanded=["']false["']/, /data-open-label=["']開啟選單["']/, /data-close-label=["']關閉選單["']/]) {
      assert.match(toggle, attribute);
    }
    assert.match(html, /<script\b[^>]*src=["']\/assets\/autodev-v2\.js["'][^>]*><\/script>/);
    assert.doesNotMatch(html, /src=["']\/nav\.js["']/);
  }
});


test("legacy articles use one scoped stylesheet and LM Studio drops only its dead TOC", async () => {
  const legacyPages = [
    "blog/agent-skills-complete-guide-2026.html", "blog/agentmemory-claude-code-tutorial-2026.html",
    "blog/claude-video-watch-tutorial-2026.html", "blog/geo-blym-seo-ai-search-optimization-2026.html",
    "blog/officecli-mcp-claude-code-tutorial-2026.html", "blog/tencentdb-agent-memory-tutorial-2026.html",
    "blog/warp-terminal-review-2026.html",
  ];
  const linkedPages = [];
  for (const file of await walkHtml()) {
    const html = await readFile(file, "utf8");
    if (html.includes("assets/legacy-article.css")) linkedPages.push(relative(root, file));
  }
  assert.deepEqual(linkedPages.sort(), legacyPages.sort());
  for (const page of legacyPages) {
    const html = await readFile(join(root, page), "utf8");
    assert.match(html, /<body class=["']legacy-article["']>/);
    assert.match(html, /href=["']\.\.\/assets\/legacy-article\.css["']/);
    assert.doesNotMatch(html, /href=["']\.\.\/styles\.css["']/);
  }
  const css = await readFile(join(root, "assets/legacy-article.css"), "utf8");
  const selectorGroups = [...css.matchAll(/(?:^|[{}])\s*([^{}]+)\{/gm)].map((match) => match[1].trim()).filter((group) => !group.startsWith("@"));
  assert.ok(selectorGroups.length > 10);
  for (const group of selectorGroups) {
    for (const selector of group.replace(/:is\([^)]*\)/g, ":is()").split(",")) assert.match(selector.trim(), /^body\.legacy-article(?:\b|\s|:)/);
  }

  const lmPath = join(root, "blog/lm-studio-bionic-guide-2026.html");
  const lmHtml = await readFile(lmPath, "utf8");
  const withoutToc = lmHtml.replace(/\n\s*<div class=["']toc["']>[\s\S]*?<\/div>\n/, "\n");
  assert.equal(lmHtml, withoutToc);
  assert.equal(createHash("sha256").update(withoutToc).digest("hex"), "138995edc2767802ae10c07c8928023606fc275b558bb8c7bc40c81e57132450");
});

for (const page of costPages) {
  test(`${page.path} keeps integrations and publishes scoped pricing`, async () => {
    const html = await readFile(join(root, page.path), "utf8");
    assert.match(html, new RegExp(`<link[^>]+href=["']${page.canonical.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}["'][^>]+rel=["']canonical["']`));
    assert.match(html, /"datePublished":"2026-03-20"/);
    assert.match(html, /"dateModified":"2026-09-21"/);
    for (const value of page.budget) assert.match(html, new RegExp(value.replace("$", "\\$")));
    for (const value of page.banned) assert.ok(!html.toLowerCase().includes(value.toLowerCase()), `retired claim remains: ${value}`);
    assert.ok(html.includes(`href="${page.tgLink}"`));
    assert.match(html, /googletagmanager\.com\/gtag\/js\?id=G-4ZWDT650BM/);
    assert.match(html, /pagead2\.googlesyndication\.com\/pagead\/js\/adsbygoogle\.js/);
    assert.match(html, /src=["']\/chat-widget\.js\?v=20260502e["']/);
    assert.match(html, /src=["']\/lang\.js\?v=20260505["']/);
    assert.doesNotMatch(html, /body\s*\{[^}]*min-width\s*:/i);
    assert.match(html, /\.table-scroll\s*\{[^}]*overflow-x\s*:\s*auto/i);
    assert.match(html, /<div class="table-scroll">\s*<table class="price-table">/);

    const blocks = jsonLdBlocks(html);
    const article = blocks.find((block) => block["@type"] === "Article");
    const faq = blocks.find((block) => block["@type"] === "FAQPage");
    assert.equal(article.mainEntityOfPage, page.canonical);
    const visible = [...html.matchAll(/<div class="faq-item[^>]*>\s*<div class="faq-q"[^>]*>([\s\S]*?)<\/div>\s*<div class="faq-a"[^>]*>([\s\S]*?)<\/div>/g)]
      .map((match) => ({ question: textOnly(match[1]), answer: textOnly(match[2]) }));
    const structured = faq.mainEntity.map((item) => ({ question: item.name, answer: item.acceptedAnswer.text }));
    assert.deepEqual(visible, structured);
  });
}
