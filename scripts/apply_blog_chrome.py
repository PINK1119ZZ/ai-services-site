#!/usr/bin/env python3
"""Deterministic, idempotent AutoDev 2.0 chrome (nav + footer) applier for blog articles.

Replaces the legacy site navigation and legacy site footer of each blog article
with the unified v2 chrome (assets/v2-chrome.css + a fixed header/footer markup),
while leaving article content, head metadata, embedded <style>/<script>, and any
content-only navigation (table of contents, breadcrumb, series/related-article
lists) untouched.

Usage:
    python3 scripts/apply_blog_chrome.py [file ...]
    python3 scripts/apply_blog_chrome.py --verify [file ...]

With no file arguments, operates on every ``blog/*.html`` and ``en/blog/*.html``
file except the two hub pages (``blog/index.html`` and ``en/blog/index.html``).

The script only ever touches:
  - the legacy site <nav> (and its wrapping <header> when that header holds
    nothing but the logo/nav);
  - the legacy site <footer>: a plain one (just copyright + site links) is
    deleted outright; one that also carries disclosure-worthy prose (an
    affiliate/commission disclosure, or other article-specific attribution)
    is replaced in place by a <!-- v2-chrome:disclosure --> aside that keeps
    that sentence verbatim (see extract_disclosure_text());
  - one <link rel="stylesheet" href="/assets/v2-chrome.css"> line before </head>;
  - one <script defer src="/assets/autodev-v2.js"></script> line before </body>
    when that script is not already referenced anywhere in the document.

Everything else -- title, meta, canonical, hreflang, JSON-LD, analytics tags,
article body, inline <style>/<script>, whitespace -- is preserved byte for byte.
"""
from __future__ import annotations

import html as html_entities
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

MARK_HEADER_START = "<!-- v2-chrome:header -->"
MARK_HEADER_END = "<!-- /v2-chrome:header -->"
MARK_FOOTER_START = "<!-- v2-chrome:footer -->"
MARK_FOOTER_END = "<!-- /v2-chrome:footer -->"
MARK_DISCLOSURE_START = "<!-- v2-chrome:disclosure -->"
MARK_DISCLOSURE_END = "<!-- /v2-chrome:disclosure -->"

CSS_LINK_TAG = '<link rel="stylesheet" href="/assets/v2-chrome.css">'
JS_SCRIPT_TAG = '<script defer src="/assets/autodev-v2.js"></script>'
JS_REFERENCE_NEEDLE = "/assets/autodev-v2.js"

ZH_NAV_MARKUP = (
    '<header class="v2c-header" id="nav"><div class="v2c-inner">'
    '<a class="v2c-logo" href="/">AutoDev <span>Systems Studio</span></a>'
    '<div class="v2c-links" id="navLinks" data-nav-links>'
    '<a href="/services.html">服務</a>'
    '<a href="/portfolio.html">案例</a>'
    '<a href="/blog/" aria-current="page">洞察</a>'
    '<a href="/about.html">關於</a>'
    '<a href="/contact.html">聯絡</a>'
    '<a class="v2c-cta" href="/contact.html" data-analytics="nav_contact">需求諮詢</a>'
    '</div>'
    '<button class="v2c-toggle" type="button" data-nav-toggle '
    'aria-controls="navLinks" aria-expanded="false" aria-label="開啟選單" '
    'data-open-label="開啟選單" data-close-label="關閉選單">☰</button>'
    '<button class="v2c-legacy-hook" id="mobileMenuBtn" type="button" hidden aria-hidden="true" tabindex="-1"></button>'
    '</div></header>'
)

EN_NAV_MARKUP = (
    '<header class="v2c-header" id="nav"><div class="v2c-inner">'
    '<a class="v2c-logo" href="/en/">AutoDev <span>Systems Studio</span></a>'
    '<div class="v2c-links" id="navLinks" data-nav-links>'
    '<a href="/en/services.html">Services</a>'
    '<a href="/en/portfolio.html">Work</a>'
    '<a href="/en/blog/" aria-current="page">Insights</a>'
    '<a href="/en/about.html">About</a>'
    '<a href="/en/contact.html">Contact</a>'
    '<a class="v2c-cta" href="/en/contact.html" data-analytics="nav_contact">Discuss a project</a>'
    '</div>'
    '<button class="v2c-toggle" type="button" data-nav-toggle '
    'aria-controls="navLinks" aria-expanded="false" aria-label="Open menu" '
    'data-open-label="Open menu" data-close-label="Close menu">☰</button>'
    '<button class="v2c-legacy-hook" id="mobileMenuBtn" type="button" hidden aria-hidden="true" tabindex="-1"></button>'
    '</div></header>'
)

ZH_FOOTER_MARKUP = (
    '<footer class="v2c-footer"><div class="v2c-inner"><div class="v2c-footer-grid">'
    '<div><h2>AutoDev</h2><p>企業自動化與數位系統工作室。以 Telegram Bot 為核心，'
    '把複雜工作整理成簡單流程。</p></div>'
    '<div><h3>Studio</h3>'
    '<a href="/services.html">服務</a>'
    '<a href="/portfolio.html">案例</a>'
    '<a href="/pricing.html">專案範圍</a>'
    '<a href="/contact.html">需求諮詢</a></div>'
    '<div><h3>Labs & Tools</h3>'
    '<a href="/bot-cloud.html">Bot Cloud</a>'
    '<a href="/ai-model.html">AI 模特</a>'
    '<a href="/line-bot-saas.html">LINE Bot SaaS</a>'
    '<a href="/tools/">工具</a>'
    '<a href="/demo.html">Demo</a></div>'
    '<div><h3>更多</h3>'
    '<a href="https://chat.autodev-ai.com/form">原有表單</a>'
    '<a href="/blog/">洞察</a>'
    '<a href="https://liff.line.me/2009694545-LJmZCiEX">原有 LIFF 諮詢</a>'
    '<a href="https://pink1119zz.github.io/ai-tools-tw/">AI Tools TW</a>'
    '<a href="https://pink1119zz.github.io/ai-tools-en/">AI Tools EN</a></div>'
    '</div><div class="v2c-footer-bottom"><span>© AutoDev</span>'
    '<span><a href="/privacy.html">隱私權</a> · <a href="/terms.html">使用條款</a> · '
    '<a href="/disclaimer.html">免責聲明</a></span></div></div></footer>'
)

EN_FOOTER_MARKUP = (
    '<footer class="v2c-footer"><div class="v2c-inner"><div class="v2c-footer-grid">'
    '<div><h2>AutoDev</h2><p>Automation & Digital Systems Studio. Telegram-first '
    'systems that turn complex work into clear workflows.</p></div>'
    '<div><h3>Studio</h3>'
    '<a href="/en/services.html">Services</a>'
    '<a href="/en/portfolio.html">Work</a>'
    '<a href="/en/pricing.html">Project scope</a>'
    '<a href="/en/contact.html">Discuss a project</a></div>'
    '<div><h3>Labs & Tools</h3>'
    '<a href="/en/bot-cloud.html">Bot Cloud</a>'
    '<a href="/en/ai-model.html">AI Model</a>'
    '<a href="/line-bot-saas.html">LINE Bot SaaS</a>'
    '<a href="/en/tools/">Tools</a>'
    '<a href="/en/demo.html">Demo</a></div>'
    '<div><h3>More</h3>'
    '<a href="https://chat.autodev-ai.com/form">Existing form</a>'
    '<a href="/en/blog/">Insights</a>'
    '<a href="https://liff.line.me/2009694545-LJmZCiEX">Existing LIFF enquiry</a>'
    '<a href="https://pink1119zz.github.io/ai-tools-tw/">AI Tools TW</a>'
    '<a href="https://pink1119zz.github.io/ai-tools-en/">AI Tools EN</a></div>'
    '</div><div class="v2c-footer-bottom"><span>© AutoDev</span>'
    '<span><a href="/en/privacy.html">Privacy</a> · <a href="/en/terms.html">Terms</a> · '
    '<a href="/en/disclaimer.html">Disclaimer</a></span></div></div></footer>'
)

# ---------------------------------------------------------------------------
# Generic balanced-tag scanning
# ---------------------------------------------------------------------------


def find_balanced(html: str, tag: str, start: int = 0):
    """Return a list of (tag_start, tag_end, inner_start, inner_end) spans for
    every top-level (non-overlapping) <tag>...</tag> region found from `start`
    onward, correctly skipping over any same-named nested tags."""
    open_re = re.compile(r"<" + tag + r"(\s[^>]*)?>", re.I)
    close_re = re.compile(r"</" + tag + r"\s*>", re.I)
    spans = []
    pos = start
    while True:
        m = open_re.search(html, pos)
        if not m:
            break
        depth = 1
        scan_pos = m.end()
        while depth > 0:
            nm = open_re.search(html, scan_pos)
            cm = close_re.search(html, scan_pos)
            if not cm:
                depth = -1
                break
            if nm and nm.start() < cm.start():
                depth += 1
                scan_pos = nm.end()
            else:
                depth -= 1
                scan_pos = cm.end()
        if depth == 0:
            spans.append((m.start(), scan_pos, m.end(), cm.start()))
            pos = scan_pos
        else:
            # Unbalanced; skip this open tag and keep scanning.
            pos = m.end()
    return spans


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html)


# ---------------------------------------------------------------------------
# Site-route recognition (for classifying legacy <nav>/<footer> as site chrome)
# ---------------------------------------------------------------------------

KNOWN_PAGES = {
    "about.html", "services.html", "pricing.html", "contact.html",
    "portfolio.html", "demo.html", "bot-cloud.html", "ai-model.html",
    "line-bot-saas.html", "privacy.html", "terms.html", "disclaimer.html",
}


def route_key(href: str):
    """Normalize an href to a canonical site-route key, or None if it does not
    resolve to a recognized top-level site route (home, a known root page, or
    a bare section index such as /blog/, /tools/, /en/)."""
    if not href:
        return None
    href = href.split("#")[0].split("?")[0]
    if href.lower().startswith(("http://", "https://")):
        m = re.match(r"https?://(?:www\.)?autodev-ai\.com(/.*)?$", href, re.I)
        if not m:
            return None
        href = m.group(1) or "/"
    stripped = re.sub(r"^(\.\./|\./)+", "", href).lstrip("/")
    lang = ""
    if stripped.startswith("en/"):
        lang = "en/"
        stripped = stripped[3:]
    if stripped in ("", "index.html"):
        return lang + "home"
    if stripped in KNOWN_PAGES:
        return lang + stripped
    if stripped in ("blog/", "blog/index.html"):
        return lang + "blog"
    if stripped in ("tools/", "tools/index.html"):
        return lang + "tools"
    return None


TOC_BREADCRUMB_RE = re.compile(r"toc|breadcrumb|目錄", re.I)
LOGO_CLASS_RE = re.compile(r"\b(nav-logo|logo)\b", re.I)

# Keywords that mark a legacy site-footer sentence as "disclosure-worthy"
# content that must be preserved rather than silently deleted with the rest
# of the footer shell. The first five are the affiliate/commission-marketing
# disclosure terms; the rest catch other article-specific attribution prose
# (e.g. an open-source license note) that a plain "site footer" signature
# (copyright + nav links) would otherwise sweep away.
DISCLOSURE_KEYWORDS_RE = re.compile(
    r"聯盟|联盟|affiliate|佣金|commission"
    r"|本文|本站文章|本站含|this article|this post|this guide",
    re.I,
)


def tag_attr(tagtext: str, name: str):
    m = re.search(name + r"=[\"']([^\"']*)[\"']", tagtext, re.I)
    return m.group(1) if m else ""


def classify_nav(inner: str, tagtext: str):
    """Return 'toc_breadcrumb', 'site_nav', or 'content' for a <nav> block
    found outside <article> and outside any <footer>."""
    cls = tag_attr(tagtext, "class")
    aria = tag_attr(tagtext, "aria-label")
    if TOC_BREADCRUMB_RE.search(cls) or TOC_BREADCRUMB_RE.search(aria):
        return "toc_breadcrumb"
    has_logo = False
    for a in re.findall(r"<a\b[^>]*>", inner, re.I):
        if LOGO_CLASS_RE.search(tag_attr(a, "class")):
            has_logo = True
            break
    hrefs = re.findall(r"href=[\"']([^\"']*)[\"']", inner, re.I)
    keys = {route_key(h) for h in hrefs if route_key(h)}
    if has_logo or len(keys) >= 2:
        return "site_nav"
    return "content"


def classify_footer(inner: str):
    """Return ('site_footer', None) | ('disclosure', matched_keywords) |
    ('none', None) for a <footer> block found outside <article>. A footer is
    only ever a candidate at all when it looks like site chrome (a copyright
    notice or a link to a known site route); among those, one that also
    carries disclosure-worthy prose is converted rather than deleted."""
    hrefs = re.findall(r"href=[\"']([^\"']*)[\"']", inner, re.I)
    has_copyright = "©" in inner or "&copy;" in inner.lower()
    has_route = any(route_key(h) for h in hrefs)
    if not (has_copyright or has_route):
        return "none", None
    text = re.sub(r"\s+", " ", strip_tags(inner)).strip()
    matched = DISCLOSURE_KEYWORDS_RE.findall(text)
    if matched:
        return "disclosure", matched
    return "site_footer", None


COPYRIGHT_LEAD_RE = re.compile(r"。|\. ")


def extract_disclosure_text(footer_inner: str) -> str:
    """Pull the disclosure-worthy sentence(s) out of a legacy footer's own
    text nodes, verbatim. Only text nodes that (after HTML-entity decoding)
    contain a disclosure keyword are kept; a kept node that itself opens with
    a copyright notice ("©"/"&copy;") has just that leading copyright
    sentence removed (up to and including the first "。" or ". "), leaving
    every other character untouched. Nodes without the keyword -- nav link
    labels, the copyright-only node, separators -- are dropped entirely.
    Multiple qualifying nodes are joined, in document order, with a single
    space."""
    pieces = re.split(r"<[^>]+>", footer_inner)
    kept = []
    for piece in pieces:
        decoded = html_entities.unescape(piece)
        if not DISCLOSURE_KEYWORDS_RE.search(decoded):
            continue
        if decoded.lstrip().startswith("©"):
            m = COPYRIGHT_LEAD_RE.search(decoded)
            remainder = decoded[m.end():] if m else decoded
        else:
            remainder = decoded
        remainder = remainder.strip()
        if remainder:
            kept.append(remainder)
    return " ".join(kept)


def html_escape_text(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


AFFILIATE_TERMS_RE = re.compile(r"聯盟|联盟|affiliate|佣金|commission", re.I)


def build_disclosure_markup(disclosure_text: str, english: bool) -> str:
    if AFFILIATE_TERMS_RE.search(disclosure_text):
        aria_label = "Affiliate disclosure" if english else "聯盟行銷揭露"
    else:
        aria_label = "Article note" if english else "文章說明"
    escaped = html_escape_text(disclosure_text)
    return (
        f'{MARK_DISCLOSURE_START}<aside class="v2c-disclosure" aria-label="{aria_label}">'
        f"<p>{escaped}</p></aside>{MARK_DISCLOSURE_END}"
    )


# ---------------------------------------------------------------------------
# Removal-span computation
# ---------------------------------------------------------------------------


class FileReport:
    def __init__(self, path: str):
        self.path = path
        self.nav_removed = False
        self.header_removed_with_nav = False
        self.footer_removed = False
        self.footer_disclosure = False
        self.disclosure_text = None
        self.no_nav_found = False
        self.no_footer_found = False
        self.duplicate_ids = []  # list of id names still found elsewhere
        self.body_padding_hint = False
        self.changed = False


def compute_removal_spans(html: str, protect_spans, english: bool):
    """Scan `html` for the legacy site <nav> (or its wrapping <header>) and the
    legacy site <footer> outside of `protect_spans` (e.g. existing v2-chrome
    marker blocks, <article> regions). Returns (removal_ops, info) where each
    removal_op is (start, end, replacement) -- replacement is "" for a plain
    deletion (nav/header/plain footer) or a <!-- v2-chrome:disclosure -->
    aside block for a footer that carries disclosure-worthy prose -- and
    info carries classification detail for reporting/verification."""

    def protected(pos):
        return any(s <= pos < e for (s, e) in protect_spans)

    article_spans = [s for s in find_balanced(html, "article") if not protected(s[0])]

    def in_article(pos):
        return any(s[0] <= pos < s[1] for s in article_spans)

    footer_spans_all = find_balanced(html, "footer")
    footer_spans = [s for s in footer_spans_all if not protected(s[0]) and not in_article(s[0])]

    def in_footer(pos):
        return any(s[0] <= pos < s[1] for s in footer_spans_all)

    nav_spans = find_balanced(html, "nav")
    header_spans = find_balanced(html, "header")

    removal_ops = []
    info = {
        "nav_removed": False,
        "header_removed_with_nav": False,
        "footer_removed": False,
        "footer_disclosure": False,
        "disclosure_text": None,
        "disclosure_source_text": None,
        "no_nav_found": False,
        "no_footer_found": False,
    }

    site_navs = []
    any_nav_candidate = False
    for (s, e, is_, ie) in nav_spans:
        if protected(s) or in_article(s) or in_footer(s):
            continue
        any_nav_candidate = True
        inner = html[is_:ie]
        tagtext = html[s:html.find(">", s) + 1]
        verdict = classify_nav(inner, tagtext)
        if verdict == "site_nav":
            site_navs.append((s, e))

    if not any_nav_candidate:
        info["no_nav_found"] = True
    elif not site_navs:
        info["no_nav_found"] = True

    if len(site_navs) >= 1:
        nav_s, nav_e = site_navs[0]
        wrapping_header = None
        for (hs, he, his_, hie) in header_spans:
            if protected(hs) or in_article(hs):
                continue
            if hs <= nav_s and nav_e <= he:
                wrapping_header = (hs, he, his_, hie)
                break
        if wrapping_header:
            hs, he, his_, hie = wrapping_header
            header_inner = html[his_:hie]
            without_nav = header_inner[: nav_s - his_] + header_inner[nav_e - his_:]
            remaining = re.sub(r"\s+", "", strip_tags(without_nav))
            if len(remaining) <= 20:
                removal_ops.append((hs, he, ""))
                info["header_removed_with_nav"] = True
                info["nav_removed"] = True
            else:
                removal_ops.append((nav_s, nav_e, ""))
                info["nav_removed"] = True
        else:
            removal_ops.append((nav_s, nav_e, ""))
            info["nav_removed"] = True

    footer_found_any = False
    for (s, e, is_, ie) in footer_spans:
        footer_found_any = True
        inner = html[is_:ie]
        verdict, kw = classify_footer(inner)
        if verdict == "site_footer":
            removal_ops.append((s, e, ""))
            info["footer_removed"] = True
        elif verdict == "disclosure":
            source_text = re.sub(r"\s+", " ", strip_tags(inner)).strip()
            disclosure_text = extract_disclosure_text(inner)
            removal_ops.append((s, e, build_disclosure_markup(disclosure_text, english)))
            info["footer_disclosure"] = True
            info["disclosure_text"] = disclosure_text
            info["disclosure_source_text"] = source_text
        # 'none' -> leave in place silently (not a site-footer signal at all)
    if not footer_found_any:
        info["no_footer_found"] = True

    removal_ops.sort(key=lambda op: op[0])
    return removal_ops, info


def widen_span_over_line_indent(html: str, s: int, e: int):
    """If a removed tag sits alone on its own line (only spaces/tabs before it
    since the last newline, and only spaces/tabs after it before the next
    newline), widen the span to swallow that horizontal whitespace too. This
    avoids leaving a whitespace-only "blank" line behind, which would
    otherwise trip trailing-whitespace lint (git diff --check) even though no
    non-whitespace byte was touched."""
    while s > 0 and html[s - 1] in " \t":
        s -= 1
    while e < len(html) and html[e] in " \t":
        e += 1
    return s, e


def apply_removals(html: str, removal_ops):
    """Apply a sorted list of (start, end, replacement) ops. A pure deletion
    (replacement == "") has its span widened over any pure-indentation
    whitespace so it doesn't leave a whitespace-only line behind; a
    replacement (e.g. a disclosure aside taking a footer's place) is inserted
    exactly in place, since it is real content, not a gap to be closed."""
    if not removal_ops:
        return html
    out = []
    pos = 0
    for (s, e, replacement) in removal_ops:
        if replacement == "":
            s, e = widen_span_over_line_indent(html, s, e)
        out.append(html[pos:s])
        out.append(replacement)
        pos = e
    out.append(html[pos:])
    return "".join(out)


# ---------------------------------------------------------------------------
# Marker block insertion / update
# ---------------------------------------------------------------------------


def upsert_marker_block(html: str, start_marker: str, end_marker: str, markup: str,
                          insert_at: str):
    """If a start_marker...end_marker block already exists, replace its inner
    content with `markup`. Otherwise insert a fresh block right after the
    `<body ...>` open tag (insert_at == 'after_body_open') or right before
    `</body>` (insert_at == 'before_body_close')."""
    start_idx = html.find(start_marker)
    if start_idx != -1:
        end_idx = html.find(end_marker, start_idx)
        if end_idx == -1:
            raise ValueError(f"unbalanced marker: {start_marker} without {end_marker}")
        before = html[:start_idx]
        after = html[end_idx + len(end_marker):]
        return before + start_marker + markup + end_marker + after

    block = start_marker + markup + end_marker
    if insert_at == "after_body_open":
        m = re.search(r"<body(\s[^>]*)?>", html, re.I)
        if not m:
            raise ValueError("no <body> tag found")
        return html[: m.end()] + block + html[m.end():]
    elif insert_at == "before_body_close":
        idx = html.rfind("</body>")
        if idx == -1:
            raise ValueError("no </body> tag found")
        return html[:idx] + block + html[idx:]
    raise ValueError(f"unknown insert_at {insert_at!r}")


def ensure_css_link(html: str) -> str:
    if "v2-chrome.css" in html:
        return html
    idx = html.rfind("</head>")
    if idx == -1:
        raise ValueError("no </head> tag found")
    return html[:idx] + CSS_LINK_TAG + "\n" + html[idx:]


def ensure_js_script(html: str) -> str:
    if JS_REFERENCE_NEEDLE in html:
        return html
    idx = html.rfind("</body>")
    if idx == -1:
        raise ValueError("no </body> tag found")
    return html[:idx] + JS_SCRIPT_TAG + "\n" + html[idx:]


# ---------------------------------------------------------------------------
# Body padding/margin-top hint detection (diagnostic only, no file changes)
# ---------------------------------------------------------------------------


def has_body_padding_hint(html: str) -> bool:
    body_tag_m = re.search(r"<body(\s[^>]*)?>", html, re.I)
    if body_tag_m and re.search(r"padding-top\s*:\s*[1-9]|margin-top\s*:\s*[1-9]",
                                 body_tag_m.group(0), re.I):
        return True
    for style_body in re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I):
        if re.search(r"(^|\})\s*body\s*\{[^}]*(padding-top|margin-top)\s*:\s*[1-9]",
                      style_body, re.I | re.S):
            return True
    return False


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------


def process_html(html: str, english: bool, report: FileReport) -> str:
    nav_markup = EN_NAV_MARKUP if english else ZH_NAV_MARKUP
    footer_markup = EN_FOOTER_MARKUP if english else ZH_FOOTER_MARKUP

    report.body_padding_hint = has_body_padding_hint(html)

    header_exists = MARK_HEADER_START in html
    footer_exists = MARK_FOOTER_START in html

    protect_spans = []
    if header_exists:
        s = html.find(MARK_HEADER_START)
        e = html.find(MARK_HEADER_END, s) + len(MARK_HEADER_END)
        protect_spans.append((s, e))
    if footer_exists:
        s = html.find(MARK_FOOTER_START)
        e = html.find(MARK_FOOTER_END, s) + len(MARK_FOOTER_END)
        protect_spans.append((s, e))

    if not header_exists or not footer_exists:
        removal_ops, info = compute_removal_spans(html, protect_spans, english)
        html = apply_removals(html, removal_ops)
        report.nav_removed = info["nav_removed"]
        report.header_removed_with_nav = info["header_removed_with_nav"]
        report.footer_removed = info["footer_removed"]
        report.footer_disclosure = info["footer_disclosure"]
        report.disclosure_text = info["disclosure_text"]
        report.no_nav_found = info["no_nav_found"]
        report.no_footer_found = info["no_footer_found"]

    html = upsert_marker_block(html, MARK_HEADER_START, MARK_HEADER_END, nav_markup,
                                "after_body_open")
    html = upsert_marker_block(html, MARK_FOOTER_START, MARK_FOOTER_END, footer_markup,
                                "before_body_close")
    html = ensure_css_link(html)
    html = ensure_js_script(html)

    # Duplicate-id check: after our own marker block, do id="nav" / id="navLinks"
    # / id="mobileMenuBtn" still appear anywhere else in the document?
    header_span = None
    s = html.find(MARK_HEADER_START)
    e = html.find(MARK_HEADER_END, s) + len(MARK_HEADER_END)
    header_span = (s, e)
    for idname in ('id="nav"', "id='nav'", 'id="navLinks"', "id='navLinks'",
                   'id="mobileMenuBtn"', "id='mobileMenuBtn'"):
        for m in re.finditer(re.escape(idname), html):
            if not (header_span[0] <= m.start() < header_span[1]):
                report.duplicate_ids.append(idname)

    return html


DEFAULT_GLOBS = ["blog/*.html", "en/blog/*.html"]
EXCLUDE = {"blog/index.html", "en/blog/index.html"}


def discover_files():
    files = []
    for pattern in DEFAULT_GLOBS:
        for p in sorted(REPO_ROOT.glob(pattern)):
            rel = p.relative_to(REPO_ROOT).as_posix()
            if rel in EXCLUDE:
                continue
            files.append(p)
    return files


# ---------------------------------------------------------------------------
# --verify mode
# ---------------------------------------------------------------------------


VERIFY_BASE = "HEAD"


def git_show_head(rel_path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{VERIFY_BASE}:{rel_path}"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return result.stdout


META_FIELDS_RE = re.compile(r"<title>([^<]*)</title>", re.I)


def extract_meta(html: str):
    title = META_FIELDS_RE.search(html)
    title = title.group(1) if title else None

    def meta_content(name, attr="name"):
        for m in re.finditer(r"<meta\b[^>]*>", html, re.I):
            tag = m.group(0)
            n = tag_attr(tag, attr)
            if n == name:
                return tag_attr(tag, "content")
        return None

    description = meta_content("description")

    def link_href(rel, hreflang=None):
        out = []
        for m in re.finditer(r"<link\b[^>]*>", html, re.I):
            tag = m.group(0)
            if tag_attr(tag, "rel") != rel:
                continue
            if hreflang is not None and tag_attr(tag, "hreflang") != hreflang:
                continue
            out.append(tag_attr(tag, "href"))
        return out

    canonical = link_href("canonical")
    hreflangs = []
    for m in re.finditer(r"<link\b[^>]*>", html, re.I):
        tag = m.group(0)
        if tag_attr(tag, "rel") == "alternate" and tag_attr(tag, "hreflang"):
            hreflangs.append((tag_attr(tag, "hreflang"), tag_attr(tag, "href")))

    jsonld = re.findall(r'<script type=["\']application/ld\+json["\']>(.*?)</script>',
                         html, re.S | re.I)

    return {
        "title": title,
        "description": description,
        "canonical": canonical,
        "hreflangs": sorted(hreflangs),
        "jsonld": jsonld,
    }


def strip_removed_spans(html: str, removal_ops):
    """Like apply_removals, but never inserts a replacement -- used to derive
    "baseline minus everything that got removed-or-replaced" for --verify,
    since the comparison target is baseline-minus-old-chrome, not
    baseline-minus-old-chrome-plus-new-chrome."""
    if not removal_ops:
        return html
    out = []
    pos = 0
    for (s, e, replacement) in removal_ops:
        if replacement == "":
            s, e = widen_span_over_line_indent(html, s, e)
        out.append(html[pos:s])
        pos = e
    out.append(html[pos:])
    return "".join(out)


def verify_one(path: Path):
    rel = path.relative_to(REPO_ROOT).as_posix()
    baseline = git_show_head(rel)
    current = path.read_text(encoding="utf-8")
    english = "en/blog" in rel

    protect_spans = []  # baseline never has our markers
    removal_ops, info = compute_removal_spans(baseline, protect_spans, english)
    baseline_stripped = strip_removed_spans(baseline, removal_ops)

    current_stripped = current
    for start_marker, end_marker in ((MARK_HEADER_START, MARK_HEADER_END),
                                      (MARK_FOOTER_START, MARK_FOOTER_END)):
        s = current_stripped.find(start_marker)
        if s == -1:
            return False, f"missing marker {start_marker}"
        e = current_stripped.find(end_marker, s)
        if e == -1:
            return False, f"unbalanced marker {start_marker}"
        e += len(end_marker)
        current_stripped = current_stripped[:s] + current_stripped[e:]

    disclosure_expected = info["footer_disclosure"]
    disclosure_present = MARK_DISCLOSURE_START in current_stripped
    if disclosure_expected != disclosure_present:
        return False, (
            f"disclosure marker presence mismatch (baseline expects "
            f"disclosure={disclosure_expected}, current has={disclosure_present})"
        )
    if disclosure_present:
        s = current_stripped.find(MARK_DISCLOSURE_START)
        e = current_stripped.find(MARK_DISCLOSURE_END, s)
        if e == -1:
            return False, "unbalanced disclosure marker"
        e += len(MARK_DISCLOSURE_END)
        disclosure_block = current_stripped[s:e]
        current_stripped = current_stripped[:s] + current_stripped[e:]

        p_match = re.search(r"<p>(.*?)</p>", disclosure_block, re.S)
        if not p_match:
            return False, "disclosure aside missing <p>"
        p_text_norm = re.sub(r"\s+", " ", html_entities.unescape(p_match.group(1))).strip()
        if not p_text_norm:
            return False, "disclosure <p> is empty"
        source_norm = re.sub(
            r"\s+", " ", html_entities.unescape(info["disclosure_source_text"] or "")
        ).strip()
        if p_text_norm not in source_norm:
            return False, "disclosure text is not a substring of the baseline footer text"

    if CSS_LINK_TAG in current_stripped:
        current_stripped = current_stripped.replace(CSS_LINK_TAG + "\n", "", 1)
        if CSS_LINK_TAG in current_stripped:
            current_stripped = current_stripped.replace(CSS_LINK_TAG, "", 1)
    else:
        return False, "missing v2-chrome.css link"

    baseline_had_js = JS_REFERENCE_NEEDLE in baseline_stripped
    if not baseline_had_js:
        if JS_SCRIPT_TAG in current_stripped:
            current_stripped = current_stripped.replace(JS_SCRIPT_TAG + "\n", "", 1)
            if JS_SCRIPT_TAG in current_stripped:
                current_stripped = current_stripped.replace(JS_SCRIPT_TAG, "", 1)
        else:
            return False, "missing autodev-v2.js script"

    if current_stripped != baseline_stripped:
        return False, "byte mismatch after stripping chrome/link/script"

    base_meta = extract_meta(baseline)
    cur_meta = extract_meta(current)
    if base_meta != cur_meta:
        return False, f"metadata mismatch: {base_meta} != {cur_meta}"

    return True, "OK"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main(argv):
    global VERIFY_BASE
    verify = "--verify" in argv
    for a in argv:
        if a.startswith("--base="):
            VERIFY_BASE = a.split("=", 1)[1]
    file_args = [a for a in argv if a != "--verify" and not a.startswith("--base=")]
    if file_args:
        files = [Path(a).resolve() for a in file_args]
    else:
        files = discover_files()

    if verify:
        fail_count = 0
        for path in files:
            ok, msg = verify_one(path)
            rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
            print(f"{'PASS' if ok else 'FAIL'} {rel}" + ("" if ok else f" -- {msg}"))
            if not ok:
                fail_count += 1
        total = len(files)
        print(f"\n{total - fail_count}/{total} PASS")
        return 1 if fail_count else 0

    nav_removed = 0
    header_removed = 0
    footer_removed = 0
    footer_disclosures = []
    no_nav_direct_insert = 0
    duplicate_ids = {}
    body_padding_files = []
    changed_files = 0

    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
        english = "en/blog" in rel
        original = path.read_text(encoding="utf-8")
        report = FileReport(rel)
        new_html = process_html(original, english, report)

        if report.nav_removed:
            nav_removed += 1
        if report.header_removed_with_nav:
            header_removed += 1
        if report.footer_removed:
            footer_removed += 1
        if report.footer_disclosure:
            footer_disclosures.append((rel, report.disclosure_text))
        if report.no_nav_found:
            no_nav_direct_insert += 1
        if report.duplicate_ids:
            duplicate_ids[rel] = report.duplicate_ids
        if report.body_padding_hint:
            body_padding_files.append(rel)

        if new_html != original:
            path.write_text(new_html, encoding="utf-8")
            changed_files += 1

    print(f"Processed {len(files)} files ({changed_files} changed).")
    print(f"Nav removed: {nav_removed}")
    print(f"  of which header removed together with nav: {header_removed}")
    print(f"Footer removed (plain deletion): {footer_removed}")
    print(f"Footer converted to v2c-disclosure: {len(footer_disclosures)}")
    for rel, text in footer_disclosures:
        print(f"  - {rel}: {text}")
    print(f"No site nav found (direct insert): {no_nav_direct_insert}")
    print(f"Duplicate id candidates: {len(duplicate_ids)}")
    for rel, ids in duplicate_ids.items():
        print(f"  - {rel}: {ids}")
    print(f"Body padding/margin-top hint files: {len(body_padding_files)}")
    for rel in body_padding_files:
        print(f"  - {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
