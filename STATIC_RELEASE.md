# Static release artifact

`scripts/build_static.py` creates a deterministic static artifact from an explicit allowlist. It does not deploy, start a server, alter the source tree, or remove an existing output.

```bash
npm run test:static
npm run build:static -- --output /absolute/path/to/new-dist
```

The output path is required, must be outside the source tree, and must be absent or empty. A non-empty directory is refused without deleting or overwriting any file.

## Included surface

- Explicit root public pages and files: commercial, legal and product HTML; `404.html`; `CNAME`; root CSS/JS; icons; and public SEO files.
- Public files with approved static extensions under `blog/`, `en/`, `tools/`, and `assets/`.
- `downloads/index.html`, `downloads/ai-tools-guide-2026.html`, and `kira/index.html`.
- Four exact public Reel files referenced by `ai-model.html`: `assets/showcase/kira-reel.mp4`, `kira-reel-2.mp4`, `kira-reel-3.mp4`, and `kira-reel-4.mp4`. No video wildcard is enabled.

The root verification text file remains excluded pending ownership verification. Product archives are also excluded; the current public HTML does not link them as downloadable resources.

## Safety and verification

Every selected entry must be a regular file. Symlinks in any existing source, output, public-tree, or exact-file path component; path traversal; references to source files excluded by the allowlist; and non-empty output directories stop the build before copying. Operational state, databases, WAL/SHM files, environment files, source scripts, internal Markdown, tests, reports, backups, and `downloads/income_report.html` are not selected.

Each selected file is read once; that byte snapshot is used for both its SHA-256 and output, so a source change during the build cannot produce a manifest/copy mismatch. `static-manifest.json` contains the sorted file list, byte size, SHA-256, and deterministic warnings.

The ten redesigned commercial pages have a strict link boundary: a missing local target or anchor stops the build. Outside that changed-page set, a target already absent from the source is recorded as `source-existing-missing`, and a missing anchor as `source-existing-anchor`. A reference to a file that exists in source but is excluded is always a release error, because the build would introduce a broken resource.

Serve only the generated output directory during preview. Do not run an HTTP directory server from the repository root.
