#!/usr/bin/env python3
"""定期檢查所有聯盟連結是否有效（v2: 支援 403 bot-protection）"""
import requests, json, time

LINKS = {
    "DigitalOcean": "https://m.do.co/c/6121a295f624",
    "Hahow": "https://abzcoupon.com/track/clicks/4850/c627c2bc9b0125d8fa8cec23d62e9842226e4edf2aabebf00f65b213234652eed671a3ea103a9e71",
    "Systeme.io": "https://systeme.io/?sa=sa0087788052d81d9e6cfd5c00f0773e37e01e27f",
    "UltaHost": "https://aftck.com/track/clicks/9568/c627c2bc9b0126dafe89ec23d62e9842226e4edf2aabebfd0266ba13234652eed671a3ea103a9e71",
    "DataCamp": "https://afflink.one/s/aavAC",
    "Cloudways": "https://vbtrax.com/track/clicks/9532/c627c2bc9b0126dafe8fec2bd32e9d452c6644ca63bcb0f90067b504641200a8cd3ea4e4566e9f663499abdb4aee7abb970d",
    "CapCut": "https://vbtrax.com/track/clicks/9453/c627c2bc9b0126dafe8dec2bd32e9d452d6745c963bcb0f90067b504641200a8cd3ea5e2576e9f663499abdb4aee7abb970d",
    "NordVPN": "https://onelink.one/s/7WSzC",
    "Decodo": "https://afflink.one/s/rrR3t",
    "Gumroad": "https://xiaofan8.gumroad.com/l/kknad",
}

# 403 = bot protection, still OK if redirect landed on correct domain
EXPECTED_DOMAINS = {
    "DataCamp": "datacamp.com",
    "Cloudways": "cloudways.com",
    "NordVPN": "nordvpn.com",
    "UltaHost": "ultahost.com",
    "Decodo": "decodo.",
    "CapCut": "capcut.com",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"}

results = []
errors = []

for name, url in LINKS.items():
    try:
        r = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        status = r.status_code
        final_url = r.url
        
        # Check if redirect landed on expected domain (403 = bot protection, OK)
        if status == 403 and name in EXPECTED_DOMAINS:
            if EXPECTED_DOMAINS[name] in final_url:
                results.append(f"✅ {name}: HTTP {status} (bot-protection, redirect OK)")
                continue
        
        if status >= 400 and "404" in final_url:
            results.append(f"❌ {name}: HTTP {status} -> {final_url[:80]}")
            errors.append(name)
        elif status < 500:
            results.append(f"✅ {name}: HTTP {status}")
        else:
            results.append(f"❌ {name}: HTTP {status}")
            errors.append(name)
    except Exception as e:
        results.append(f"❌ {name}: {str(e)[:60]}")
        errors.append(name)

print(f"=== 聯盟連結檢查 {time.strftime('%Y-%m-%d %H:%M')} ===")
for r in results:
    print(r)

if errors:
    print(f"\n⚠️ {len(errors)} 個連結異常: {', '.join(errors)}")
else:
    print(f"\n✅ 全部 {len(LINKS)} 個連結正常")
