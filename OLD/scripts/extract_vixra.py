#!/usr/bin/env python3
"""Extract and anonymize viXra GUT papers for benchmark."""
import os, re
from PyPDF2 import PdfReader

BASE = os.path.expanduser("~/Desktop/Academic/graduated_dissent_bench_v6")
VIXRA_DIR = os.path.join(BASE, "dataset/vixra_gut")
ANON_DIR = os.path.join(BASE, "dataset/anonymized")

# Paper metadata for anonymization
PAPERS = {
    "V01": {
        "file": "V01_raw.pdf",
        "authors": ["Kozo Koizumi", "Koizumi"],
        "strip": ["viXra", "vixra", "2603.0048"],
    },
    "V02": {
        "file": "V02_raw.pdf",
        "authors": ["Bijon Kumar Sen", "Subha Sen", "B. K. Sen", "B.K. Sen", "Sen"],
        "strip": ["viXra", "vixra", "2601.0005"],
    },
    "V03": {
        "file": "V03_raw.pdf",
        "authors": ["Hacı Soğukpınar", "Sogukpinar", "Soğukpınar", "Haci"],
        "strip": ["viXra", "vixra", "2508.0006"],
    },
    "V04": {
        "file": "V04_raw.pdf",
        "authors": ["Bin Li"],
        "strip": ["viXra", "vixra", "2507.0041"],
    },
    "V05": {
        "file": "V05_raw.pdf",
        "authors": ["Rubén Yruretagoyena Conde", "Yruretagoyena", "Rubén", "Ruben"],
        "strip": ["viXra", "vixra", "2507.0015", "Hijolumínic", "hijoluminic"],
    },
}

os.makedirs(ANON_DIR, exist_ok=True)

for pid, meta in PAPERS.items():
    pdf_path = os.path.join(VIXRA_DIR, meta["file"])
    print(f"\n{'='*60}")
    print(f"Processing {pid}: {meta['file']}")

    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    except Exception as e:
        print(f"  ERROR reading PDF: {e}")
        continue

    if not text.strip():
        print(f"  WARNING: No text extracted from PDF")
        continue

    print(f"  Extracted {len(text)} chars, {len(reader.pages)} pages")

    # Anonymize
    anon = text

    # Remove author names (case insensitive)
    for author in meta["authors"]:
        anon = re.sub(re.escape(author), "[AUTHOR]", anon, flags=re.IGNORECASE)

    # Remove viXra identifiers and other strip terms
    for term in meta["strip"]:
        anon = re.sub(re.escape(term), "[REDACTED]", anon, flags=re.IGNORECASE)

    # Remove email addresses
    anon = re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+', '[EMAIL]', anon)

    # Remove URLs
    anon = re.sub(r'https?://\S+', '[URL]', anon)

    # Remove date patterns that could identify the paper
    # But keep dates that are scientifically relevant

    # Remove affiliation patterns (university, institute, department)
    # Be conservative - just flag obvious ones
    anon = re.sub(r'(?i)(department|faculty|university|institute|college)\s+of\s+\w+[\w\s,]*', '[AFFILIATION]', anon)

    # Remove "submitted to" or "accepted by" journal references
    anon = re.sub(r'(?i)(submitted to|accepted by|published in|to appear in)\s+\w+[\w\s]*', '[REDACTED]', anon)

    # Write anonymized version
    out_path = os.path.join(ANON_DIR, f"{pid}_anon.txt")
    with open(out_path, "w") as f:
        f.write(anon)

    print(f"  Anonymized: {len(anon)} chars -> {out_path}")

    # Quick check: search for any remaining author names
    for author in meta["authors"]:
        if author.lower() in anon.lower():
            print(f"  WARNING: Author name '{author}' still found in anonymized text!")

print("\n\nDone. Check anonymized files for any remaining identifying information.")
