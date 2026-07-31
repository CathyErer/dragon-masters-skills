# Dragon Keep UI Standard

## 1. Purpose

Design a Dragon Masters teacher workspace, not a game screen. The outer shell should feel like a castle and dragon-training world; the teaching surface must remain calm, clear, editable, bilingual, responsive, and printable.

## 2. Signature design

Use one memorable device: a **Dragon Stone Course Path** (one stone per lesson). The current lesson glows; inactive stones remain subdued. Keep the effect subtle and disable it under reduced-motion preferences.

### Visual tokens

| Role | Token | Value |
|---|---|---|
| Outer background | `--night` | `#0b1512` |
| Primary dark surface | `--forest` | `#1e3a2d` |
| Teaching surface | `--parchment` | `#f4ead0` |
| Primary accent | `--gold` | `#d6ad53` |
| Earth-dragon accent | `--bronze` | `#b96d32` |
| Interactive accent | `--teal` | `#198b83` |

Use dark green and stone tones outside; use parchment inside. Do not use purple gradients, generic blue classroom templates, star-field backgrounds, or emoji as the primary theme.

## 3. Page contract

Expected hierarchy:

```html
<nav class="daynav">...</nav>
<div class="toolbar">...</div>
<div id="doc">
  <header class="ed">...</header>
  <div class="tabs">
    <button class="tab on" data-p="p1">...</button>
    <button class="tab" data-p="p2">...</button>
    <button class="tab" data-p="p3">...</button>
    <button class="tab" data-p="p4">...</button>
  </div>
  <div class="panel on ed" id="p1">...</div>
  <div class="panel ed" id="p2">...</div>
  <div class="panel ed" id="p3">...</div>
  <div class="panel ed" id="p4">...</div>
</div>
```

The shared JS adds `dragon-hero`, chapter metadata, hero art, the Dragon Stone path, and tab seals after saved edits are restored. Keep it after existing inline scripts and before `</body>`.

## 4. Module treatment

- **Vocabulary:** parchment ledger; desktop table; mobile cards only inside `#p1`.
- **Pause Points:** vertical reading trail with restrained stone markers.
- **Close Reading:** Dragon Master training chamber; preserve all Graphic Organizers and answer controls.
- **Task Card:** white, ink-friendly student handout. Decorative web styling must disappear when printed.

## 5. Hero configuration

Edit the `chapters` object in `dragon-keep-theme.js` — one entry per lesson; the
Dragon Stone path sizes itself from the config:

```js
2:{
  label:'CHAPTER TWO · THE DRAGON STONE',
  art:'ch02-workshop.webp',   // optional
  position:'50%'
}
```

**Hero art is optional.** `ART_BASE` at the top of the JS points at a folder of
chapter art the user owns, resolved relative to each lesson HTML; leave it `''`
to skip art entirely — the parchment hero renders fine without images. Never
ship or hotlink the book's illustrations. When art is configured, verify every
path before delivery (`install_theme.py --check` does this automatically).

## 6. Per-chapter configuration

This studio generates **one lesson per chapter**, so a DM1 set has 16 config
entries (`1:{label:'CHAPTER ONE · …'}` … `16:{…}`) and the path shows CH 1–16.
The bundled `dragon-keep-theme.js` still carries the original 10-entry teaching
run as an example — replace it with the real chapter list when starting a book.
The theme JS reads the lesson number from the page `<title>` (`Ch N` or `Day N`
both work).

## 7. Readability

- Body and Chinese: `400`.
- Headings and emphasis: `600`.
- Decorative serif: Iowan Old Style/Baskerville with Songti fallbacks.
- Interface/body sans: Avenir Next/Nunito with PingFang SC fallbacks.
- Avoid synthetic bold, cramped all-caps, and overly wide tracking.

## 8. QA

Run the installer in `--check` mode, then inspect at least one short page and the structurally densest page. Pick the chapter with the most Graphic Organizer tables as the mobile stress case.

When browser rendering is unavailable, report static checks only. Do not claim screenshot or browser QA.
