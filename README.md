# Dragon Masters Studio 🐉

**One skill, three workflows** — an open-source agent skill that makes bilingual
(English + 简体中文) ESL teaching materials for the **Dragon Masters** series
(Tracey West, Scholastic Branches).

**一个 skill 装完所有功能** —— 为 **Dragon Masters（驯龙大师）** 系列制作双语
ESL 教学材料的开源 agent skill。

Follows the open [Agent Skills](https://agentskills.io) standard (`SKILL.md` +
YAML frontmatter), so the same skill folder works in **Claude Code / Claude
Cowork**, **OpenAI Codex**, **腾讯 WorkBuddy**, and any other agent that supports
the standard.

## What it makes · 产出什么

| Workflow | Output · 产出 |
|---|---|
| Lesson plan 教案 | One interactive lesson-plan HTML **per chapter** 每章一个课件（4 tabs、drawing-first printable task card、中英双语 + EN-only toggle）。 |
| Workbook 练习册 | Per-chapter student workbook + red answer key（.docx，需要 Node.js）。 |
| Retelling 复述 | Whole-book retelling page（.html）— STOP cards with WHO / DID WHAT keyword groups，每章一个 tab，可打印（需要 Python 3）。 |

Built in: house rules 风格规范、DM1 16 章 / DM2 14 章的逐章 reading skill +
任务卡对照表、**给 DM3 及以后用的逐章设计标准**（8 条规律 + 7 步流程）。

## Install · 安装

It's **one skill folder**: `skills/dragon-masters-studio/`. Install it one of
two ways — 只有一个 skill 文件夹，两种装法任选：

### 方式 A · Download the zip（不用 git，推荐）

From [Releases](https://github.com/CathyErer/dragon-masters-skills/releases/latest)
download **`dragon-masters-studio.zip`** (not "Source code"), then:

- **Claude.ai / Claude Cowork**: Settings → Capabilities → Skills, upload the zip.
  设置 → 功能 → Skills，直接上传这个 zip。
- **腾讯 WorkBuddy**: 控制面板 →「安装技能」，上传这个 zip；或解压后放进
  `~/.workbuddy/skills/dragon-masters-studio/`。
- **Claude Code / OpenAI Codex**: unzip into `~/.claude/skills/dragon-masters-studio/`
  or `~/.agents/skills/dragon-masters-studio/`.

### 方式 B · git clone

```bash
git clone https://github.com/CathyErer/dragon-masters-skills.git
cd dragon-masters-skills

# Claude Code
mkdir -p ~/.claude/skills && cp -r skills/dragon-masters-studio ~/.claude/skills/

# OpenAI Codex
mkdir -p ~/.agents/skills && cp -r skills/dragon-masters-studio ~/.agents/skills/

# 腾讯 WorkBuddy
mkdir -p ~/.workbuddy/skills && cp -r skills/dragon-masters-studio ~/.workbuddy/skills/
```

Claude Code can also install it as a plugin:

```
/plugin marketplace add CathyErer/dragon-masters-skills
/plugin install dragon-masters-skills@dragon-masters-skills
```

Verify 验证: restart the agent, then ask 「做 DM1 第 1 章的教案」 — it should load
`dragon-masters-studio` and ask you for the chapter PDF.

Any other tool that reads `SKILL.md` per the [agentskills.io](https://agentskills.io)
standard works the same way — point it at `skills/dragon-masters-studio/`.

## Usage · 用法

Give the agent the chapter PDF from your own copy of the book — drag it into the
chat, or (in Claude Code / Codex) drop it in the working folder and say the
filename. One chapter at a time is enough. If it's a scan, add 「这是扫描件，请先
OCR 再读」.

把你自己那本书的章节 PDF 给它（拖进对话框，或放在当前文件夹里告诉它文件名），
一次一章就够。然后直接说：

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

| Workflow | Needs | If it's missing |
|---|---|---|
| Lesson plan 教案 | nothing — copies and edits an HTML template | works everywhere |
| Retelling 复述 | **Python 3** (standard library only) | build the HTML by hand from the reference template |
| Workbook 练习册 | **Node.js 18+** and `npm install docx` (needs internet once) | ask the agent for the workbook as HTML instead of .docx |

如果你用的 agent 不能执行命令，workbook 就跑不了 —— 让它直接出 HTML 版练习册。

## Troubleshooting · 常见问题

**打印任务卡** — 用 Chrome 打开课件 → 点「🖨 打印」→ 边距选「默认」，勾上「背景图形」
→ 任务卡正好占满一页。

**重新生成后页面还是旧内容** — 课件会把你的编辑存在浏览器 localStorage 里。点右上角
↺ 重置，或用无痕窗口打开。

**`npm: command not found`** — 这台电脑没装 Node.js，见上面 Requirements。

## Copyright note · 版权说明

*Dragon Masters* is © Tracey West / Scholastic Inc.

The bundled reference assets carry **no verbatim sentences or dialogue from the
book** — every such slot is a visible placeholder (`[quote from the chapter]`,
`Sentence from the chapter containing <word> — replace with the real one`,
`Write the model retell for this chapter here`). Chapter titles, character names
and plot facts are used in the planning tables; those appear on the publisher's
own product pages.

The skills read chapter PDFs **you provide from books you own** and fill the
placeholders with the real sentences at generation time. Materials generated with
these skills are for personal classroom use.

随附的参考模板**不含书中原句或台词**——凡是该放原文的位置都是显式占位符。章节标题、
人物名和情节事实用于排课表（这些在出版社的商品页上就有）。skill 运行时从**你自己拥有
的书**的章节 PDF 里读出真实原句填进去。生成的材料仅供个人课堂教学使用。

《Dragon Masters》版权归 Tracey West / Scholastic 所有。本仓库**不含任何书籍原文**。
自带的参考模板只是样式参考：凡是原本该放书中原句或台词的位置，都换成了显式占位符
（`[quote from the chapter]`、`Sentence from the chapter containing <词> — replace
with the real one`）。skill 运行时会从**你自己拥有的书**的章节 PDF 里读出真实原句
填进去。生成的材料仅供个人课堂教学使用。

## License

Code and skill instructions are released under the [MIT License](LICENSE).

---

Made with ❤️ by Cathy Chu — originally built and battle-tested in real ESL
classrooms across a full DM1 + DM2 teaching cycle.
