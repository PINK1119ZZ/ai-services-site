#!/bin/bash
# LINE Bot n8n 模板包安裝腳本
# 將所有 workflow JSON 複製到 n8n 匯入目錄

N8N_IMPORT_DIR="${HOME}/.n8n/workflows"
mkdir -p "$N8N_IMPORT_DIR"

for f in workflows/*.json; do
  cp "$f" "$N8N_IMPORT_DIR/"
  echo "✅ 已複製：$f"
done

echo ""
echo "完成！請前往 n8n → Workflows → Import from File 匯入上述檔案。"
echo "或直接從 ~/.n8n/workflows/ 目錄選取。"
