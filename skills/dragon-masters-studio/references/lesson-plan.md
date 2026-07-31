# DM Chapter Lesson Plan (Dragon Keep edition)

One interactive HTML per **chapter** (DM1 = 16 files, DM2 = 14 files), in the
approved **Dragon Keep** visual system — castle-dark shell, parchment teaching
surface. Every rule below is a hard requirement; do not regress.

## Route the request

- **New chapter or teaching-content change** → read this file AND
  `references/ui-standard.md`.
- **Visual-only restyle, typography fix, responsive fix, print fix, or batch
  theme sync** → read `references/ui-standard.md` only. Preserve all verified
  teaching content — never rewrite questions, answers, vocabulary, timing, or
  task-card instructions during a visual-only request.
- **Missing or conflicting chapter facts, page numbers, or mappings** → write
  `待补/待核对`; never guess.

## Source authority

Use real project files, not chat memory:

1. The chapter PDF the user provides (ask for it if missing) — quotes and page
   references must come from it.
2. `references/dm-series-data.md` (this skill) — each chapter's SKILL A,
   optional SKILL B, and task card. DM3+: build the table first with
   `references/design-standard.md` and get the user's confirmation.
3. Existing verified lesson-plan HTML for content not explicitly being revised.

## Create or revise a lesson

1. Confirm the book, chapter, reading skill, task card, and output folder.
2. Read the chapter text before authoring vocabulary, quotes, page anchors,
   answers, or examples.
3. Start from an approved page in the same lesson set. If a structural template
   is needed:
   - `assets/template-world-card.html` — chapters with a world-building card
     (character / dragon / name / power / home / dream);
   - `assets/template-story-card.html` — chapters with a story/sequence card
     (4-panel board).
   The bundled templates carry **placeholders** (`[quote from the chapter]`,
   `Sentence from the chapter containing <word> — replace with the real one`) —
   always replace them with real sentences from the user's book. They are also
   still Day-labelled: **relabel nav, title, header, footer and the `<select>`
   options from days to chapters** (`DM1 · Ch N · Title`).
4. Build exactly four tabs and matching panels in this order:
   Vocabulary `#p1`, Pause Points `#p2`, Close Reading `#p3`, Task Card `#p4`.
5. Preserve EN-only, edit, reset, answer reveal, print, chapter navigation, and
   `localStorage`. Give every new or substantively revised page a unique storage
   key (`var KEY='dm<book>-ch<NN>-lp-v1'`; bump the suffix on every content
   revision so stale saved edits don't mask updates).
6. Update the current chapter, previous/next targets, dropdown selection, title,
   chapter metadata, and target filename **together** —
   `DM<book>_Ch<NN>_Lesson_Plan.html`, all chapter files in one folder so the
   relative nav links work.
7. Apply the shared Dragon Keep theme and run validation before delivery
   (see below).

## Four-panel teaching contract

### Vocabulary `#p1`
- About ten high-value words for ESL Grades 1–3.
- Exactly three columns: Word (+pos) / short English-English Definition /
  In the Book (real chapter sentence, target word italicized).
- No Chinese column, no Quick Check, no pre-teach groups, no highlighted rows.

### Pause Points `#p2`
- 3–5 stops anchored to verified page numbers and brief real-text cues.
- Exactly ONE question per stop, practising the chapter's reading skill.
- Progress from recall toward inference, synthesis, or prediction as the
  chapter permits.
- Answer hidden by default inside `<details class="ans">`.

### Close Reading `#p3`
- Two skills → teach separately with distinct skill sections (SKILL A blue,
  SKILL B gold).
- Short student-facing definition in English, Chinese support below, plus a
  verified chapter example.
- Rebuild the matching Graphic Organizer as editable HTML: every `.fill` starts
  blank (no hints / no `data-hint`); every answerable box has its own
  `data-ans`; one Answer Key button calls `toggleGO(this)` to fill or clear.
- Narrative chapter answers in past tense; quotations, general facts, theme
  statements keep their natural tense.
- No reference-answer paragraph below the organizer.
- Practice only material already taught in this lesson. No teaching-method
  labels ("I do / We do / You do", "project this card") in visible content.

### Task Card `#p4`
- Printable, all-English, **drawing-first**: replace multi-sentence writing with
  drawing space and at most one short caption line. Keep short single-word
  labels and word/trait choices. No tip lines, no model-answer notes.
- One filled print page, never cut. The `Print Task Card only` button
  (body.print-card) must keep working.
- Take the card from the per-chapter table in `dm-series-data.md` — the card is
  always **the drawing-form of that chapter's reading skill** (lookup table in
  `design-standard.md` Rule 5). World-building cards = big draw-frame + label
  grid (+ `.draw-pair` for cause→effect); story cards = 4-panel `.board` with
  one ✍ caption per panel. The final chapter's card adds a Story Mountain SVG +
  Before/After pair — no reference asset ships for the SVG; author a simple
  5-point mountain path and give it `class="sc-mtn"`.

## Apply or synchronize Dragon Keep

Use the bundled shared assets instead of baking theme copies into every page:

- `assets/dragon-keep-theme.css`
- `assets/dragon-keep-theme.js`

```bash
python3 scripts/install_theme.py "/absolute/path/to/lesson folder"
python3 scripts/install_theme.py "/absolute/path/to/lesson folder" --check
```

(Needs **Python 3**; the pages themselves work without it, so if Python is
unavailable, link the two assets manually in each page and say so.)

For a new book, copy the shared assets into that lesson folder and update only
the `chapters` configuration in `dragon-keep-theme.js` (one entry per lesson —
the Dragon Stone path sizes itself from the config). Hero art is **optional**:
set `ART_BASE` to a folder of chapter art the user owns, or leave it `''` — the
parchment hero renders fine without images. Never ship or hotlink book
illustrations.

## Validation contract

Before delivery:

1. Run `install_theme.py --check` on the complete lesson folder.
2. Confirm all navigation targets exist, CSS braces balance, JS parses.
3. Confirm title chapter, selected nav chapter, and filename agree.
4. Confirm no conflict markers and no duplicate shared-asset tags.
5. For content work, check every quote, page number, answer, and chapter mapping
   against the source PDF.
6. Render at least one short page and the densest page when browser QA is
   available; report static checks only when it is not.

## After delivering

End with one short question offering the companion materials (see SKILL.md —
"After delivering"): a workbook for this chapter, and the whole-book retelling
page. Ask once; skip anything already made in this conversation.
