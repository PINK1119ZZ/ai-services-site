# Historical maintainability repair evidence

Date: 2026-09-21 (Asia/Taipei)

> Historical scope: this record covers `ba7980a12de0fdb2c010362a4a81ae05eefab487` → `2e3fd2b2fa07d52c438834ed2574abd165d7767d`. Its 1-pass/2-Contact-fail commercial result, 5-test SEO result, and other counts below belong to that snapshot and are not current-candidate claims. See [`docs/AUTODEV_2_OPERATIONS.md`](docs/AUTODEV_2_OPERATIONS.md) for current status and remaining release work.

## Input snapshot and scope

- Candidate baseline: `ba7980a12de0fdb2c010362a4a81ae05eefab487`.
- Scope is exactly six files: `AGENTS.md`, `CLAUDE.md`, `docs/AUTODEV_2_OPERATIONS.md`, two named scripts, and this evidence file.
- No Contact, HTML, static builder, dependency, production configuration, credential file, other worktree, or global rule was changed.
- Neither script main path was executed or imported. No network request or external message was made.

## Red evidence

- A value-redacting AST inspection found `get_tg_token` returning a string literal at line 24 of `scripts/daily_ga4_report.py` and `GPTPROTO_KEY` assigned a string literal at line 7 of `scripts/fb_reply_comments.py`.
- Redacted gitleaks reported one finding in `scripts/fb_reply_comments.py` before the repair. It did not identify the other literal; AST inspection remained the authoritative check for both contract-named expressions.

## Changes

- Replaced the generic OpenClaw workspace template with a concise AutoDev project entry covering architecture, Telegram-first positioning, project budget positions, truth boundaries, bilingual/shared asset scope, data separation, static allowlisting, safe defaults, verification, and separate publication approval.
- Reduced `CLAUDE.md` to a pointer to `AGENTS.md` as the single project-specific rule source. It does not grant additional permissions.
- Added candidate operations documentation using `source` and `target` terms without private host addresses. It records current GitHub Pages behavior, incomplete cutover, safe artifact preview, test commands, known Contact failures, and pending seven-width/Lighthouse checks.
- `get_tg_token` now reads required `AUTODEV_REPORT_TG_TOKEN` through `os.environ[...]` with no fallback.
- `GPTPROTO_KEY` now reads required `AUTODEV_FB_MODEL_API_KEY` through `os.environ[...]` with no fallback.

## Validation

- Corrected scoped AST check: both target expressions are exact `os.environ[...]` lookups; no fallback is present. The initial validator was intentionally recorded as a false positive because it scanned constant returns outside `get_tg_token`; narrowing it to that function passed.
- `PYTHONPYCACHEPREFIX=/private/tmp/autodev-maint-pycache python3 -m py_compile ...`: passed for both scripts without writing cache files into the repository.
- Redacted gitleaks on each changed script: no leaks found.
- `npm run test:seo`: 5 passed, 0 failed.
- `npm run test:static`: 8 passed, 0 failed.
- Commercial test: 1 passed, 2 failed, unchanged. The two failures remain the legacy Contact asset and prohibited copy checks.
- `git diff --check`: passed.

## Limits and required follow-up

- Removing literals from the current candidate does not revoke previously exposed credentials or remove them from Git history.
- The credential owner must revoke or rotate the old values in the relevant services. This local slice did not read, print, transmit, or use those values.
- Production environment variables have not been updated or tested. Missing variables now fail explicitly when the affected script path is used.
- AutoDev 2.0, Pi integration, target-host cutover, seven-width browser review, Lighthouse, CI integration, and public release remain incomplete.
