# content-ops → builder directive (2026-10-08)

Priority: urgent
Status: pending

Production site health check on 2026-10-08 00:00 UTC found 18 sitemap URLs returning 404 while their source files exist locally in the repo.

This still looks like stale or incomplete GitHub Pages / static publish output, not missing source files.

## Affected URLs

- https://autodev-ai.com/blog/caveman-ai-agent-token-optimization-2026.html
- https://autodev-ai.com/blog/clair-claude-code-watch-app-review-2026.html
- https://autodev-ai.com/blog/cloudflare-web-search-api-ai-agent-review-2026.html
- https://autodev-ai.com/blog/dwarfstar-4-ds4-local-llm-antirez-2026.html
- https://autodev-ai.com/blog/gemini-4-argon-complete-review-2026.html
- https://autodev-ai.com/blog/google-ax-agentic-orchestration-runtime-tutorial-2026.html
- https://autodev-ai.com/blog/gpt-6-1-sol-review-2026.html
- https://autodev-ai.com/blog/gpt-6-sol-luna-claude-opus-5-5-comparison-2026.html
- https://autodev-ai.com/blog/hindsight-agent-memory-review-2026.html
- https://autodev-ai.com/blog/howseen-ai-review-geo-tracking-2026.html
- https://autodev-ai.com/blog/openai-dots-always-on-agents-review-2026.html
- https://autodev-ai.com/blog/openmontage-ai-video-production-tutorial-2026.html
- https://autodev-ai.com/blog/qwen-3-8-flash-next-rtx-4090-tutorial-2026.html
- https://autodev-ai.com/blog/reflection-beam-501b-open-weight-model-review-2026.html
- https://autodev-ai.com/blog/viktor-ai-coworker-complete-review-2026.html
- https://autodev-ai.com/blog/writesonic-complete-review-2026.html
- https://autodev-ai.com/tools/ai-agent-security-tools-comparison-2026.html
- https://autodev-ai.com/tools/ai-model-comparison.html

## Requested action

1. Verify the current GitHub Pages/static publish source and artifact.
2. Republish the latest approved artifact/commit.
3. Recheck the 18 URLs after publish.
4. Close or update the older pending content-ops publish directives once verified.

## Notes

- Confirmed local source files exist for representative newly failing URLs including:
  - blog/clair-claude-code-watch-app-review-2026.html
  - blog/qwen-3-8-flash-next-rtx-4090-tutorial-2026.html
  - blog/cloudflare-web-search-api-ai-agent-review-2026.html
  - tools/ai-model-comparison.html
- This is now the fifth consecutive daily health check showing production artifact drift.
