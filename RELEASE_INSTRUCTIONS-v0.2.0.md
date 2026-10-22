# v0.2.0 Release Instructions

Prepared 19 October 2026. This document does not publish, tag, push or upload
anything. Keep the prior PDFs and Zenodo records unchanged.

## Read and Reproduce

1. Read the abstract, results-and-limits table and Appendix D in
   [the new PDF](Informational-Cyclic-Cosmology-v0.2.0.pdf).
2. Read the separately prompted [mathematical review](feedback/v0.2.0-pdf-mathematical-review.md),
   [physics review](feedback/v0.2.0-pdf-physics-review.md), and
   [integration record](feedback/v0.2.0-integration-verification.md). Resolve
   any blocking findings. These are AI reviews, not external peer review.
3. Run `python3 research/v020/run_checks.py --timeout 120` with NumPy available.
4. Recheck the formal package using its [Lean instructions](research/v020/lean/README.md).
   The two-hour development limit did not formalize the continuum theorem.
5. Keep the source, PDF, `CITATION.cff`, release notes and supplement together.
   Preserve the explicit boundaries between diagnostics, formal components,
   analytic arguments and unresolved physics.

## Rebuild the PDF

The editable source is `PAPER.md`; do not edit the generated PDF directly.
The renderer needs Node.js with `marked` and `playwright` resolvable, and a
Chrome/Chromium executable. It uses the installed macOS Chrome by default;
set `CHROME_EXECUTABLE` for another installation. The verified build loads
MathJax 3.2.2 from its CDN and needs network access. `MATHJAX_PATH` can override
the entry script, but a fully offline setup, including fonts and extensions,
has not been verified here.

From the repository root:

```bash
node research/v020/build_pdf.cjs
python3 research/v020/check_pdf.py
```

The second command requires `pypdf`, `pdfplumber`, Pillow and Poppler's
`pdftoppm` (`PDFTOPPM` can point to that executable). It extracts text and
links, checks metadata and margins, and renders all pages to
`tmp/pdfs/v020/qa/`. Inspect the contact sheets and detailed pages: automated
checks cannot certify legible equations or good pagination.

The new PDF is written to `output/pdf/`. After visual checks and any review
corrections, copy those final bytes to
`Informational-Cyclic-Cosmology-v0.2.0.pdf` at repository root. A content change
requires a rebuild and updated review hash. Render timestamps can also change
the PDF hash even when the manuscript is unchanged; identify the actual
reviewed file rather than promising byte-identical rebuilds.

## GitHub

Retain the established root PDF location. Include `PAPER.md`, `README.md`,
`CITATION.cff`, the v0.2.0 PDF, release notes/instructions, `research/v020/`,
and the final review reports. Preserve previous research and cited supplements.
Do not use an indiscriminate add-all on this dirty working tree; inspect the
intended file list before committing. Exclude `.lake/`, `tmp/`, `output/`,
`verification-output/`, `.DS_Store`, `._*`, `__MACOSX`, local toolchains and
dependency caches. Create a `v0.2.0` tag/release only after approving the files.

## Zenodo and DOI

Use **New version** on the existing record, not an unrelated new deposition.
Upload the new PDF and the intended source/supplement package; do not retain
an old PDF accidentally as the new version's main file. Check version `0.2.0`,
creator, ORCID, description, keywords and the existing CC BY 4.0 license before
publishing. Zenodo versions have separate identifiers and remain linked.
[Official versioning instructions](https://help.zenodo.org/docs/deposit/manage-versions/).

The PDF deliberately retains the all-versions DOI
`10.5281/zenodo.21115416`, labelled as such. There is no need to rebuild it
solely because Zenodo assigns a version DOI later. Do not enter that concept
DOI as an already-issued DOI for a new, separate upload.

If a version-specific DOI inside the PDF is required, reserve the draft's
DOI before finalizing the file, rebuild once with that verified identifier,
and upload those final bytes before publication. Do not invent or predict it.
[Official DOI reservation instructions](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/).

If GitHub-Zenodo automatic archiving is already enabled for this repository,
choose that established workflow or a manual Zenodo new-version workflow,
not both independently for the same release. This task has not inspected or
changed that integration.

## Safe Summary for the Record

Version 0.2.0 adds a conditional continuum detector and outcome-bearing tick
study. Two retained-record marginals have distinct operator systems under a
specified instrument; different generated algebras and a physical ICC selector
are not established. A same-POVM counterexample, two finite diagnostic methods
and scoped Lean proofs clarify the result and its limitations.
