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
