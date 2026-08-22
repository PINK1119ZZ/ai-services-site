# 安全基線掃描

**分類：** 安全測試自動化 | **框架：** CIS Benchmarks  
**適用平台：** Claude Code、Cursor、Copilot

## 用途
對伺服器、容器、雲端環境執行 CIS Benchmark 基線掃描，識別配置偏差。

## 使用方式
```
請協助對 [環境類型] 執行安全基線掃描：
1. 選擇對應的 CIS Benchmark（Ubuntu/Windows/K8s/Docker）
2. 生成掃描腳本（bash/PowerShell）
3. 識別 Level 1（最小影響）vs Level 2（深度防禦）項目
4. 評估每個發現的修復優先順序
5. 生成修復腳本（批量自動化）
6. 設計定期基線驗證 cron job
```

## CIS Ubuntu 22.04 快速基線
```bash
# 安裝 CIS-CAT（免費版）或使用 OpenSCAP
apt-get install -y openscap-scanner
oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis_level1_server \
  --results-arf results.xml \
  --report report.html \
  /usr/share/xml/scap/ssg/content/ssg-ubuntu2204-ds.xml

# 快速手動基線檢查
echo "=== SSH 安全配置 ===" 
grep -E "^PermitRootLogin|^PasswordAuthentication|^X11Forwarding" /etc/ssh/sshd_config

echo "=== 防火牆狀態 ==="
ufw status verbose

echo "=== 監聽端口 ==="
ss -tlnp
```

## 參考框架
- CIS Benchmarks（cisecurity.org）
- OpenSCAP / SCAP Security Guide
- InSpec（Chef 合規即程式碼）
- AWS Config Rules（雲端基線）
