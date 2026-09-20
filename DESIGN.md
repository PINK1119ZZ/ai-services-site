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
- Contact target: Telegram-first contact plus the existing FormSubmit contract. The redesigned pages link to the verified `https://chat.autodev-ai.com/form` Bot entry. The current Chinese and English contact files remain on the legacy design because automated approval rejected rewriting a form that posts business-contact fields to an unverified public destination.

## Legacy function mapping

- Newsletter: retained on the home page with the existing subscribe endpoint and success/failure behavior.
- Analytics: the existing GA4 instance and Google Ads conversion helper remain; 2.0 adds only non-PII click labels.
- Chat: the existing `chat-widget.js` stays loaded on commercial pages.
- Language switch: the existing `lang.js` injects one paired-language link into `#navLinks`; the new shared script does not inject another switch.
- Contact: both legacy contact pages still own the existing FormSubmit action. The ten redesigned commercial pages use the verified absolute Bot form URL; neither Contact file was changed.

## Tokens and behavior

All 2.0 additions use the `.v2-site` root, the `.v2-*` namespace and the `--v2-*` tokens appended to `style.css`. Existing selectors remain intact for legacy pages. The shared `assets/autodev-v2.js` controls the keyboard-accessible menu, optional reveal and non-PII click events. Content stays visible without JavaScript and motion stops under `prefers-reduced-motion`.
