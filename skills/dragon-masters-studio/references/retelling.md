
# Dragon Masters — Key-Word Retelling page

> Update (2026-07-15): **chapter Prev/Next buttons** added, matching the lesson-plan
> navigation. The sticky tab bar starts with `<button class="navtab"
> onclick="stepCh(-1)">← Prev</button>` and ends with `<button class="navtab"
> onclick="stepCh(1)">Next →</button>`; `stepCh(d)` finds the `.active` tab and calls
> `showCh()` on its neighbor (clamped at first/last chapter). `.navtab` buttons must
> NOT have the `.tab` class (so tab click-wiring and active-toggling ignore them);
> they hide in print along with `.tabs`. The reference template and
> `generate_retelling.py` both already contain the buttons, CSS and `stepCh` — keep
> them in every generated file.

Generate ONE self-contained `.html` so students retell a whole Dragon Masters book in
their own words. The page is white, English-only, and has a sticky tab bar (one tab per
chapter). It is built to **prevent reading-aloud**: no full sentences are ever printed on
the student side — only key words, split into WHO and DID WHAT.

## Why this format (the design rule)

A full retelling script invites "reading," not retelling. So:

- The card already gives the **setting** — `Where` and `When`.
- The student's only job is to find **WHO + DID WHAT** and say it as
  *"Somebody did something."* This is the core subject-verb spine of a retell.
- Key words are **fragments**, never full sentences (`came on a black horse`,
  not "A soldier came on a black horse"). A fragment read aloud sounds wrong, which
  forces the child to build the sentence.
- Two color groups make the WHO + DID WHAT move visible:
  - **WHO** — blue chips (`#9CC2E2` border, `#F4F9FD` fill): people / dragons.
  - **DID WHAT** — orange chips (`#E8B877` border, `#FFF9F1` fill): actions, each
    starting with a verb.

Do **not** print a per-card "Say it like: SOMEBODY did SOMETHING" line — the one
instruction at the top of the page is enough; repeating it on every card is clutter.

## Style reference (match it exactly)

`assets/template_reference_DM1.html` (bundled with this skill) is the locked style
reference. It is the **exact output** of `assets/generate_retelling.py` as shipped —
run the script and you get that file byte for byte. Match its layout, palette, fonts,
and behavior.

Its book quotes and model retells are **placeholders** (`[quote from the chapter]`,
"Write the model retell for this chapter here") — the structure is real, the content
is not. Fill both in from the user's own copy of the book.

For a new book, copy the script and replace **four** things:

| What | Where |
|---|---|
| `BOOK_NUM`, `BOOK_TITLE` | the constants block at the top — they drive `<title>`, the `<h1>` and the output filename |
| `chapters` | the STOP data |
| `models` | the per-chapter model retells |

Changing only `chapters` / `models` and leaving `BOOK_NUM` alone will emit a page
titled "Dragon Masters #1" **and overwrite the DM1 file** — always set the constants.

### Locked house rules

- **English only.** No Chinese on the page.
- **White background**, `Trebuchet MS / Segoe UI / Arial`. Brand orange `#B85C00`,
  navy `#1A2744`.
- **No emoji, no checkboxes.** STOP cards use a plain text badge: `STOP 1`, `STOP 2`…
- One **combined** HTML for the whole book; chapter tabs `1…N` switch panels via the
  `showCh()` script; default shows chapter 1. Each panel is `page-break-after` for print.
- Per chapter, a **Model retell** in a `<details>` block labelled "Model retell (teacher
  only)", **collapsed by default** so it is hidden when projected to students.
- Meaningful arrows inside a chip (e.g. `put on stone → tingly`, `sparks → red bull's-eye`)
  are allowed — they show cause→effect and are not decoration.

## Inputs

1. Which book + which chapters (default: the whole book, all chapters).
2. The real events. **Read the chapter PDFs the user provides** (ask for them if
   missing) so every WHO / DID WHAT is faithful to the text. Never invent events.

## Build steps

1. Gather, per chapter, 1–3 **STOP** scenes. For each STOP write:
   `Where`, `When`, a `who[]` list (2–4 characters/dragons in that scene), and a `did[]`
   list (2–5 action fragments, **verb-led wherever the event allows**, in story order).
   A fragment must not be a complete sentence a child could just read aloud.
2. Write a short **model retell** per chapter (1 short paragraph, ESL G1–3, faithful to
   events) for the teacher-only `<details>`.
3. **Prerequisite: Python 3** on whatever machine runs commands (standard library only —
   nothing to `pip install`; check with `python3 --version`). Copy
   `assets/generate_retelling.py`, set `BOOK_NUM` / `BOOK_TITLE`, replace the `chapters`
   and `models` data, then run `python3 generate_retelling.py`. It writes the `.html`
   into the current folder and prints the filename.
   If Python is not available, build the HTML by hand from the reference template instead.
4. **Verify before delivering**: tags balanced (`<div>`==`</div>`, `<section>`==
   `</section>`), panel count == chapter count, `showCh('1')` present, **no emoji**, no
   `checkbox`, no per-card "Say it like" line, and `<title>` / `<h1>` / the filename all
   name the right book. Render-check chapter 1 in a real browser.

## Output

Name the file `DM<book>_KeyWord_Retelling_AllChapters.html` and deliver it to the
user (into their book folder's `4-Retelling/` subfolder if they keep one — see the
studio's suggested folder layout in SKILL.md).

## DM2 note

For DM2 ("Saving the Sun Dragon") and later titles, mirror this exact format — the
`BOOK_NUM` / `BOOK_TITLE` constants, the chapter data and the model retells change;
nothing else does.
