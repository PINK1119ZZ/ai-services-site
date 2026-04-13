#!/usr/bin/env python3
"""
update_sitemaps.py — Regenerate sitemap.xml for 3 sites
"""
import os
import glob
from datetime import datetime

def get_mtime(path):
    """Return file mtime as YYYY-MM-DD string."""
    try:
        ts = os.path.getmtime(path)
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')
    except Exception:
        return datetime.utcnow().strftime('%Y-%m-%d')

# ─────────────────────────────────────────────────────────────
# Site 1: ai-services-site  (autodev-ai.com)
# Has ZH + EN pages with hreflang pairs
# ─────────────────────────────────────────────────────────────
def update_autodev():
    base = 'https://autodev-ai.com'
    root = '/root/ai-services-site'

    # Main pages (ZH root): path relative to site root, (priority, changefreq)
    main_pages = [
        ('index.html',     1.0, 'weekly'),
        ('services.html',  0.9, 'weekly'),
        ('pricing.html',   0.9, 'weekly'),
        ('demo.html',      0.9, 'monthly'),
        ('portfolio.html', 0.8, 'weekly'),
        ('contact.html',   0.8, 'weekly'),
        ('about.html',     0.7, 'weekly'),
    ]

    # Collect ZH blog articles
    zh_blog_files = sorted([
        f for f in glob.glob(f'{root}/blog/*.html')
        if os.path.basename(f) != 'index.html'
    ])

    # Collect EN blog articles
    en_blog_files = sorted([
        f for f in glob.glob(f'{root}/en/blog/*.html')
        if os.path.basename(f) != 'index.html'
    ])

    urls = []

    # ZH main pages
    for page, pri, freq in main_pages:
        fpath = f'{root}/{page}'
        loc_zh = f'{base}/{page}' if page != 'index.html' else f'{base}/'
        loc_en = f'{base}/en/{page}' if page != 'index.html' else f'{base}/en/'
        mtime = get_mtime(fpath)
        tag = '  <url>\n'
        tag += f'    <loc>{loc_zh}</loc>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{loc_zh}"/>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>\n'
        if page == 'index.html':
            tag += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{loc_zh}"/>\n'
        tag += f'    <lastmod>{mtime}</lastmod>\n'
        tag += f'    <changefreq>{freq}</changefreq>\n'
        tag += f'    <priority>{pri:.1f}</priority>\n'
        tag += '  </url>'
        urls.append(tag)

    # ZH blog index
    fpath = f'{root}/blog/index.html'
    mtime = get_mtime(fpath)
    tag = '  <url>\n'
    tag += f'    <loc>{base}/blog/</loc>\n'
    tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{base}/blog/"/>\n'
    tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{base}/en/blog/"/>\n'
    tag += f'    <lastmod>{mtime}</lastmod>\n'
    tag += '    <changefreq>weekly</changefreq>\n'
    tag += '    <priority>0.8</priority>\n'
    tag += '  </url>'
    urls.append(tag)

    # ZH blog articles
    for fpath in zh_blog_files:
        fname = os.path.basename(fpath)
        slug = fname
        loc_zh = f'{base}/blog/{slug}'
        loc_en = f'{base}/en/blog/{slug}'
        mtime = get_mtime(fpath)
        # Check if EN version exists
        en_fpath = f'{root}/en/blog/{fname}'
        has_en = os.path.exists(en_fpath)
        tag = '  <url>\n'
        tag += f'    <loc>{loc_zh}</loc>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{loc_zh}"/>\n'
        if has_en:
            tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>\n'
        tag += f'    <lastmod>{mtime}</lastmod>\n'
        tag += '    <changefreq>monthly</changefreq>\n'
        tag += '    <priority>0.8</priority>\n'
        tag += '  </url>'
        urls.append(tag)

    # EN main pages
    en_main_pages = [
        ('index.html',     1.0, 'weekly'),
        ('services.html',  0.9, 'weekly'),
        ('pricing.html',   0.9, 'weekly'),
        ('demo.html',      0.9, 'monthly'),
        ('portfolio.html', 0.8, 'weekly'),
        ('contact.html',   0.8, 'weekly'),
        ('about.html',     0.7, 'weekly'),
    ]
    for page, pri, freq in en_main_pages:
        fpath_en = f'{root}/en/{page}'
        if not os.path.exists(fpath_en):
            continue
        loc_zh = f'{base}/{page}' if page != 'index.html' else f'{base}/'
        loc_en = f'{base}/en/{page}' if page != 'index.html' else f'{base}/en/'
        mtime = get_mtime(fpath_en)
        tag = '  <url>\n'
        tag += f'    <loc>{loc_en}</loc>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{loc_zh}"/>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>\n'
        if page == 'index.html':
            tag += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{loc_zh}"/>\n'
        tag += f'    <lastmod>{mtime}</lastmod>\n'
        tag += f'    <changefreq>{freq}</changefreq>\n'
        tag += f'    <priority>{pri:.1f}</priority>\n'
        tag += '  </url>'
        urls.append(tag)

    # EN blog index
    en_blog_idx = f'{root}/en/blog/index.html'
    mtime = get_mtime(en_blog_idx)
    tag = '  <url>\n'
    tag += f'    <loc>{base}/en/blog/</loc>\n'
    tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{base}/blog/"/>\n'
    tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{base}/en/blog/"/>\n'
    tag += f'    <lastmod>{mtime}</lastmod>\n'
    tag += '    <changefreq>weekly</changefreq>\n'
    tag += '    <priority>0.8</priority>\n'
    tag += '  </url>'
    urls.append(tag)

    # EN blog articles
    for fpath in en_blog_files:
        fname = os.path.basename(fpath)
        slug = fname
        loc_zh = f'{base}/blog/{slug}'
        loc_en = f'{base}/en/blog/{slug}'
        mtime = get_mtime(fpath)
        zh_fpath = f'{root}/blog/{fname}'
        has_zh = os.path.exists(zh_fpath)
        tag = '  <url>\n'
        tag += f'    <loc>{loc_en}</loc>\n'
        if has_zh:
            tag += f'    <xhtml:link rel="alternate" hreflang="zh-Hant" href="{loc_zh}"/>\n'
        tag += f'    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>\n'
        tag += f'    <lastmod>{mtime}</lastmod>\n'
        tag += '    <changefreq>monthly</changefreq>\n'
        tag += '    <priority>0.8</priority>\n'
        tag += '  </url>'
        urls.append(tag)

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    xml += '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n'
    xml += '\n'.join(urls)
    xml += '\n\n</urlset>\n'

    out = f'{root}/sitemap.xml'
    with open(out, 'w') as f:
        f.write(xml)

    total = len(main_pages) + 1 + len(zh_blog_files) + len(en_main_pages) + 1 + len(en_blog_files)
    print(f'[autodev-ai.com] {total} URLs written to {out}')
    print(f'  ZH blog articles: {len(zh_blog_files)}')
    print(f'  EN blog articles: {len(en_blog_files)}')


# ─────────────────────────────────────────────────────────────
# Site 2: ai-tools-tw  (pink1119zz.github.io/ai-tools-tw)
# ─────────────────────────────────────────────────────────────
def update_ai_tools_tw():
    base = 'https://pink1119zz.github.io/ai-tools-tw'
    root = '/root/ai-tools-tw'
    out = f'{root}/sitemap.xml'

    urls = []

    def url_tag(loc, mtime, priority, changefreq='weekly'):
        return (f'<url>'
                f'<loc>{loc}</loc>'
                f'<lastmod>{mtime}</lastmod>'
                f'<changefreq>{changefreq}</changefreq>'
                f'<priority>{priority:.1f}</priority>'
                f'</url>')

    # Homepage
    urls.append(url_tag(f'{base}/', get_mtime(f'{root}/index.html'), 1.0))

    # Special pages
    for rel_path, loc_suffix in [
        ('mcp/index.html',              'mcp/'),
        ('agent-skills-pack/index.html','agent-skills-pack/'),
    ]:
        fpath = f'{root}/{rel_path}'
        if os.path.exists(fpath):
            urls.append(url_tag(f'{base}/{loc_suffix}', get_mtime(fpath), 0.9))

    # Blog articles
    blog_files = sorted([
        f for f in glob.glob(f'{root}/blog/*.html')
        if os.path.basename(f) != 'index.html'
    ])
    for fpath in blog_files:
        fname = os.path.basename(fpath)
        loc = f'{base}/blog/{fname}'
        urls.append(url_tag(loc, get_mtime(fpath), 0.8, 'weekly'))

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '\n'.join(urls)
    xml += '\n</urlset>\n'

    with open(out, 'w') as f:
        f.write(xml)

    total = 1 + 2 + len(blog_files)
    print(f'[ai-tools-tw] {total} URLs written to {out}')
    print(f'  Blog articles: {len(blog_files)}')


# ─────────────────────────────────────────────────────────────
# Site 3: ai-tools-en  (pink1119zz.github.io/ai-tools-en)
# ─────────────────────────────────────────────────────────────
def update_ai_tools_en():
    base = 'https://pink1119zz.github.io/ai-tools-en'
    root = '/root/ai-tools-en'
    out = f'{root}/sitemap.xml'

    urls = []

    def url_tag(loc, mtime, priority, changefreq='weekly'):
        lines = ['  <url>',
                 f'    <loc>{loc}</loc>',
                 f'    <lastmod>{mtime}</lastmod>',
                 f'    <changefreq>{changefreq}</changefreq>',
                 f'    <priority>{priority:.1f}</priority>',
                 '  </url>']
        return '\n'.join(lines)

    # Homepage
    urls.append(url_tag(f'{base}/', get_mtime(f'{root}/index.html'), 1.0))

    # Posts
    post_files = sorted([
        f for f in glob.glob(f'{root}/posts/*.html')
        if os.path.basename(f) != 'index.html'
    ])
    for fpath in post_files:
        fname = os.path.basename(fpath)
        loc = f'{base}/posts/{fname}'
        urls.append(url_tag(loc, get_mtime(fpath), 0.8, 'weekly'))

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '\n'.join(urls)
    xml += '\n</urlset>\n'

    with open(out, 'w') as f:
        f.write(xml)

    total = 1 + len(post_files)
    print(f'[ai-tools-en] {total} URLs written to {out}')
    print(f'  Posts: {len(post_files)}')


if __name__ == '__main__':
    print(f'=== Sitemap Update [{datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")} UTC] ===')
    update_autodev()
    update_ai_tools_tw()
    update_ai_tools_en()
    print('=== Done ===')
