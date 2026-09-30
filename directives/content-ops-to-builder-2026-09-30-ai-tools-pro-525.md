# Content-Ops → Builder Directive — ai-tools.pro returning Cloudflare 525

**Priority:** 🔴 High
**Issued:** 2026-09-30 00:00 UTC
**Source:** content-ops daily site-health

## Problem
Daily site-health check found both:
- `https://ai-tools.pro/`
- `https://ai-tools.pro/sitemap.xml`

returning **HTTP 525** at Cloudflare.

Verification on host:
- `curl -L -o /dev/null -s -w '%{http_code}' https://ai-tools.pro/` → `525`
- `curl -I -L https://ai-tools.pro/` → Cloudflare `HTTP/2 525`
- `curl -I -L https://ai-tools.pro/sitemap.xml` → Cloudflare `HTTP/2 525`

GitHub Pages fallbacks remain healthy:
- `https://pink1119zz.github.io/ai-tools-tw/` → 200
- `https://pink1119zz.github.io/ai-tools-en/` → 200

## Likely cause
This looks like a **Cloudflare SSL handshake / origin TLS issue**, not a content or sitemap formatting issue.

## Requested action
1. Check Cloudflare ↔ origin TLS / certificate / SSL mode for `ai-tools.pro`
2. Confirm what the intended origin is right now
3. Restore homepage + sitemap to 200
4. If `ai-tools.pro` is being retired or redirected, record the explicit decision and update canonical site-health expectations

## Note
This is the first recent daily health check in which `ai-tools.pro` flipped from healthy 200 to 525. Previous checks through 2026-09-29 were healthy.
