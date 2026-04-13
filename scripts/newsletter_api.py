#!/usr/bin/env python3
"""Lightweight newsletter subscription API — saves emails to SQLite."""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json, sqlite3, re, os, datetime

DB_PATH = '/root/ai-services-site/newsletter.db'
PORT = 8891
ALLOWED_ORIGINS = [
    'https://autodev-ai.com',
    'https://pink1119zz.github.io',
    'http://localhost',
    'https://newsletter-api.76.13.219.163.nip.io',
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS subscribers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        source TEXT DEFAULT '',
        subscribed_at TEXT DEFAULT (datetime('now')),
        active INTEGER DEFAULT 1
    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS clicks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        page TEXT,
        ts INTEGER,
        clicked_at TEXT DEFAULT (datetime('now'))
    )''')
    conn.commit()
    conn.close()

class Handler(BaseHTTPRequestHandler):
    def _cors(self, origin=''):
        for allowed in ALLOWED_ORIGINS:
            if origin.startswith(allowed):
                self.send_header('Access-Control-Allow-Origin', origin)
                break
        else:
            self.send_header('Access-Control-Allow-Origin', ALLOWED_ORIGINS[0])
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors(self.headers.get('Origin', ''))
        self.end_headers()

    def do_POST(self):
        origin = self.headers.get('Origin', '')
        if self.path == '/api/subscribe':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8') if length else '{}'
            try:
                data = json.loads(body)
            except:
                self.send_response(400)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'ok': False, 'error': 'Invalid JSON'}).encode())
                return

            email = data.get('email', '').strip().lower()
            source = data.get('source', '')

            # Validate email
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                self.send_response(400)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'ok': False, 'error': 'Invalid email'}).encode())
                return

            # Save to DB
            try:
                conn = sqlite3.connect(DB_PATH)
                conn.execute('INSERT OR IGNORE INTO subscribers (email, source) VALUES (?, ?)', (email, source))
                conn.commit()
                count = conn.execute('SELECT COUNT(*) FROM subscribers WHERE active=1').fetchone()[0]
                conn.close()
                self.send_response(200)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'ok': True, 'count': count}).encode())
            except Exception as e:
                self.send_response(500)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'ok': False, 'error': str(e)}).encode())
        elif self.path == '/api/subscribers/count':
            try:
                conn = sqlite3.connect(DB_PATH)
                count = conn.execute('SELECT COUNT(*) FROM subscribers WHERE active=1').fetchone()[0]
                conn.close()
                self.send_response(200)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'count': count}).encode())
            except Exception as e:
                self.send_response(500)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        elif self.path == '/api/track-click':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8') if length else '{}'
            try:
                data = json.loads(body)
                url = data.get('url', '')[:2000]
                page = data.get('page', '')[:500]
                ts = int(data.get('ts', 0))
                conn = sqlite3.connect(DB_PATH)
                conn.execute('INSERT INTO clicks (url, page, ts) VALUES (?, ?, ?)', (url, page, ts))
                conn.commit()
                conn.close()
            except Exception:
                pass
            self.send_response(200)
            self._cors(origin)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"ok":true}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        origin = self.headers.get('Origin', '')
        if self.path == '/api/subscribers/count':
            try:
                conn = sqlite3.connect(DB_PATH)
                count = conn.execute('SELECT COUNT(*) FROM subscribers WHERE active=1').fetchone()[0]
                conn.close()
                self.send_response(200)
                self._cors(origin)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'count': count}).encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()

        elif self.path == '/dashboard':
            conn = sqlite3.connect(DB_PATH)
            subs = conn.execute('SELECT id,email,source,subscribed_at,active FROM subscribers ORDER BY subscribed_at DESC').fetchall()
            sub_count = conn.execute('SELECT COUNT(*) FROM subscribers WHERE active=1').fetchone()[0]
            click_count = conn.execute('SELECT COUNT(*) FROM clicks').fetchone()[0]
            click_stats = conn.execute('SELECT url, COUNT(*) as cnt FROM clicks GROUP BY url ORDER BY cnt DESC LIMIT 20').fetchall()
            page_stats = conn.execute('SELECT page, COUNT(*) as cnt FROM clicks GROUP BY page ORDER BY cnt DESC LIMIT 20').fetchall()
            clicks_recent = conn.execute('SELECT url,page,clicked_at FROM clicks ORDER BY clicked_at DESC LIMIT 30').fetchall()
            conn.close()
            html = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Dashboard</title>'
            html += '<style>body{font-family:-apple-system,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem;background:#0f0f1a;color:#e2e8f0}'
            html += 'h1{color:#a5b4fc}h2{color:#818cf8;border-bottom:1px solid #333;padding-bottom:0.5rem}'
            html += 'table{width:100%;border-collapse:collapse;margin:1rem 0}th,td{padding:0.5rem;text-align:left;border-bottom:1px solid #1e293b}'
            html += 'th{color:#a5b4fc;font-size:0.85rem}td{color:#94a3b8;font-size:0.9rem;word-break:break-all}'
            html += '.stat{display:inline-block;background:#1e293b;padding:1.5rem 2rem;border-radius:12px;margin:0.5rem;text-align:center}'
            html += '.stat .num{font-size:2rem;font-weight:700;color:#a5b4fc}.stat .label{color:#64748b;font-size:0.85rem}'
            html += '</style></head><body>'
            html += '<h1>\U0001f4ca AutoDev AI Dashboard</h1><div>'
            html += f'<div class="stat"><div class="num">{sub_count}</div><div class="label">\U0001f4e7 \u8a02\u95b1\u8005</div></div>'
            html += f'<div class="stat"><div class="num">{click_count}</div><div class="label">\U0001f517 \u806f\u76df\u9ede\u64ca</div></div></div>'
            html += '<h2>\U0001f4e7 Email \u8a02\u95b1\u8005</h2><table><tr><th>Email</th><th>\u4f86\u6e90</th><th>\u6642\u9593</th></tr>'
            for s in subs:
                html += f'<tr><td>{s[1]}</td><td>{s[2]}</td><td>{s[3]}</td></tr>'
            html += '</table>'
            html += '<h2>\U0001f517 \u806f\u76df\u9023\u7d50\u9ede\u64ca\u6392\u884c</h2><table><tr><th>\u9023\u7d50</th><th>\u9ede\u64ca\u6578</th></tr>'
            for c in click_stats:
                short = c[0][:80]
                html += f'<tr><td>{short}</td><td>{c[1]}</td></tr>'
            html += '</table>'
            html += '<h2>\U0001f4c4 \u9801\u9762\u9ede\u64ca\u6392\u884c</h2><table><tr><th>\u9801\u9762</th><th>\u9ede\u64ca\u6578</th></tr>'
            for p in page_stats:
                html += f'<tr><td>{p[0]}</td><td>{p[1]}</td></tr>'
            html += '</table>'
            html += '<h2>\U0001f550 \u6700\u8fd1\u9ede\u64ca</h2><table><tr><th>\u9023\u7d50</th><th>\u9801\u9762</th><th>\u6642\u9593</th></tr>'
            for c in clicks_recent:
                short = c[0][:60]
                html += f'<tr><td>{short}</td><td>{c[1]}</td><td>{c[2]}</td></tr>'
            html += '</table></body></html>'
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html.encode())
        elif self.path == '/report':
            report_path = '/root/ai-services-site/downloads/income_report.html'
            try:
                with open(report_path, 'r') as rf:
                    report_html = rf.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(report_html.encode())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'Report not found')
        elif self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'ok')
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {args[0]}")

if __name__ == '__main__':
    init_db()
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f'Newsletter API running on port {PORT}')
    server.serve_forever()
