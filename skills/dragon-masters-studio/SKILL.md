---
name: dragon-masters-studio
description: >
  All-in-one bilingual (English + 简体中文) ESL teaching-material studio for the
  Dragon Masters series (Tracey West, Scholastic Branches) — DM1 "Rise of the
  Earth Dragon", DM2 "Saving the Sun Dragon", and every later title. Generates
  THREE kinds of material, one chapter at a time: (1) an interactive Chapter
  Lesson Plan HTML (课堂手账 style, drawing-first printable task card, EN-only
  toggle); (2) a Student Workbook + red Answer Key pair (.docx, needs Node.js);
  (3) a whole-book Key-Word Retelling page (.html, needs Python 3). Trigger
  whenever the user asks for ANY Dragon Masters / 驯龙大师 / 龙骑士 teaching
  material: "做 DM1 第 N 章教案/课件/任务卡", "DM 第X章 workbook / 练习册 /
  学生版 / 答案版", "做 DM 复述 / retelling / 关键词复述卡", "继续做下一章",
  "按 studio 风格做", uploads Dragon Masters chapter PDFs, or references Drake,
  Worm, Bo, Ana, Rori, the Dragon Stone, or King Roland. Carries the shared
  house rules, per-chapter reading-skill + task-card maps for DM1 (16 ch) and
  DM2 (14 ch), and a design standard for planning any later book.
---

# Dragon Masters Studio

One skill, three workflows. Figure out which material the user wants, apply the
**house rules** below, then follow the matching reference file — read it fully
before generating:

| The user asks for… | Follow | Extra prerequisite |
|---|---|---|
| 教案 / 课件 / lesson plan / 任务卡 / task card | `references/lesson-plan.md` | none |
| workbook / 练习册 / 学生版 + 答案版 | `references/workbook.md` | Node.js + `npm install docx` |
| 复述 / retelling / 关键词复述卡 | `references/retelling.md` | Python 3 |

Some requests need two workflows (one chapter = lesson plan **and** workbook).
If a prerequisite is missing, say so and offer an HTML fallback — never fail
silently.

## After delivering — always offer the next material (do not skip)

Most users only know about the material they asked for. So **every delivery ends
with ONE short question offering what this studio can also make** — one sentence,
asked once, never pushy, and never re-offering something already made in this
conversation:

- After a **chapter lesson plan** → “要不要给第 N 章配一份 workbook 练习册（学生版 + 答案版）？这个 skill 还能做整本书的关键词复述页。”
- After a **chapter workbook** → “要不要做第 N 章的互动课件（含可打印任务卡）？还可以做整本书的关键词复述页。”
- After a **whole-book retelling page** → “要不要按章节做课件或 workbook？可以从第 1 章开始。”

If the user asked for two materials in one request, deliver both, then offer only
the remaining one. English-speaking users get the same offer in English.

## Per-chapter data (read before generating anything)

- `references/dm-series-data.md` — finished chapter → skill → task-card tables
  for **DM1 (16 ch) and DM2 (14 ch)**.
- **DM3 and every later title have no ready-made table.** Build one with
  `references/design-standard.md` (8 design rules + a 7-step procedure). Rule 1
  is binding: the skill for a chapter comes from that chapter's text, so **read
  the whole book first**. If the user has not supplied the chapter PDFs, ask for
  them and stop — never invent a per-chapter table. Show the user the table for
  confirmation before generating lesson files.

## House rules (apply to EVERY deliverable — do not regress)

- **Audience**: ESL Grade 1–3 (workbooks calibrated to CCSS Grade 2). Short, common-word English.
- **Bilingual**: English on top, Chinese below; HTML deliverables include an EN-only toggle.
- **No teaching-method text in student-facing material** — no "I do/We do/You do", no "project this card", no printing notes.
- **You-do only practices content already taught in this lesson** — never introduce new material.
- **Task cards are DRAWING-FIRST** — replace "write N sentences" with draw frames / 4-panel comics + at most one caption; print to one filled page. Full spec in `references/lesson-plan.md`.
- **Real quotes only** — vocabulary sentences and page numbers must be verbatim from the chapter PDF the user provides. Never invent quotes; if the book text is not available, ask for it. (The bundled templates carry `[quote from the chapter]` placeholders — always replace them with real sentences from the user's book.)
- **Answer keys**: answers in red, bold + underlined.

## Series facts

- **DM1 "Rise of the Earth Dragon"** = 16 chapters → 16 chapter lesson plans + 16 task cards. **DM1 = 创角期**: card by card students build their own Dragon Master + dragon, bound at the end into 《My Dragon Master Book 1》.
- **DM2 "Saving the Sun Dragon"** = 14 chapters → 14 lessons + 14 cards. **DM2 = 续集冒险**: students reuse the DM1 character / dragon / hidden power and write a 6-chapter sequel, bound into 《My Dragon Master Book 2》.

## Suggested folder layout (optional)

If the user keeps per-book folders, this layout works well (adapt to whatever
they already use — never force it):

- `1-书籍和音频/` — chapter PDFs (`CHn.pdf`) + audio
- `2-Workbook/` — student + answer-key docx per chapter
- `3-Lesson Plan/` — chapter lesson-plan HTML (all chapter files in one folder)
- `4-Retelling/` — whole-book retelling HTML

## Workflow for "做 DM<book> 第 N 章"

1. Read `references/dm-series-data.md` → chapter N's reading skill and task card
   (DM3+: build the table first, see above).
2. Read the chapter PDF the user provides (ask for it if missing).
3. Follow `references/lesson-plan.md` and/or `references/workbook.md`, applying
   the house rules.
4. Deliver the files to the user (into their book folder if they keep one).
