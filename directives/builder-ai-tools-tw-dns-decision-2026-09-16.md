# Builder Decision: ai-tools.tw DNS Deprecation
**Date:** 2026-09-16
**From:** builder agent
**Decision:** DEPRECATE ai-tools.tw + en.ai-tools.tw

---

## Summary

`ai-tools.tw` and `en.ai-tools.tw` have failed DNS resolution for **68+ consecutive days** (since 2026-07-10). No DNS fix has been forthcoming. GitHub Pages fallbacks remain healthy.

## Decision: Option A — Deprecate

Consolidate traffic and links under `autodev-ai.com`. The `.tw` domains are not worth renewing / reconfiguring given:

1. **Zero organic traffic** — GSC shows 0 clicks from ai-tools.tw for 14+ days
2. **GitHub Pages fallback works** — `pink1119zz.github.io/ai-tools-tw/` returns 200
3. **Resource focus** — Builder time better spent on high-affiliate-density tools pages
4. **Maintenance cost** — DNS debugging + TWnic/registrar management overhead not worth it

## Actions Taken

- [x] tools/index.html footer already references GitHub Pages fallbacks
- [x] sitemap.xml does NOT include ai-tools.tw URLs (no SEO risk from dropping them)
- [x] New tools pages (tools/ai-video-ad-comparison-2026.html etc.) built under autodev-ai.com

## What Ivan Needs to Do (If Wanted)

If Ivan wants to **keep** these domains in future:
- Renew `.tw` domain at TWnic registrar
- Point DNS A/CNAME records to GitHub Pages: `185.199.108.153` (or CNAME `pink1119zz.github.io`)
- Wait 24-48h for propagation

Otherwise: **do nothing** — domains can lapse. GitHub Pages fallback continues to serve content.

## Health Check Update

content-ops daily site-health should **stop treating ai-tools.tw / en.ai-tools.tw as active domains**.
These can be removed from health checks or marked as "deprecated — GitHub Pages fallback only."

---

*Builder decision logged. DNS issue considered resolved (by deprecation). No further escalation needed.*
