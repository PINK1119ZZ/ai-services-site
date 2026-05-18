#!/bin/bash
# Claude Code Agent Skills 繁中工程師包 — 一鍵安裝腳本
# 版本：1.0.0
# 使用方式：bash install.sh [--local]

set -e

SKILLS_DIR="$(dirname "$0")/skills"
GLOBAL_CLAUDE_DIR="$HOME/.claude"
LOCAL_CLAUDE_DIR=".claude"

# 顏色輸出
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo ""
echo "🤖 Claude Code Agent Skills 繁中工程師包 v1.0.0"
echo "================================================"
echo ""

# 判斷安裝模式
if [ "$1" == "--local" ]; then
  INSTALL_DIR="$LOCAL_CLAUDE_DIR"
  echo -e "${YELLOW}📁 安裝模式：專案本地（.claude/ 目錄）${NC}"
else
  INSTALL_DIR="$GLOBAL_CLAUDE_DIR"
  echo -e "${GREEN}📁 安裝模式：全域（~/.claude/ 目錄）${NC}"
fi

# 建立目標目錄
mkdir -p "$INSTALL_DIR"

# 計數器
INSTALLED=0
SKIPPED=0

# 安裝每個 skill
for skill_file in "$SKILLS_DIR"/*.md; do
  skill_name=$(basename "$skill_file")
  target_path="$INSTALL_DIR/$skill_name"
  
  if [ -f "$target_path" ]; then
    echo -e "  ${YELLOW}⚠️  跳過：$skill_name（已存在，使用 --force 強制覆蓋）${NC}"
    SKIPPED=$((SKIPPED + 1))
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
if [ $SKIPPED -gt 0 ]; then
  echo "   跳過：$SKIPPED 個（已存在）"
  echo "   提示：使用 bash install.sh --force 強制覆蓋"
fi
echo ""
echo "🎯 使用方式："
echo "   在 Claude Code 對話中輸入以下指令："
echo ""
echo "   /grill-me        → 嚴格程式碼審查"
echo "   /tdd             → 測試驅動開發引導"
echo "   /to-prd          → 想法轉產品需求文件"
echo "   /explain-code    → 深度程式碼解說（繁中）"
echo "   /security-review → 安全性漏洞掃描"
echo "   /refactor        → 重構建議與評分"
echo "   /api-docs        → API 文件自動生成"
echo "   /debug-expert    → 系統化 Debug 引導"
echo "   /deploy-check    → 上線前安全檢查"
echo "   /taiwan-code-review → 台灣電商/金流專屬審查"
echo ""
echo "📖 更多使用範例請參閱 EXAMPLES.md"
echo ""
