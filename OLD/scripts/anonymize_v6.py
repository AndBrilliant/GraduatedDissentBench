#!/usr/bin/env python3
"""
v6 Anonymizer — strips all identifying information from papers.

Removes: author names, journal names, institutions, dates, DOIs, PMC IDs,
retraction mentions, references section, PMC footer boilerplate, PubMed links.

Each file is verified after anonymization.
"""
import os
import re
import sys

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dataset")
DST = os.path.join(SRC, "anonymized")

AUTHOR_NAMES = [
    "Hahn", "Manny", "Mamede", "Dhaliwal",
    "Kotz", "Levermann", "Wenz",
    "Protzko", "Krosnick", "Nelson", "Nosek",
    "Fortuna", "Gonzalez", "González", "Fritzler",
    "Elser", "Frankland", "Casey",
    "Schmidt", "Loef", "Ostermann", "Walach",
    "Allison",
]

INSTITUTIONS = [
    "University of Alberta", "Alberta", "Edmonton",
    "Potsdam Institute", "PIK", "Potsdam",
    "Buenos Aires", "Argentina",
    "Kaiser Permanente", "KPSC",
    "Taipei", "Taiwan",
    "Lebanon", "Beirut",
    "Israel", "Leumit",
    "McMaster", "Hamilton",
    "Freiburg",
]

JOURNALS = [
    "JAMA Pediatrics", "JAMA Neurology", "JAMA Neurol", "JAMA Network",
    "Nature Human Behaviour", "Nature Human Behavior",
    "Nature Climate Change", "Nature Medicine",
    "BMJ Nutrition", "BMJ Nutrition Prevention",
    "Scientific Reports", "Sci Rep", "Sci. Rep.",
    "International Journal of Obesity",
    "Lancet Regional Health", "Lancet Reg Health",
    "Journal of Clinical Epidemiology", "J Clin Epidemiol",
    "PLOS ONE", "PLoS ONE", "PLOS Medicine",
    "The Lancet", "Lancet",
    "The BMJ", "BMJ",
    "Nature", "JAMA", "PLOS", "PLoS",
]
# Sort longest first so "JAMA Pediatrics" gets replaced before "JAMA"
JOURNALS.sort(key=len, reverse=True)


def anonymize(text):
    """Strip all identifying information from paper text."""

    # 1. Strip PMC footer (everything after common footer markers)
    for marker in [
        "Articles from ",
        "ACTIONS View on publisher",
        "Follow NCBI",
        "Connect with NLM",
        "National Library of Medicine",
        "Back to Top",
        "RESOURCES Similar articles",
    ]:
        idx = text.rfind(marker)
        if idx > 0 and idx > len(text) * 0.7:
            text = text[:idx].strip()
            break

    # 2. Strip references section
    for marker in ["References ", "REFERENCES", "Bibliography", "Literature Cited"]:
        idx = text.rfind(marker)
        if idx > 0 and idx > len(text) * 0.5:
            text = text[:idx].strip()
            break

    # 3. Strip supplementary/data sections at end
    for section in [
        "Associated Data",
        "Supplementary Materials",
        "Supplement 1",
        "Data Sharing Statement",
        "Author Contributions",
        "Data Availability Statement",
    ]:
        idx = text.rfind(section)
        if idx > 0 and idx > len(text) * 0.8:
            text = text[:idx].strip()

    # 4. Strip acknowledgments/funding/conflicts at end
    for section in [
        "Acknowledgment",
        "Acknowledgement",
        "Funding Statement",
        "Conflict of Interest",
        "Conflicts of Interest",
        "Ethics Statement",
        "Ethics Approval",
    ]:
        idx = text.rfind(section)
        if idx > 0 and idx > len(text) * 0.75:
            text = text[:idx].strip()

    # 5. Strip author names
    for name in AUTHOR_NAMES:
        text = re.sub(r'\b' + re.escape(name) + r'\b', '[AUTHOR]', text)

    # 6. Strip institutions
    for inst in INSTITUTIONS:
        text = re.sub(re.escape(inst), '[INSTITUTION]', text, flags=re.IGNORECASE)

    # 7. Strip journal names
    for journal in JOURNALS:
        text = re.sub(re.escape(journal), '[JOURNAL]', text, flags=re.IGNORECASE)

    # 8. Strip dates
    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    text = re.sub(r'\b(' + months + r')\s+\d{1,2},?\s*\d{4}', '[DATE]', text)
    text = re.sub(r'\b20[012]\d-\d{2}-\d{2}\b', '[DATE]', text)

    # 9. Strip DOIs and IDs
    text = re.sub(r'doi:\s*\S+', '[DOI]', text, flags=re.IGNORECASE)
    text = re.sub(r'https?://doi\.org/\S+', '[DOI]', text)
    text = re.sub(r'10\.\d{4,}/\S+', '[DOI]', text)
    text = re.sub(r'PMC\d+', '[ID]', text)
    text = re.sub(r'PMID:?\s*\d+', '[ID]', text)

    # 10. Strip retraction mentions
    text = re.sub(r'(?i)\bretract(ed|ion|ions|ing)?\b', '', text)

    # 11. Strip PubMed/Scholar citation tags
    text = re.sub(r'\[\s*(PubMed|Google Scholar|PMC free article|DOI|CrossRef)\s*\]', '', text)

    # 12. Strip URLs
    text = re.sub(r'https?://\S+', '[URL]', text)

    # 13. Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def verify(text, fname):
    """Check for remaining identifying information."""
    problems = []

    # Check author names
    for name in AUTHOR_NAMES:
        if re.search(r'\b' + re.escape(name) + r'\b', text, re.IGNORECASE):
            count = len(re.findall(re.escape(name), text, re.IGNORECASE))
            problems.append(f"AUTHOR:{name}({count})")

    # Check institutions
    for inst in INSTITUTIONS:
        if re.search(re.escape(inst), text, re.IGNORECASE):
            count = len(re.findall(re.escape(inst), text, re.IGNORECASE))
            problems.append(f"INST:{inst}({count})")

    # Check journal names (raw, not [JOURNAL] tags)
    for j in ["JAMA", "BMJ", "Lancet", "PLOS", "Nature", "Scientific Reports"]:
        # Count raw mentions that aren't inside [JOURNAL]
        raw = len(re.findall(r'\b' + re.escape(j) + r'\b', text, re.IGNORECASE))
        tagged = text.count("[JOURNAL]")
        if raw > 0:
            problems.append(f"JOURNAL:{j}({raw})")

    # Check retraction
    if re.search(r'(?i)\bretract', text):
        problems.append("RETRACT")

    # Check PMC boilerplate
    for term in ["NCBI", "National Library", "PubMed", "Google Scholar", "courtesy of"]:
        if term.lower() in text.lower():
            problems.append(f"BOILERPLATE:{term}")

    return problems


def main():
    # Process all subdirectories
    for subdir in ["retracted", "controls", "hard_negatives"]:
        src_dir = os.path.join(SRC, subdir)
        if not os.path.exists(src_dir):
            continue

        print(f"\n=== Anonymizing {subdir}/ ===")
        for f in sorted(os.listdir(src_dir)):
            if not f.endswith(".txt"):
                continue

            with open(os.path.join(src_dir, f)) as fh:
                text = fh.read()

            orig_len = len(text)
            text = anonymize(text)
            new_len = len(text)

            outfile = os.path.join(DST, f.replace(".txt", "_anon.txt"))
            with open(outfile, "w") as fh:
                fh.write(text)

            problems = verify(text, f)
            status = "CLEAN" if not problems else f"ISSUES: {', '.join(problems[:6])}"
            print(f"  {f}: {orig_len}->{new_len} ({orig_len-new_len} removed) [{status}]")

    # Summary
    print(f"\n=== SUMMARY ===")
    total = 0
    clean = 0
    for f in sorted(os.listdir(DST)):
        if not f.endswith(".txt"):
            continue
        total += 1
        with open(os.path.join(DST, f)) as fh:
            text = fh.read()
        problems = verify(text, f)
        if not problems:
            clean += 1
        else:
            print(f"  REMAINING ISSUES in {f}: {', '.join(problems[:6])}")

    print(f"\n  {clean}/{total} files fully clean")
    if clean < total:
        print(f"  {total-clean} files need manual review")


if __name__ == "__main__":
    main()
