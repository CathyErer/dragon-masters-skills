---
name: dm-lesson-plan
description: >
  Generates a Chapter Lesson Plan interactive HTML for the Dragon Masters series
  (DM1 "Rise of the Earth Dragon", DM2 "Saving the Sun Dragon", and later titles),
  ONE FILE PER CHAPTER. Trigger when the user says "做 DM1 第 N 章教案", "DM
  Chapter N lesson plan", "继续做下一章", "按模板做下一章", or uploads Dragon
  Masters chapter PDFs asking for a lesson plan / 教案 / 课件. Output is a single
  self-contained HTML in the locked "课堂手账" style (sky-blue notebook background
  + lemon-yellow highlighter + 📌 pinned cards, rounded sans-serif, full-screen).
  Task cards are DRAWING-FIRST (draw, don't write sentences) and print to one
  filled page. NEVER invent a new layout — copy assets/template_day01.html (world
  card) or assets/template_story_card_day08.html (story card) and replace content
  only.
---

# DM Chapter Lesson Plan (per-chapter edition)

One interactive HTML per **chapter** (DM1 = 16 files, DM2 = 14 files). The
template was finalized with the original author after several rounds —
**every rule below is a hard requirement. Do not regress.**

> **Chapter navigation bar**: every chapter file starts with `<nav
> class="daynav">` right after `<body>`: a centered pill cluster — `← Ch N-1`
> link · a `<select>` dropdown listing all chapters of the book (label =
> `Ch N · Title`, current chapter `selected` with empty value, `onchange`
> navigates via `location.href`) · `Ch N+1 →` link. Chapter 1's prev is
> `<span class="off">← Prev</span>` (grayed, unclickable); the last chapter's
> next is `<span class="off">The End 🐉</span>`. Links are **relative
> filenames** — works only if all chapter files stay in the same folder with
> unchanged names. The matching CSS block (`/* ── Day navigation (auto-added)
> ── */` … `@media print{.daynav{display:none !important;}}`) is injected
> before the first `</style>`; nav is hidden in print and stays clear of the
> fixed top-right toolbar (centered, `z-index:40`). Both reference templates
> already contain the nav + CSS — they were built when lessons were grouped by
> teaching day, so when creating a chapter file **relabel the nav from days to
> chapters** and update the prev/next hrefs + dropdown options accordingly.
>
> Locked content rules (v5): (1) vocab table = **Word / Definition (英英释义) /
> In the Book** (中文 + Quick Check columns removed); (2) GOs have **no hints**,
> and an **Answer Key button fills the answers straight into the boxes**
> (`toggleGO`, per-box `data-ans`) — no reference paragraph under the GO;
> (3) GO answers that narrate the chapter are **past tense**; (4) **no 💡/⚠️
> tipline notes** on task cards. The reference templates already contain all of this.
>
> Locked card rules (v4): task cards are **DRAWING-FIRST** (draw, don't write
> sentences) and print to **exactly one page, filled, never cut**. See the
> Task Card rules below and the two reference assets.

## Inputs

1. **Chapter PDF**: provided by the user (ask for it if missing) —
   always read the actual chapter text first; quotes and page numbers must be real.
2. **Chapter → skill → task card mapping**: the `dragon-studio` hub skill's
   `references/dm-series-data.md` (per-chapter reading-skill map + per-chapter
   task-card table + 11-card story arc). If the user maintains their own plan
   document, use theirs instead.
3. **Graphic organizer designs**: one GO per reading skill. Follow the GO
   patterns already present in the two reference templates (fillable `.fill`
   boxes, one `data-ans` per box); if the user supplies their own GO designs,
   convert those into HTML inside the lesson plan.
4. **Task card content**: follow the 11-card story arc and the per-chapter card
   table in `dm-series-data.md`. Card prompts are rendered as a printable
   all-English **drawing-first** student card — convert any "write" prompts into
   draw frames / 4-panel boards (see Task Card v4). **Chapters with no card of
   their own** get a lightweight "Continue your card" page instead: finish or
   improve the most recent card using what this chapter added (same drawing-first
   rules, no new writing blocks).

## Output

- File: `DM<book>_Ch<NN>_Lesson_Plan.html` (e.g. `DM1_Ch04_Lesson_Plan.html`),
  delivered to the user (into their book folder's `3-Lesson Plan/` subfolder if
  they keep one — all chapter files must stay together in one folder for the
  relative chapter-nav links to work).
- Start from `assets/template_day01.html` (final approved version).
  **Copy it, keep ALL CSS/JS untouched, replace content only.**
- Bump the localStorage key: `var KEY='dm<book>-ch<NN>-lp-v1'` (unique per file;
  bump suffix on every content revision so stale saved edits don't mask updates).

## Locked template rules

### Layout & style
- 课堂手账 style: sky-blue (`#1d6cab` / `#2f8fd4`) on notebook ruled background,
  lemon-yellow highlighter accents (`#ffe261`), 📌 pinned cards, slight card rotation.
- Rounded sans font stack (Quicksand / Varela Round / Yuanti SC / 幼圆 / PingFang SC).
  **No serif fonts.**
- Full-screen layout — no max-width container ("不要细长的，要全屏").
- Header: eyebrow (🐉 series line) + highlighted H1 `Chapter N · Chapter Title` +
  subtitle + 4 meta cards (Chapter / Reading Skill / Task Card / Time).

### Four tabs (exactly these, in this order)
1. **Vocabulary 词汇** — ~10 words. Table columns: **Word (+pos) / Definition
   (英英释义) / In the Book** (real sentence from the chapter, target word
   italicized). Definition = a short English-English definition (ESL Gr 1–3,
   dictionary style, present tense is fine here). **NO 中文 column, NO Quick Check
   column, NO pre-teach grouping, NO highlighted rows** — all of these were
   removed in v5.
2. **Pause Points 共读停顿点** — 3–5 stops anchored to real page numbers
   ("PAUSE ① · end of p.2 — quote"). Each stop asks **exactly ONE question that
   points at the chapter's reading skill** (+ a yellow skill tag). The answer sits
   inside `<details class="ans">` — 👁 click-to-show, never visible by default.
3. **Close Reading 精读策略** — if the chapter has two skills, **teach them separately**:
   `SKILL A` blue bar, `SKILL B` gold bar. Each skill section =
   (a) concept definition cards — student-facing definitions, e.g.
   "CHARACTER: the people or animals in the story", English first, Chinese below,
   plus a chapter example; then
   (b) practice with the matching Graphic Organizer for the chapter's reading skill
   rebuilt as fillable HTML (`.fill` contenteditable lines, **NO hints / no
   `data-hint`** — boxes start blank). Each GO ends with an **Answer Key button**
   `<button class="ansbtn" onclick="toggleGO(this)">👁 Answer Key</button>`:
   clicking fills every `.fill` in that GO with its own `data-ans` (green),
   clicking again clears. **Author one `data-ans` per box.** GO answers that
   NARRATE the chapter are **past tense** (book quotes, theme sentences, and
   general "what I know" facts keep their natural tense).
   **NO reference-answer paragraph under the GO** — answers live only in the boxes (v5).
   **You-do work must only practice content already taught in this lesson — never new material.**
   **NO teaching-method instructions in the visible text**: no "I do/We do/You do"
   labels, no "project this card", no "fill together / on their own", no printing
   notes. Pure teaching content only (definitions, examples, GO, answers).
4. **Task Card 任务卡 — DRAWING-FIRST (v4)** — the
   `Print Task Card only` button (body.print-card mechanism prints just the card),
   then a **printable all-English student card built around DRAWING, not
   sentence-writing**. Hard rule: **replace every "write N sentences" block with a
   drawing area + at most ONE caption line.** Keep guiding `.checks` (trait/word
   choices) and short single-word fills; never multi-line writing.
   **NO 💡/⚠️ `.tipline` notes** at the bottom of the card — every
   "In the book…" model and writing tip was removed in v5; the `.tipline` print CSS may stay
   (harmless, no element uses it). Two patterns:
   - **World-building cards (#1–#5)** → one big `.draw-frame` (draw the character /
     dragon / power / dream) + a `.draw-grid` of small `.draw-cell` label boxes
     ("1 word OR a tiny picture") + `.checks` for trait/word choices. #5 (A Strange
     Dream) adds a `.draw-pair` (cause → effect, two mini-sketches). Naming (#3)
     keeps ONE short name line only. Reference: `assets/template_day01.html`.
   - **Story cards (#6–#11)** → a 4-panel comic `.board` of `.frame-cell`s
     (`.fc-num` beat label + `.fc-draw` panel + `.fc-cap` one ✍ caption line). The
     four panels map to the chapter's structure — #6 secret plan (4 show-don't-tell
     beats); #7 quiet moment (activity → share → past → alike); #8 cause-&-effect
     chain (action → because → so → finally); #9 trap → try1❌ → try2❌ →
     cliffhanger; #10 climax (small → BIG → saved → faces); #11 keeps the Story
     Mountain SVG + a `.draw-pair` Before/After. Each chapter prints ONE card
     (see the per-chapter card table in `dm-series-data.md`).
     Reference: `assets/template_story_card_day08.html`.
   - All prompts stay English (e.g. "Label it — 1 word or a tiny picture",
     "draw 4 panels"). `.draw-*` / `.board` CSS is appended in both reference
     templates — see "Drawing-first CSS & print" below; paste it verbatim.

### Bilingual & interaction (already wired in the template JS/CSS — keep intact)
- Bilingual layout: **English on top, Chinese below** (`.cn` spans render as block,
  smaller gray). Exceptions stay inline/table-cell: `.tab .cn`, `th.cn`, `td.cn`, etc.
- `EN only` toggle button hides every `.cn`; preference persisted.
- Edit mode: ✏️ 编辑 makes all `.ed` regions contenteditable; every `[data-del]`
  block gets a ✕ delete button; autosaves `#doc.innerHTML` to localStorage;
  ↺ 重置 restores original; 🖨 打印 prints all tabs expanded.
- **Pause-Point answers**: `<details class="ans"><summary>👁 Answer 答案</summary>…</details>` (click-to-show, hidden by default).
- **GO answers**: per-box `data-ans` + an `.ansbtn` calling `toggleGO(this)`, which fills/clears every `.fill` in that GO. CSS `.fill.ans-filled{color:#1f7a4d;font-weight:600}` + `.ansbtn`; the JS stashes the student's text in `data-user` and restores it on toggle-off. (Already wired in both reference templates.)
- Print CSS: `.go, .pause, .def, .defs, .se-grid, .ot-wrap, .student-card, .task,
  .teacher-only, .meta, table, .idwy { break-inside: avoid; }` — **GOs and cards
  must never be cut across PDF pages**.

### Drawing-first CSS & print (v4 — paste verbatim into every chapter file)

Append this block **after** the base `@media print{…}` and the
`@media (max-width:640px){…}` block (so its print rules win by source order),
right before `</style>`. It is identical in every chapter file (already present
in both reference templates):

```css
/* ── drawing-first / storyboard task card (shared) ── */
.student-card .draw-frame{border:1.5px solid #555;border-radius:8px;min-height:200px;margin:6px 0 12px;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:12px;}
.student-card .draw-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(108px,1fr));gap:8px;margin-bottom:6px;}
.student-card .draw-cell{border:1.5px solid #777;border-radius:6px;min-height:84px;display:flex;flex-direction:column;}
.student-card .draw-cell .dc-lab{font-size:12px;font-weight:700;text-align:center;border-bottom:1px solid #999;padding:3px 4px;}
.student-card .draw-cell .dc-box{flex:1;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:10px;text-align:center;}
.student-card .draw-pair{display:grid;grid-template-columns:1fr 34px 1fr;align-items:center;gap:6px;margin-bottom:10px;}
.student-card .draw-pair .dp-box{border:1.5px solid #555;border-radius:8px;min-height:120px;display:flex;flex-direction:column;}
.student-card .draw-pair .dp-lab{font-size:12px;font-weight:700;text-align:center;border-bottom:1px solid #999;padding:3px 4px;}
.student-card .draw-pair .dp-draw{flex:1;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:10px;}
.student-card .draw-pair .dp-arrow{text-align:center;font-size:24px;color:#555;font-weight:800;}
.student-card .board{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0 4px;}
.student-card .frame-cell{border:1.5px solid #555;border-radius:8px;overflow:hidden;}
.student-card .frame-cell .fc-num{font-size:11px;font-weight:800;background:#eee;padding:2px 8px;}
.student-card .frame-cell .fc-draw{min-height:110px;display:flex;align-items:center;justify-content:center;color:#bbb;font-size:10px;}
.student-card .frame-cell .fc-cap{border-top:1px dashed #999;min-height:24px;font-size:12px;padding:3px 6px;}
.student-card .frame-cell .fc-cap::before{content:"✍ ";color:#999;}
@media print{
  body.print-card{padding:6mm 10mm;}
  .student-card{padding:16px 24px;break-inside:avoid;page-break-inside:avoid;}
  .student-card .sc-task{padding:6px 12px;margin-bottom:8px;}
  .student-card h5{margin:9px 0 4px;}
  .student-card .tipline{margin-top:8px;padding-top:6px;}
  /* fill exactly one page: card stretches, drawing areas absorb the slack */
  body.print-card #p4 .student-card{display:flex !important;flex-direction:column;min-height:86vh;box-sizing:border-box;}
  body.print-card #p4 .student-card .draw-frame{flex:3 1 0;}
  body.print-card #p4 .student-card .draw-pair{flex:2 1 0;}
  body.print-card #p4 .student-card .draw-pair .dp-box{min-height:0;height:100%;}
  body.print-card #p4 .student-card .board{flex:1 1 0;grid-auto-rows:1fr;}
  body.print-card #p4 .student-card .frame-cell{display:flex;flex-direction:column;}
  body.print-card #p4 .student-card .frame-cell .fc-draw{flex:1 1 0;}
  /* #11 only: cap the Story Mountain SVG so the dense capstone card still fits */
  body.print-card #p4 .student-card .sc-mtn{max-width:360px;height:auto;margin:2px auto 6px;}
}
```

**Why each rule matters (do not regress):**
- `display:flex !important` is **required** — the base template has
  `body.print-card #p4 .student-card{display:block !important}`; without
  `!important` here it wins and the card stays block, leaving huge bottom whitespace.
- `min-height:86vh` < 100vh **guarantees one page** (can't overflow) while the
  flex-grow on `.draw-frame` / `.draw-pair` / `.board` fills the slack — so the card
  is full, not half-empty, and the drawing space is large.
- These are **CSS-only**, outside `#doc`, so they take effect on reload without a
  KEY bump. (Still bump KEY when card *content* changes.)

### Content calibration
- ESL Grade 1–3; definitions and questions in short, common-word English.
- Quotes must be verbatim from the chapter PDF with correct page numbers.
- Question ladder across pause points: recall → outside-trait/skill question →
  synthesis → prediction at the chapter cliffhanger (when the chapter has one).
- Each chapter must reference its task card's role in the 11-card story arc
  (Cards #6–#11 = the student's own 6-chapter story).

## Workflow

1. Read the chapter PDF (provided by the user).
2. Pull the chapter's skill + task card from the per-chapter tables in the
   `dragon-studio` hub's `references/dm-series-data.md` (or the user's own plan
   document); design the GO for that skill following the patterns in the
   reference templates.
3. Copy `assets/template_day01.html` → new filename; replace header/meta,
   vocabulary rows (Word / Definition / In the Book), pause points, skill sections
   + GOs (blank `.fill` boxes + one `data-ans` each, past-tense narration, no ref
   paragraph), task card (drawing-first, no tipline; "Continue your card" page
   for chapters without their own card). Keep CSS/JS.
4. Bump the localStorage KEY.
5. **Fix the chapter nav**: relabel `<nav class="daynav">` to chapters — update
   prev/next hrefs and the `<select>` options (current chapter = `selected`,
   empty value; list all chapters of the book).
6. Deliver the file to the user (keep all chapter files together in one folder).

## Files

- `assets/template_day01.html` — final approved file for a chapter teaching a
  WORLD-building drawing card (`.draw-frame` + `.draw-grid` + `.checks`). Single
  source of truth for structure, CSS and JS. Copy this for any new chapter.
- `assets/template_story_card_day08.html` — final approved file for a chapter
  teaching a **STORY card**: the 4-panel `.board` storyboard pattern + captions.
- (The template filenames keep their original `day01`/`day08` names from the
  day-based edition — the structure is unchanged; only the nav labels and
  header change when authoring per-chapter files.)
