import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import apply_blog_chrome as chrome  # noqa: E402


class DisclosureBoundaryTest(unittest.TestCase):
    def check(self, footer_inner, text, expected):
        self.assertIs(chrome.disclosure_is_whole_sentence(footer_inner, text), expected)

    def test_sentence_cut_at_link_start_is_rejected(self):
        self.check('<p>本文含<a href="/d">聯盟連結</a>，點擊可能獲得佣金。</p>', "聯盟連結", False)

    def test_english_sentence_cut_at_link_is_rejected(self):
        self.check('<p>This article contains <a href="/d">affiliate links</a>. We may earn a commission.</p>', "affiliate links", False)

    def test_dropped_inline_prefix_is_rejected(self):
        self.check("<p><strong>注意</strong>本文含聯盟連結。</p>", "本文含聯盟連結。", False)

    def test_sentence_after_site_link_is_accepted(self):
        self.check('<p>© AutoDev <a href="/p">隱私政策</a>\n本文含聯盟連結，不影響價格。</p>', "本文含聯盟連結，不影響價格。", True)

    def test_sentence_after_copyright_is_accepted(self):
        self.check("<p>&copy; 2026 AutoDev AI. 本文含聯盟連結，不影響價格。</p>", "本文含聯盟連結，不影響價格。", True)


if __name__ == "__main__":
    unittest.main()
