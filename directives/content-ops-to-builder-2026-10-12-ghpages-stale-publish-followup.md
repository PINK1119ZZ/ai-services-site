# content-ops → builder / Ivan

**Timestamp:** 2026-10-12T00:00:00Z  
**Priority:** urgent  
**Status:** pending

Production site health check on 2026-10-12 still shows stale/incomplete publish output.

## Findings
- Curled all sitemap URLs from `https://autodev-ai.com/sitemap.xml` equivalent local source list.
- Result: **193 URLs returned 200, 27 URLs returned 404**.
- All 27 failing URLs **exist locally in repo**, so this is **not** a missing source-file issue.
- Failure set expanded again with additional newer blog posts (`herdr`, `plugin4shell`, `stepfun`).

## Affected URLs
- https://autodev-ai.com/blog/ai-cost-management-tools-llm-comparison-2026.html
- https://autodev-ai.com/blog/caveman-ai-agent-token-optimization-2026.html
- https://autodev-ai.com/blog/clair-claude-code-watch-app-review-2026.html
- https://autodev-ai.com/blog/claude-haiku-5-5-review-2026.html
- https://autodev-ai.com/blog/cloudflare-acquires-deno-workers-migration-guide-2026.html
- https://autodev-ai.com/blog/cloudflare-web-search-api-ai-agent-review-2026.html
- https://autodev-ai.com/blog/dwarfstar-4-ds4-local-llm-antirez-2026.html
- https://autodev-ai.com/blog/gemini-4-argon-complete-review-2026.html
- https://autodev-ai.com/blog/google-ax-agentic-orchestration-runtime-tutorial-2026.html
- https://autodev-ai.com/blog/gpt-6-1-sol-review-2026.html
- https://autodev-ai.com/blog/gpt-6-sol-luna-claude-opus-5-5-comparison-2026.html
- https://autodev-ai.com/blog/herdr-multi-agent-terminal-orchestrator-2026.html
- https://autodev-ai.com/blog/hindsight-agent-memory-review-2026.html
- https://autodev-ai.com/blog/howseen-ai-review-geo-tracking-2026.html
- https://autodev-ai.com/blog/mistral-large-4-le-chonk-review-2026.html
- https://autodev-ai.com/blog/openai-dots-always-on-agents-review-2026.html
- https://autodev-ai.com/blog/openmontage-ai-video-production-tutorial-2026.html
- https://autodev-ai.com/blog/plugin4shell-ai-coding-agent-security-cve-2026.html
- https://autodev-ai.com/blog/qwen-3-8-flash-next-rtx-4090-tutorial-2026.html
- https://autodev-ai.com/blog/rea-reverse-engineer-ai-agent-mcp-tutorial-2026.html
- https://autodev-ai.com/blog/reflection-beam-501b-open-weight-model-review-2026.html
- https://autodev-ai.com/blog/stepfun-step5-open-weights-oct15-tutorial-2026.html
- https://autodev-ai.com/blog/viktor-ai-coworker-complete-review-2026.html
- https://autodev-ai.com/blog/writesonic-complete-review-2026.html
- https://autodev-ai.com/tools/ai-agent-security-tools-comparison-2026.html
- https://autodev-ai.com/tools/ai-model-comparison.html
- https://autodev-ai.com/tools/chatbot-platform-comparison.html

## Local verification
Checked commit: `ce811023e86f716c5e2a678da37937d07d4744ea`

All affected files exist in repo at this commit.

## Required next action
This still matches a **stale GitHub Pages/static artifact** problem.

Builder: verify publish pipeline / artifact source.  
Ivan: run GitHub Pages `workflow_dispatch` with the latest approved SHA if manual approval is still required.

Preserve the exact approved SHA / workflow instructions in follow-up notes when available.
