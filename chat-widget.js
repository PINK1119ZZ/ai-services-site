(function() {
  const API_URL = 'https://line-bot.76.13.219.163.nip.io/api/chat';
  const SESSION_ID = 'web_' + Math.random().toString(36).substr(2, 9);

  // Inject styles
  const style = document.createElement('style');
  style.textContent = `
    #chat-widget-btn {
      position: fixed; bottom: 24px; right: 24px; z-index: 9999;
      width: 60px; height: 60px; border-radius: 50%;
      background: linear-gradient(135deg, #6C5CE7, #00D2D3);
      border: none; cursor: pointer; box-shadow: 0 4px 20px rgba(108,92,231,0.4);
      display: flex; align-items: center; justify-content: center;
      transition: transform 0.3s, box-shadow 0.3s;
      animation: chat-pulse 2s infinite;
    }
    #chat-widget-btn:hover { transform: scale(1.1); box-shadow: 0 6px 30px rgba(108,92,231,0.6); }
    @keyframes chat-pulse {
      0%, 100% { box-shadow: 0 4px 20px rgba(108,92,231,0.4); }
      50% { box-shadow: 0 4px 30px rgba(108,92,231,0.7); }
    }
    #chat-widget-btn svg { width: 28px; height: 28px; fill: white; }
    #chat-widget-btn .close-icon { display: none; }
    #chat-widget-btn.open .chat-icon { display: none; }
    #chat-widget-btn.open .close-icon { display: block; }
    #chat-widget-btn.open { animation: none; }

    #chat-widget-box {
      position: fixed; bottom: 100px; right: 24px; z-index: 9998;
      width: 370px; max-height: 520px; border-radius: 16px;
      background: #1A1A2E; border: 1px solid rgba(108,92,231,0.3);
      box-shadow: 0 8px 40px rgba(0,0,0,0.5);
      display: none; flex-direction: column; overflow: hidden;
      font-family: 'Noto Sans TC', 'Inter', sans-serif;
    }
    #chat-widget-box.open { display: flex; }

    .chat-header {
      background: linear-gradient(135deg, #6C5CE7, #00D2D3);
      padding: 16px 20px; display: flex; align-items: center; gap: 12px;
    }
    .chat-header-avatar {
      width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.2);
      display: flex; align-items: center; justify-content: center; font-size: 20px;
    }
    .chat-header-info h4 { color: white; margin: 0; font-size: 15px; font-weight: 700; }
    .chat-header-info p { color: rgba(255,255,255,0.8); margin: 2px 0 0; font-size: 12px; }
    .chat-header-dot { width: 8px; height: 8px; border-radius: 50%; background: #00FF88; margin-left: auto; }

    .chat-messages {
      flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px;
      max-height: 340px; scrollbar-width: thin; scrollbar-color: #2D2D44 transparent;
    }
    .chat-messages::-webkit-scrollbar { width: 4px; }
    .chat-messages::-webkit-scrollbar-thumb { background: #2D2D44; border-radius: 4px; }

    .chat-msg { max-width: 85%; padding: 10px 14px; border-radius: 12px; font-size: 14px; line-height: 1.6; word-break: break-word; }
    .chat-msg.bot { background: #2D2D44; color: #E0E0E0; align-self: flex-start; border-bottom-left-radius: 4px; }
    .chat-msg.user { background: #6C5CE7; color: white; align-self: flex-end; border-bottom-right-radius: 4px; }
    .chat-msg.bot a { color: #00D2D3; text-decoration: none; }
    .chat-msg.bot a:hover { text-decoration: underline; }

    .chat-typing { align-self: flex-start; padding: 10px 14px; background: #2D2D44; border-radius: 12px; border-bottom-left-radius: 4px; }
    .chat-typing span { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #8E8EA0; margin: 0 2px; animation: typing 1.4s infinite; }
    .chat-typing span:nth-child(2) { animation-delay: 0.2s; }
    .chat-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typing { 0%, 60%, 100% { transform: translateY(0); } 30% { transform: translateY(-6px); } }

    .chat-input-area {
      padding: 12px 16px; border-top: 1px solid #2D2D44; display: flex; gap: 8px; align-items: center;
    }
    .chat-input {
      flex: 1; background: #0F0F1A; border: 1px solid #2D2D44; border-radius: 8px;
      color: #E0E0E0; padding: 10px 14px; font-size: 14px; outline: none;
      font-family: 'Noto Sans TC', 'Inter', sans-serif;
    }
    .chat-input:focus { border-color: #6C5CE7; }
    .chat-input::placeholder { color: #555; }
    .chat-send {
      background: #6C5CE7; border: none; border-radius: 8px; padding: 10px 14px;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: background 0.3s;
    }
    .chat-send:hover { background: #5A4BD1; }
    .chat-send:disabled { background: #333; cursor: not-allowed; }
    .chat-send svg { width: 18px; height: 18px; fill: white; }

    .chat-quick-btns { padding: 0 16px 12px; display: flex; gap: 6px; flex-wrap: wrap; }
    .chat-quick-btn {
      background: rgba(108,92,231,0.15); border: 1px solid rgba(108,92,231,0.3);
      color: #B8B0FF; border-radius: 16px; padding: 5px 12px; font-size: 12px;
      cursor: pointer; transition: all 0.3s; font-family: 'Noto Sans TC', sans-serif;
    }
    .chat-quick-btn:hover { background: rgba(108,92,231,0.3); color: white; }

    @media (max-width: 480px) {
      #chat-widget-box { width: calc(100vw - 24px); right: 12px; bottom: 90px; max-height: 70vh; }
      #chat-widget-btn { bottom: 16px; right: 16px; width: 54px; height: 54px; }
    }
  `;
  document.head.appendChild(style);

  // Create button
  const btn = document.createElement('button');
  btn.id = 'chat-widget-btn';
  btn.innerHTML = `
    <svg class="chat-icon" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.17L4 17.17V4h16v12z"/><path d="M7 9h2v2H7zm4 0h2v2h-2zm4 0h2v2h-2z"/></svg>
    <svg class="close-icon" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
  `;
  document.body.appendChild(btn);

  // Create chat box
  const box = document.createElement('div');
  box.id = 'chat-widget-box';
  box.innerHTML = `
    <div class="chat-header">
      <div class="chat-header-avatar">🤖</div>
      <div class="chat-header-info">
        <h4>AutoDev AI 客服</h4>
        <p>通常在幾秒內回覆</p>
      </div>
      <div class="chat-header-dot"></div>
    </div>
    <div class="chat-messages" id="chatMessages"></div>
    <div class="chat-quick-btns" id="chatQuickBtns">
      <button class="chat-quick-btn" data-msg="你們有什麼服務？">服務介紹</button>
      <button class="chat-quick-btn" data-msg="LINE Bot 開發多少錢？">報價詢問</button>
      <button class="chat-quick-btn" data-msg="開發要多久？">交付時間</button>
      <button class="chat-quick-btn" data-msg="可以免費諮詢嗎？">免費諮詢</button>
    </div>
    <div class="chat-input-area">
      <input class="chat-input" id="chatInput" placeholder="輸入你的問題..." maxlength="500" />
      <button class="chat-send" id="chatSend">
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

  function addMsg(text, type) {
    const div = document.createElement('div');
    div.className = 'chat-msg ' + type;
    // Convert URLs to links for bot messages
    if (type === 'bot') {
      text = text.replace(/(https?:\/\/[^\s）\)]+)/g, '<a href="$1" target="_blank">$1</a>');
      text = text.replace(/\n/g, '<br>');
      div.innerHTML = text;
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
    const resp = await fetchWithTimeout(
      API_URL,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, session_id: SESSION_ID }),
      },
      attempt === 0 ? 12000 : 25000   // 12s first try, 25s retry (warm)
    );
    if (!resp.ok) throw new Error('http_' + resp.status);
    const data = await resp.json();
    return data.reply || '';
  }

  async function sendMessage(text) {
    if (!text.trim()) return;
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
      const msg = isAbort
        ? '伺服器回應有點慢，可能是首次喚醒。請再試一次，或加 LINE 諮詢：<a href="https://line.me/R/ti/p/@882vhisc" target="_blank" rel="noopener">@882vhisc</a>'
        : '連線暫時不穩，請稍後再試，或加 LINE：<a href="https://line.me/R/ti/p/@882vhisc" target="_blank" rel="noopener">@882vhisc</a>';
      addMsg(msg, 'bot');
    }
    sendBtn.disabled = false;
    input.focus();
  }

  // Toggle
  btn.addEventListener('click', () => {
    isOpen = !isOpen;
    box.classList.toggle('open', isOpen);
    btn.classList.toggle('open', isOpen);
    if (isOpen && messages.children.length === 0) {
      setTimeout(() => {
        addMsg('你好！👋 我是 AutoDev AI 的智慧助手。\n\n有什麼我可以幫你的嗎？可以問我關於 LINE Bot 開發、AI 客服、報價等任何問題！', 'bot');
      }, 500);
    }
    if (isOpen) input.focus();
  });

  // Send
  sendBtn.addEventListener('click', () => sendMessage(input.value));
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter' && !e.isComposing) sendMessage(input.value); });

  // Quick buttons
  quickBtns.querySelectorAll('.chat-quick-btn').forEach(b => {
    b.addEventListener('click', () => sendMessage(b.dataset.msg));
  });
})();
