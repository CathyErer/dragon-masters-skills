---
name: dm-workbook
description: >
  Generates a matched pair of .docx files — a Student Workbook (pure black &
  white) and an Answer Key (answers in red, bold + underlined) — for any chapter
  of the Dragon Masters series by Tracey West (Scholastic Branches), e.g. "Rise
  of the Earth Dragon", "Saving the Sun Dragon", "Secret of the Water Dragon",
  and later titles. Trigger whenever the user uploads Dragon Masters book pages
  and asks to create, regenerate, or update a workbook, student worksheet,
  answer key, 练习册, 答案版, 学生版, or 答案; or says things like "给龙骑士做
  workbook", "给驯龙大师做练习", "Dragon Masters 第X章 练习", "给 Dragon Masters
  做个 workbook" with Dragon Masters pages in context.
  Each workbook has exactly 5 sections: Vocabulary Matching (5), Multiple Choice
  (5), Fill in the Blank (5 + word bank), Short Answer (1), and Think & Create
  (1 creative prompt with drawing box). Content is calibrated to CCSS Grade 2
  reading and writing standards. Needs Node.js to run the bundled build script.
  Always produce BOTH files unless explicitly told otherwise.
---

# Dragon Masters Workbook Generator

Produces a matched pair of `.docx` files from a single Node.js build script:

- **`<Book_Title>_Ch<N>_Workbook.docx`** — student-facing, pure black & white, blank answer spaces
- **`<Book_Title>_Ch<N>_AnswerKey.docx`** — teacher-facing, same layout, answers in RED

---

## How to run

The build script ships with this skill at `assets/build_workbook.js` (in the
same folder as this SKILL.md — resolve the path from wherever this skill is
installed; do NOT rewrite the script from scratch). It generates BOTH files in
one run and self-checks the content arrays before building (item counts,
`VOCAB_DEF_ORDER` permutation, word-bank usage).

**Prerequisite: Node.js 18+** (`node -v` to check; macOS `brew install node`, or
nodejs.org). The first run also needs internet for `npm install docx`. If Node is
not available, say so to the user and offer the workbook as HTML or Markdown
instead — do not fail silently.

**Build in a scratch folder, never in the user's teaching-materials folder** —
`npm install` drops ~11 MB of `node_modules` wherever it runs. Move only the two
`.docx` files to where the user wants them.

```bash
mkdir -p /tmp/dm-workbook-build && cd /tmp/dm-workbook-build
cp <this-skill-folder>/assets/build_workbook.js .
# EDIT the content arrays at the top of build_workbook.js to match the chapter
npm install docx   # once per environment, if not already installed
node build_workbook.js
```

Then verify both files: if the environment provides a docx validation script
(e.g. a bundled docx skill), run it on both outputs; otherwise open/unzip each
`.docx` and confirm it is well-formed and every section rendered.

Finally, deliver BOTH files to the user through whatever file-delivery mechanism
the current agent environment provides — Workbook first, then Answer Key.

---

## Workflow

### Step 1 — Read the chapter
The Dragon Masters PDF pages are in context. Read carefully to identify:
- Main character(s) introduced or featured
- Setting (castle, forest, cave, kingdom, etc.)
- Key plot events and actions
- New vocabulary from the chapter
- Emotional beats or surprising moments (good for the creative question)

### Step 2 — Fill in the content blocks
Open `build_workbook.js` and edit ONLY the content blocks between the
`// ===== EDIT CONTENT BELOW =====` and `// ===== END EDIT =====` markers.
Everything outside those markers is layout/styling — do not touch it.

The 7 things to edit:
1. `BOOK_TITLE` and `CHAPTER` — strings at top
2. `VOCAB` — 5 words from the chapter, Grade-2 definitions
3. `VOCAB_DEF_ORDER` — scrambled letter order for the right column
4. `MCQ` — 5 questions, 4 options each (A–D), one correct answer
5. `FILL_WORDS` + `FILL` — 5-word word bank and 5 sentences with `______` placeholder
6. `SHORT_Q` / `SHORT_A` — one concrete recall question + model answer
7. `CREATIVE_Q` — one imagination prompt (student draws + writes 1–2 sentences)

### Step 3 — Build, validate, present
Run the build, verify BOTH outputs are valid, then deliver them to the user.
Student Workbook first, Answer Key second.

---

## Content writing rules (CCSS Grade 2)

All content must be calibrated to:
- **RI.2.1** — Ask and answer questions about key details (who, what, where, why)
- **RI.2.4 / L.2.6** — Grade-appropriate vocabulary from the text
- **W.2.1** — Write short informative sentences (1–2 per short answer)
- **W.2.3** — Write narratives recounting events or using imagination

### Vocabulary (Part 1)
- Pick 5 words that actually appear in the chapter (not invented)
- Prefer concrete nouns and simple action verbs over abstract concepts
- Definitions: 8 words or fewer, no complex clauses
  - ✅ "a poor farmer long ago"
  - ❌ "a person of low social rank in agrarian societies"
- Scramble the definition-column order so students must actually match
  (e.g. display order `['E', 'A', 'D', 'B', 'C']`)

### Multiple Choice (Part 2)
- Questions under 12 words each
- 4 options, each 3–6 words
- Answers must be directly findable in the text (key detail recall)
- Distractors should be plausible but clearly wrong from the chapter
  - Good distractor: swapping a named object from the story
  - Bad distractor: abstract options students have to reason about

### Fill in the Blank (Part 3)
- Word bank of exactly 5 words, all used once
- Sentences are simple subject-verb-object, one blank each
- Blank goes where the key content word belongs
- The sentence should give enough context that the right word is obvious
  once the student has read the chapter

### Short Answer (Part 4) — ONE question only
- Target a single key detail from the chapter (why / what / how)
- Answer must be 1 short complete sentence grounded in the text
- Do not ask multi-step reasoning or inference questions

### Think and Create (Part 5) — ONE creative question only
- Open-ended: "If you were [character], what would you do?",
  "Draw your own [thing from chapter]", "Imagine what happens next..."
- Always include: "Draw a picture and write 1–2 sentences about it."
- The worksheet has a drawing box + 3 writing lines — no need to add more

---

## Design specifications

Both files use **identical layout**, differing only in answer visibility and the
Name/Date line (student workbook only).

| Setting | Value |
|---------|-------|
| Page size | US Letter (12240 × 15840 DXA) |
| Margins | 0.75 inch all sides (1080 DXA) |
| Font | Arial throughout |
| Body text | 14pt (PT14 = 28 half-points) |
| Small text (instructions, table headers) | 12pt |
| Header line | 11pt italic, right-aligned |
| Title block | 16pt bold centered |
| Section headings | 14pt bold + underline |
| Line spacing | 1.2 (LINE = 288 twips) |
| Table borders | Single 0.5pt gray `#AAAAAA` |
| Table cell margins | top/bot 80, left/right 120 DXA |
| Backgrounds/shading | NONE — no fills on any cell or paragraph |
| Writing lines | 64 underscores, NOT paragraph bottom borders |

### Student Workbook — pure black & white
- Vocab Answer column: empty
- MCQ options: all plain black
- Fill-in-blank: `______________` (14 underscores) inline in sentence
- Short answer: 2 writing lines below the question
- Drawing box: 3200 DXA tall, plain black border
- 3 writing lines below the drawing box for sentences

### Answer Key — RED answers
- Color: `#CC0000`
- Style: bold + underline
- Vocab Answer column: shows the letter in red
- MCQ: entire correct option (letter + text) in red
- Fill-in-blank: answer word replaces the blank inline in red
- Short answer: model answer shown in red on a line before the (one) writing line
- Creative question: red italic teacher note:
  *"(Student answers will vary. Accept any thoughtful response with a picture and 1–2 complete sentences.)"*

---

## Critical implementation rules

These are NOT optional — they come from hard-won experience:

1. **Writing lines = plain underscores, NOT paragraph bottom borders.**
   When multiple consecutive paragraphs have identical bottom borders, Word
   collapses them into one visible line. Always use 64 underscore characters.

2. **Tables need dual widths.** Set both `columnWidths` on the table AND
   `width` on each cell, both in DXA.

3. **Never use `ShadingType.SOLID`** — use `CLEAR` or omit shading entirely.
   Student workbook has NO shading anywhere.

4. **Never `\n` inside text.** Use separate `Paragraph` elements.

5. **Smart apostrophes** — use `\u2019` in JS source strings for `'` to avoid
   parse errors when the source text has curly quotes.

6. **`VOCAB_DEF_ORDER` must be a permutation of all vocab letters.** If VOCAB
   has letters A–E, VOCAB_DEF_ORDER must contain all of A, B, C, D, E exactly
   once. Missing or duplicate letters will mis-label the definition column.

7. **Filename convention:** the script derives it from `BOOK_TITLE` — it does
   NOT shorten the title.
   - Pattern: `<Title_With_Underscores>_Ch<N>_Workbook.docx` and `_AnswerKey.docx`
   - Example: `Rise_of_the_Earth_Dragon_Ch1_Workbook.docx`

---

## Quality checklist before presenting files

- [ ] Both files validate with no errors
- [ ] Exactly 5 vocab items, 5 MCQ, 5 fill-in-blank, 1 short answer, 1 creative
- [ ] Word bank has exactly 5 words, all used in the fill-in-blank sentences
- [ ] `VOCAB_DEF_ORDER` contains all 5 letters exactly once
- [ ] Answer key vocab letters match what's shown in the scrambled definition column
- [ ] Every MCQ has exactly one correct answer marked in `ans`
- [ ] Short answer question has a concrete 1-sentence model answer
- [ ] Creative question includes "Draw a picture and write 1–2 sentences"
- [ ] Student workbook PDF preview has NO red anywhere
- [ ] Answer key PDF preview shows red answers in all 5 sections
- [ ] Writing lines render as separate lines (not collapsed into one)

---

## Known variants of the series

If the user uploads a chapter from any of these, this skill applies:

- Rise of the Earth Dragon (#1)
- Saving the Sun Dragon (#2)
- Secret of the Water Dragon (#3)
- Power of the Fire Dragon (#4)
- Song of the Poison Dragon (#5)
- Flight of the Moon Dragon (#6)
- Search for the Lightning Dragon (#7)
- Roar of the Thunder Dragon (#8)
- Chill of the Ice Dragon (#9)
- Waking the Rainbow Dragon (#10)
- ...and all subsequent Dragon Masters titles by Tracey West

The layout and formula are identical across all books — only the content
arrays in `build_workbook.js` change.
