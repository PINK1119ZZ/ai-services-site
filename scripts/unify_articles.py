#!/usr/bin/env python3
"""Deterministic, idempotent AutoDev 2.0 article-content unifier.

Strips a blog article's own inline chrome (embedded <style> elements,
non-v2-chrome stylesheet links, Google Fonts links/preconnects, and every
element's style="" attribute) from the content that scripts/apply_blog_chrome.py
already wrapped in the <!-- v2-chrome:header --> / <!-- v2-chrome:footer -->
(and, when present, <!-- v2-chrome:disclosure -->) markers, so the article's
own text renders on the shared v2-chrome canvas (assets/v2-chrome.css)
instead of whatever background/font/width its own removed styles used to
set.

This script must run on a file that has *already* had apply_blog_chrome.py
applied (it looks for the v2-chrome marker comments and raises a clear error
if they are missing). It never touches the header/footer/disclosure marker
blocks themselves, never adds/removes/reorders a <script> tag or its
content, and never changes any <head> content other than removing <style>
elements and non-v2-chrome-chrome stylesheet/font <link> tags.

Per file, in order:
  1. <head>: remove every <style> element and every stylesheet-or-Google-Fonts
     <link> (rel="stylesheet" pointing anywhere other than
     /assets/v2-chrome.css, plus any <link> -- stylesheet, preconnect, or
     preload -- whose href is on fonts.googleapis.com/fonts.gstatic.com).
     Everything else in <head> is untouched byte for byte.
  2. <body>: add the `v2c-page` class (existing classes kept) and remove any
     stray <style> element that happens to sit in the body.
  3. Within the content region (the marker's header end to the disclosure or,
     failing that, footer marker start):
       a. remove a residual legacy site-chrome block -- a <header>/<div>/<nav>
          that holds nothing but one link to "/" or "/en/" whose text
          contains "AutoDev", and no <h1> -- if one is found;
       b. remove every element's style="..." attribute (skipping the inside
          of <script> elements, whose content is never touched);
       c. wrap the whole region in <main class="v2c-article">...</main>, or,
          if the region is already exactly one <main>...</main> spanning it
          end to end, just add the v2c-article class to that existing tag.

Usage:
    python3 scripts/unify_articles.py [file ...]
    python3 scripts/unify_articles.py --verify [--base=<ref>] [file ...]

With no file arguments, operates on every ``blog/*.html`` and
``en/blog/*.html`` file except the two hub pages, matching
apply_blog_chrome.py's own default file discovery.
"""
from __future__ import annotations

import difflib
import html as html_entities
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True  # don't litter scripts/__pycache__ on import
sys.path.insert(0, str(Path(__file__).resolve().parent))
import apply_blog_chrome as abc  # noqa: E402  (reuse parsing helpers only)

find_balanced = abc.find_balanced
strip_tags = abc.strip_tags
tag_attr = abc.tag_attr
apply_removals = abc.apply_removals

MARK_HEADER_START = abc.MARK_HEADER_START
MARK_HEADER_END = abc.MARK_HEADER_END
MARK_FOOTER_START = abc.MARK_FOOTER_START
MARK_FOOTER_END = abc.MARK_FOOTER_END
MARK_DISCLOSURE_START = abc.MARK_DISCLOSURE_START
MARK_DISCLOSURE_END = abc.MARK_DISCLOSURE_END
CSS_LINK_HREF = "/assets/v2-chrome.css"

FONT_HOST_RE = re.compile(r"fonts\.(?:googleapis|gstatic)\.com", re.I)


# ---------------------------------------------------------------------------
# small generic helpers
# ---------------------------------------------------------------------------


def add_class(tag_html: str, new_class: str) -> str:
    """Add `new_class` to a tag's class="..."/'...' attribute (creating one
    if absent). No-op if the class token is already present."""
    for quote in ('"', "'"):
        pattern = re.compile(r"\bclass\s*=\s*" + quote + r"([^" + quote + r"]*)" + quote, re.I)
        m = pattern.search(tag_html)
        if m:
            classes = m.group(1).split()
            if new_class in classes:
                return tag_html
            new_val = (m.group(1) + " " + new_class).strip()
            return tag_html[: m.start(1)] + new_val + tag_html[m.end(1):]
    tag_name_m = re.match(r"<([a-zA-Z][a-zA-Z0-9-]*)", tag_html)
    insert_at = tag_name_m.end()
    return tag_html[:insert_at] + f' class="{new_class}"' + tag_html[insert_at:]


def visible_text(segment: str) -> str:
    """Whitespace-normalized visible text of an HTML fragment: <script> and
    <style> elements (tag + content) are dropped first, every remaining tag
    becomes a space, entities are decoded, and runs of whitespace collapse."""
    for tag in ("script", "style"):
        for (s, e, _is, _ie) in reversed(find_balanced(segment, tag)):
            segment = segment[:s] + segment[e:]
    text = html_entities.unescape(strip_tags(segment))
    return re.sub(r"\s+", " ", text).strip()


def script_spans(html: str):
    return [(s, e) for (s, e, _is, _ie) in find_balanced(html, "script")]


# ---------------------------------------------------------------------------
# 1. <head> cleanup
# ---------------------------------------------------------------------------


def find_head_span(html: str):
    m = re.search(r"<head(\s[^>]*)?>", html, re.I)
    if not m:
        raise ValueError("no <head> tag found")
    idx = html.lower().find("</head>")
    if idx == -1:
        raise ValueError("no </head> tag found")
    return m.end(), idx


def remove_head_noise(html: str):
    start, end = find_head_span(html)
    head = html[start:end]
    ops = []
    style_count = 0
    for (s, e, _is, _ie) in find_balanced(head, "style"):
        ops.append((s, e, ""))
        style_count += 1
    link_count = 0
    for m in re.finditer(r"<link\b[^>]*>", head, re.I):
        tag = m.group(0)
        href = tag_attr(tag, "href")
        rel = tag_attr(tag, "rel")
        is_font = bool(FONT_HOST_RE.search(href))
        is_other_stylesheet = rel.lower() == "stylesheet" and href != CSS_LINK_HREF
        if is_font or is_other_stylesheet:
            ops.append((m.start(), m.end(), ""))
            link_count += 1
    ops.sort(key=lambda op: op[0])
    new_head = apply_removals(head, ops)
    return html[:start] + new_head + html[end:], style_count, link_count


def remove_body_stray_styles(html: str, body_content_start: int):
    spans = [(s, e) for (s, e, _is, _ie) in find_balanced(html[body_content_start:], "style")]
    if not spans:
        return html, 0
    seg = html[body_content_start:]
    ops = sorted([(s, e, "") for (s, e) in spans], key=lambda op: op[0])
    seg = apply_removals(seg, ops)
    return html[:body_content_start] + seg, len(spans)


# ---------------------------------------------------------------------------
# 2. residual legacy site-chrome header/div/nav removal
# ---------------------------------------------------------------------------

HOME_HREF_RE = re.compile(r"^https?://(?:www\.)?autodev-ai\.com(/.*)?$", re.I)


def is_home_href(href: str) -> bool:
    if not href:
        return False
    href = href.split("#")[0].split("?")[0]
    if href.lower().startswith(("http://", "https://")):
        m = HOME_HREF_RE.match(href)
        if not m:
            return False
        href = m.group(1) or "/"
    return href in ("/", "/en/", "/en")


def find_stale_headers(content: str):
    """Return (removal_spans, removed_info) for every <header>/<div>/<nav>
    block in `content` that is nothing but a single "/" or "/en/" link whose
    text contains "AutoDev", with no <h1> anywhere inside -- the residual
    legacy site-chrome pattern described in the task (e.g. the black
    AutoDev AI bar left behind under the new nav on some articles)."""
    scripts = script_spans(content)

    def in_script(pos):
        return any(s <= pos < e for (s, e) in scripts)

    candidates = []
    for tag in ("header", "div", "nav"):
        for (s, e, is_, ie) in find_balanced(content, tag):
            if in_script(s):
                continue
            candidates.append((s, e, is_, ie))
    candidates.sort(key=lambda c: (c[0], -(c[1] - c[0])))

    removed_spans = []
    removed_info = []
    for (s, e, is_, ie) in candidates:
        if any(rs <= s < re_ for (rs, re_) in removed_spans):
            continue
        inner = content[is_:ie]
        if re.search(r"<h1\b", inner, re.I):
            continue
        a_tags = re.findall(r"<a\b[^>]*>.*?</a>", inner, re.S | re.I)
        if len(a_tags) != 1:
            continue
        a_match = re.search(r"<a\b([^>]*)>(.*?)</a>", inner, re.S | re.I)
        href = tag_attr("<a " + a_match.group(1) + ">", "href")
        if not is_home_href(href):
            continue
        link_text_plain = re.sub(r"\s+", "", html_entities.unescape(strip_tags(a_match.group(2))))
        if "autodev" not in link_text_plain.lower():
            continue
        block_text_plain = re.sub(r"\s+", "", html_entities.unescape(strip_tags(inner)))
        if block_text_plain != link_text_plain:
            continue
        removed_spans.append((s, e))
        removed_info.append({
            "tag": content[s:content.find(">", s) + 1],
            "text": re.sub(r"\s+", " ", html_entities.unescape(strip_tags(inner))).strip(),
        })
    removed_spans.sort()
    return removed_spans, removed_info


# ---------------------------------------------------------------------------
# 3. style="" attribute stripping (content region only, skipping <script>)
# ---------------------------------------------------------------------------

STYLE_ATTR_RE = re.compile(r'\s+style\s*=\s*("[^"]*"|\'[^\']*\')', re.I)


TAG_RE = re.compile(r"<[a-zA-Z][a-zA-Z0-9-]*(?:\s[^<>]*)?/?>", re.S)


def strip_style_attrs(content: str):
    """Remove every style="..."/'...' attribute, but only when it sits
    inside an actual opening tag's own text (matched by TAG_RE, which never
    spans a `<` or `>`). Scanning tag-by-tag -- instead of scanning the raw
    style="..." pattern across the whole content -- is what keeps this from
    misreading a JS object literal shown inside a <pre><code> example (e.g.
    `const { prompt, style = 'cinematic' } = req.body;`) as an HTML
    attribute: that text sits between two tags, so no TAG_RE match ever
    covers it. <script> elements are skipped outright since their content
    is never touched."""
    scripts = script_spans(content)

    def in_script(pos):
        return any(s <= pos < e for (s, e) in scripts)

    out = []
    pos = 0
    count = 0
    for tm in TAG_RE.finditer(content):
        if in_script(tm.start()):
            continue
        tag_text = tm.group(0)
        new_tag_text, n = STYLE_ATTR_RE.subn("", tag_text)
        if n:
            out.append(content[pos:tm.start()])
            out.append(new_tag_text)
            pos = tm.end()
            count += n
    out.append(content[pos:])
    return "".join(out), count


# ---------------------------------------------------------------------------
# 4. <main class="v2c-article"> wrap/reuse
# ---------------------------------------------------------------------------


MAIN_OPEN_TAG_RE = re.compile(r"<main(\s[^>]*)?>", re.I)
MAIN_CLOSE_TAG_RE = re.compile(r"</main\s*>", re.I)


def wrap_main(content: str):
    main_spans = find_balanced(content, "main")
    if len(main_spans) == 1:
        s, e, _is, _ie = main_spans[0]
        if content[:s].strip() == "" and content[e:].strip() == "":
            tag_close = content.find(">", s) + 1
            new_tag = add_class(content[s:tag_close], "v2c-article")
            return content[:s] + new_tag + content[tag_close:], False

    # No balanced <main>...</main> spans the whole region -- but if the
    # region opens with an unclosed <main ...> whose matching </main> sits
    # further along in the document (past content_end), just tag that
    # opening tag with v2c-article instead of wrapping again: apply_blog_chrome.py's
    # page_credits conversion (e.g. Kira's <footer class="kira-footer">) can
    # leave a <!-- v2-chrome:disclosure --> block *inside* a page's own
    # top-level <main>, which is exactly this shape. A synthetic </main>
    # here would either double-close that wrapper or cut it short.
    lead = len(content) - len(content.lstrip())
    m = MAIN_OPEN_TAG_RE.match(content, lead)
    if m and not MAIN_CLOSE_TAG_RE.search(content):
        new_tag = add_class(content[m.start():m.end()], "v2c-article")
        return content[:m.start()] + new_tag + content[m.end():], False

    return '<main class="v2c-article">' + content + "</main>", True


# ---------------------------------------------------------------------------
# per-file transform
# ---------------------------------------------------------------------------


class Report:
    def __init__(self, rel: str):
        self.rel = rel
        self.style_elements_removed = 0
        self.stylesheet_links_removed = 0
        self.style_attrs_removed = 0
        self.stale_headers_removed = []
        self.main_reused = False


def trim_newly_touched_trailing_whitespace(original: str, transformed: str) -> str:
    """Some pre-existing article lines already end in a stray space/tab
    before our own edit ever touches them (a pre-existing site quirk, not
    something we introduce). Editing a style="" attribute earlier on that
    same line still rewrites the whole line for diff purposes, so
    `git diff --check` would flag that pre-existing trailing whitespace as
    newly introduced. This trims trailing horizontal whitespace only on
    lines that a same-line-count `replace` opcode shows we actually edited
    (never on a line that is unchanged, and never as a side effect of a
    block insertion/deletion such as a whole <style> block disappearing)."""
    if original == transformed:
        return transformed
    orig_lines = original.split("\n")
    new_lines = transformed.split("\n")
    sm = difflib.SequenceMatcher(a=orig_lines, b=new_lines, autojunk=False)
    changed = False
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and (i2 - i1) == (j2 - j1):
            for k in range(j1, j2):
                stripped = new_lines[k].rstrip(" \t")
                if stripped != new_lines[k]:
                    new_lines[k] = stripped
                    changed = True
    return "\n".join(new_lines) if changed else transformed


def process_html(html: str, report: Report) -> str:
    original_html = html
    html, style_head, links = remove_head_noise(html)
    report.style_elements_removed += style_head
    report.stylesheet_links_removed += links

    body_m = re.search(r"<body(\s[^>]*)?>", html, re.I)
    if not body_m:
        raise ValueError("no <body> tag found")
    new_body_tag = add_class(body_m.group(0), "v2c-page")
    html = html[: body_m.start()] + new_body_tag + html[body_m.end():]
    body_content_start = body_m.start() + len(new_body_tag)

    html, style_body = remove_body_stray_styles(html, body_content_start)
    report.style_elements_removed += style_body

    hs = html.find(MARK_HEADER_START)
    if hs == -1:
        raise ValueError(
            "missing v2-chrome header marker -- run scripts/apply_blog_chrome.py first"
        )
    he = html.find(MARK_HEADER_END, hs)
    if he == -1:
        raise ValueError("unbalanced v2-chrome header marker")
    content_start = he + len(MARK_HEADER_END)

    disc_s = html.find(MARK_DISCLOSURE_START)
    foot_s = html.find(MARK_FOOTER_START)
    if foot_s == -1:
        raise ValueError(
            "missing v2-chrome footer marker -- run scripts/apply_blog_chrome.py first"
        )
    content_end = disc_s if disc_s != -1 else foot_s

    content = html[content_start:content_end]

    stale_spans, stale_info = find_stale_headers(content)
    if stale_spans:
        ops = sorted([(s, e, "") for (s, e) in stale_spans], key=lambda op: op[0])
        content = apply_removals(content, ops)
        report.stale_headers_removed = stale_info

    content, style_attrs = strip_style_attrs(content)
    report.style_attrs_removed = style_attrs

    content, wrapped_new = wrap_main(content)
    report.main_reused = not wrapped_new

    final_html = html[:content_start] + content + html[content_end:]
    return trim_newly_touched_trailing_whitespace(original_html, final_html)


# ---------------------------------------------------------------------------
# file discovery (mirrors apply_blog_chrome.py's defaults)
# ---------------------------------------------------------------------------

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


def git_show(base: str, rel_path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{base}:{rel_path}"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return result.stdout


def extract_hrefs(html: str):
    return [tag_attr(m.group(0), "href") for m in re.finditer(r"<a\b[^>]*>", html, re.I)]


def extract_imgsrcs(html: str):
    return [tag_attr(m.group(0), "src") for m in re.finditer(r"<img\b[^>]*>", html, re.I)]


def extract_headings(html: str):
    out = []
    for m in re.finditer(r"<(h[1-6])\b[^>]*>(.*?)</\1\s*>", html, re.S | re.I):
        text = re.sub(r"\s+", " ", html_entities.unescape(strip_tags(m.group(2)))).strip()
        out.append((m.group(1).lower(), text))
    return out


def extract_scripts(html: str):
    return [m.group(1) for m in re.finditer(r"<script\b[^>]*>(.*?)</script>", html, re.S | re.I)]


def find_stylesheet_hrefs(html: str):
    start, end = find_head_span(html)
    head = html[start:end]
    out = []
    for m in re.finditer(r"<link\b[^>]*>", head, re.I):
        tag = m.group(0)
        if tag_attr(tag, "rel").lower() == "stylesheet":
            out.append(tag_attr(tag, "href"))
    return out


def verify_one(path: Path, base: str):
    rel = path.relative_to(REPO_ROOT).as_posix()
    baseline = git_show(base, rel)
    current = path.read_text(encoding="utf-8")

    if MARK_HEADER_START not in baseline:
        # `base` predates apply_blog_chrome.py for this path entirely (e.g.
        # a non-article page whose chrome and content were both unified in
        # the same uncommitted working session, so there is no commit with
        # a "chrome applied, not yet unified" snapshot to diff against).
        # Derive that intermediate snapshot by running apply_blog_chrome's
        # own transform on the pristine baseline in memory -- using its
        # exact same english/is_blog rules -- so every check below still
        # compares against "chrome already applied", just computed instead
        # of read from git.
        english = rel.startswith("en/")
        is_blog = rel.startswith("blog/") or rel.startswith("en/blog/")
        baseline = abc.process_html(baseline, english, abc.FileReport(rel), is_blog)

    hs = baseline.find(MARK_HEADER_START)
    he = baseline.find(MARK_HEADER_END, hs) if hs != -1 else -1
    if hs == -1 or he == -1:
        return False, "baseline missing v2-chrome header marker", []
    b_content_start = he + len(MARK_HEADER_END)
    b_disc_s = baseline.find(MARK_DISCLOSURE_START)
    b_foot_s = baseline.find(MARK_FOOTER_START)
    if b_foot_s == -1:
        return False, "baseline missing v2-chrome footer marker", []
    b_content_end = b_disc_s if b_disc_s != -1 else b_foot_s
    b_content = baseline[b_content_start:b_content_end]

    stale_spans, _info = find_stale_headers(b_content)
    abs_spans = [(s + b_content_start, e + b_content_start) for (s, e) in stale_spans]
    excluded_texts = [visible_text(baseline[s:e]) for (s, e) in abs_spans]

    baseline_cmp = apply_removals(
        baseline, sorted([(s, e, "") for (s, e) in abs_spans], key=lambda op: op[0])
    )

    if visible_text(baseline_cmp) != visible_text(current):
        return False, "visible text sequence mismatch", excluded_texts

    if Counter(extract_hrefs(baseline_cmp)) != Counter(extract_hrefs(current)):
        return False, "link href multiset mismatch", excluded_texts

    if Counter(extract_imgsrcs(baseline_cmp)) != Counter(extract_imgsrcs(current)):
        return False, "img src multiset mismatch", excluded_texts

    if extract_headings(baseline_cmp) != extract_headings(current):
        return False, "heading sequence mismatch", excluded_texts

    base_meta = abc.extract_meta(baseline)
    cur_meta = abc.extract_meta(current)
    if base_meta != cur_meta:
        return False, f"metadata mismatch: {base_meta} != {cur_meta}", excluded_texts

    if extract_scripts(baseline) != extract_scripts(current):
        return False, "script content mismatch", excluded_texts

    # --- structural checks specific to this migration ---
    body_m = re.search(r"<body([^>]*)>", current, re.I)
    if not body_m or "v2c-page" not in (tag_attr(body_m.group(0), "class") or "").split():
        return False, "body missing v2c-page class", excluded_texts

    if re.search(r"<style\b", current, re.I):
        return False, "current still contains a <style> element", excluded_texts

    stylesheets = find_stylesheet_hrefs(current)
    if stylesheets != [CSS_LINK_HREF]:
        return False, f"unexpected stylesheet links remain: {stylesheets}", excluded_texts

    c_hs = current.find(MARK_HEADER_START)
    c_he = current.find(MARK_HEADER_END, c_hs) if c_hs != -1 else -1
    c_disc_s = current.find(MARK_DISCLOSURE_START)
    c_foot_s = current.find(MARK_FOOTER_START)
    if c_hs == -1 or c_he == -1 or c_foot_s == -1:
        return False, "current missing v2-chrome marker(s)", excluded_texts
    c_content_start = c_he + len(MARK_HEADER_END)
    c_content_end = c_disc_s if c_disc_s != -1 else c_foot_s
    c_content = current[c_content_start:c_content_end]

    scripts = script_spans(c_content)
    for tm in TAG_RE.finditer(c_content):
        if any(s <= tm.start() < e for (s, e) in scripts):
            continue
        if STYLE_ATTR_RE.search(tm.group(0)):
            return False, "content region still has a style= attribute", excluded_texts

    main_spans = find_balanced(c_content, "main")
    ok_wrap = False
    for (s, e, _is, _ie) in main_spans:
        if c_content[:s].strip() == "" and c_content[e:].strip() == "":
            tag_close = c_content.find(">", s) + 1
            if "v2c-article" in (tag_attr(c_content[s:tag_close], "class") or "").split():
                ok_wrap = True
    if not ok_wrap:
        # Same unclosed-<main> shape wrap_main() handles: the region opens
        # with a <main ...> whose matching </main> sits past content_end
        # (e.g. Kira's page_credits disclosure block sits inside its own
        # top-level <main>). The class was added to that opening tag in
        # place, with no synthetic </main> inserted here.
        lead = len(c_content) - len(c_content.lstrip())
        m = MAIN_OPEN_TAG_RE.match(c_content, lead)
        if (
            m and not MAIN_CLOSE_TAG_RE.search(c_content)
            and "v2c-article" in (tag_attr(c_content[m.start():m.end()], "class") or "").split()
        ):
            ok_wrap = True
    if not ok_wrap:
        return False, "content region is not wrapped in <main class=\"v2c-article\">", excluded_texts

    for start_marker, end_marker, required in (
        (MARK_HEADER_START, MARK_HEADER_END, True),
        (MARK_FOOTER_START, MARK_FOOTER_END, True),
    ):
        if current.count(start_marker) != 1 or current.count(end_marker) != 1:
            return False, f"marker {start_marker} does not appear exactly once", excluded_texts

    return True, "OK", excluded_texts


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def main(argv):
    verify = "--verify" in argv
    base = "HEAD"
    for a in argv:
        if a.startswith("--base="):
            base = a.split("=", 1)[1]
    file_args = [a for a in argv if a != "--verify" and not a.startswith("--base=")]
    files = [Path(a).resolve() for a in file_args] if file_args else discover_files()

    if verify:
        fail_count = 0
        for path in files:
            rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
            try:
                ok, msg, excluded = verify_one(path, base)
            except Exception as exc:  # noqa: BLE001
                ok, msg, excluded = False, f"error: {exc}", []
            print(f"{'PASS' if ok else 'FAIL'} {rel}" + ("" if ok else f" -- {msg}"))
            for text in excluded:
                print(f"    excluded residual-header text: {text!r}")
            if not ok:
                fail_count += 1
        total = len(files)
        print(f"\n{total - fail_count}/{total} PASS")
        return 1 if fail_count else 0

    changed_files = 0
    total_style_elements = 0
    total_stylesheets = 0
    total_style_attrs = 0
    stale_header_files = []
    main_reused_files = []

    for path in files:
        rel = path.relative_to(REPO_ROOT).as_posix() if path.is_relative_to(REPO_ROOT) else str(path)
        original = path.read_text(encoding="utf-8")
        report = Report(rel)
        try:
            new_html = process_html(original, report)
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR {rel}: {exc}")
            continue

        print(
            f"{rel}: style_elements_removed={report.style_elements_removed} "
            f"stylesheet_links_removed={report.stylesheet_links_removed} "
            f"style_attrs_removed={report.style_attrs_removed} "
            f"main_reused={report.main_reused}"
        )
        for info in report.stale_headers_removed:
            print(f"    removed stale header: {info['tag']} text={info['text']!r}")

        total_style_elements += report.style_elements_removed
        total_stylesheets += report.stylesheet_links_removed
        total_style_attrs += report.style_attrs_removed
        if report.stale_headers_removed:
            stale_header_files.append(rel)
        if report.main_reused:
            main_reused_files.append(rel)

        if new_html != original:
            path.write_text(new_html, encoding="utf-8")
            changed_files += 1

    print(f"\nProcessed {len(files)} files ({changed_files} changed).")
    print(f"Total style elements removed: {total_style_elements}")
    print(f"Total stylesheet/font links removed: {total_stylesheets}")
    print(f"Total style= attributes removed: {total_style_attrs}")
    print(f"Files with a residual stale header removed: {len(stale_header_files)}")
    for rel in stale_header_files:
        print(f"  - {rel}")
    print(f"Files where an existing <main> was reused: {len(main_reused_files)}")
    for rel in main_reused_files:
        print(f"  - {rel}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
