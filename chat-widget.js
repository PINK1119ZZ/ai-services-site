(function() {
  // Dual-domain failover: prefer the brand domain (more stable on mobile carriers
  // that occasionally block .nip.io), fall back to the IP-based nip.io domain
  // until the chat.autodev-ai.com DNS record is verified live.
  const API_URLS = [
    'https://chat.autodev-ai.com/api/chat',
    'https://line-bot.76.13.219.163.nip.io/api/chat',
  ];
  const SESSION_ID = 'web_' + Math.random().toString(36).substr(2, 9);
  const isEnglish = /^\/en(?:\/|$)/.test(location.pathname);
  const copy = isEnglish ? {
    open: 'Open project chat', close: 'Close project chat', panel: 'AutoDev project chat',
    title: 'AutoDev project assistant', status: 'AI-assisted. Confirm important details with the founder.',
    placeholder: 'Type your question...', input: 'Your question', send: 'Send question',
    typing: 'AI assistant is preparing a reply', user: 'Your message', bot: 'AI-assisted reply',
    welcome: 'Hello. Ask about Telegram Bot services, project scope, budget positioning, or how to start an enquiry. AI-assisted answers are for initial guidance; the founder confirms important details.',
    slow: 'The service is taking longer to respond. Please try again, message us on Telegram: https://t.me/AUTO_DEV_AI_BOT, or open the project enquiry: https://chat.autodev-ai.com/form',
    unavailable: 'The connection is temporarily unavailable. Please try again, message us on Telegram: https://t.me/AUTO_DEV_AI_BOT, or open the project enquiry: https://chat.autodev-ai.com/form',
    quick: [['Services', 'What services does AutoDev offer?'], ['Budget', 'How are project budgets positioned?'], ['Scope', 'How do you clarify project scope?'], ['Enquiry', 'How can I start a project enquiry?']],
  } : {
    open: '開啟專案諮詢', close: '關閉專案諮詢', panel: 'AutoDev 專案諮詢',
    title: 'AutoDev 專案助理', status: 'AI 輔助回覆，重要細節由創辦人確認。',
    placeholder: '輸入你的問題…', input: '你的問題', send: '送出問題',
    typing: 'AI 助理正在準備回覆', user: '你的訊息', bot: 'AI 輔助回覆',
    welcome: '你好。你可以詢問 Telegram Bot 服務、專案範圍、預算定位或如何開始諮詢。AI 輔助內容供初步參考，重要細節由創辦人確認。',
    slow: '目前回覆較慢。請稍後再試、使用 Telegram 聯繫：https://t.me/AUTO_DEV_AI_BOT，或開啟需求諮詢：https://chat.autodev-ai.com/form',
    unavailable: '目前連線不穩。請稍後再試、使用 Telegram 聯繫：https://t.me/AUTO_DEV_AI_BOT，或開啟需求諮詢：https://chat.autodev-ai.com/form',
    quick: [['服務', 'AutoDev 提供哪些服務？'], ['預算', '專案預算如何定位？'], ['範圍', '你們如何澄清專案範圍？'], ['諮詢', '如何開始需求諮詢？']],
  };

  // Inject styles
  const style = document.createElement('style');
  style.textContent = `
    #chat-widget-btn {
      position: fixed; bottom: 24px; right: 24px; z-index: 9999;
      width: 60px; height: 60px; border-radius: 50%;
      background: #2D2620;
      border: none; cursor: pointer; box-shadow: 0 4px 20px rgba(184,148,106,0.4);
      display: flex; align-items: center; justify-content: center;
      transition: transform 0.3s, box-shadow 0.3s;
      animation: chat-pulse 2s infinite;
    }
    #chat-widget-btn:hover { transform: scale(1.1); box-shadow: 0 6px 30px rgba(184,148,106,0.6); }
    @keyframes chat-pulse {
      0%, 100% { box-shadow: 0 4px 20px rgba(184,148,106,0.4); }
      50% { box-shadow: 0 4px 30px rgba(184,148,106,0.7); }
    }
    #chat-widget-btn svg { width: 28px; height: 28px; fill: #FFF8F3; }
    #chat-widget-btn .close-icon { display: none; }
    #chat-widget-btn.open .chat-icon { display: none; }
    #chat-widget-btn.open .close-icon { display: block; }
    #chat-widget-btn.open { animation: none; }

    #chat-widget-box {
      position: fixed; bottom: 100px; right: 24px; left: auto; z-index: 9998;
      width: min(370px, calc(100vw - 24px));
      max-height: min(520px, calc(100vh - 140px));
      border-radius: 16px;
      background: #FFF8F3; border: 1px solid rgba(184,148,106,0.3);
      box-shadow: 0 8px 40px rgba(0,0,0,0.5);
      display: none; flex-direction: column; overflow: hidden;
      font-family: 'Noto Sans TC', 'Inter', sans-serif;
      box-sizing: border-box;
    }
    #chat-widget-box.open { display: flex; }

    .chat-header {
      background: #2D2620;
      padding: 16px 20px; display: flex; align-items: center; gap: 12px;
    }
    .chat-header-avatar {
      width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.2);
      display: flex; align-items: center; justify-content: center; font-size: 20px;
    }
    .chat-header-info h4 { color: white; margin: 0; font-size: 15px; font-weight: 700; }
    .chat-header-info p { color: rgba(255,255,255,0.8); margin: 2px 0 0; font-size: 12px; }
    .chat-header-dot { width: 8px; height: 8px; border-radius: 50%; background: #C4A57B; margin-left: auto; }

    .chat-messages {
      flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px;
      min-height: 200px; scrollbar-width: thin; scrollbar-color: #F5EDE3 transparent;
    }
    .chat-messages::-webkit-scrollbar { width: 4px; }
    .chat-messages::-webkit-scrollbar-thumb { background: #F5EDE3; border-radius: 4px; }

    .chat-msg { max-width: 85%; padding: 10px 14px; border-radius: 12px; font-size: 14px; line-height: 1.6; word-break: break-word; white-space: pre-wrap; }
    .chat-msg.bot { background: #F5EDE3; color: #2D2620; align-self: flex-start; border-bottom-left-radius: 4px; }
    .chat-msg.user { background: #2D2620; color: #FFF8F3; align-self: flex-end; border-bottom-right-radius: 4px; }
    .chat-msg.bot a { color: #634628; text-decoration: underline; }
    .chat-msg.bot a:hover { text-decoration: underline; }

    .chat-typing { align-self: flex-start; padding: 10px 14px; background: #F5EDE3; border-radius: 12px; border-bottom-left-radius: 4px; }
    .chat-typing span { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #9A8B7E; margin: 0 2px; animation: typing 1.4s infinite; }
    .chat-typing span:nth-child(2) { animation-delay: 0.2s; }
    .chat-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typing { 0%, 60%, 100% { transform: translateY(0); } 30% { transform: translateY(-6px); } }

    .chat-input-area {
      padding: 12px 16px; border-top: 1px solid #F5EDE3; display: flex; gap: 8px; align-items: center;
    }
    .chat-input {
      flex: 1; background: #FAF3EA; border: 1px solid #F5EDE3; border-radius: 8px;
      color: #2D2620; padding: 10px 14px; font-size: 14px; outline: none;
      font-family: 'Noto Sans TC', 'Inter', sans-serif;
    }
    .chat-input:focus { border-color: #B8946A; }
    .chat-input::placeholder { color: #555; }
    .chat-send {
      background: #2D2620; border: none; border-radius: 8px; padding: 10px 14px;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: background 0.3s;
    }
    .chat-send:hover { background: #4A4038; }
    .chat-send:disabled { background: #6B625C; cursor: not-allowed; }
    .chat-send svg { width: 18px; height: 18px; fill: #FFF8F3; }

    .chat-quick-btns { padding: 0 16px 12px; display: flex; gap: 6px; flex-wrap: wrap; }
    .chat-quick-btn {
      background: rgba(184,148,106,0.15); border: 1px solid rgba(184,148,106,0.3);
      color: #4D3522; border-radius: 16px; padding: 5px 12px; font-size: 12px;
      cursor: pointer; transition: all 0.3s; font-family: 'Noto Sans TC', sans-serif;
    }
    .chat-quick-btn:hover { background: #EADCCA; color: #2D2620; }

    @media (prefers-reduced-motion: reduce) {
      #chat-widget-btn, .chat-typing span { animation: none; transition: none; }
      #chat-widget-btn:hover { transform: none; }
    }

    @media (max-width: 480px) {
      #chat-widget-box { right: 12px; bottom: 88px; }
      #chat-widget-btn { bottom: 16px; right: 16px; width: 54px; height: 54px; }
    }
  `;
  document.head.appendChild(style);

  // Create button
  const btn = document.createElement('button');
  btn.id = 'chat-widget-btn';
  btn.type = 'button';
  btn.setAttribute('aria-label', copy.open);
  btn.setAttribute('aria-expanded', 'false');
  btn.setAttribute('aria-controls', 'chat-widget-box');
  btn.innerHTML = `
    <svg class="chat-icon" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12z"/><path d="M7 9h2v2H7zm4 0h2v2h-2zm4 0h2v2h-2z"/></svg>
    <svg class="close-icon" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
  `;
  document.body.appendChild(btn);

  // Create chat box
  const box = document.createElement('div');
  box.id = 'chat-widget-box';
  box.setAttribute('role', 'region');
  box.setAttribute('aria-label', copy.panel);
  box.setAttribute('aria-busy', 'false');
  box.innerHTML = `
    <div class="chat-header">
      <div class="chat-header-avatar"></div>
      <div class="chat-header-info">
        <h4>${copy.title}</h4>
        <p>${copy.status}</p>
      </div>
      <div class="chat-header-dot"></div>
    </div>
    <div class="chat-messages" id="chatMessages" role="log" aria-live="polite" aria-relevant="additions"></div>
    <div class="chat-quick-btns" id="chatQuickBtns">
      ${copy.quick.map(([label, message]) => `<button type="button" class="chat-quick-btn" data-msg="${message}">${label}</button>`).join('')}
    </div>
    <div class="chat-input-area">
      <input class="chat-input" id="chatInput" aria-label="${copy.input}" placeholder="${copy.placeholder}" maxlength="500" />
      <button type="button" class="chat-send" id="chatSend" aria-label="${copy.send}">
        <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </div>
  `;
  document.body.appendChild(box);

  const messages = document.getElementById('chatMessages');
  const input = document.getElementById('chatInput');
  const sendBtn = document.getElementById('chatSend');
  const quickBtns = document.getElementById('chatQuickBtns');
  let isOpen = false;
  let isSending = false;

  function appendReply(parent, text) {
    let cursor = 0;
    for (const match of text.matchAll(/https?:\/\/[A-Za-z0-9\-._~:/?#\[\]@!$&*+=%,;]+/g)) {
      parent.appendChild(document.createTextNode(text.slice(cursor, match.index)));
      const href = match[0].replace(/[.,]+$/, '');
      let parsed = null;
      try { parsed = new URL(href); } catch (_) {}
      if (parsed && ['http:', 'https:'].includes(parsed.protocol) && !parsed.username && !parsed.password) {
        const link = document.createElement('a');
        link.href = href;
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        link.textContent = href;
        parent.appendChild(link);
      } else {
        parent.appendChild(document.createTextNode(href));
      }
      cursor = match.index + href.length;
    }
    parent.appendChild(document.createTextNode(text.slice(cursor)));
  }

  function addMsg(text, type) {
    const div = document.createElement('div');
    div.className = 'chat-msg ' + type;
    div.setAttribute('role', 'article');
    div.setAttribute('aria-label', type === 'bot' ? copy.bot : copy.user);
    if (type === 'bot') {
      appendReply(div, text);
    } else {
      div.textContent = text;
    }
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function showTyping() {
    const div = document.createElement('div');
    div.className = 'chat-typing';
    div.id = 'chatTyping';
    div.setAttribute('role', 'status');
    div.setAttribute('aria-label', copy.typing);
    div.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function hideTyping() {
    const el = document.getElementById('chatTyping');
    if (el) el.remove();
  }

  async function fetchWithTimeout(url, options, timeoutMs) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const resp = await fetch(url, { ...options, signal: controller.signal });
      return resp;
    } finally {
      clearTimeout(timer);
    }
  }

  async function callApi(text, attempt) {
    // attempt 0: try preferred URL with 12s timeout
    // attempt 1: cycle to next URL with 25s timeout (covers cold start)
    const url = API_URLS[Math.min(attempt, API_URLS.length - 1)];
    const resp = await fetchWithTimeout(
      url,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, session_id: SESSION_ID }),
      },
      attempt === 0 ? 12000 : 25000
    );
    if (!resp.ok) throw new Error('http_' + resp.status);
    const data = await resp.json();
    return data.reply || '';
  }

  async function sendMessage(text) {
    if (isSending || !text.trim()) return;
    isSending = true;
    box.setAttribute('aria-busy', 'true');
    addMsg(text, 'user');
    input.value = '';
    sendBtn.disabled = true;
    quickBtns.style.display = 'none';
    showTyping();

    let reply = '';
    let lastErr = null;
    for (let attempt = 0; attempt < 2; attempt++) {
      try {
        reply = await callApi(text, attempt);
        break;
      } catch (e) {
        lastErr = e;
        // brief pause then retry once
        if (attempt === 0) {
          await new Promise(r => setTimeout(r, 800));
        }
      }
    }

    hideTyping();
    if (reply) {
      addMsg(reply, 'bot');
    } else {
      const isAbort = lastErr && (lastErr.name === 'AbortError' || String(lastErr).includes('abort'));
      addMsg(isAbort ? copy.slow : copy.unavailable, 'bot');
    }
    isSending = false;
    box.setAttribute('aria-busy', 'false');
    sendBtn.disabled = false;
    if (isOpen) input.focus();
  }

  function setOpen(nextOpen) {
    isOpen = nextOpen;
    box.classList.toggle('open', isOpen);
    btn.classList.toggle('open', isOpen);
    btn.setAttribute('aria-expanded', String(isOpen));
    btn.setAttribute('aria-label', isOpen ? copy.close : copy.open);
    if (isOpen && messages.children.length === 0) {
      setTimeout(() => {
        addMsg(copy.welcome, 'bot');
      }, 500);
    }
    if (isOpen) input.focus();
  }

  // Toggle
  btn.addEventListener('click', () => setOpen(!isOpen));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && isOpen) {
      setOpen(false);
      btn.focus();
    }
  });

  // Send
  sendBtn.addEventListener('click', () => sendMessage(input.value));
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.isComposing) { e.preventDefault(); sendMessage(input.value); } });

  // Quick buttons
  quickBtns.querySelectorAll('.chat-quick-btn').forEach(b => {
    b.addEventListener('click', () => sendMessage(b.dataset.msg));
  });
})();
