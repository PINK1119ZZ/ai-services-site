# content-ops → builder / Ivan

**Timestamp:** 2026-10-18T00:01:26Z  
**Priority:** urgent  
**Status:** pending

Production site health check on 2026-10-18 still shows stale/incomplete publish output, and the failure set grew again.

## Findings
- Curled all sitemap URLs from local `sitemap.xml` (**234 URLs total**).
- Result: **193 URLs returned 200, 41 URLs returned 404**.
- All 41 failing URLs **exist locally in repo**, so this is still **not** a missing source-file issue.
- Failure count increased from **37 → 41** since the 2026-10-17 check.
- Newly failing recent production URLs now include:
  - `cert-in-ai-agent-security-2026-enterprise-guide`
  - `openai-gpt56-sol-unauthorized-eth-wallet-ai-safety-2026`
  - `ai-subscription-cost-calculator`
  - `geo-tools-comparison-2026`
- Previously failing recent posts/tools are still missing in production, including:
  - `anthropic-ai-iot-botnet-warning-2026`
  - `articos-mcp-simulated-user-research-2026`
  - `ghost-core-personal-ai-computer-review-2026`
  - `typesafe-ai-jev-system-one-model-tutorial-2026`
  - `ai-code-review-comparison`
- This still strongly indicates the published static artifact / GitHub Pages output is stale or incomplete.

## Affected URLs
- https://autodev-ai.com/blog/ai-cost-management-tools-llm-comparison-2026.html
- https://autodev-ai.com/blog/anthropic-ai-iot-botnet-warning-2026.html
- https://autodev-ai.com/blog/artcraft-storytold-rust-creative-suite-2026.html
- https://autodev-ai.com/blog/articos-mcp-simulated-user-research-2026.html
- https://autodev-ai.com/blog/caveman-ai-agent-token-optimization-2026.html
- https://autodev-ai.com/blog/cert-in-ai-agent-security-2026-enterprise-guide.html
- https://autodev-ai.com/blog/clair-claude-code-watch-app-review-2026.html
- https://autodev-ai.com/blog/claude-haiku-5-5-review-2026.html
- https://autodev-ai.com/blog/cloudflare-acquires-deno-workers-migration-guide-2026.html
- https://autodev-ai.com/blog/cloudflare-web-search-api-ai-agent-review-2026.html
- https://autodev-ai.com/blog/diagram-design-ai-agent-skill-claude-code-2026.html
- https://autodev-ai.com/blog/dwarfstar-4-ds4-local-llm-antirez-2026.html
- https://autodev-ai.com/blog/gemini-4-argon-complete-review-2026.html
- https://autodev-ai.com/blog/ghost-core-personal-ai-computer-review-2026.html
- https://autodev-ai.com/blog/google-ax-agentic-orchestration-runtime-tutorial-2026.html
- https://autodev-ai.com/blog/gpt-6-1-sol-review-2026.html
- https://autodev-ai.com/blog/gpt-6-sol-luna-claude-opus-5-5-comparison-2026.html
- https://autodev-ai.com/blog/herdr-multi-agent-terminal-orchestrator-2026.html
- https://autodev-ai.com/blog/hindsight-agent-memory-review-2026.html
- https://autodev-ai.com/blog/howseen-ai-review-geo-tracking-2026.html
- https://autodev-ai.com/blog/mistral-large-4-le-chonk-review-2026.html
- https://autodev-ai.com/blog/nvidia-reflection-ai-acquisition-beam-model-2026.html
- https://autodev-ai.com/blog/openai-dots-always-on-agents-review-2026.html
- https://autodev-ai.com/blog/openai-gpt56-sol-unauthorized-eth-wallet-ai-safety-2026.html
- https://autodev-ai.com/blog/openmontage-ai-video-production-tutorial-2026.html
- https://autodev-ai.com/blog/openseo-self-hosted-seo-platform-tutorial-2026.html
- https://autodev-ai.com/blog/plugin4shell-ai-coding-agent-security-cve-2026.html
- https://autodev-ai.com/blog/qwen-3-8-flash-next-rtx-4090-tutorial-2026.html
- https://autodev-ai.com/blog/rea-reverse-engineer-ai-agent-mcp-tutorial-2026.html
- https://autodev-ai.com/blog/reflection-beam-501b-open-weight-model-review-2026.html
- https://autodev-ai.com/blog/stepfun-step5-open-weights-oct15-tutorial-2026.html
- https://autodev-ai.com/blog/telegram-cve-2026-10718-account-security-guide.html
- https://autodev-ai.com/blog/typesafe-ai-jev-system-one-model-tutorial-2026.html
- https://autodev-ai.com/blog/viktor-ai-coworker-complete-review-2026.html
- https://autodev-ai.com/blog/writesonic-complete-review-2026.html
- https://autodev-ai.com/tools/ai-agent-security-tools-comparison-2026.html
- https://autodev-ai.com/tools/ai-code-review-comparison.html
- https://autodev-ai.com/tools/ai-model-comparison.html
- https://autodev-ai.com/tools/ai-subscription-cost-calculator.html
- https://autodev-ai.com/tools/chatbot-platform-comparison.html
- https://autodev-ai.com/tools/geo-tools-comparison-2026.html

## Local verification
Checked against current repo working tree on 2026-10-18 00:01 UTC.

All affected files exist locally in the repository.

## Required next action
Builder: verify publish pipeline / artifact source, especially whitelist build output and Pages artifact completeness.

Ivan: trigger GitHub Pages `workflow_dispatch` with the latest approved SHA if manual approval is still required, then confirm the deployed commit SHA matches repo `main`.

Please preserve the exact approved SHA / workflow run link / artifact source in follow-up notes.
