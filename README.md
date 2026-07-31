# Dragon Masters Skills 🐉

Open-source agent skills for making bilingual (English + 简体中文) ESL teaching
materials for the **Dragon Masters** series (Tracey West, Scholastic Branches) —
drawing-first per-chapter lesson plans, student workbooks + answer keys, and
key-word retelling pages.

为 **Dragon Masters（驯龙大师）** 系列制作双语 ESL 教学材料的开源 agent skills：
画画优先的每日课件、学生练习册 + 答案版、关键词复述页。

Follows the open [Agent Skills](https://agentskills.io) standard (`SKILL.md` +
YAML frontmatter), so the same skill folders work in **Claude Code / Claude
Cowork**, **OpenAI Codex**, **腾讯 WorkBuddy**, and any other agent that supports
the standard.

## What's inside · 包含什么

| Skill | What it makes · 产出 |
|---|---|
| `dragon-studio` | The hub 中枢：house rules 风格规范、DM1 16 章 / DM2 14 章的逐章 reading skill + 任务卡对照表、**给 DM3 及以后用的逐章设计标准**（8 条规律 + 7 步流程）；自动路由到下面三个 skill。 |
| `dm-lesson-plan` | One interactive lesson-plan HTML **per chapter** 每章一个课件（4 tabs、drawing-first printable task cards、中英双语 + EN-only toggle）。 |
| `dm-workbook` | Per-chapter student workbook + red answer key（.docx，需要 Node.js + `docx` 包）。 |
| `dm-retelling` | Whole-book retelling practice page（.html）— STOP cards with WHO / DID WHAT keyword groups，浏览器可编辑。 |

## Install · 安装

The four skill folders live in `skills/`. Copy them into your agent's skill
directory (all four together — the hub references the others):

四个 skill 都在 `skills/` 目录下，整体复制到你所用工具的 skill 目录（四个要一起装，
hub 会引用其他三个）：

### Claude Code

```bash
cp -r skills/* ~/.claude/skills/
```

Or install the whole repo as a plugin (it ships a `.claude-plugin/plugin.json`):
add this repo to a plugin marketplace, or use per-project skills at
`.claude/skills/` in your repo. 也可以作为 plugin 安装（仓库自带
`.claude-plugin/plugin.json`）。

### Claude.ai / Claude Cowork

Zip each skill folder (the folder containing `SKILL.md`) and upload it in
**Settings → Capabilities → Skills**. 把每个 skill 文件夹压缩成 zip 后在
设置 → 功能 → Skills 里上传。

### OpenAI Codex

```bash
mkdir -p ~/.agents/skills && cp -r skills/* ~/.agents/skills/
```

Or per-repo: `.agents/skills/` in your project. Invoke with `$skill-name` or let
Codex pick the skill automatically from its description.

### 腾讯 WorkBuddy

```bash
mkdir -p ~/.workbuddy/skills && cp -r skills/* ~/.workbuddy/skills/
```

或在 WorkBuddy 控制面板选择「安装技能」，指向本仓库/本地目录。

### Other agents · 其他工具

Any tool that reads `SKILL.md` per the [agentskills.io](https://agentskills.io)
standard works — point it at the folders in `skills/`.

## Usage · 用法

Provide the chapter PDFs of the book you own, then ask in plain language —
先提供你自己书的章节 PDF，然后直接说：

- "做 DM1 第 7 章的课件" → chapter lesson plan HTML
- "给 DM1 第 12 章做 workbook" → workbook + answer key (.docx)
- "做 DM2 复述" → whole-book retelling HTML

House rules baked in 内置风格规范：ESL Grade 1–3 · English on top / 中文在下 ·
学生材料不出现教学法术语 · drawing-first 任务卡打印正好一页 · 只用书中真实原句和页码 ·
答案版红字加粗下划线。

### DM3 及以后 · Books 3 and beyond

DM1 和 DM2 的逐章 reading skill + 任务卡表是现成的。**DM3–DM10 没有现成表**，
skill 会按 `design-standard.md` 里的 8 条规律先读完整本书、逐章从文本证据推出
技能和任务卡，把表给你确认后再生成课件。核心规则是「技能由文本决定」——
没有书就不排表。

DM1/DM2 have ready-made per-chapter tables. For **any later title**, the hub
skill derives one from the book itself using a documented design standard
(8 rules + a 7-step procedure) and shows you the table before generating
lessons. Rule 1 is binding: no book, no table.

## Requirements · 依赖

- `dm-workbook` needs **Node.js** with the `docx` package (`npm install docx`).
- `dm-retelling` needs **Python 3** (standard library only).
- `dm-lesson-plan` has no dependencies (template-copy + edit).

## Copyright note · 版权说明

*Dragon Masters* is © Tracey West / Scholastic Inc. This repository contains
**no book text** for redistribution — the skills read chapter PDFs **you
provide from books you own** and generate original teaching materials from
them. The bundled reference templates contain only teacher-authored keyword
fragments and short model summaries used as style references. Materials
generated with these skills are intended for personal classroom use.

《Dragon Masters》版权归 Tracey West / Scholastic 所有。本仓库不含任何可再分发的
书籍原文 —— skill 读取的是**你自己拥有的书**的章节 PDF，并据此生成原创教学材料。
自带的参考模板仅包含教师编写的关键词片段和简短示范摘要，用作样式参考。
生成的材料仅供个人课堂教学使用。

## License

Code and skill instructions are released under the [MIT License](LICENSE).

---

Made with ❤️ by Cathy Chu — originally built and battle-tested in real ESL
classrooms across a full DM1 + DM2 teaching cycle.
