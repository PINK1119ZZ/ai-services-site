import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "build_static.py"
sys.dont_write_bytecode = True


def load_builder():
    spec = importlib.util.spec_from_file_location("build_static", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class StaticBuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve())
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        self.source.mkdir()

    def write(self, relative, content=b""):
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content if isinstance(content, bytes) else content.encode())
        return path

    def make_public_fixture(self):
        self.write(
            "index.html",
            '<link rel="stylesheet" href="/style.css">'
            '<script src="/assets/app.js"></script>'
            '<a href="/blog/page.html#answer">Read</a>',
        )
        self.write("style.css", "body { color: #111; }")
        self.write("assets/app.js", "globalThis.ready = true;")
        self.write("assets/showcase/kira-reel.mp4", b"public-video")
        self.write("assets/private.mp4", b"not-allowlisted")
        self.write("blog/page.html", '<main id="answer">42</main><a href="/legacy-missing.html#old">Legacy</a>')
        self.write("agent-state.json", '{"private":true}')
        self.write("newsletter.db", b"private-db")
        self.write("scripts/operate.py", "raise SystemExit")
        self.write("downloads/income_report.html", "internal")

    def test_build_is_allowlisted_hashed_and_reproducible(self):
        builder = load_builder()
        self.make_public_fixture()
        first = self.base / "dist-a"
        second = self.base / "dist-b"

        builder.build_static(self.source, first)
        builder.build_static(self.source, second)

        self.assertTrue((first / "blog/page.html").is_file())
        self.assertTrue((first / "assets/showcase/kira-reel.mp4").is_file())
        self.assertFalse((first / "assets/private.mp4").exists())
        self.assertFalse((first / "agent-state.json").exists())
        self.assertFalse((first / "newsletter.db").exists())
        self.assertFalse((first / "scripts").exists())
        self.assertFalse((first / "downloads/income_report.html").exists())
        manifest_a = json.loads((first / "static-manifest.json").read_text())
        manifest_b = json.loads((second / "static-manifest.json").read_text())
        self.assertEqual(manifest_a, manifest_b)
        paths = [entry["path"] for entry in manifest_a["files"]]
        self.assertEqual(paths, sorted(paths))
        expected = hashlib.sha256((first / "style.css").read_bytes()).hexdigest()
        style_entry = next(item for item in manifest_a["files"] if item["path"] == "style.css")
        self.assertEqual(style_entry["sha256"], expected)
        self.assertEqual(manifest_a["warnings"][0]["kind"], "source-existing-missing")

    def test_nonempty_output_is_preserved_and_rejected(self):
        builder = load_builder()
        self.make_public_fixture()
        output = self.base / "dist"
        output.mkdir()
        sentinel = output / "keep.txt"
        sentinel.write_text("keep")

        with self.assertRaises(builder.BuildError):
            builder.build_static(self.source, output)
        self.assertEqual(sentinel.read_text(), "keep")

    def test_manifest_and_copy_use_the_same_byte_snapshot(self):
        builder = load_builder()
        self.make_public_fixture()
        output = self.base / "dist"
        original_read = Path.read_bytes
        original_css = (self.source / "style.css").read_bytes()
        changed = False

        def read_then_change(path):
            nonlocal changed
            data = original_read(path)
            if path == self.source / "style.css" and not changed:
                path.write_bytes(b"changed after snapshot")
                changed = True
            return data

        with mock.patch.object(Path, "read_bytes", read_then_change):
            manifest = builder.build_static(self.source, output)

        copied = (output / "style.css").read_bytes()
        entry = next(item for item in manifest["files"] if item["path"] == "style.css")
        self.assertEqual(copied, original_css)
        self.assertEqual(entry["sha256"], hashlib.sha256(copied).hexdigest())

    def test_allowlisted_symlink_is_rejected(self):
        builder = load_builder()
        self.make_public_fixture()
        target = self.base / "outside.js"
        target.write_text("outside")
        (self.source / "assets/link.js").symlink_to(target)

        with self.assertRaises(builder.BuildError):
            builder.build_static(self.source, self.base / "dist")

        output_target = self.base / "output-target"
        output_target.mkdir()
        output_link = self.base / "output-link"
        output_link.symlink_to(output_target, target_is_directory=True)
        with self.assertRaises(builder.BuildError):
            builder.build_static(self.source, output_link)

    def test_symlink_ancestor_escape_is_rejected(self):
        builder = load_builder()
        self.make_public_fixture()
        outside = self.base / "outside"
        outside.mkdir()
        (outside / "index.html").write_text("outside")
        (self.source / "kira").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(builder.BuildError, "allowlisted path has a symlink component"):
            builder.build_static(self.source, self.base / "dist-exact")

        real_parent = self.base / "real-parent"
        shutil.copytree(self.source, real_parent / "source", symlinks=True, ignore=shutil.ignore_patterns("kira"))
        linked_parent = self.base / "linked-parent"
        linked_parent.symlink_to(real_parent, target_is_directory=True)
        with self.assertRaisesRegex(builder.BuildError, "source has a symlink component"):
            builder.build_static(linked_parent / "source", self.base / "dist-source")

        clean_source = self.base / "clean-source"
        shutil.copytree(self.source, clean_source, symlinks=True, ignore=shutil.ignore_patterns("kira"))
        output_parent = self.base / "output-parent"
        output_parent.mkdir()
        output_parent_link = self.base / "output-parent-link"
        output_parent_link.symlink_to(output_parent, target_is_directory=True)
        with self.assertRaisesRegex(builder.BuildError, "output has a symlink component"):
            builder.build_static(clean_source, output_parent_link / "dist")

    def test_reference_to_excluded_source_file_fails_before_copy(self):
        builder = load_builder()
        self.make_public_fixture()
        self.write("index.html", '<img src="/agent-state.json">')
        output = self.base / "dist"

        with self.assertRaises(builder.BuildError):
            builder.build_static(self.source, output)
        self.assertFalse(output.exists())

    def test_missing_reference_on_redesigned_page_fails_before_copy(self):
        builder = load_builder()
        cases = {
            "resource": '<img src="/missing-new.png">',
            "anchor": '<a href="/blog/page.html#missing-new">Missing</a>',
        }
        for page in ("index.html", "contact.html", "en/contact.html"):
            for kind, html in cases.items():
                with self.subTest(page=page, kind=kind):
                    self.source = self.base / f"source-{page.replace('/', '-')}-{kind}"
                    self.source.mkdir()
                    self.make_public_fixture()
                    self.write(page, html)
                    output = self.base / f"dist-{page.replace('/', '-')}-{kind}"
                    with self.assertRaises(builder.BuildError):
                        builder.build_static(self.source, output)
                    self.assertFalse(output.exists())

    def test_fragment_anchor_rejects_name_on_non_anchor_before_copy(self):
        builder = load_builder()
        for tag in ("input", "meta", "form"):
            with self.subTest(tag=tag):
                self.source = self.base / f"source-name-{tag}"
                self.source.mkdir()
                self.make_public_fixture()
                self.write("blog/page.html", f'<{tag} name="answer">')
                output = self.base / f"dist-name-{tag}"

                with self.assertRaisesRegex(builder.BuildError, "missing anchor"):
                    builder.build_static(self.source, output)
                self.assertFalse(output.exists())

    def test_fragment_anchor_accepts_any_id_and_anchor_name(self):
        builder = load_builder()
        cases = {
            "tag-id": '<section id="answer">Target</section>',
            "anchor-name": '<a name="answer">Target</a>',
        }
        for case, html in cases.items():
            with self.subTest(case=case):
                self.source = self.base / f"source-{case}"
                self.source.mkdir()
                self.make_public_fixture()
                self.write("blog/page.html", html)
                output = self.base / f"dist-{case}"

                builder.build_static(self.source, output)
                self.assertTrue((output / "static-manifest.json").is_file())

    def test_traversal_reference_is_rejected(self):
        builder = load_builder()
        self.make_public_fixture()
        self.write("blog/page.html", '<a href="../../outside.html">bad</a>')

        with self.assertRaises(builder.BuildError):
            builder.build_static(self.source, self.base / "dist")


if __name__ == "__main__":
    unittest.main()
