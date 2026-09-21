# SEO reference repair evidence

## Input snapshot and scope

- Baseline `HEAD`: `2e3fd2b2fa07d52c438834ed2574abd165d7767d`.
- Scope: repair seven high-confidence references in two AI model pages, two blog pages, and three pages with obsolete `/nav.js` references; add one focused SEO regression test.
- Explicit exclusions: no changes to CSS, the shared navigation helper, prices, Contact/FormSubmit, article body copy, deployment, Git state, browser state, or production.

## Acceptance criteria

1. Both Kira links to `#editorial-series` resolve to real sections without changing section content.
2. Remove only the stylesheet reference on the OpenAI government-stake article whose layout is already defined by its inline stylesheet.
3. Remove only the obsolete `/script.js` reference on the GEO comparison article while retaining its existing inline mobile navigation handler and `/lang.js`.
4. The prompt-pack article and both calculators use the existing `/assets/autodev-v2.js` helper with its required `data-*` and ARIA contract; `/nav.js` is no longer referenced.
5. Preserve all 208 original HTML paths, pass SEO/static tests, and reduce a fresh static build from 23 to 16 source-existing warnings.

## Red-green evidence

- Red: `npm run test:seo` after adding the focused contract produced 5 passes and 1 failure: `missing section#editorial-series`. Existing path, JSON-LD, link, and pricing checks stayed green.
- Green: `npm run test:seo` produced 6/6 passes. Its first test counted exactly 208 HTML documents and parsed every JSON-LD block.
- Static unit suite: `npm run test:static` produced 8/8 passes.
- Fresh build: `python3 scripts/build_static.py --output /private/tmp/autodev-static-reference-repair-20260921` built 254 files with 16 source-existing warnings.
- Manifest classification: 9 `source-existing-anchor` warnings, all on `blog/lm-studio-bionic-guide-2026.html`; 7 `source-existing-missing` warnings, all for `styles.css` on the seven known articles. No repaired reference remains in the warning set.
- `git diff --check` passed.

## Implemented repairs

- `ai-model.html`: assigned `id="editorial-series"` to the existing `.editorial-series` section.
- `en/ai-model.html`: assigned the same anchor to the existing `.scenes-section` section.
- `blog/openai-government-stake-ai-nationalization-2026.html`: removed the missing `../styles.css` link; retained its complete inline stylesheet.
- `blog/best-geo-tools-comparison-2026.html`: removed the missing `/script.js` load; retained `/lang.js` and the existing inline `mobileMenuBtn`/`navLinks` handler.
- `blog/claude-code-prompt-pack-guide-2026.html`, `tools/ai-coding-cost-calculator.html`, and `tools/ai-subscription-calculator.html`: added `data-nav-links`, `data-nav-toggle`, `aria-controls`, initial `aria-expanded`, and open/close labels, then replaced `/nav.js` with the existing deferred `/assets/autodev-v2.js` helper.

## Remaining-warning history audit

### LM Studio article

- Read-only `git log --all --follow` found five reachable versions of `blog/lm-studio-bionic-guide-2026.html`: `40d2c12`, `c9d3324`, `026cc43`, `1b76954`, and `9613732`.
- Read-only `git show <commit>:<path>` inspection found none of the nine TOC target IDs in any version. The first version (`40d2c12`) ends after the TOC block; later versions add surrounding/CTA markup but never add the nine article sections.
- Across those versions, the only headings are the title, TOC label, and later CTA headings. There is no recoverable tracked body for `what-is-bionic`, `key-features`, `code-projects`, `work-projects`, `voxtral`, `vs-cursor`, `hardware`, `install`, or `faq`.
- No content was restored or invented.

### Missing `styles.css`

- `git log --all -- styles.css` and `git log --all -- ':(glob)**/styles.css'` returned no commits: a file named `styles.css` has never been tracked on the reachable refs inspected. The repository history does contain the distinct root file `style.css`.
- Six affected articles referenced `../styles.css` in their first tracked version: Agent Skills (`d1e7c4d`), AgentMemory (`6e76ad0`), Claude Video (`839f8af`), GEO Blym (`bddf4f2`), OfficeCLI (`7c03890`), and TencentDB Agent Memory (`48cf47c`).
- Warp Terminal first appears at `41d27cc` without that reference; `../styles.css` first appears at `3725ec3` one day later.
- Because history provides no matching stylesheet and prior inspection found that root `style.css` does not implement these article templates' class suites, no automatic substitution or empty compatibility file was created.

## Unresolved items

- The 9 LM Studio anchors require real article content or deliberate TOC removal; repository history cannot supply the missing body.
- The 7 article stylesheet warnings require a separately approved design decision: implement the required template rules or migrate each article to a proven existing template.
- No browser visual check was performed because the browser remains user-controlled for this slice.


## Legacy article readability repair

### Input snapshot and acceptance

- Baseline `HEAD`: `23c9e10ef68d0809a5754296c699954939cc968a`.
- Seven named legacy articles must reference one real stylesheet and opt into a page-specific body namespace; no other HTML page may load the asset.
- Every stylesheet selector must remain under `body.legacy-article`; the implementation must cover the articles' existing nav, content, code, table, media, card, CTA, and footer structures without changing article facts or links.
- The LM Studio article must lose only the TOC that points to nine absent sections. Its remaining bytes are protected by a pre-change SHA-256 snapshot after subtracting that TOC.
- Browser, network, production, global styles, helpers, Contact, and deployment remain outside this slice.

### Red-green and static evidence

- Red: the new SEO contract produced 6 passes and 1 failure because zero pages referenced `assets/legacy-article.css`; all prior SEO checks stayed green.
- Green: `npm run test:seo` produced 7/7 passes. The suite confirmed exactly 208 HTML paths, exact use by the seven named pages, their body namespace and asset replacement, stylesheet selector scoping, removal of the LM TOC, and the preserved-file hash `138995edc2767802ae10c07c8928023606fc275b558bb8c7bc40c81e57132450`.
- `npm run test:static` produced 8/8 passes.
- Fresh build: `python3 scripts/build_static.py --output /private/tmp/autodev-static-legacy-article-repair-20260921` built 255 files with 0 source-existing warnings. Its manifest contains 255 file records, including `assets/legacy-article.css`, and an empty warning list.
- `git diff --check` passed.

### Implemented behavior

- Added a 123-line, dependency-free `assets/legacy-article.css`. It uses the existing warm neutral palette direction and system Traditional Chinese font fallbacks, caps the reading column near 800px, keeps nav links visible and wrapping, and constrains code, tables, grids, media, CTA blocks, and footer content.
- Added explicit keyboard focus treatment and a `prefers-reduced-motion` override. No animations, fonts, JavaScript, images, packages, or global selectors were introduced.
- Replaced the missing `../styles.css` reference with `../assets/legacy-article.css` and added `class="legacy-article"` on exactly the seven contracted pages.
- Removed the LM Studio TOC block containing the nine dead anchors. No replacement body was invented; the title, metadata, introduction, stat cards, CTA, outbound links, and all other file bytes remain unchanged.

### Remaining limitations

- The LM Studio article still lacks the substantive body promised by its title and metadata. Warning removal means its dead navigation is gone; it does not mean the content is complete. A rewrite requires current official sources and separate approval for network research.
- Browser control remained with the user. Seven-page desktop/mobile layout, contrast, focus appearance, full-page horizontal overflow, and Lighthouse behavior have not been visually verified and are not claimed as passed.

主控独立验收：SEO7/7、static8/8通过。对CSS做4行局部修正：移除body全页overflow裁切以避免隐藏实际溢出；焦点使用更深的accent，CTA与按钮明确前景/背景。视觉/手机实际验收仍未执行，上述旧hash仅对应agent初稿。


## LM Studio sourced content repair

### Input snapshot and boundaries

- Baseline `HEAD`: `1cfe13a37847e19076f444f4daded400203c25fb`.
- The implementation follows `LM_STUDIO_IMPLEMENTATION_CONTRACT.md` and the locally supplied `LM_STUDIO_CONTENT_CANDIDATE.md`, whose four official sources were verified by the controller on 2026-09-21. This slice did not browse or independently re-fetch them.
- Scope is limited to the existing LM Studio URL, its focused SEO regression, and this evidence file. The canonical URL, Open Graph URL, original publication date, and Organization author remain unchanged.
- The previous byte-preservation assertion was intentionally retired because this contract authorizes a factual body rewrite. Unrelated legacy-article style coverage remains intact.

### Red-green and build evidence

- Red: `npm run test:seo` produced 7 passes and 1 failure at the new LM Studio test because the old title remained and the promised sections did not exist. All unrelated checks stayed green.
- Green: `npm run test:seo` produced 8/8 passes. It retained exactly 208 HTML paths and valid JSON-LD, then verified title/schema synchronization, canonical URL, original publication date, updated date, Organization author, six real sections and matching TOC links, four official source links, the non-performance-test disclosure, the no-coding-directory Quick Start nuance, removal of retired claims, and replacement of unrelated affiliate CTAs.
- `npm run test:static` produced 8/8 passes.
- Fresh build: `python3 scripts/build_static.py --output /private/tmp/autodev-static-lm-studio-content-20260921` built 255 files with 0 source-existing warnings.
- `git diff --check` passed. The generated Python test cache was removed, leaving only the three contracted files changed.

### Local candidate behavior

- Synchronized the document title, H1, Open Graph title, and Article headline to `LM Studio Bionic 入門教學：本地、雲端模型與第一個專案`.
- Replaced the descriptions with an accurate overview of Project setup, Local/Cloud/Remote models, costs, Allow coding permissions, and manual review. `dateModified` and the visible update date are `2026-09-21`; `datePublished` remains `2026-07-21`.
- Added a normal reader-facing disclosure that the article is based on official documents and is not a product performance test, with a `2026-09-21` verification date.
- Added practical sections for first Project setup, model modes, cost boundaries, permissions/review, fit, and three reader FAQs. The Quick Start text explicitly says a code root is not required when Allow coding is disabled.
- Linked the official Bionic overview, Quick Start, model modes, and pricing pages near the relevant guidance. No FAQ schema was added.
- Removed unsupported superlatives, platform/model-count guarantees, zero-cost/offline/risk-free claims, the stale reading-time claim, and the DataCamp, DigitalOcean, and Gumroad CTAs.
- Replaced those CTAs with one related workflow block linking to `/services.html` and the verified `https://chat.autodev-ai.com/form` entry point.

### Remaining limitations

- The article is an official-document-based introduction, not an AutoDev hands-on test, benchmark, or customer case. Interface, model availability, plans, and billing can change; readers are directed to current official pages.
- Browser and Lighthouse checks were not run because browser control remains with the user. No visual, responsive, contrast, or runtime claim is made for this slice.

主控独立验收（2026-09-21）：完整3文件diff复核，SEO8/8、static8/8通过；新制品255文件、0warnings，gitleaks扫描约19.26MB无命中。浏览器与两Contact依赖仍未解除；此候选未公开。

## Legacy cost article and Bot scope repair — 2026-09-21

### Input snapshot and acceptance

- Baseline `HEAD`: `a46a47994ad4e2f60e500f76b82cfbc69f139b48`.
- Scope follows `LEGACY_REVIEW_REPAIR_CONTRACT.md`: the two LINE Bot cost articles, scoped legacy CSS, existing calculator URL, focused SEO/DOM behavior tests, package test entry, and this evidence section.
- The calculator keeps its canonical URL, GA4, navigation, language helper, Contact route, and Bot Cloud entry. It does not introduce a pricing, financial-estimate, storage, submission, or backend service.

### Red-green evidence

- RED `npm test`: 14/17 passed. All three new Bot-scope tests failed because the old page had no behavior script, no agreed budget guidance, and still exposed pseudo-cost content.
- RED `npm run test:seo`: 6/8 passed. Both cost-article checks failed because their horizontal table wrappers were not keyboard-focusable regions.
- GREEN `npm test`: 17/17 passed. The `node:vm` DOM fixture verifies default Telegram selection, feature and channel changes, clearing all features, text-only list rendering, zero fake network calls, and absence of cost attributes/retired affiliate claims.
- GREEN `npm run test:seo`: 8/8 passed, including all 208 original HTML paths, JSON-LD parsing, exact shared image metadata, and bilingual table-region labels.
- `npm run test:static`: 8/8 passed. `git diff --check` passed.

### Implemented behavior

- Chinese cost article social images now use the existing `autodev-logo2.png`; the old SVG and URL remain untouched. Both language articles expose their existing horizontally scrolling comparison table as `tabindex="0"`, `role="region"`, with a language-matched accessible name.
- The legacy article accent is `#8a5830`, which computes to 5.436:1 against `#f7f4ee`. The scoped navigation list now resets bullets and left padding. No layout, global selector, or `!important` rule was added.
- The existing calculator URL is now a local Bot requirements and budget preparation tool. Telegram is the default channel, with LINE and Messenger alternatives. It retains all 12 functional topics in concise form and displays only the selected channel, selected feature names, and count.
- The page never derives a price from feature count. It presents NT$50,000 / NT$100,000 / NT$200,000+ only as project-scale positioning and states that final scope determines the quote.
- Its new inline behavior uses `textContent` and created list nodes, with no `innerHTML`, `fetch`, storage, dependency, prefilled customer message, or submitted data. The old unsupported market median, NT$8,000 entry claim, fixed maintenance inclusions, pseudo totals/comparisons, and two price/return affiliate promotions were removed.

### Remaining limitations

- No browser, real keyboard, assistive-technology, Lighthouse, real network, form, provider, or production test ran in this slice. A focusable labelled region is source- and contract-tested; actual scrolling behavior is not claimed as manually verified.
- Static contrast was calculated from declared colors and is not a browser computed-style result.
- The main controller owns the fresh allowlisted build, independent review, Git, deployment, and publication decisions. Nothing was published.

Main acceptance: independently read the complete change and ran 17/17 Node, SEO 8/8, and static 8/8. Corrected the test's network counter to retain a live reference across interactions. Scoped tool text/control colors now use the existing dark text/background tokens rather than pale legacy gold on the light page. Browser/AT remain unverified; no external requests or publication.

## Bilingual Bot requirements tool and entry-point repair — 2026-09-21

### Input snapshot and acceptance

- Baseline `HEAD`: `015d992f3a48bc8c771fbe8456ce7d4c49e16f47`.
- Scope follows the final section of `LEGACY_REVIEW_REPAIR_CONTRACT.md`: pair the existing English tool with the accepted Chinese requirements checklist, correct both directory cards and the Chinese cost-article CTA, add the missing Chinese-to-English hreflang, and extend the existing public behavior test.
- The seven-file allowlist and zero-dependency limit were kept. The five implementation HTML files add 53 lines in the diff, below the 100-line implementation budget.

### Red-green evidence

- RED `npm test`: 14/18 passed and 4 failed. The failures directly identified the absent English `bot-scope-script`, missing English NT$ budget positioning, and stale calculator/instant-estimate wording in the entry cards and article CTA.
- GREEN `npm test`: 18/18 passed. The shared `node:vm` DOM fixture now verifies both languages: Telegram defaults, 12 feature choices, channel change, clear-all, text-only output, exact local routes, paired hreflang, and a live zero-network-call counter.
- `npm run test:seo`: 8/8 passed, including retention of all 208 original HTML paths and parseable JSON-LD.
- `npm run test:static`: 8/8 passed. `git diff --check` passed.

### Implemented behavior

- Replaced the English fixed-price calculator with the same local Bot requirements workflow as the Chinese page. It defaults to Telegram, offers LINE and Messenger, preserves 12 English feature topics, and presents NT$50,000 / NT$100,000 / NT$200,000+ only as project-scale positions.
- Preserved the English canonical URL, complete hreflang set, GA4 loader/config, navigation, menu helper, language helper, footer, Bot Cloud entry, and language-matched Contact route `/en/contact.html?from=calculator`.
- Removed the page's unsupported USD price arithmetic, automatic estimate, Taiwan-market claim, monthly totals, and Free 30-Min promise. The replacement uses created list nodes and `textContent`; it has no network, storage, submission, or dependency.
- Added the missing English alternate URL to the Chinese tool. Updated only the two directory cards and the Chinese article's tool CTA to describe requirements, scope, and budget preparation without instant-price claims.
- Reused the controller's readable dark tokens and 44px minimum interactive control height. The public test retains the controller's mutable `networkCalls` object so post-interaction calls remain observable.

### Remaining limitations

- Browser, real keyboard, assistive-technology, Lighthouse, real network, form, and production checks did not run. No visual or AT result is claimed.
- This slice did not create the fresh allowlisted build; the main controller owns that build, independent review, Git, deployment, and publication decisions. Nothing was published.

Controller integration: preserved the original English tool CTA analytics event and the existing 50% claim regression check. Independently passed 18/18 Node, 8/8 SEO and 10/10 static after the fragment-anchor repair, then built 255 files with 0 warnings and scanned 19,253,118 bytes with 0 findings. The four social/icon assets are present in the artifact; shared chat/v2 scripts contain no removed Ads-helper caller. Current browser/AT remain unverified.

Metadata-test follow-up: a reviewer identified that a quoted attribute containing an apostrophe was truncated by tagAttr. Main reproduced the failure (AutoDev instead of the complete value), changed only the quote-delimited capture, and independently passed all 19 Node tests. Both mixed-quote cases now pass; page/build inputs did not change, so the previous 255-file artifact remains the same candidate bytes.
