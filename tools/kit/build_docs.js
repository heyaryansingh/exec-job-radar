// Build a tailored resume and cover letter (.docx) from one JSON spec.
//
//   node tools/kit/build_docs.js spec.json out_dir/
//
// Writes out_dir/resume.docx and out_dir/cover_letter.docx. Convert to PDF with:
//   soffice --headless --convert-to pdf --outdir out_dir out_dir/*.docx
//
// Spec (all text must come from the candidate's verified master resume):
// {
//   "name": "...", "contact": ["City, ST", "email", "phone", "linkedin.com/in/..."],
//   "headline": "...", "summary": "...", "highlights": ["...", ...],
//   "experience": [{"org": "...", "location": "...", "dates": "...",
//                   "roles": [{"title": "...", "dates": "...", "bullets": ["..."]}]}],
//   "education": ["..."], "certifications": ["..."], "skills": [["Label", "text"], ...],
//   "letter": {"date": "...", "to": ["..."], "salutation": "...", "paragraphs": ["..."],
//              "closing": "Sincerely,", "signature": "..."}
// }
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat, BorderStyle,
  TabStopType,
} = require("docx");

const spec = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const outDir = process.argv[3] || ".";
fs.mkdirSync(outDir, { recursive: true });

const FONT = "Calibri";
const INK = "1F2933";
const ACCENT = "1F4E79";
const PAGE = { size: { width: 12240, height: 15840 }, margin: { top: 864, bottom: 864, left: 1008, right: 1008 } };
const CONTENT_RIGHT = 12240 - 1008 * 2;

const numbering = {
  config: [{
    reference: "bullets",
    levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 360, hanging: 220 } } } }],
  }],
};
const styles = { default: { document: { run: { font: FONT, size: 20, color: INK } } } };

const run = (text, o = {}) => new TextRun({ text, font: FONT, ...o });

function sectionHead(text) {
  return new Paragraph({
    spacing: { before: 200, after: 80 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 2 } },
    children: [run(text.toUpperCase(), { bold: true, size: 21, color: ACCENT, characterSpacing: 20 })],
  });
}
const bullet = (text) => new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 50 },
  children: [run(text, { size: 20 })] });

function lineWithRight(left, right, leftOpts = {}, rightOpts = {}) {
  return new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_RIGHT }],
    spacing: { before: 60, after: 20 },
    children: [run(left, leftOpts), run("\t" + (right || ""), { size: 19, color: "52606D", ...rightOpts })],
  });
}

// ------------------------------------------------------------------ resume
const r = [];
r.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
  children: [run(spec.name, { bold: true, size: 34, color: ACCENT })] }));
r.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
  children: [run(spec.contact.filter(Boolean).join("  |  "), { size: 19, color: "52606D" })] }));
if (spec.headline) {
  r.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 },
    children: [run(spec.headline, { bold: true, size: 21 })] }));
}
r.push(sectionHead("Summary"));
r.push(new Paragraph({ spacing: { after: 60 }, children: [run(spec.summary, { size: 20 })] }));
if (spec.highlights && spec.highlights.length) {
  r.push(sectionHead("Selected Results"));
  spec.highlights.forEach((h) => r.push(bullet(h)));
}
r.push(sectionHead("Experience"));
for (const job of spec.experience) {
  r.push(lineWithRight(job.org + (job.location ? `, ${job.location}` : ""), job.dates, { bold: true, size: 21 }));
  for (const role of job.roles || []) {
    r.push(lineWithRight(role.title, role.dates, { italics: true, size: 20, color: ACCENT }, { italics: true }));
    (role.bullets || []).forEach((b) => r.push(bullet(b)));
  }
}
if (spec.education && spec.education.length) {
  r.push(sectionHead("Education"));
  spec.education.forEach((e) => r.push(new Paragraph({ spacing: { after: 30 }, children: [run(e)] })));
}
if (spec.certifications && spec.certifications.length) {
  r.push(sectionHead("Certifications"));
  r.push(new Paragraph({ children: [run(spec.certifications.join("  |  "))] }));
}
if (spec.skills && spec.skills.length) {
  r.push(sectionHead("Skills"));
  spec.skills.forEach(([label, text]) => r.push(new Paragraph({ spacing: { after: 40 },
    children: [run(label + ": ", { bold: true }), run(text)] })));
}

// ------------------------------------------------------------------ cover letter
const L = spec.letter;
const c = [];
c.push(new Paragraph({ spacing: { after: 20 }, children: [run(spec.name, { bold: true, size: 28, color: ACCENT })] }));
c.push(new Paragraph({ spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACCENT, space: 4 } },
  children: [run(spec.contact.filter(Boolean).join("  |  "), { size: 19, color: "52606D" })] }));
c.push(new Paragraph({ spacing: { after: 200 }, children: [run(L.date)] }));
(L.to || []).forEach((t) => c.push(new Paragraph({ children: [run(t)] })));
c.push(new Paragraph({ spacing: { before: 200, after: 160 }, children: [run(L.salutation)] }));
L.paragraphs.forEach((p) => c.push(new Paragraph({ spacing: { after: 160, line: 276 }, children: [run(p, { size: 21 })] })));
c.push(new Paragraph({ spacing: { before: 120, after: 360 }, children: [run(L.closing || "Sincerely,")] }));
c.push(new Paragraph({ children: [run(L.signature || spec.name, { bold: true })] }));

const mk = (children) => new Document({ styles, numbering, sections: [{ properties: { page: PAGE }, children }] });
Promise.all([
  Packer.toBuffer(mk(r)).then((b) => fs.writeFileSync(path.join(outDir, "resume.docx"), b)),
  Packer.toBuffer(mk(c)).then((b) => fs.writeFileSync(path.join(outDir, "cover_letter.docx"), b)),
]).then(() => console.log("wrote", outDir));
