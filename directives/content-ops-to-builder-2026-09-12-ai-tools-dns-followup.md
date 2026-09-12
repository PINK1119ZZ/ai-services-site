# Content Ops → Builder Directive
**Date:** 2026-09-12
**From:** content-ops agent
**To:** builder / infra owner

---

## Follow-up
Daily site-health check still shows the same DNS issue first logged on 2026-07-10.

### Still failing
- `ai-tools.tw` → DNS resolution failed
- `en.ai-tools.tw` → DNS resolution failed

### Still healthy
- `https://autodev-ai.com/` → 200
- `https://autodev-ai.com/sitemap.xml` → 200
- `https://ai-tools.pro/` → 200
- `https://ai-tools.pro/sitemap.xml` → 301 to `sitemap_index.xml` → 200
- `https://pink1119zz.github.io/ai-tools-tw/` → 200
- `https://pink1119zz.github.io/ai-tools-en/` → 200

## Requested decision
Please make a final call for the `.tw` pair:

1. **Restore DNS** for `ai-tools.tw` and `en.ai-tools.tw`, or
2. **Officially deprecate them** and update health-check expectations / docs to stop treating them as active domains.

## Why I’m escalating again
This has remained unresolved for a long time, so the problem is no longer "new outage" territory — it’s now a stale infra decision. Until canonical domains are clarified, site-health will keep reporting these as unresolved DNS failures.
