---
name: dragon-studio
description: >
  Hub and house-style guide for "Dragon Studio" — a bilingual (English + Simplified
  Chinese) ESL teaching-material studio for the Dragon Masters series (Tracey West,
  Scholastic Branches): Book 1 "Rise of the Earth Dragon", Book 2 "Saving the Sun
  Dragon", and later titles. Load this whenever the user asks to make ANY Dragon
  Masters teaching material — "做 DM1/DM2 第 N 章", "DM 第X章 workbook", "Dragon
  Masters 任务卡/复述", "继续做下一章", "按 studio 风格做", or references Drake,
  Worm, Bo, Ana, Rori, the Dragon Stone, or King Roland. It carries the shared house
  rules, the per-chapter reading-skill + task-card maps for DM1 and DM2, and the
  bound-book card arc, then routes to the right sub-skill.
---

# Dragon Studio — house guide

This skill is the **hub**. When the user asks for any Dragon Masters teaching material:
(1) apply the shared **house rules** below, (2) **route** to the right sub-skill,
(3) read `references/dm-series-data.md` for per-chapter / per-card details before generating.

## Route to the right sub-skill

| The user asks for… | Use skill |
|---|---|
| 章节课件 / lesson plan / 教案 / 第 N 章 HTML | `dm-lesson-plan` |
| Workbook / 练习册 / 学生版 + 答案版 docx | `dm-workbook` |
| 复述 / retelling 练习 | `dm-retelling` |

Some requests need two skills (a full teaching day = lesson plan **and** workbook).

## Suggested folder layout (optional)

If the user keeps per-book folders, this layout works well (adapt to whatever the
user already uses — never force it):

- `1-书籍和音频/` — chapter PDFs (`CHn.pdf`) + audio
- `2-Workbook/` — student + answer-key docx per chapter
- `3-Lesson Plan/` — chapter lesson-plan HTML (all chapter files in one folder)
- `4-Retelling/` — whole-book retelling HTML

If the user has no folder convention, simply deliver files and let them file the
outputs themselves.

## House rules (apply to EVERY deliverable — do not regress)

- **Audience**: ESL Grade 1–3 (workbooks calibrated to CCSS Grade 2). Short, common-word English.
- **Bilingual**: English on top, Chinese below; HTML deliverables include an EN-only toggle.
- **No teaching-method text in student-facing material** — no "I do/We do/You do", no "project this card", no printing notes.
- **You-do only practices content already taught that day** — never introduce new material.
- **Task cards are DRAWING-FIRST** — replace "write N sentences" with draw frames / 4-panel comics + at most one caption; print to one filled page. Full spec in `dm-lesson-plan` (Task Card v4).
- **Real quotes only** — vocabulary sentences and page numbers must be verbatim from the chapter PDF the user provides. Never invent quotes; if the book text is not available, ask for it.
- **Answer keys**: answers in red, bold + underlined.

## Series facts

- **DM1 "Rise of the Earth Dragon"** = 16 chapters → 16 chapter lesson plans + 16 task cards. **DM1 = 创角期**: card by card students build their own Dragon Master + dragon, bound at the end into 《My Dragon Master Book 1》.
- **DM2 "Saving the Sun Dragon"** = 14 chapters → 14 lessons + 14 cards. **DM2 = 续集冒险**: students reuse the DM1 character / dragon / hidden power and write a 6-chapter sequel, bound into 《My Dragon Master Book 2》.
- The per-chapter reading-skill + task-card maps for both books are in
  `references/dm-series-data.md`. **Read it before generating any chapter or card.**

## Workflow for "做 DM<book> 第 N 章"

1. Read `references/dm-series-data.md` → chapter N's reading skill and task card.
2. Read the chapter PDF the user provides (ask for it if missing).
3. Invoke `dm-lesson-plan` (chapter lesson-plan HTML) and/or `dm-workbook` (workbook), applying the house rules.
4. Deliver the files to the user (into their book folder if they keep one).
