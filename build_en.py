#!/usr/bin/env python3
"""
Build script: generate /en/ static English pages from Chinese HTML.
Reads data-en attributes, replaces content, updates SEO meta, adds hreflang.
Run: python3 build_en.py
"""
import os, re, copy
from bs4 import BeautifulSoup, NavigableString

SITE = '/Users/pink1119zz/Desktop/claude/ai-services-site'
BASE_URL = 'https://autodev-ai.com'

# English SEO meta for each page
EN_META = {
    'index.html': {
        'title': 'AI Bot Development | Smart Customer Service, Booking Bots, Workflow Automation — AutoDev AI',
        'description': 'Professional AI bot development — LINE, Telegram, Discord, Slack, Web Chat. Smart customer service, booking systems, workflow automation. From $250, done in 2 weeks.',
        'og_title': 'AI Bot Development | Smart Customer Service & Automation — AutoDev AI',
        'og_description': 'Professional AI bot development from $250. Smart customer service, booking bots, workflow automation. Done in 2 weeks.',
    },
    'services.html': {
        'title': 'AI Bot Development Services | Chatbots, Smart CS, Automation — AutoDev AI',
        'description': 'AI chatbot development for LINE, Telegram, Discord, Slack, Web Chat. Smart customer service from $400, booking bots, workflow automation. Free consultation.',
        'og_title': 'AI Bot Development Services — AutoDev AI',
        'og_description': 'AI chatbot from $250, smart customer service from $400. LINE, Telegram, Discord, Slack, Web Chat.',
    },
    'pricing.html': {
        'title': 'AI Bot Pricing | Starter $250, Pro $500 — Transparent Pricing | AutoDev AI',
        'description': 'AI bot development pricing: Starter from $250, Pro from $500, Enterprise custom. Add-on services a la carte. Monthly maintenance from $65/mo. Free consultation.',
        'og_title': 'AI Bot Pricing — From $250, Transparent | AutoDev AI',
        'og_description': 'Starter from $250, Pro from $500, Enterprise custom. Free consultation, no hidden fees.',
    },
    'contact.html': {
        'title': 'Free Consultation | AI Bot Development Quote — AutoDev AI',
        'description': 'Free AI bot development consultation. Contact via LINE, Telegram, or Email. Smart customer service, booking systems, workflow automation. 30-min free assessment.',
        'og_title': 'Free Consultation — AI Bot Development | AutoDev AI',
        'og_description': 'Free AI bot consultation. 30-min assessment. No satisfaction, no charge.',
    },
    'about.html': {
        'title': 'About AutoDev AI | AI Automation Engineer — Bot Development Expert',
        'description': 'AutoDev AI founder Ivan built 20+ AI Agent automation systems. Specializing in chatbot development, AI customer service. AI-native development, done in 2 weeks.',
        'og_title': 'About AutoDev AI — AI Automation Engineer',
        'og_description': 'Built 20+ AI Agent systems. Specializing in chatbot development & AI customer service. Done in 2 weeks.',
    },
    'demo.html': {
        'title': 'Free AI Customer Service Demo | Try Smart Chatbot Now — AutoDev AI',
        'description': 'Try our AI smart customer service for free. Chat with the AI bot right on this page. Experience automated booking, smart replies, and instant notifications.',
        'og_title': 'Free AI Customer Service Demo — AutoDev AI',
        'og_description': 'Try AI smart customer service for free. 30 seconds to experience the power of automation.',
    },
    'portfolio.html': {
        'title': 'Portfolio | AI Bot & Automation Case Studies — AutoDev AI',
        'description': 'AI bot development case studies: brand websites, LINE AI smart customer service, LIFF forms, Telegram notification bots. From requirements to launch in 2 weeks.',
        'og_title': 'Portfolio — AI Bot Case Studies | AutoDev AI',
        'og_description': 'AI bot development case studies: websites, LINE AI smart CS, LIFF forms, Telegram bots. 2 weeks delivery.',
    },
    'blog/index.html': {
        'title': 'Blog — AI Automation & Bot Development Knowledge | AutoDev AI',
        'description': 'AutoDev AI blog: chatbot development tutorials, AI customer service guides, booking system reviews, small business automation tools.',
        'og_title': 'Blog — AI Automation & Bot Development | AutoDev AI',
        'og_description': 'Bot development tutorials, AI customer service guides, booking system reviews, automation tools.',
    },
    'blog/line-bot-cost.html': {
        'title': 'How Much Does Bot Development Cost? 2026 Pricing & Feature Comparison | AutoDev AI',
        'description': 'Complete chatbot development pricing: basic auto-reply from $250, AI smart customer service from $400. Feature comparison, money-saving tips, and common pitfalls.',
        'og_title': 'Bot Development Cost — 2026 Pricing Guide | AutoDev AI',
        'og_description': 'Basic auto-reply from $250, AI smart CS from $400. Complete pricing breakdown & tips.',
    },
    'blog/line-bot-tutorial-2026.html': {
        'title': 'LINE Bot Development Tutorial: Complete Guide from Zero to Launch (2026) | AutoDev AI',
        'description': 'Build your own LINE bot from scratch. Complete tutorial covering LINE Developer setup, Messaging API, common features. Evaluate DIY vs outsourcing.',
        'og_title': 'LINE Bot Tutorial — Zero to Launch (2026) | AutoDev AI',
        'og_description': 'Complete LINE bot development guide. From setup to launch, evaluate DIY vs outsourcing.',
    },
    'blog/ai-customer-service-line.html': {
        'title': 'What Is AI Customer Service? Complete Smart CS Guide (2026) | AutoDev AI',
        'description': 'Replace repetitive CS work with AI: GPT/Claude-powered smart customer service, available 24/7. Complete guide with implementation steps and cost analysis.',
        'og_title': 'AI Customer Service Guide (2026) | AutoDev AI',
        'og_description': 'GPT/Claude-powered 24/7 smart CS. Complete guide with implementation steps & cost analysis.',
    },
    'blog/line-bot-booking-system.html': {
        'title': 'Booking System: Auto-Scheduling for Salons, Clinics & Restaurants | AutoDev AI',
        'description': 'Automated booking bot handles reservations 24/7, reduces no-shows, boosts return visits. Full feature comparison and industry analysis for salons, clinics, restaurants.',
        'og_title': 'Booking Bot — Auto-Scheduling Solution | AutoDev AI',
        'og_description': 'Automated booking bot: 24/7 reservations, reduce no-shows, boost return visits.',
    },
    'blog/small-business-automation.html': {
        'title': 'Small Businesses Can Automate Too! 5 AI Tools to Save Time & Cut Costs | AutoDev AI',
        'description': 'No big budget needed for digital transformation! 5 practical AI automation tools that save small businesses 40+ hours per month. From auto-reply to AI reports.',
        'og_title': '5 AI Automation Tools for Small Businesses | AutoDev AI',
        'og_description': '5 practical AI tools that save 40+ hours/month. From auto-reply to AI reports.',
    },
}

# Nav translations
NAV_ZH_TO_EN = {
    '服務': 'Services',
    '作品': 'Portfolio',
    '方案': 'Pricing',
    '部落格': 'Blog',
    '關於': 'About',
    '體驗 Demo': 'Try Demo',
    '免費諮詢': 'Consult',
}

def get_en_path(rel_path):
    """Get the /en/ version URL path."""
    if rel_path == 'index.html':
        return '/en/'
    elif rel_path.startswith('blog/'):
        return f'/en/{rel_path}'
    else:
        return f'/en/{rel_path}'

def get_zh_path(rel_path):
    """Get the Chinese version URL path."""
    if rel_path == 'index.html':
        return '/'
    elif rel_path.startswith('blog/') and rel_path.endswith('index.html'):
        return '/blog/'
    else:
        return f'/{rel_path}'

def process_file(rel_path):
    filepath = os.path.join(SITE, rel_path)
    if not os.path.exists(filepath):
        print(f'  SKIP (not found): {rel_path}')
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Change lang
    if soup.html:
        soup.html['lang'] = 'en'

    # 2. Update <title>
    meta = EN_META.get(rel_path, {})
    if meta.get('title') and soup.title:
        soup.title.string = meta['title']

    # 3. Update meta description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag and meta.get('description'):
        desc_tag['content'] = meta['description']

    # 4. Update OG tags
    og_title = soup.find('meta', attrs={'property': 'og:title'})
    if og_title and meta.get('og_title'):
        og_title['content'] = meta['og_title']

    og_desc = soup.find('meta', attrs={'property': 'og:description'})
    if og_desc and meta.get('og_description'):
        og_desc['content'] = meta['og_description']

    og_url = soup.find('meta', attrs={'property': 'og:url'})
    if og_url:
        og_url['content'] = f'{BASE_URL}{get_en_path(rel_path)}'

    # 5. Update Twitter Card
    tw_title = soup.find('meta', attrs={'name': 'twitter:title'})
    if tw_title and meta.get('og_title'):
        tw_title['content'] = meta['og_title']

    tw_desc = soup.find('meta', attrs={'name': 'twitter:description'})
    if tw_desc and meta.get('og_description'):
        tw_desc['content'] = meta['og_description']

    # 6. Update canonical
    canonical = soup.find('link', attrs={'rel': 'canonical'})
    if canonical:
        canonical['href'] = f'{BASE_URL}{get_en_path(rel_path)}'

    # 7. Add hreflang tags (after canonical)
    insert_point = canonical or soup.find('link', attrs={'rel': 'icon'})
    if insert_point:
        # zh-Hant
        hreflang_zh = soup.new_tag('link', rel='alternate', hreflang='zh-Hant',
                                     href=f'{BASE_URL}{get_zh_path(rel_path)}')
        insert_point.insert_after(hreflang_zh)
        # en
        hreflang_en = soup.new_tag('link', rel='alternate', hreflang='en',
                                     href=f'{BASE_URL}{get_en_path(rel_path)}')
        hreflang_zh.insert_after(hreflang_en)
        # x-default
        hreflang_xd = soup.new_tag('link', rel='alternate', hreflang='x-default',
                                     href=f'{BASE_URL}{get_zh_path(rel_path)}')
        hreflang_en.insert_after(hreflang_xd)

    # 8. Translate nav links
    nav_links = soup.select('#navLinks a')
    for a in nav_links:
        txt = a.get_text(strip=True)
        if txt in NAV_ZH_TO_EN:
            a.string = NAV_ZH_TO_EN[txt]
        # Update href to /en/ versions
        href = a.get('href', '')
        if href == '/':
            a['href'] = '/en/'
        elif href.startswith('/') and not href.startswith('/en/') and href.endswith('.html'):
            a['href'] = f'/en{href}'
        elif href == '/blog/':
            a['href'] = '/en/blog/'

    # 9. Replace data-en content
    for el in soup.find_all(attrs={'data-en': True}):
        en_text = el['data-en']
        # Use BeautifulSoup to parse the en_text in case it has HTML entities
        el.clear()
        # Parse the English content as HTML fragment
        en_parsed = BeautifulSoup(en_text, 'html.parser')
        for child in list(en_parsed.children):
            el.append(copy.copy(child))

    # 10. Update internal links in content (not nav) to /en/
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Skip external links, anchors, javascript, and already /en/ links
        if (href.startswith('http') or href.startswith('#') or
            href.startswith('javascript:') or '/en/' in href):
            continue
        # Internal page links
        if href == '/':
            a['href'] = '/en/'
        elif href.startswith('/') and (href.endswith('.html') or href.endswith('/')):
            a['href'] = f'/en{href}'

    # 11. Update lang.js to use /en/ version behavior
    # The lang.js on /en/ pages should link back to Chinese
    # We'll handle this in lang.js itself

    # 12. Update CSS/JS paths to be absolute (they already are with /)

    # Output
    en_path = get_en_path(rel_path)
    if en_path.endswith('/'):
        out_dir = os.path.join(SITE, 'en', os.path.dirname(rel_path))
        out_file = os.path.join(SITE, 'en', rel_path.replace('index.html', '') if rel_path == 'index.html' else rel_path)
        if rel_path == 'index.html':
            out_file = os.path.join(SITE, 'en', 'index.html')
        elif rel_path == 'blog/index.html':
            out_file = os.path.join(SITE, 'en', 'blog', 'index.html')
    else:
        out_file = os.path.join(SITE, 'en', rel_path)

    out_dir = os.path.dirname(out_file)
    os.makedirs(out_dir, exist_ok=True)

    output = str(soup)
    # Fix self-closing tags that BS4 might break
    output = output.replace('</meta>', '').replace('</link>', '').replace('</br>', '')

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'  OK: {rel_path} -> en/{rel_path}')

def add_hreflang_to_zh(rel_path):
    """Add hreflang tags to the original Chinese page."""
    filepath = os.path.join(SITE, rel_path)
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if hreflang already exists
    if 'hreflang' in html:
        return

    # Insert hreflang tags after canonical
    zh_url = f'{BASE_URL}{get_zh_path(rel_path)}'
    en_url = f'{BASE_URL}{get_en_path(rel_path)}'

    hreflang_tags = f'''
    <link rel="alternate" hreflang="zh-Hant" href="{zh_url}">
    <link rel="alternate" hreflang="en" href="{en_url}">
    <link rel="alternate" hreflang="x-default" href="{zh_url}">'''

    # Insert after canonical link
    canonical_pattern = r'(<link rel="canonical"[^>]+>)'
    match = re.search(canonical_pattern, html)
    if match:
        insert_pos = match.end()
        html = html[:insert_pos] + hreflang_tags + html[insert_pos:]
    else:
        # Fallback: insert before </head>
        html = html.replace('</head>', hreflang_tags + '\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  hreflang added to: {rel_path}')

# All pages to process
PAGES = [
    'index.html',
    'services.html',
    'pricing.html',
    'contact.html',
    'about.html',
    'demo.html',
    'portfolio.html',
    'blog/index.html',
    'blog/line-bot-cost.html',
    'blog/line-bot-tutorial-2026.html',
    'blog/ai-customer-service-line.html',
    'blog/line-bot-booking-system.html',
    'blog/small-business-automation.html',
]

if __name__ == '__main__':
    print('=== Building English pages ===')
    for page in PAGES:
        process_file(page)

    print('\n=== Adding hreflang to Chinese pages ===')
    for page in PAGES:
        add_hreflang_to_zh(page)

    print('\nDone!')
