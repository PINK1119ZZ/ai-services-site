# Content Ops → Builder Directive
**Date:** 2026-07-10
**From:** content-ops agent
**To:** builder / infra owner

---

## Issue
Daily site-health check found that these domains currently fail DNS resolution:

- `ai-tools.tw`
- `en.ai-tools.tw`

`curl` returns `Could not resolve host` / HTTP `000`.

Meanwhile these endpoints are healthy:

- `https://autodev-ai.com/` → 200
- `https://autodev-ai.com/sitemap.xml` → 200
- `https://ai-tools.pro/` → 200
- `https://ai-tools.pro/sitemap.xml` → 200 (redirected to `sitemap_index.xml`)

Repo references suggest the active published URLs for the AI Tools sites may still be GitHub Pages:

- `https://pink1119zz.github.io/ai-tools-tw/`
- `https://pink1119zz.github.io/ai-tools-en/`

## Requested action
1. Confirm intended canonical domains for AI Tools TW / EN.
2. If `ai-tools.tw` and `en.ai-tools.tw` should be live, restore DNS records.
3. If they are deprecated, remove them from health-check expectations and keep `ai-tools.pro` / GitHub Pages as canonical.
4. If redirects are intended, set proper 301 redirects and update internal docs/config/scripts.

## Why this matters
Current DNS failure makes the domains appear down during automated health checks and could also hurt user trust / SEO if those domains are still linked anywhere externally.
