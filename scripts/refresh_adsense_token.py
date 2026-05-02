#!/usr/bin/env python3
"""
Refresh AutoDev AI 的 AdSense OAuth token（手动跑一次即可）。

用法：
  1. 在 macOS 本地 cd 到 /Users/pink1119zz/Desktop/claude/ai-services-site/
  2. pip install google-auth-oauthlib google-api-python-client
  3. python3 /tmp/refresh_adsense.py
  4. 浏览器会跳出来，用你的 Google 帐号（有 AdSense 权限的那个）授权
  5. 完成后会印出新的 refresh_token，复制贴回 VPS

如果你想跳过这步直接让我跑：你只需要 (a) 复制贴 OAuth Client ID + Secret 给我（或确认本机 ~/.config/gcloud 里已经有），然后我可以全自动接管。
"""
import json
import sys
from pathlib import Path

# 你 VPS 上现有 token.json 的 client_id（从 ssh 拉到本地用的）
# 如果没有 client_secret，需要去 Google Cloud Console 重新下载 OAuth client JSON
CLIENT_CONFIG_PATH = Path.home() / "adsense-oauth-client.json"

if not CLIENT_CONFIG_PATH.exists():
    print(f"""
❌ 找不到 {CLIENT_CONFIG_PATH}

请先去 Google Cloud Console 下载 OAuth client JSON：
  1. 开 https://console.cloud.google.com/apis/credentials
  2. 选你 AdSense 用的 project
  3. 找到 OAuth 2.0 Client ID（应该叫 'AdSense Reporter' 或类似的）
  4. 点右边铅笔编辑 → 「应用程序类型」如果是 Web app 要先建一个 Desktop app type 的新 client
  5. 下载 JSON → 存到 {CLIENT_CONFIG_PATH}
  6. 重跑这个脚本
""")
    sys.exit(1)

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/adsense.readonly']

flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_CONFIG_PATH), SCOPES)
creds = flow.run_local_server(port=0)

token_data = {
    "token": creds.token,
    "refresh_token": creds.refresh_token,
    "token_uri": creds.token_uri,
    "client_id": creds.client_id,
    "client_secret": creds.client_secret,
    "scopes": list(creds.scopes),
}

out_path = Path("/tmp/adsense-token-new.json")
out_path.write_text(json.dumps(token_data, indent=2))

print(f"\n✅ 新 token 已存到 {out_path}")
print(f"\n下一步：\n  scp {out_path} root@76.13.219.163:/root/.openclaw/adsense-token.json\n")
print("然后在 VPS 跑：python3 /root/ai-services-site/scripts/gsc_reporter.py 验证")
