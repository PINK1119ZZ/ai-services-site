import test from "node:test";
import assert from "node:assert/strict";
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
    tableLabel: "LINE Bot 費用範圍比較表",
    budget: ["NT$50,000", "NT$100,000", "NT$200,000+"],
    banned: ["NT$8,000", "NT$12,000", "NT$15,000", "5-10 倍", "免費維護", "全額退款"],
  },
  {
    path: "en/blog/line-bot-cost.html",
    canonical: "https://autodev-ai.com/en/blog/line-bot-cost.html",
    tgLink: "/en/services.html#telegram",
    tableLabel: "LINE Bot cost comparison table",
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


test("legacy articles use one scoped stylesheet", async () => {
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
  assert.match(css, /body\.legacy-article nav \.nav-links\s*\{[^}]*margin:\s*0/);
  const selectorGroups = [...css.matchAll(/(?:^|[{}])\s*([^{}]+)\{/gm)].map((match) => match[1].trim()).filter((group) => !group.startsWith("@"));
  assert.ok(selectorGroups.length > 10);
  for (const group of selectorGroups) {
    for (const selector of group.replace(/:is\([^)]*\)/g, ":is()").split(",")) assert.match(selector.trim(), /^body\.legacy-article(?:\b|\s|:)/);
  }
});


test("LM Studio guide publishes sourced setup guidance without retired claims", async () => {
  const html = await readFile(join(root, "blog/lm-studio-bionic-guide-2026.html"), "utf8");
  const title = "LM Studio Bionic 入門教學：本地、雲端模型與第一個專案";
  assert.ok(html.includes(`<title>${title}</title>`));
  assert.ok(html.includes(`<meta property="og:title" content="${title}">`));
  assert.ok(html.includes(`<h1>${title}</h1>`));
  assert.match(html, /<link rel="canonical" href="https:\/\/autodev-ai\.com\/blog\/lm-studio-bionic-guide-2026\.html">/);
  assert.match(html, /依據 LM Studio 官方文件整理，未進行產品性能實測；核對日期：2026-09-21/);
  assert.match(html, /若不啟用 <strong>Allow coding<\/strong>[^。]*不需要選擇程式碼根目錄/);

  for (const id of ["project-setup", "model-modes", "costs", "permissions-review", "fit", "faq"]) {
    assert.match(html, new RegExp(`id=["']${id}["']`));
    assert.match(html, new RegExp(`href=["']#${id}["']`));
  }
  for (const href of [
    "https://lmstudio.ai/docs/bionic", "https://lmstudio.ai/docs/bionic/quick-start",
    "https://lmstudio.ai/docs/bionic/models", "https://lmstudio.ai/pricing",
  ]) assert.ok(html.includes(`href="${href}"`), `missing official source: ${href}`);

  const blocks = jsonLdBlocks(html);
  const article = blocks.find((block) => block["@type"] === "Article");
  assert.equal(article.headline, title);
  assert.equal(article.datePublished, "2026-07-21");
  assert.equal(article.dateModified, "2026-09-21");
  assert.equal(article.author.name, "AutoDev AI");
  assert.ok(!blocks.some((block) => block["@type"] === "FAQPage"));
  const visibleText = html.replace(/<style[\s\S]*?<\/style>/gi, "").replace(/<script[\s\S]*?<\/script>/gi, "").replace(/<[^>]+>/g, " ");
  for (const retired of ["完整教學", "最佳方案", "最大版本更新", "媲美 Cursor", "媲美 GPT-4o", "完全免費", "完全離線", "完全不用擔心資料外洩", "100%", "0 元", "200+", "Win/Mac/Linux", "約 12 分鐘", "哪些舊說法應替換", "編輯註記"]) {
    assert.ok(!visibleText.includes(retired), `retired claim remains: ${retired}`);
  }
  for (const retiredDomain of ["afflink.one", "m.do.co", "gumroad.com"]) assert.ok(!html.includes(retiredDomain));
  assert.match(html, /href="\/services\.html"/);
  assert.match(html, /href="https:\/\/chat\.autodev-ai\.com\/form"/);
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
    const tableRegion = html.match(/<div\b[^>]*class=["'][^"']*\btable-scroll\b[^"']*["'][^>]*>/i)?.[0] ?? "";
    assert.match(tableRegion, /tabindex=["']0["']/i);
    assert.match(tableRegion, /role=["']region["']/i);
    assert.ok(tableRegion.includes(`aria-label="${page.tableLabel}"`));
    assert.match(html, /<div\b[^>]*class=["'][^"']*\btable-scroll\b[^"']*["'][^>]*>\s*<table class="price-table">/i);
    for (const kind of ["og:image", "twitter:image"]) {
      const key = kind === "og:image" ? "property" : "name";
      const tag = [...html.matchAll(/<meta\b[^>]*>/gi)].map((match) => match[0])
        .find((candidate) => candidate.includes(`${key}="${kind}"`)) ?? "";
      assert.match(tag, /content=["']https:\/\/autodev-ai\.com\/autodev-logo2\.png["']/);
    }

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
