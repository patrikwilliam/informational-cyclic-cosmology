const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { parseArgs } = require('node:util');
const { marked } = require('marked');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..', '..');
const INPUT = path.join(ROOT, 'PAPER.md');
const OUTPUT_DIRECTORY = path.join(ROOT, 'output', 'pdf');
const HTML_OUTPUT = path.join(ROOT, 'tmp', 'pdfs', 'v020', 'paper.html');
const REPOSITORY = 'https://github.com/patrikwilliam/informational-cyclic-cosmology';

function extractLine(markdown, label) {
  const match = markdown.match(new RegExp(`^${label}:\\s*(.+)$`, 'm'));
  if (!match) throw new Error(`Missing metadata line: ${label}`);
  return match[1].trim();
}

function protectMath(markdown) {
  const expressions = [];
  const reserve = (kind, source) => {
    const index = expressions.push({ kind, source }) - 1;
    return `MATHPLACEHOLDER${index}END`;
  };

  let protectedText = markdown.replace(/\$\$([\s\S]*?)\$\$/g, (_, source) =>
    reserve('display', source.trim())
  );
  protectedText = protectedText.replace(/\$([^\n$]+?)\$/g, (_, source) =>
    reserve('inline', source.trim())
  );

  return { protectedText, expressions };
}

function restoreMath(html, expressions) {
  return html.replace(/MATHPLACEHOLDER(\d+)END/g, (_, rawIndex) => {
    const expression = expressions[Number(rawIndex)];
    const source = expression.source.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    return expression.kind === 'display' ? `\\[${source}\\]` : `\\(${source}\\)`;
  });
}

function absoluteSupplementLinks(markdown) {
  return markdown
    .replaceAll(
      '](./feedback/',
      `](${REPOSITORY}/blob/main/feedback/`
    )
    .replaceAll(
      '](./research)',
      `](${REPOSITORY}/tree/main/research)`
    )
    .replaceAll(
      '](./research/',
      `](${REPOSITORY}/blob/main/research/`
    );
}

async function renderMarkdown(marked, markdown) {
  const normalized = absoluteSupplementLinks(markdown);
  const { protectedText, expressions } = protectMath(normalized);
  return restoreMath(await marked.parse(protectedText), expressions);
}

async function main() {
  const { values } = parseArgs({
    options: { 'draft-date': { type: 'string' } },
  });
  const draftDate = values['draft-date'];
  let draftDateLabel;
  if (draftDate) {
    if (!/^\d{4}-\d{2}-\d{2}$/.test(draftDate)) {
      throw new Error('Draft date must use YYYY-MM-DD');
    }
    const date = new Date(`${draftDate}T00:00:00Z`);
    if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== draftDate) {
      throw new Error('Invalid draft date');
    }
    draftDateLabel = new Intl.DateTimeFormat('en-GB', {
      day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC',
    }).format(date);
  }
  marked.setOptions({
    gfm: true,
    breaks: false,
    mangle: false,
    headerIds: true,
  });

  const markdown = fs.readFileSync(INPUT, 'utf8');
  const title = markdown.match(/^#\s+(.+)$/m)?.[1];
  const subtitle = markdown.match(/^##\s+(.+)$/m)?.[1];
  if (!title || !subtitle) throw new Error('Missing title or subtitle');

  const author = extractLine(markdown, 'Author');
  const orcid = markdown.match(/^ORCID:\s+\[([^\]]+)\]\(([^)]+)\)$/m);
  const doi = markdown.match(/^DOI \(all versions\):\s+\[([^\]]+)\]\(([^)]+)\)$/m);
  const version = extractLine(markdown, 'Version');
  const draftSuffix = draftDate ? `-working-draft-${draftDate}` : '';
  const documentLabel = draftDate ? `Working draft based on v${version}` : `v${version}`;
  const output = path.join(
    OUTPUT_DIRECTORY,
    `Informational-Cyclic-Cosmology-v${version}${draftSuffix}.pdf`
  );
  const releaseDate = extractLine(markdown, 'Release date');
  const status = extractLine(markdown, 'Status');
  if (!orcid || !doi) throw new Error('Missing ORCID or DOI metadata');

  const revisionMatch = markdown.match(
    /^Revision note:\s*([\s\S]*?)\n\n## Abstract$/m
  );
  const revisionNote = revisionMatch
    ? revisionMatch[1].replace(/\n/g, ' ').replace(/\s+/g, ' ').trim()
    : '';

  const abstractMatch = markdown.match(
    /## Abstract\n\n([\s\S]*?)\n\n## Scope and Claimed Contribution/
  );
  if (!abstractMatch) throw new Error('Could not isolate abstract');

  const bodyStart = markdown.indexOf('## Scope and Claimed Contribution');
  const bodyMarkdown = markdown.slice(bodyStart);
  const abstractHtml = await renderMarkdown(marked, abstractMatch[1]);
  const bodyHtml = await renderMarkdown(marked, bodyMarkdown);

  const documentHtml = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} - ${documentLabel}</title>
<script>
window.MathJax = {
  tex: {
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    processEscapes: true
  },
  chtml: { scale: 0.92 },
  startup: { typeset: false }
};
</script>
<style>
  :root {
    --ink: #18201e;
    --muted: #59615f;
    --green: #1f5b52;
    --line: #bfc9c6;
    --panel: #f3f6f5;
    --code: #eef2f1;
    --link: #0b6097;
  }
  * { box-sizing: border-box; }
  html { font-size: 10.6pt; }
  body {
    margin: 0;
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    line-height: 1.46;
    text-rendering: optimizeLegibility;
    hyphens: auto;
  }
  a { color: var(--link); text-decoration: none; }
  a:hover { text-decoration: underline; }
  p { margin: 0 0 0.78em; orphans: 3; widows: 3; }
  ul, ol { margin: 0.35em 0 0.9em 1.45em; padding: 0; }
  li { margin: 0.22em 0; padding-left: 0.18em; }
  strong { font-weight: 700; }
  .title-block {
    border-top: 4px solid var(--green);
    padding-top: 18px;
    margin-bottom: 18px;
  }
  .eyebrow {
    color: var(--green);
    font: 700 9pt/1.2 Arial, Helvetica, sans-serif;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 13px;
  }
  .eyebrow .divider { color: #8a9b97; padding: 0 10px; }
  h1 {
    margin: 0 0 11px;
    font: 700 28pt/1.08 Georgia, 'Times New Roman', serif;
    letter-spacing: 0;
    color: #121917;
  }
  .subtitle {
    max-width: 92%;
    color: var(--muted);
    font: 400 14.5pt/1.25 Arial, Helvetica, sans-serif;
    margin-bottom: 16px;
  }
  .author {
    font: 700 13.2pt/1.25 Georgia, 'Times New Roman', serif;
    margin-bottom: 7px;
  }
  .identifiers, .release {
    color: var(--muted);
    font: 400 9.8pt/1.45 Arial, Helvetica, sans-serif;
  }
  .identifiers { color: var(--link); }
  .meta-divider { color: #9aa6a3; padding: 0 9px; }
  .status {
    margin-top: 12px;
    border-left: 2px solid var(--green);
    background: var(--panel);
    padding: 8px 13px;
    color: var(--muted);
    font: 400 9.8pt/1.35 Arial, Helvetica, sans-serif;
  }
  .revision {
    margin-top: 9px;
    color: var(--muted);
    font: 400 9.2pt/1.42 Arial, Helvetica, sans-serif;
  }
  .revision strong { color: #33413e; }
  .abstract {
    margin: 0 0 25px;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    background: #f7f9f8;
    padding: 11px 18px 11px;
  }
  .abstract h2 {
    border-top: 1px solid var(--green);
    padding-top: 8px;
    margin: 0 0 12px;
    font-size: 11.5pt;
    letter-spacing: 0.03em;
    text-transform: uppercase;
  }
  .abstract p { font-size: 10.2pt; line-height: 1.38; margin-bottom: 0.55em; }
  h2 {
    color: var(--green);
    border-top: 1px solid var(--green);
    padding-top: 9px;
    margin: 25px 0 14px;
    font: 700 18pt/1.2 Arial, Helvetica, sans-serif;
    letter-spacing: 0;
    break-after: avoid-page;
    page-break-after: avoid;
  }
  h3 {
    color: #303d3a;
    margin: 20px 0 8px;
    font: 700 13.2pt/1.25 Arial, Helvetica, sans-serif;
    letter-spacing: 0;
    break-after: avoid-page;
    page-break-after: avoid;
  }
  h4 {
    color: #303d3a;
    margin: 16px 0 7px;
    font: 700 11pt/1.25 Arial, Helvetica, sans-serif;
    break-after: avoid-page;
    page-break-after: avoid;
  }
  blockquote {
    margin: 13px 0 15px;
    border-left: 3px solid var(--green);
    background: var(--panel);
    padding: 10px 14px 8px;
    break-inside: avoid-page;
    page-break-inside: avoid;
  }
  blockquote p { margin-bottom: 0.3em; }
  pre {
    margin: 12px 0 15px;
    padding: 11px 14px;
    background: var(--code);
    border-left: 2px solid #859d97;
    color: #273431;
    font: 8.8pt/1.42 Menlo, Consolas, monospace;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    break-inside: avoid-page;
    page-break-inside: avoid;
  }
  code {
    font-family: Menlo, Consolas, monospace;
    font-size: 0.88em;
    background: var(--code);
    padding: 0.08em 0.24em;
  }
  a code { color: inherit; background: transparent; padding: 0; }
  pre code { padding: 0; background: transparent; font-size: inherit; }
  table {
    width: 100%;
    margin: 12px 0 16px;
    border-collapse: collapse;
    font-size: 9.2pt;
    line-height: 1.32;
  }
  thead { display: table-header-group; }
  tr { break-inside: avoid-page; page-break-inside: avoid; }
  th, td {
    padding: 5px 7px;
    border-bottom: 0.5px solid #d5ddda;
    vertical-align: top;
    overflow-wrap: anywhere;
  }
  th {
    color: #303d3a;
    background: var(--panel);
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 700;
  }
  th:first-child, td:first-child { text-align: left; }
  table.results-summary { break-inside: avoid; page-break-inside: avoid; }
  table.results-summary th, table.results-summary td { padding: 3px 7px; }
  th:not(:first-child), td:not(:first-child) {
    text-align: left;
    white-space: normal;
  }
  mjx-container[jax='CHTML'][display='true'] {
    margin: 0.9em 0 !important;
    overflow: visible;
    break-inside: avoid-page;
    page-break-inside: avoid;
  }
  mjx-container { max-width: 100%; }
  p.equation-block { break-inside: avoid-page; page-break-inside: avoid; }
  p.scale-clarification { break-inside: avoid-page; page-break-inside: avoid; }
  p.equation-lead { break-after: avoid-page; page-break-after: avoid; }
  .references { font-size: 10pt; line-height: 1.4; }
  .references li { margin: 0.08em 0; break-inside: avoid-page; page-break-inside: avoid; }
  h2.disclosure-heading { break-before: page; page-break-before: always; }
  @media print {
    a { color: var(--link); }
    h2, h3, h4 { break-after: avoid-page; }
  }
</style>
</head>
<body>
  <section class="title-block">
    <div class="eyebrow">${draftDate ? 'Working Draft' : 'Conceptual Research Note'}<span class="divider">|</span>${draftDate ? 'Based on version' : 'Version'} ${version}</div>
    <h1>${title}</h1>
    <div class="subtitle">${subtitle}</div>
    <div class="author">${author}</div>
    <div class="identifiers">
      <a href="${orcid[2]}">ORCID ${orcid[1]}</a>
      <span class="meta-divider">|</span>
      <a href="${doi[2]}">Concept DOI ${doi[1]}</a>
    </div>
    <div class="release">${draftDate ? `${draftDateLabel}<span class="meta-divider">|</span>Revised from the ${releaseDate} release` : `Prepared ${releaseDate}<span class="meta-divider">|</span>Open preprint`}</div>
    <div class="status"><strong>Status:</strong> ${status}</div>
    ${revisionNote ? `<div class="revision"><strong>Revision note:</strong> ${revisionNote}</div>` : ''}
  </section>
  <section class="abstract">
    <h2>Abstract</h2>
    ${abstractHtml}
  </section>
  <main>${bodyHtml}</main>
</body>
</html>`;

  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.mkdirSync(path.dirname(HTML_OUTPUT), { recursive: true });
  fs.writeFileSync(HTML_OUTPUT, documentHtml);

  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.CHROME_EXECUTABLE ||
      (fs.existsSync('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        ? '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' : undefined),
  });
  try {
    const page = await browser.newPage();
    await page.goto(pathToFileURL(HTML_OUTPUT).href, { waitUntil: 'load' });
    await page.addScriptTag(process.env.MATHJAX_PATH
      ? { path: process.env.MATHJAX_PATH }
      : { url: 'https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js' });
    await page.waitForFunction(() => window.MathJax?.startup?.promise);
    await page.evaluate(async () => {
      await window.MathJax.startup.promise;
      await window.MathJax.typesetPromise();
      document.fonts && (await document.fonts.ready);
      for (const heading of document.querySelectorAll('h2')) {
        if (heading.textContent.trim() === 'References') {
          heading.nextElementSibling?.classList.add('references');
        }
        if (heading.textContent.trim() === 'Conceptual Provenance and AI-Assistance Disclosure') {
          heading.classList.add('disclosure-heading');
        }
      }
      for (const table of document.querySelectorAll('table')) {
        if (table.previousElementSibling?.textContent.trim() === 'Results and Limits') {
          table.classList.add('results-summary');
        }
      }
      for (const paragraph of document.querySelectorAll('p')) {
        if (paragraph.textContent.includes('Local inaccessibility alone does not establish conformal scale invariance')) {
          paragraph.classList.add('scale-clarification');
        }
        if (paragraph.querySelector('mjx-container[display="true"]')) {
          paragraph.classList.add('equation-block');
        } else if (paragraph.textContent.length <= 180 &&
                   paragraph.nextElementSibling?.matches('p') &&
                   paragraph.nextElementSibling.querySelector('mjx-container[display="true"]')) {
          paragraph.classList.add('equation-lead');
        }
      }
    });

    const mathErrors = await page.locator('mjx-merror').allTextContents();
    if (mathErrors.length) throw new Error(`MathJax errors: ${mathErrors.join('; ')}`);

    const renderCheck = await page.evaluate(() => ({
      displayMath: document.querySelectorAll('mjx-container[display="true"]').length,
      tables: document.querySelectorAll('table').length,
      placeholders: document.body.textContent.includes('MATHPLACEHOLDER'),
    }));
    if (renderCheck.placeholders) throw new Error('Unresolved math placeholders');
    console.log(JSON.stringify(renderCheck));

    const headerTemplate = `
      <div style="width:100%;margin:0 20mm;padding:0 0 5px;border-bottom:0.5px solid #bfc9c6;color:#2f3b38;font:6.8px Arial,sans-serif;display:flex;justify-content:space-between;">
        <span>${title}</span>
        <span>${author} | ${documentLabel}</span>
      </div>`;
    const footerTemplate = `
      <div style="width:100%;margin:0 20mm;padding:5px 0 0;border-top:0.5px solid #bfc9c6;color:#2f3b38;font:6.5px Arial,sans-serif;display:flex;justify-content:space-between;">
        <span>doi.org/${doi[1]}</span>
        <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
      </div>`;

    await page.pdf({
      path: output,
      format: 'A4',
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate,
      footerTemplate,
      margin: { top: '20mm', right: '20mm', bottom: '20mm', left: '20mm' },
      tagged: true,
      outline: true,
    });
  } finally {
    await browser.close();
  }

  process.stdout.write(`${output}\n`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
