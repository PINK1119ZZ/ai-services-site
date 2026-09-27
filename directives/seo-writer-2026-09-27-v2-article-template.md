# SEO-Writer / English-SEO-Writer / Internal-Linker 指令 — v2 文章外框模板（2026-09-27）

**適用對象：** seo-writer、english-seo-writer、internal-linker
**狀態：** 長期有效（standing，非單次任務，直到有新指令取代）
**背景：** 全站 `blog/*.html`（135 篇）與 `en/blog/*.html`（23 篇）已統一換成 AutoDev 2.0（v2）導覽與頁尾（`assets/v2-chrome.css` + `<!-- v2-chrome:header/footer -->` 標記，`scripts/apply_blog_chrome.py`），內文也已統一跑過 `scripts/unify_articles.py`（移除文章自帶 `<style>`/舊 stylesheet/`style=""`，正文統一包在 `<main class="v2c-article">`）。新文章一律從 v2 模板開始，不再用舊版（`.nav`/`footer` 手刻外框、自帶 `<style>`）起草。

---

## 1. 新文章一律從模板開始

- 繁體中文新文章：複製 `docs/templates/blog-article-v2.html` 為起點。
- 英文新文章：複製 `docs/templates/blog-article-v2.en.html` 為起點。
- 模板已內建：
  - 完整 head 佔位（`{{TITLE}}`、`{{DESCRIPTION}}`、`{{SLUG}}`、`{{DATE_PUBLISHED}}` 等 `{{...}}` 標記，逐一替換為真實內容，不留任何 `{{...}}` 未替換）；
  - canonical / hreflang（預設只自我對應 + `x-default`；若確定會同時發布配對語言版本，另行補上對方語言的 hreflang，兩邊 URL 都必須是**真實存在**的頁面，不得憑空造一個尚未發布的語言 URL）；
  - Open Graph / Twitter Card；
  - JSON-LD `Article`（`datePublished`/`author` 為佔位，寫作時填入真實發布日期與作者）；
  - GA4：沿用既有全站量測 ID `G-4ZWDT650BM`，不要換成別的 ID、不要另外加 Google Ads 或其他量測工具；
  - 已含 v2 外框標記（`<!-- v2-chrome:header -->…<!-- /v2-chrome:header -->`、`<!-- v2-chrome:footer -->…<!-- /v2-chrome:footer -->`）、`/assets/v2-chrome.css`、`/assets/autodev-v2.js`；
  - 正文放在 `<main class="v2c-article">` 內，已有標題、前言、兩三個章節、一個 CTA 範例的排版 class（`.v2c-lede`、`.v2c-cta-box`、`.v2c-button` 等），可直接沿用或視文章需要增減段落/小標，但不要移除或改名這些既有 class（其樣式定義在 `assets/v2-chrome.css` 的 `.v2c-article` 區塊）。

## 2. 寫完之後：依序跑外框腳本、再跑內文統一腳本

```bash
python3 scripts/apply_blog_chrome.py <新文章路徑>
python3 scripts/unify_articles.py <新文章路徑>
# 例如：
python3 scripts/apply_blog_chrome.py blog/your-new-slug-2026.html
python3 scripts/unify_articles.py blog/your-new-slug-2026.html
```

- 這兩步都是保險，不是選項，且順序固定：先 `apply_blog_chrome.py`（外框），再 `unify_articles.py`（內文：清掉文章自己可能誤帶的 `<style>`/`style=""`/舊 stylesheet，並確保正文包在 `<main class="v2c-article">` 內）。兩者都是幂等的：如果格式已經正確，重跑不會產生任何改動；如果不小心動到了外框（見下），`apply_blog_chrome.py` 會用正確的 v2 外框覆蓋回去。
- 跑完後檢查：`grep -c "v2-chrome:header" <新文章路徑>` 與 `grep -c "v2-chrome:footer" <新文章路徑>` 都是 1；再各跑一次 `python3 scripts/apply_blog_chrome.py <新文章路徑>` 與 `python3 scripts/unify_articles.py <新文章路徑>`，兩者都顯示 `0 changed`（新檔尚未被 Git 追蹤，不能用 `git diff` 判斷）。
- 模板已經是 `unify_articles.py` 眼中「已統一」的結構（`<body class="v2c-page">`、正文只有一個 `<main class="v2c-article">`、揭露區塊已包在 `<!-- v2-chrome:disclosure -->`/`<!-- /v2-chrome:disclosure -->` 標記內），照抄模板寫作時不要移除這些、也不要在正文裡新增 `style=""` 行內樣式——否則 `unify_articles.py` 會把它清掉，等於白寫。
- 若本文含聯盟連結：保留模板 `</main>` 之後的 `<!-- v2-chrome:disclosure -->…<!-- /v2-chrome:disclosure -->` 整段（可改寫 `<aside>` 裡的句子本身，但保留這兩個標記註解，否則下次腳本重跑無法辨識這是揭露區塊）；沒有聯盟連結則連同這兩個標記註解一起整段刪除。

## 3. 絕對不要動的部分

- 不要手動修改 `<!-- v2-chrome:header -->…<!-- /v2-chrome:header -->` 與 `<!-- v2-chrome:footer -->…<!-- /v2-chrome:footer -->` 標記之間的內容（導覽/頁尾的連結、文字、`id="nav"`/`id="navLinks"`/`id="mobileMenuBtn"`）。這些由 `scripts/apply_blog_chrome.py` 統一產生，手動改了下次腳本重跑會被覆蓋，也會讓這篇文章的外框跟其他 157 篇不一致。
- 不要修改 `assets/v2-chrome.css`。外框與正文排版（顏色、字體、間距、手機選單行為、`.v2c-article` 內 `h1`–`h6`/表格/引言/按鈕等元素樣式）都在這個檔案裡統一定義；單篇文章不需要、也不應該覆寫它。
- **不要在文章正文裡寫內嵌 `<style>` 或 `style=""`**——`scripts/unify_articles.py` 會把它們整段清掉，等於白寫。正文需要的排版（按鈕、提示框、標籤、目錄、卡片、統計方塊、多欄排列等）改用既有 class 命名慣例讓 `assets/v2-chrome.css` 的通用選擇器自動套用即可：連結 class 含 `btn`/`cta`/`button` 會變按鈕；`div`/`aside`/`section` class 含 `callout`/`note`/`tip`/`warning`/`alert`/`box`/`highlight`/`summary`/`info` 會變淡紙色面板；`span` class 含 `tag`/`badge`/`pill`/`label` 會變膠囊標籤；`nav`/`div` class 含 `toc` 會變目錄面板；`div` class 含 `stat`/`card` 會變面板卡片；`div` class 含 `grid`/`cards`/`stats` 的父層會自動排成多欄 grid。真的需要既有規則之外的樣式時，先跟主控確認是否該擴充 `assets/v2-chrome.css` 的 `.v2c-article` 區塊，而不是在單篇文章裡另開一個內嵌 `<style>`。
- 不要新增第三方資源或依賴（額外的 CDN 字型、第三方 JS 函式庫、額外的分析/廣告腳本）。GA4 只用模板內建的 `G-4ZWDT650BM`。
- 模板本身不含聯盟連結，段落只是骨架，不可原樣發布、不可捏造內容。聯盟連結照你的任務提示放在 `<main class="v2c-article">` 正文中；本文含聯盟連結時，保留模板 `</main>` 後的 `v2c-disclosure` 揭露區塊（可改寫成符合本文的揭露句），沒有聯盟連結才刪除該區塊。

## 4. Internal-linker 的範圍

- internal-linker 對這類新文章，一樣只能改 `<main class="v2c-article">` 裡面的正文（`<p>`、`<li>`、`<td>`、`<th>`、`<h2>`–`<h6>` 文字），照 `AGENTS.md` 既有邊界：不注入 `<h1>`、同一關鍵詞只處理首次合適匹配、不建立 nested anchor。
- 外框標記區塊（header/footer）、`<head>` 內的任何內容、`<script>`、`<style>` 一律不動——這點跟既有規則一致，只是再次強調：v2 外框標記也算在「不動」的範圍內，不是可以插入連結的地方。

## 5. 列表頁卡片

- 繁中新文章：在 `blog/index.html` 找到註解 `<!-- AGENT-NEW-POST-CARDS: ... -->`，在它下一行（`<div class="v2-post-grid">` 之內、第一張卡片之前）插入一張新卡片，最新在最上。英文新文章：在 `en/blog/index.html` 的同名註解下插入。
- 卡片格式照列表中的下一張卡片逐字仿照（同樣的 class 與結構），只替換日期、標籤、標題、摘要與兩處連結；連結用站內絕對路徑（例如 `/blog/your-new-slug-2026.html`）。
- 不修改列表頁的其他部分（導覽、頁尾、三條主線、既有卡片、`<head>`）；不要重新加入舊版的分類篩選按鈕或舊導覽。
