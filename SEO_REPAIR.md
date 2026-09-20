# SEO repair evidence

Date: 2026-09-21 (Asia/Taipei)

## Input snapshot and scope

- Candidate HEAD before this slice: `c49812a20bf6a337ecccfe6baf2276d64dfad376`.
- The source tree contained 208 HTML documents before the repair and still contains 208 after it.
- The worker did not locate the Phase0 link inventory in its searched directories and used a fresh local scan of all 208 HTML files. The main controller subsequently located the original inventory in the separate phase0 audit directory and compared its 17 link records; the candidate preserves existing URLs and fixes confirmed broken destinations.
- Contact pages, FormSubmit, the static builder, global `style.css`, production, and deployment were not changed. No dependency was added.

## Red signals

- The pre-change all-HTML parser found exactly five JSON-LD failures: `blog/ai-customer-service-line.html`, `blog/ai-tools-comparison-2026.html`, `blog/how-to-write-ai-prompts.html`, `blog/line-bot-cost.html`, and `blog/n8n-hitl-tutorial-2026.html`.
- The first `npm run test:seo` run had 1 pass and 4 failures: the five JSON-LD errors, known broken article links, and both stale LINE Bot cost pages.
- The first static artifact after those fixes exposed additional same-class relative links. The expanded regression test then had 3 passes and 2 failures for relative `../blog.html` navigation and remaining missing article targets before the second repair.

## Repairs

- Removed injected HTML anchors from the five broken breadcrumb names and kept the original plain-text meaning. Every JSON-LD block now parses.
- Replaced `/blog.html`-class navigation with `/blog/` in the two affected articles.
- Repointed only two semantically equivalent missing articles, updating visible labels with the href:
  - the missing CapCut/Runway/Premiere comparison now points to the existing AI video tools comparison;
  - the missing Claude Code vs Cursor comparison now points to the existing OpenCode vs Cursor vs Claude Code comparison.
- For missing Claude Code guide, Qwen local deployment, Scrapling, superpowers, Cursor 3, and n8n/Make/Zapier articles without an equivalent existing page, removed the link while retaining its visible text.
- Rewrote the Chinese and English LINE Bot cost pages at their existing URLs. Both describe scope-based quoting and the NT$50,000 / NT$100,000 / NT$200,000+ project budget positions as guidance rather than fixed packages or market statistics.
- Retained LINE as an offered channel and added a related link to the Telegram-first service. Removed the old low-price, speed, maintenance, refund, and savings claims.
- Synced visible FAQ text with FAQ JSON-LD, retained `datePublished` 2026-03-20, and set `dateModified` to 2026-09-21.
- Added a local `.table-scroll` wrapper for horizontal table scrolling. The page body has no fixed minimum width.
- Preserved canonical/hreflang, GA4, Google Ads loading, chat widget, language routing, navigation, and the existing page URLs.

## Verification

- `npm run test:seo`: 5 passed, 0 failed. It checks all 208 HTML paths, all JSON-LD blocks, repaired routes, both cost-page canonical/FAQ/budget contracts, retained integrations, and table containment.
- `npm run test:static`: 8 passed, 0 failed.
- Fresh allowlisted artifact build: 254 files, 23 source-existing warnings. Remaining warnings are 12 missing legacy CSS/JS resources and 11 legacy missing anchors; no missing article target or `blog.html` route remains. This is lower than the 37-warning accepted baseline.
- `npm test`: 1 passed, 2 failed. The two retained failures are the pre-existing Contact blockers: missing `/assets/autodev-v2.js` on legacy Contact and prohibited `不滿意不收費` copy. No Contact assertion was removed or weakened.

## Remaining review

- Browser/mobile visual review remains pending because browser control was outside this slice. Static markup verifies the local scroll container but does not claim viewport or Lighthouse results.
- The 23 legacy static warnings remain outside this contract. Their exact list is recorded in the generated `static-manifest.json` from the fresh local artifact check.
