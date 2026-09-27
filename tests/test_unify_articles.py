import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "unify_articles.py"
sys.dont_write_bytecode = True


def load_module():
    spec = importlib.util.spec_from_file_location("unify_articles_under_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


unify = load_module()


BASELINE_HTML = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<title>Sample Article</title>
<meta name="description" content="A sample article for testing.">
<link rel="canonical" href="https://autodev-ai.com/blog/sample.html">
<link rel="alternate" hreflang="en" href="https://autodev-ai.com/en/blog/sample.html">
<style>body{background:#111;color:#eee;}</style>
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"Sample Article"}</script>
<link rel="stylesheet" href="/assets/v2-chrome.css">
</head>
<body><!-- v2-chrome:header --><header class="v2c-header">NAV</header><!-- /v2-chrome:header -->
<div class="hero" style="background:#000;">
<h1>Sample Article</h1>
<p style="color:red;">Intro paragraph with a <a href="https://example.com/a">link</a>.</p>
<h2>Section</h2>
<p>More text and an image below.</p>
<img src="/img/sample.png" alt="sample">
</div>
<!-- v2-chrome:footer --><footer class="v2c-footer">FOOTER</footer><!-- /v2-chrome:footer --><script defer src="/assets/autodev-v2.js"></script>
</body>
</html>
"""


def run(cmd, cwd):
    subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)


class VerifyOneTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve())
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        (self.repo / "blog").mkdir()

        run(["git", "init", "-q"], cwd=self.repo)
        run(["git", "config", "user.email", "test@example.com"], cwd=self.repo)
        run(["git", "config", "user.name", "Test"], cwd=self.repo)

        self.article = self.repo / "blog" / "sample.html"
        self.article.write_text(BASELINE_HTML, encoding="utf-8")
        run(["git", "add", "blog/sample.html"], cwd=self.repo)
        run(["git", "commit", "-q", "-m", "baseline"], cwd=self.repo)

        # Point the module at our throwaway repo instead of the real one.
        self._real_repo_root = unify.REPO_ROOT
        unify.REPO_ROOT = self.repo
        self.addCleanup(self._restore_repo_root)

        report = unify.Report("blog/sample.html")
        self.correct_current = unify.process_html(BASELINE_HTML, report)

    def _restore_repo_root(self):
        unify.REPO_ROOT = self._real_repo_root

    def verify(self, current_html):
        self.article.write_text(current_html, encoding="utf-8")
        return unify.verify_one(self.article, "HEAD")

    def test_correct_transform_passes(self):
        ok, msg, excluded = self.verify(self.correct_current)
        self.assertTrue(ok, msg)
        self.assertEqual(excluded, [])

    def test_changed_visible_text_fails(self):
        mutated = self.correct_current.replace("Intro paragraph", "Rewritten paragraph")
        ok, msg, _ = self.verify(mutated)
        self.assertFalse(ok)
        self.assertIn("text", msg)

    def test_removed_link_fails(self):
        mutated = self.correct_current.replace(
            '<a href="https://example.com/a">link</a>', "link"
        )
        ok, msg, _ = self.verify(mutated)
        self.assertFalse(ok)

    def test_removed_image_fails(self):
        mutated = self.correct_current.replace(
            '<img src="/img/sample.png" alt="sample">', ""
        )
        ok, msg, _ = self.verify(mutated)
        self.assertFalse(ok)
        self.assertIn("img", msg)

    def test_changed_json_ld_fails(self):
        mutated = self.correct_current.replace(
            '"headline":"Sample Article"', '"headline":"Changed Headline"'
        )
        ok, msg, _ = self.verify(mutated)
        self.assertFalse(ok)
        self.assertIn("metadata", msg)

    def test_reintroduced_style_attribute_fails(self):
        # A style="" attribute surviving in the content region should also
        # be caught by the structural checks, independent of the semantic
        # (text/links/meta) comparisons above.
        mutated = self.correct_current.replace(
            "<h2>Section</h2>", '<h2 style="color:blue;">Section</h2>'
        )
        ok, msg, _ = self.verify(mutated)
        self.assertFalse(ok)
        self.assertIn("style", msg)

    def test_verify_one_falls_back_when_baseline_predates_chrome(self):
        # blog.higgsfield etc. were already chrome-applied at HEAD, so
        # test_correct_transform_passes above exercises the normal path.
        # A legacy page (privacy.html, 404.html, ...) instead had both
        # apply_blog_chrome.py and unify_articles.py run in the same
        # uncommitted session, so its HEAD baseline predates the
        # v2-chrome markers entirely. verify_one() must still pass by
        # deriving the "chrome applied" snapshot in memory instead of
        # erroring out with "baseline missing v2-chrome header marker".
        legacy_baseline = (
            '<html lang="zh-Hant"><head><title>Legacy</title></head>'
            '<body>'
            '<nav class="nav" id="nav"><a class="nav-logo" href="/">AutoDev AI</a></nav>'
            '<main style="padding:2rem;"><h1>Legacy Page</h1>'
            '<p style="color:red;">Some legacy text.</p></main>'
            '<footer><p>&copy; 2026 AutoDev AI.</p></footer>'
            "</body></html>"
        )
        legacy_path = self.repo / "blog" / "legacy.html"
        legacy_path.write_text(legacy_baseline, encoding="utf-8")
        run(["git", "add", "blog/legacy.html"], cwd=self.repo)
        run(["git", "commit", "-q", "-m", "legacy baseline"], cwd=self.repo)

        chromed = unify.abc.process_html(
            legacy_baseline, english=False, report=unify.abc.FileReport("blog/legacy.html"),
        )
        current = unify.process_html(chromed, unify.Report("blog/legacy.html"))
        legacy_path.write_text(current, encoding="utf-8")

        ok, msg, excluded = unify.verify_one(legacy_path, "HEAD")
        self.assertTrue(ok, msg)
        self.assertEqual(excluded, [])


class StripStyleAttrsTests(unittest.TestCase):
    """Regression coverage for the tag-bounded style="" stripper: it must
    only ever touch a real HTML attribute, never text that merely looks
    like one (e.g. a JS object literal shown inside <pre><code>)."""

    def test_example_code_with_style_variable_is_untouched(self):
        content = (
            "<pre><code>const { prompt, style = 'cinematic', duration = 10 } "
            "= req.body;</code></pre>"
        )
        new_content, count = unify.strip_style_attrs(content)
        self.assertEqual(count, 0)
        self.assertEqual(new_content, content)

    def test_real_style_attribute_is_still_removed(self):
        content = '<p style="color:red;">hello</p>'
        new_content, count = unify.strip_style_attrs(content)
        self.assertEqual(count, 1)
        self.assertEqual(new_content, "<p>hello</p>")

    def test_mixed_real_attribute_and_code_sample_on_one_line(self):
        content = (
            '<p style="color:red;">See: '
            "<code>const { style = 'x' } = opts;</code></p>"
        )
        new_content, count = unify.strip_style_attrs(content)
        self.assertEqual(count, 1)
        self.assertIn("style = 'x'", new_content)
        self.assertNotIn('style="color:red;"', new_content)


class StaleHeaderRemovalTests(unittest.TestCase):
    """Unit coverage for find_stale_headers(), independent of git/verify."""

    def test_pure_brand_link_header_is_removed(self):
        content = (
            '<header class="site-header"><div class="container">'
            '<a href="/">AutoDev AI</a></div></header>'
            "<article><h1>Title</h1><p>Body text.</p></article>"
        )
        spans, info = unify.find_stale_headers(content)
        self.assertEqual(len(spans), 1)
        self.assertEqual(info[0]["text"], "AutoDev AI")

    def test_header_with_h1_is_kept(self):
        content = '<header><a href="/">AutoDev</a><h1>Title</h1></header>'
        spans, info = unify.find_stale_headers(content)
        self.assertEqual(spans, [])

    def test_header_with_extra_content_is_kept(self):
        content = (
            '<header><a href="/">AutoDev</a><span>extra text</span></header>'
        )
        spans, info = unify.find_stale_headers(content)
        self.assertEqual(spans, [])

    def test_link_to_unrelated_page_is_kept(self):
        content = '<header><a href="/blog/">AutoDev Blog</a></header>'
        spans, info = unify.find_stale_headers(content)
        self.assertEqual(spans, [])


class WrapMainUnclosedTests(unittest.TestCase):
    """Regression coverage for the Kira page_credits shape: a top-level
    <main> whose </main> sits past content_end because apply_blog_chrome.py
    replaced a footer that was nested *inside* it, in place."""

    def test_unclosed_main_gets_class_added_not_rewrapped(self):
        content = (
            '\n<main class="kira-page">\n<header><h1>Kira</h1></header>\n'
            '<!-- v2-chrome:disclosure --><aside>credits</aside><!-- /v2-chrome:disclosure -->'
        )
        new_content, wrapped_new = unify.wrap_main(content)
        self.assertFalse(wrapped_new)
        self.assertEqual(new_content.count("<main"), 1)
        self.assertNotIn("</main>", new_content)
        self.assertIn('class="kira-page v2c-article"', new_content)

    def test_fully_balanced_main_is_still_reused_normally(self):
        content = "\n<main class=\"kira-page\">\n<p>hi</p>\n</main>\n"
        new_content, wrapped_new = unify.wrap_main(content)
        self.assertFalse(wrapped_new)
        self.assertEqual(new_content.count("<main"), 1)
        self.assertEqual(new_content.count("</main>"), 1)
        self.assertIn('class="kira-page v2c-article"', new_content)

    def test_no_main_at_all_still_wraps_fresh(self):
        content = "\n<p>hi</p>\n"
        new_content, wrapped_new = unify.wrap_main(content)
        self.assertTrue(wrapped_new)
        self.assertEqual(new_content, '<main class="v2c-article">' + content + "</main>")


class PageCreditsFooterTests(unittest.TestCase):
    """Regression coverage for apply_blog_chrome.py's kira-footer handling:
    the full inner HTML (links and text) must survive verbatim, with only
    style="" attributes removed."""

    def test_kira_class_footer_is_classified_page_credits(self):
        tagtext = '<footer class="kira-footer">'
        verdict, kw = unify.abc.classify_footer("<p>anything</p>", tagtext)
        self.assertEqual(verdict, "page_credits")

    def test_page_credits_markup_keeps_links_and_strips_style(self):
        inner = (
            '\n  <p>Attribution <a href="https://autodev-ai.com/">AutoDev AI</a>.</p>\n'
            '  <p style="margin-top:0.5rem;"><a href="/kira/">繁中版</a></p>\n'
        )
        markup = unify.abc.build_page_credits_markup(inner)
        self.assertIn('<a href="https://autodev-ai.com/">AutoDev AI</a>', markup)
        self.assertIn('<a href="/kira/">繁中版</a>', markup)
        self.assertNotIn("style=", markup)
        self.assertTrue(markup.startswith(unify.abc.MARK_DISCLOSURE_START))
        self.assertTrue(markup.endswith(unify.abc.MARK_DISCLOSURE_END))
        self.assertIn('class="v2c-disclosure v2c-page-credits"', markup)

    def test_ai_generated_keyword_is_a_disclosure_keyword(self):
        for phrase in ("AI 生成", "AI生成", "AI-generated", "AI generated"):
            self.assertTrue(
                unify.abc.DISCLOSURE_KEYWORDS_RE.search(phrase),
                f"{phrase!r} should match DISCLOSURE_KEYWORDS_RE",
            )


if __name__ == "__main__":
    unittest.main()
