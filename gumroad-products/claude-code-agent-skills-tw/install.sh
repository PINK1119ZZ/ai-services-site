#!/bin/bash
# Claude Code Agent Skills 繁中工程師包 — 一鍵安裝腳本
# 版本：2.0.0
# 使用方式：bash install.sh [--local] [--force]

set -e

SKILLS_DIR="$(dirname "$0")/skills"
GLOBAL_CLAUDE_DIR="$HOME/.claude"
LOCAL_CLAUDE_DIR=".claude"
FORCE=0

# 顏色輸出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo ""
echo "🤖 Claude Code Agent Skills 繁中工程師包 v2.0.0"
echo "================================================"
echo ""

# 解析參數
INSTALL_DIR="$GLOBAL_CLAUDE_DIR"
for arg in "$@"; do
  case $arg in
    --local)
      INSTALL_DIR="$LOCAL_CLAUDE_DIR"
      echo -e "${YELLOW}📁 安裝模式：專案本地（.claude/ 目錄）${NC}"
      ;;
    --force)
      FORCE=1
      echo -e "${BLUE}⚡ 強制覆蓋模式：已存在的 Skills 將被更新${NC}"
      ;;
  esac
done

if [ "$INSTALL_DIR" == "$GLOBAL_CLAUDE_DIR" ] && [ $FORCE -eq 0 ]; then
  echo -e "${GREEN}📁 安裝模式：全域（~/.claude/ 目錄）${NC}"
fi

# 建立目標目錄
mkdir -p "$INSTALL_DIR"

# 計數器
INSTALLED=0
UPDATED=0
SKIPPED=0

# 安裝每個 skill
for skill_file in "$SKILLS_DIR"/*.md; do
  skill_name=$(basename "$skill_file")
  target_path="$INSTALL_DIR/$skill_name"

  if [ -f "$target_path" ] && [ $FORCE -eq 0 ]; then
    echo -e "  ${YELLOW}⚠️  跳過：$skill_name（已存在，使用 --force 強制覆蓋）${NC}"
    SKIPPED=$((SKIPPED + 1))
  elif [ -f "$target_path" ] && [ $FORCE -eq 1 ]; then
    cp "$skill_file" "$target_path"
    echo -e "  ${BLUE}🔄 更新：$skill_name${NC}"
    UPDATED=$((UPDATED + 1))
  else
    cp "$skill_file" "$target_path"
    echo -e "  ${GREEN}✅ 安裝：$skill_name${NC}"
    INSTALLED=$((INSTALLED + 1))
  fi
done

echo ""
echo "================================================"
echo -e "${GREEN}✨ 安裝完成！${NC}"
echo "   已安裝：$INSTALLED 個 Skills"
if [ $UPDATED -gt 0 ]; then
  echo "   已更新：$UPDATED 個 Skills"
fi
if [ $SKIPPED -gt 0 ]; then
  echo "   跳過：$SKIPPED 個（已存在）"
  echo "   提示：使用 bash install.sh --force 強制覆蓋"
fi
echo ""
echo "🎯 使用方式（在 Claude Code 對話中輸入）："
echo ""
echo "   ── 工程品質 ──"
echo "   /grill-me              → 嚴格程式碼審查"
echo "   /tdd                   → 測試驅動開發引導"
echo "   /to-prd                → 想法轉產品需求文件"
echo "   /explain-code          → 深度程式碼解說（繁中）"
echo "   /security-review       → 安全性漏洞掃描"
echo "   /refactor              → 重構建議與評分"
echo "   /api-docs              → API 文件自動生成"
echo "   /debug-expert          → 系統化 Debug 引導"
echo "   /deploy-check          → 上線前安全檢查"
echo "   /taiwan-code-review    → 台灣電商/金流專屬審查"
echo ""
echo "   ── v2.0 新增 ──"
echo "   /taste-skill           → AI 前端設計品質守門員"
echo "   /stop-slop             → AI 寫作品質過濾器"
echo "   /cybersecurity-review  → 資安漏洞審查（MITRE ATT&CK）"
echo ""
echo "📖 更多使用範例請參閱 EXAMPLES.md"
echo ""
