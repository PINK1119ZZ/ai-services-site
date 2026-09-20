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
