#!/usr/bin/env python3
"""IndexNow auto-submit: push new/updated URLs to Bing/Yandex for faster indexing."""
import json, os, glob, time, requests

KEY = "d4e8f2a1b5c9e3f7a0b6d2c8e4f1a5b9"
ENDPOINT = "https://api.indexnow.org/indexnow"
YANDEX_ENDPOINT = "https://yandex.com/indexnow"
STATE_FILE = "/root/ai-services-site/scripts/.indexnow_state.json"

SITES = [
    {
        "host": "autodev-ai.com",
        "key_location": f"https://autodev-ai.com/{KEY}.txt",
        "patterns": [
            ("/root/ai-services-site/blog/*.html", "https://autodev-ai.com/blog/"),
            ("/root/ai-services-site/en/blog/*.html", "https://autodev-ai.com/en/blog/"),
        ]
    },
    {
        "host": "pink1119zz.github.io",
        "key_location": f"https://pink1119zz.github.io/ai-tools-tw/{KEY}.txt",
        "patterns": [
            ("/root/ai-tools-tw/blog/*.html", "https://pink1119zz.github.io/ai-tools-tw/blog/"),
        ]
    },
    {
        "host": "pink1119zz.github.io",
        "key_location": f"https://pink1119zz.github.io/ai-tools-en/{KEY}.txt",
        "patterns": [
            ("/root/ai-tools-en/posts/*.html", "https://pink1119zz.github.io/ai-tools-en/posts/"),
        ]
    },
]

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"submitted": {}}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def submit_urls(site, new_urls):
    payload = {
        "host": site["host"],
        "key": KEY,
        "keyLocation": site["key_location"],
        "urlList": new_urls
    }
    # Try primary endpoint
    try:
        r = requests.post(ENDPOINT, json=payload, timeout=10)
        if r.status_code in (200, 202):
            print(f"[OK] {site['host']}: {len(new_urls)} URLs submitted via api.indexnow.org (HTTP {r.status_code})")
            return True
        elif r.status_code == 403:
            # Bing requires site verification; fall back to Yandex
            print(f"[WARN] {site['host']}: api.indexnow.org returned 403 (site not verified in Bing). Trying Yandex...")
            r2 = requests.post(YANDEX_ENDPOINT, json=payload, timeout=10)
            if r2.status_code in (200, 202):
                print(f"[OK] {site['host']}: {len(new_urls)} URLs submitted via Yandex IndexNow (HTTP {r2.status_code})")
                return True
            else:
                print(f"[ERR] {site['host']}: Yandex also failed (HTTP {r2.status_code}) - {r2.text[:200]}")
                return False
        else:
            print(f"[ERR] {site['host']}: HTTP {r.status_code} - {r.text[:200]}")
            return False
    except Exception as e:
        print(f"[ERR] {site['host']}: {e}")
        return False

def main():
    state = load_state()
    submitted = state.get("submitted", {})

    for site in SITES:
        new_urls = []
        for pattern, base_url in site["patterns"]:
            for filepath in glob.glob(pattern):
                fname = os.path.basename(filepath)
                if fname == "index.html":
                    continue
                url = base_url + fname
                mtime = os.path.getmtime(filepath)
                prev_mtime = submitted.get(url, 0)
                if mtime > prev_mtime:
                    new_urls.append(url)
                    submitted[url] = mtime

        if new_urls:
            ok = submit_urls(site, new_urls)
            if ok:
                for u in new_urls:
                    print(f"   -> {u}")
            else:
                # Roll back state so they retry next run
                for u in new_urls:
                    submitted.pop(u, None)
        else:
            print(f"[SKIP] {site['host']}: no new URLs")

    state["submitted"] = submitted
    state["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")
    save_state(state)

if __name__ == "__main__":
    main()
