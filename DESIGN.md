# AutoDev 2.0 — Commercial site

> Implementation resumed on 2026-09-21 after the user authorized the documented business changes. This file describes the current AutoDev 2.0 target.

## Direction

The commercial pages use a warm white canvas, charcoal text and restrained champagne accents. Large type, wide space and real interface-like flow diagrams make the offer calm and specific. Telegram Bot is the primary business entry; LINE remains a supported secondary channel.

## Content system

- Home: problem → three solutions → AutoDev internal workflow → four-step collaboration → range guidance → insights → consultation.
- Services: Telegram Bot/customer communication, operations automation and custom systems.
- Portfolio: one clearly labelled AutoDev internal system plus labelled application scenarios. No client placeholders are presented as delivered work.
- Pricing: NT$50K, NT$100K and NT$200K+ communicate project positioning and remain budget references, never automatic quotes.
- About: founder-led delivery, expressed in text without a generated portrait.
- Contact: Telegram-first project enquiry through the verified `https://chat.autodev-ai.com/form` Bot entry. The Chinese and English pages now use the same v2 system as the other commercial routes. They explain the founder-led process and position NT$50K, NT$100K and NT$200K+ as scope guidance rather than fixed packages.

## Legacy function mapping

- Newsletter: retained on the home page with the existing subscribe endpoint and success/failure behavior.
- Analytics: the existing GA4 instance and Google Ads conversion helper remain; 2.0 adds only non-PII click labels.
- Chat: the existing `chat-widget.js` stays loaded on commercial pages.
- Language switch: the existing `lang.js` injects one paired-language link into `#navLinks`; the new shared script does not inject another switch.
- Contact: the user authorized replacing both legacy Contact forms with the owned Bot enquiry entry. The old FormSubmit/Gmail receiver, form fields and simulated success state are removed. Telegram remains the primary direct channel, with LINE available as a secondary contact route.

## Tokens and behavior

All 2.0 additions use the `.v2-site` root, the `.v2-*` namespace and the `--v2-*` tokens appended to `style.css`. Existing selectors remain intact for legacy pages. The shared `assets/autodev-v2.js` controls the keyboard-accessible menu, optional reveal and non-PII click events. Content stays visible without JavaScript and motion stops under `prefers-reduced-motion`.

## Contact replacement evidence — 2026-09-21

Input snapshot: `f2720bb5acc77f9c6b613e07eefe42d7bf522ba2`. TASK spec8 records the user's approval to replace the two Contact pages' FormSubmit/Gmail path with AutoDev's owned Bot enquiry entry. The implementation changes only `contact.html`, `en/contact.html`, `tests/commercial.test.mjs`, and this document.

- Both established Contact URLs, paired canonical/hreflang links, one H1, and parseable `ContactPage` JSON-LD remain.
- The primary CTA is an ordinary link to `https://chat.autodev-ai.com/form`. It records the existing non-PII navigation category `contact_owned_bot`; it does not fire `generate_lead`, form submission, or Ads conversion events.
- Existing GA4 and Ads IDs, `chat-widget.js`, `lang.js`, and `assets/autodev-v2.js` remain. The CTA does not call the retained Ads conversion helper.
- No local form, POST endpoint, iframe, FormSubmit receiver, Gmail destination, contact field, fake success query state, or submitted-data analytics was added.
- The old commercial test was not weakened to hide its two known Contact failures. It was replaced with assertions for the newly authorized contract: owned route, absent third-party submission path, no PII/lead event, preserved metadata, navigation, and truth boundaries.

Red evidence: before the page replacement, `npm test` reported 1 pass and 3 failures. The legacy pages lacked the v2 helper, retained unsupported claims, and did not expose the owned Bot route as the primary CTA. During green work, one selector initially chose the navigation link sharing the same URL; the test was corrected to select the `v2-button` explicitly.

Green evidence: `npm test` passed 4/4; `npm run test:seo` passed 8/8; `npm run test:static` passed 8/8. A fresh build to `/private/tmp/autodev-static-contact-repair-20260921` produced 255 files with 0 source-existing warnings.

Browser visual, responsive, accessibility, and Lighthouse checks were not run in this slice because browser control remains with the main controller. No page was published, no real enquiry data was submitted, and no notification was sent.

## Chat widget security and accessibility evidence — 2026-09-21

Input snapshot: `f2720bb5acc77f9c6b613e07eefe42d7bf522ba2`, with the uncommitted Contact candidate and the main controller's three `style.css` fixes preserved. This slice changes only `chat-widget.js`, `tests/chat-widget.test.mjs`, `package.json`, and this evidence section. The first widget slice added 97 lines, used no new dependency, and kept the existing API request contract.

- Model replies and local fallback messages are appended with text nodes. Only parsed `http:` or `https:` URLs without username or password become anchors, with `noopener noreferrer`; newlines remain visible through `white-space: pre-wrap`.
- The two existing API URLs, retry order, request body, `SESSION_ID`, 500-character limit, and IME-safe Enter behavior remain. Tests replace `fetch`, so verification sends no real request.
- `/en` paths receive complete English labels and prompts; other paths receive Traditional Chinese. Telegram and the owned enquiry URL lead fallback guidance, while free, instant-response, delivery-time, and fixed-price claims are absent.
- The toggle, input, send button, message types, log, and waiting state have accessible names or status. `aria-expanded` follows the panel state, Escape closes the non-modal region and returns focus, and reduced-motion CSS disables pulse and typing animation.
- A single `isSending` guard blocks duplicate send-button, Enter, and quick-button requests while the first request is pending. The visual palette uses charcoal and warm white for primary controls instead of low-contrast gold and white.

Red evidence: after adding the DOM behavior tests, `npm test` passed 4/7 and failed 3/7. The hostile `<img onerror>` reply did not remain visible as text because the old code parsed it as HTML; the controls lacked the required ARIA/localized state; and one pending request allowed three fetch calls.

Green evidence: `npm test` passed 8/8, including four widget behavior tests; `npm run test:seo` passed 8/8; `npm run test:static` passed 8/8. A fresh build to `/private/tmp/autodev-static-chat-widget-20260921` produced 255 files with 0 source-existing warnings.

Browser visual and assistive-technology checks were not run in this slice because browser control remains with the main controller. No production API was called, and nothing was deployed or published.

### Chat widget URL boundary follow-up

Input snapshot remains `f2720bb5acc77f9c6b613e07eefe42d7bf522ba2` with the existing uncommitted website candidate preserved. The first safe-link implementation still let its broad URL matcher consume Traditional Chinese prose between the Telegram URL and the owned enquiry URL. It also included trailing ASCII periods or commas in links and refocused the hidden input after a pending request completed.

Red evidence: the focused widget suite passed 2/5 and failed 3/5. The observed Telegram `href` contained the Chinese explanation plus the second URL, `https://example.com/help,` retained its trailing comma, and resolving a request after Escape moved focus away from the toggle.

The matcher now accepts an explicit set of visible ASCII URL characters while excluding HTML brackets and quotes. A trailing period or comma stays as a text node, while legal punctuation inside a query remains in the URL. URL parsing, protocol checks, userinfo rejection, and text-node rendering remain unchanged. Async completion focuses the input only while the panel is open. This follow-up adds two implementation lines and no dependency or abstraction.

Green evidence: `node --test tests/chat-widget.test.mjs` passed 5/5. The two-failure Traditional Chinese fallback exposes exactly `https://t.me/AUTO_DEV_AI_BOT` and `https://chat.autodev-ai.com/form`, preserves the connecting prose, keeps `?q=a,b`, removes its final period from `href`, and leaves focus on the toggle after Escape. Tests use fake `fetch`; no production request was sent. Browser verification remains with the main controller.

## Main-controller acceptance — 2026-09-21

Main independently ran commercial/widget 9/9, SEO 8/8 and static 8/8; the final build contains 255 files and zero warnings. The prior full artifact scan found no leaks; changed chat content was rechecked separately. In Ego, 12 commercial routes at seven widths passed 84 no-overflow/single-H1 checks. Desktop/mobile screenshots exposed and then verified three scoped CSS fixes: heading font inheritance, primary-button contrast, and homepage headline size. Real mobile fake-fetch checks confirmed hostile markup stays text, userinfo URLs are not links, duplicate Enter triggers one request, and Escape returns focus. After the fallback correction, two failed synthetic endpoints produced two exact contact links while keeping Chinese prose and preserving focus on the closed toggle. No production message or inquiry was sent. Lighthouse and full assistive-technology validation remain unperformed; publication remains pending.
