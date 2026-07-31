// ============================================================================
// build_workbook.js — Dragon Masters chapter workbook builder (dm-workbook)
//
// Generates BOTH files in one run:
//   <Title_With_Underscores>_Ch<N>_Workbook.docx   (student, pure B&W)
//   <Title_With_Underscores>_Ch<N>_AnswerKey.docx  (answers in red bold underline)
//
// Usage:  node build_workbook.js
// Edit ONLY the content between the EDIT markers below.
// Everything after END EDIT is locked layout/styling — do not touch it.
// ============================================================================

// ===== EDIT CONTENT BELOW =====

const BOOK_TITLE = "Rise of the Earth Dragon";
const CHAPTER = 1;

// Part 1 — exactly 5 words that appear in the chapter. Grade-2 definitions
// (8 words or fewer). Letters A–E are assigned in this order.
const VOCAB = [
  { word: "peasant", def: "a poor farmer long ago" },
  { word: "soldier", def: "a person who fights for a king" },
  { word: "castle", def: "a big stone home for a king" },
  { word: "dragon", def: "a large animal that can breathe fire" },
  { word: "kingdom", def: "the land a king rules" },
];

// Display order of the definition column (a permutation of A–E).
const VOCAB_DEF_ORDER = ["E", "A", "D", "B", "C"];

// Part 2 — exactly 5 questions, 4 options each, ans is "A" | "B" | "C" | "D".
const MCQ = [
  {
    q: "Where does Drake live at the start?",
    options: ["In a castle", "On an onion farm", "In a cave", "By the sea"],
    ans: "B",
  },
  {
    q: "Who comes to take Drake away?",
    options: ["A wizard", "A dragon", "A soldier", "His brother"],
    ans: "C",
  },
  {
    q: "Who sent the soldier to find Drake?",
    options: ["King Roland", "Queen Rose", "A farmer", "A knight"],
    ans: "A",
  },
  {
    q: "How old is Drake?",
    options: ["Six years old", "Eight years old", "Ten years old", "Twelve years old"],
    ans: "B",
  },
  {
    q: "What will Drake become?",
    options: ["A cook", "A farmer", "A king", "A Dragon Master"],
    ans: "D",
  },
];

// Part 3 — word bank of exactly 5 words, each used once.
const FILL_WORDS = ["onions", "castle", "secret", "brave", "king"];
const FILL = [
  { sentence: "Drake picks ______ on the farm every day.", answer: "onions" },
  { sentence: "The soldier takes Drake to the ______.", answer: "castle" },
  { sentence: "The dragons are a big ______.", answer: "secret" },
  { sentence: "Drake tries to be ______ on the long walk.", answer: "brave" },
  { sentence: "Roland is the ______ of the land.", answer: "king" },
];

// Part 4 — ONE concrete recall question + a 1-sentence model answer.
const SHORT_Q = "Why does the soldier come to Drake's farm?";
const SHORT_A = "He comes to take Drake to the castle to train as a Dragon Master.";

// Part 5 — ONE creative prompt. The drawing box + writing lines are added
// automatically; always ends with "Draw a picture and write 1–2 sentences."
const CREATIVE_Q =
  "Imagine you are picked to leave your home and train a dragon. " +
  "What would your dragon look like?";

// ===== END EDIT =====

// ============================================================================
// Locked layout below — do not edit when making a new chapter.
// ============================================================================

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, VerticalAlign, TableLayoutType,
} = require("docx");

// ---- content self-checks (fail fast before building anything) --------------
function die(msg) { console.error("CONTENT ERROR: " + msg); process.exit(1); }

const LETTERS = ["A", "B", "C", "D", "E"];
if (VOCAB.length !== 5) die("VOCAB must have exactly 5 items");
if (VOCAB_DEF_ORDER.length !== 5 ||
    [...VOCAB_DEF_ORDER].sort().join("") !== "ABCDE")
  die("VOCAB_DEF_ORDER must be a permutation of A–E");
if (MCQ.length !== 5) die("MCQ must have exactly 5 questions");
MCQ.forEach((m, i) => {
  if (m.options.length !== 4) die(`MCQ ${i + 1} must have 4 options`);
  if (!["A", "B", "C", "D"].includes(m.ans)) die(`MCQ ${i + 1} ans must be A–D`);
});
if (FILL_WORDS.length !== 5) die("FILL_WORDS must have exactly 5 words");
if (FILL.length !== 5) die("FILL must have exactly 5 sentences");
FILL.forEach((f, i) => {
  if (!f.sentence.includes("______")) die(`FILL ${i + 1} sentence needs a ______ blank`);
  if (!FILL_WORDS.includes(f.answer)) die(`FILL ${i + 1} answer "${f.answer}" not in word bank`);
});
if (new Set(FILL.map(f => f.answer)).size !== 5) die("each word bank word must be used exactly once");

// ---- style constants -------------------------------------------------------
const FONT = "Arial";
const PT16 = 32, PT14 = 28, PT12 = 24, PT11 = 22; // half-points
const LINE = 288;              // 1.2 line spacing (240 * 1.2)
const RED = "CC0000";
const GRAY = "AAAAAA";
const PAGE_W = 12240, PAGE_H = 15840, MARGIN = 1080; // US Letter, 0.75in margins
const CONTENT_W = PAGE_W - 2 * MARGIN; // 10080
const WRITING_LINE = "_".repeat(64);
const CELL_MARGINS = { top: 80, bottom: 80, left: 120, right: 120 };

const thinGray = { style: BorderStyle.SINGLE, size: 4, color: GRAY };      // 0.5pt
const TABLE_BORDERS = {
  top: thinGray, bottom: thinGray, left: thinGray, right: thinGray,
  insideHorizontal: thinGray, insideVertical: thinGray,
};
const blackBorder = { style: BorderStyle.SINGLE, size: 8, color: "000000" }; // 1pt
const BOX_BORDERS = {
  top: blackBorder, bottom: blackBorder, left: blackBorder, right: blackBorder,
};

// ---- run/paragraph helpers -------------------------------------------------
const run    = (t, o = {}) => new TextRun({ text: t, font: FONT, size: PT14, ...o });
const redRun = (t, o = {}) => run(t, { color: RED, bold: true, underline: {}, ...o });
const para   = (children, o = {}) =>
  new Paragraph({ children, spacing: { line: LINE, after: o.after ?? 60 }, ...o });

const headerLine = () =>
  para([run(`${BOOK_TITLE} · Chapter ${CHAPTER}`, { size: PT11, italics: true })],
       { alignment: AlignmentType.RIGHT, after: 120 });

const titleBlock = (subtitle) => [
  para([run(BOOK_TITLE, { size: PT16, bold: true })],
       { alignment: AlignmentType.CENTER, after: 40 }),
  para([run(`Chapter ${CHAPTER} · ${subtitle}`, { size: PT14, bold: true })],
       { alignment: AlignmentType.CENTER, after: 120 }),
];

const nameDateLine = () =>
  para([run("Name: ____________________________        Date: ______________")],
       { after: 160 });

const sectionHeading = (t) =>
  para([run(t, { bold: true, underline: {} })], { after: 40 });

const instruction = (t) =>
  para([run(t, { size: PT12 })], { after: 100 });

const writingLine = () => para([run(WRITING_LINE)], { after: 80 });

const spacer = () => para([run("")], { after: 60 });

const cell = (children, width, opts = {}) =>
  new TableCell({
    children, width: { size: width, type: WidthType.DXA },
    margins: CELL_MARGINS, verticalAlign: VerticalAlign.CENTER, ...opts,
  });

// ---- Part 1: Vocabulary Matching ------------------------------------------
function vocabSection(isKey) {
  // Row label (A–E, top down) for the row where each word's definition sits.
  const answerFor = (wordIdx) =>
    LETTERS[VOCAB_DEF_ORDER.indexOf(LETTERS[wordIdx])];

  const widths = [2600, 1400, 700, 5380]; // sums to CONTENT_W
  const headCell = (t, w) =>
    cell([para([run(t, { size: PT12, bold: true })], { after: 0 })], w);

  const rows = [
    new TableRow({
      children: [
        headCell("Word", widths[0]), headCell("Answer", widths[1]),
        headCell("", widths[2]), headCell("Definition", widths[3]),
      ],
    }),
    ...VOCAB.map((v, i) => {
      const displayDef = VOCAB[LETTERS.indexOf(VOCAB_DEF_ORDER[i])].def;
      return new TableRow({
        children: [
          cell([para([run(`${i + 1}. ${v.word}`)], { after: 0 })], widths[0]),
          cell([para(isKey ? [redRun(answerFor(i))] : [run("")], { after: 0 })], widths[1]),
          cell([para([run(`${LETTERS[i]}.`)], { after: 0 })], widths[2]),
          cell([para([run(displayDef)], { after: 0 })], widths[3]),
        ],
      });
    }),
  ];

  return [
    sectionHeading("Part 1 · Vocabulary Matching"),
    instruction("Match each word to its definition. Write the letter in the Answer column."),
    new Table({
      rows, columnWidths: widths, layout: TableLayoutType.FIXED,
      width: { size: CONTENT_W, type: WidthType.DXA }, borders: TABLE_BORDERS,
    }),
    spacer(),
  ];
}

// ---- Part 2: Multiple Choice -----------------------------------------------
function mcqSection(isKey) {
  const out = [
    sectionHeading("Part 2 · Multiple Choice"),
    instruction("Circle the letter of the best answer."),
  ];
  MCQ.forEach((m, i) => {
    out.push(para([run(`${i + 1}. ${m.q}`)], { after: 20 }));
    m.options.forEach((opt, j) => {
      const letter = LETTERS[j];
      const text = `        ${letter}. ${opt}`;
      const isAns = isKey && letter === m.ans;
      out.push(para([isAns ? redRun(text) : run(text)], { after: 20 }));
    });
    out.push(spacer());
  });
  return out;
}

// ---- Part 3: Fill in the Blank ---------------------------------------------
function fillSection(isKey) {
  const bank = new Table({
    rows: [new TableRow({
      children: [cell(
        [para([run("Word Bank:  ", { size: PT12, bold: true }),
               run(FILL_WORDS.join("      "))],
              { alignment: AlignmentType.CENTER, after: 0 })],
        CONTENT_W)],
    })],
    columnWidths: [CONTENT_W], layout: TableLayoutType.FIXED,
    width: { size: CONTENT_W, type: WidthType.DXA }, borders: TABLE_BORDERS,
  });

  const out = [
    sectionHeading("Part 3 · Fill in the Blank"),
    instruction("Choose a word from the Word Bank to complete each sentence. Use each word once."),
    bank, spacer(),
  ];
  FILL.forEach((f, i) => {
    const [before, after] = f.sentence.split("______");
    const children = isKey
      ? [run(`${i + 1}. ${before}`), redRun(f.answer), run(after)]
      : [run(`${i + 1}. ${before}______________${after}`)]; // 14 underscores
    out.push(para(children, { after: 60 }));
  });
  out.push(spacer());
  return out;
}

// ---- Part 4: Short Answer ---------------------------------------------------
function shortSection(isKey) {
  const out = [
    sectionHeading("Part 4 · Short Answer"),
    instruction("Answer the question in one complete sentence."),
    para([run(`1. ${SHORT_Q}`)], { after: 80 }),
  ];
  if (isKey) {
    out.push(para([redRun(SHORT_A)], { after: 80 }));
    out.push(writingLine());
  } else {
    out.push(writingLine());
    out.push(writingLine());
  }
  out.push(spacer());
  return out;
}

// ---- Part 5: Think and Create ----------------------------------------------
function creativeSection(isKey) {
  const box = new Table({
    rows: [new TableRow({
      height: { value: 3200, rule: "atLeast" },
      children: [new TableCell({
        children: [para([run("")], { after: 0 })],
        width: { size: CONTENT_W, type: WidthType.DXA },
        margins: CELL_MARGINS, borders: BOX_BORDERS,
      })],
    })],
    columnWidths: [CONTENT_W], layout: TableLayoutType.FIXED,
    width: { size: CONTENT_W, type: WidthType.DXA }, borders: BOX_BORDERS,
  });

  const out = [
    sectionHeading("Part 5 · Think and Create"),
    para([run(`${CREATIVE_Q} Draw a picture and write 1–2 sentences about it.`)],
         { after: 100 }),
  ];
  if (isKey) {
    out.push(para(
      [run("(Student answers will vary. Accept any thoughtful response with a picture and 1–2 complete sentences.)",
           { color: RED, italics: true })],
      { after: 100 }));
  }
  out.push(box, para([run("")], { after: 40 }),
           writingLine(), writingLine(), writingLine());
  return out;
}

// ---- document assembly ------------------------------------------------------
function buildDoc(isKey) {
  const children = [
    headerLine(),
    ...titleBlock(isKey ? "Answer Key" : "Student Workbook"),
  ];
  if (!isKey) children.push(nameDateLine());
  children.push(
    ...vocabSection(isKey),
    ...mcqSection(isKey),
    ...fillSection(isKey),
    ...shortSection(isKey),
    ...creativeSection(isKey),
  );
  return new Document({
    styles: { default: { document: { run: { font: FONT, size: PT14 } } } },
    sections: [{
      properties: {
        page: {
          size: { width: PAGE_W, height: PAGE_H },
          margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
        },
      },
      children,
    }],
  });
}

// ---- write files ------------------------------------------------------------
const shortTitle = BOOK_TITLE.replace(/[^A-Za-z0-9 ]/g, "").trim().replace(/ +/g, "_");
const wbName = `${shortTitle}_Ch${CHAPTER}_Workbook.docx`;
const akName = `${shortTitle}_Ch${CHAPTER}_AnswerKey.docx`;

(async () => {
  fs.writeFileSync(wbName, await Packer.toBuffer(buildDoc(false)));
  fs.writeFileSync(akName, await Packer.toBuffer(buildDoc(true)));
  console.log("Wrote " + wbName);
  console.log("Wrote " + akName);
})();
