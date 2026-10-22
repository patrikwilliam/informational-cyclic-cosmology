"""Extract, validate and render the v0.2.0 PDF; visual judgment remains manual."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

import pdfplumber
from PIL import Image, ImageDraw
from pypdf import PdfReader


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path,
                        default=root / "output/pdf/Informational-Cyclic-Cosmology-v0.2.0.pdf")
    args = parser.parse_args()
    pdf = args.pdf.resolve()
    out = root / "tmp/pdfs/v020/qa"
    out.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(pdf)
    texts = [p.extract_text() for p in reader.pages]
    for expected in ("VERSION 0.2.0", "19 October 2026", "Patrik William Pustejovsky",
                     "0009-0008-1618-6619", "10.5281/zenodo.21115416"):
        require(expected in texts[0], f"Title-page metadata missing: {expected}")
    require(all("v0.2.0" in t for t in texts), "Running header mismatch")
    joined = "\n".join(texts)
    require("MATHPLACEHOLDER" not in joined and "\ufffd" not in joined,
            "Unresolved placeholder or replacement character")
    (out / "pages.txt").write_text("\n\n".join(
        f"=== PDF PAGE {i} ===\n{text}" for i, text in enumerate(texts, 1)))
    links = [str(a.get_object()["/A"]["/URI"]) for p in reader.pages
             for a in p.get("/Annots", []) if a.get_object().get("/A", {}).get("/URI")]
    require(all(link.startswith("https://") for link in links), "Non-HTTPS PDF link")
    for identifier in ("2005.04628v3", "2103.12042v3", "2110.11705v3"):
        require(f"https://arxiv.org/abs/{identifier}" in links, f"Missing citation: {identifier}")
    require(any("research/v020/lean/README.md" in link for link in links), "Missing Lean link")
    start = next(i for i, t in enumerate(texts, 1) if "Appendix D." in t and "D.1 Fixed" in t)
    end = next(i for i, t in enumerate(texts, 1) if i >= start and "References" in t)
    appendix = " ".join(re.sub(r"(?<=\w)-\n(?=\w)", "", "\n".join(texts[start-1:end])).split())
    for term in ("D.1 Fixed model", "D.2 Complete archive", "D.3 Conditional continuum",
                 "D.4 Same effects", "D.5 Physical implementation", "D.6 Verification",
                 "32 declarations", "not a universal decay no-go", "compatible marginals"):
        require(term in appendix, f"Missing appendix content: {term}")

    outliers, anomalies = [], []
    with pdfplumber.open(pdf) as doc:
        for number, page in enumerate(doc.pages, 1):
            for char in page.chars:
                if not char.get("text", "").strip():
                    continue
                if (char["x0"] < 35 or char["x1"] > page.width - 35 or
                        char["top"] < 5 or char["bottom"] > page.height - 5):
                    item = {"page": number, "text": char["text"], "font": char["fontname"]}
                    known = (("MathJax_Size1" in char["fontname"] and char["text"] in {"∥", "∣"}
                              and char["height"] > page.height) or
                             ("MathJax_Main-Regular" in char["fontname"] and char["text"] == "–"
                              and char["x1"] - char["x0"] > page.width))
                    (anomalies if known else outliers).append(item)
    bundled = Path.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm"
    poppler = os.environ.get("PDFTOPPM") or shutil.which("pdftoppm") or str(bundled)
    for pattern in ("page-*.png", "detail-*.png", "contact-*.png"):
        for old_render in out.glob(pattern):
            old_render.unlink()
    subprocess.run([poppler, "-r", "65", "-png", str(pdf), str(out / "page")], check=True, timeout=180)
    pages = sorted(out.glob("page-*.png"))
    require(len(pages) == len(reader.pages), "Rendered page count mismatch")
    for first in range(0, len(pages), 12):
        sheet = Image.new("RGB", (1080, 2136), "#d8d8d8")
        draw = ImageDraw.Draw(sheet)
        for i, file in enumerate(pages[first:first + 12]):
            with Image.open(file) as source:
                im = source.convert("RGB")
            im.thumbnail((346, 498))
            x, y = i % 3 * 360 + 7, i // 3 * 534 + 25
            sheet.paste(im, (x, y))
            draw.text((x, y - 19), f"Page {first + i + 1}", fill="black")
        sheet.save(out / f"contact-{first // 12 + 1}.png")
    details = {1, 2, 3, len(pages), *range(start, min(end + 2, len(pages)) + 1),
               *[x["page"] for x in anomalies + outliers]}
    for number in sorted(details):
        subprocess.run([poppler, "-f", str(number), "-l", str(number), "-r", "120",
                        "-singlefile", "-png", str(pdf), str(out / f"detail-{number:02d}")],
                       check=True, timeout=30)
    report = {"pdf": str(pdf), "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
              "source_sha256": hashlib.sha256((root / "PAPER.md").read_bytes()).hexdigest(),
              "pages": len(pages), "https_links": len(links), "appendix_pages": [start, end],
              "margin_outliers": outliers, "font_bbox_anomalies": anomalies,
              "visual_inspection": "pending manual inspection"}
    (out / "qa.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    require(not outliers, "Review unexplained PDF margin outliers")


if __name__ == "__main__":
    main()
