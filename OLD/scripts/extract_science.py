#!/usr/bin/env python3
"""
v6 Paper Extractor — extracts ONLY scientific content.

Philosophy: don't try to redact identifying info from messy HTML dumps.
Instead, extract only the sections that matter for methodological review:
  - Abstract
  - Introduction
  - Methods
  - Results
  - Discussion
  - Conclusion

Everything else is discarded: headers, footers, author blocks, affiliations,
acknowledgments, funding, conflicts, references, copyright, PMC boilerplate.

Each extracted paper gets a manual review flag file.
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIRS = ["dataset/retracted", "dataset/controls", "dataset/hard_negatives"]
DST = os.path.join(BASE, "dataset", "anonymized")

# Section headers we want to KEEP
KEEP_SECTIONS = [
    "Abstract",
    "Introduction",
    "Background",
    "Methods", "Materials and Methods", "Study Design", "Methodology",
    "Statistical Analysis", "Statistical Methods", "Data Analysis",
    "Results",
    "Discussion",
    "Conclusion", "Conclusions",
    "Main",  # Nature uses "Main" instead of Introduction
    "Study Population", "Study Design and Participants",
    "Measures", "Outcomes", "Variables",
    "Sensitivity Analysis", "Subgroup Analysis",
]

# Section headers that signal END of science content
STOP_SECTIONS = [
    "References",
    "Acknowledgment", "Acknowledgement", "Acknowledgments", "Acknowledgements",
    "Funding", "Funding Statement",
    "Conflict of Interest", "Conflicts of Interest", "Competing Interests",
    "Author Contributions", "Authors' Contributions", "CRediT",
    "Data Availability", "Data Sharing", "Data Access",
    "Supplementary", "Supplement", "Supporting Information",
    "Ethics Statement", "Ethics Approval", "Ethical Approval",
    "Associated Data",
    "Copyright",
    "ACTIONS",
    "Articles from",
    "Follow NCBI",
]

# PMC/publisher junk to strip entirely
JUNK_PATTERNS = [
    r"Skip to main content.*?(?=Abstract|Introduction|Background|Main)",
    r"An official website of the United States government.*?(?=Abstract|Introduction|Background|Main)",
    r"Search.*?PMC Full-Text Archive.*?(?=Abstract|Introduction|Background|Main)",
    r"PERMALINK Copy.*?(?=Abstract|Introduction|Background|Main)",
    r"As a library, NLM provides access.*?(?=Abstract|Introduction|Background|Main)",
    r"This article has been\s*\.?\s*(?:in:|See also:).*?(?=Abstract)",
    r"Search in PMC.*?(?=Abstract|Introduction)",
    r"Find articles by.*?\n",
    r"Author information.*?(?=Abstract)",
    r"Article notes.*?(?=Abstract)",
    r"Copyright and License information.*?(?=Abstract)",
    r"Open in a new tab",
    r"Click here for additional data file.*?(?:pdf|xlsx?)\)",
    r"\[\s*(?:PubMed|Google Scholar|PMC free article|DOI|CrossRef)\s*\]",
    r"NCBI.*?(?:Twitter|Facebook|LinkedIn|GitHub|RSS)",
    r"National Library of Medicine.*?(?:USA\.gov|Back to Top)",
    r"Web Policies.*?(?:HHS|NIH|NLM)",
]

# Identifying info to replace
REDACTIONS = {
    # Dates
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s*\d{4}": "[DATE]",
    r"\b20[012]\d-\d{2}-\d{2}\b": "[DATE]",
    # DOIs
    r"(?:doi:|DOI:)\s*\S+": "[DOI]",
    r"https?://doi\.org/\S+": "[DOI]",
    r"\b10\.\d{4,}/\S+": "[DOI]",
    # IDs
    r"\bPMC\d+\b": "[ID]",
    r"\bPMID:?\s*\d+\b": "[ID]",
    # URLs
    r"https?://\S+": "[URL]",
    # Email addresses
    r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b": "[EMAIL]",
}


def find_science_start(text):
    """Find where the actual scientific content begins."""
    # Look for Abstract or Introduction
    for marker in ["Abstract ", "ABSTRACT ", "Introduction ", "INTRODUCTION ", "Background ", "Main "]:
        # Find first occurrence that's NOT inside PMC junk
        idx = 0
        while True:
            pos = text.find(marker, idx)
            if pos == -1:
                break
            # Check it's not buried in boilerplate (look at surrounding context)
            before = text[max(0, pos-100):pos]
            if "PMC" not in before and "NCBI" not in before and "Search" not in before:
                return pos
            idx = pos + 1

    # Fallback: just skip first 500 chars of junk
    return min(500, len(text) // 10)


def find_science_end(text):
    """Find where the scientific content ends (before references, acknowledgments, etc)."""
    best_end = len(text)

    for section in STOP_SECTIONS:
        # Search from the back — we want the LAST occurrence of these
        # (some papers mention "References" in text, we want the section header)
        idx = len(text) - 1
        while idx > len(text) * 0.4:  # Only look in last 60% of document
            pos = text.rfind(section, 0, idx)
            if pos == -1:
                break
            # Check if this looks like a section header (preceded by whitespace or period)
            before_char = text[pos-1] if pos > 0 else " "
            if before_char in " .\n\t":
                if pos < best_end:
                    best_end = pos
                break
            idx = pos - 1

    return best_end


def extract_science(text):
    """Extract only the scientific content from a paper."""

    # Step 1: Remove known junk patterns
    for pattern in JUNK_PATTERNS:
        text = re.sub(pattern, " ", text, flags=re.DOTALL | re.IGNORECASE)

    # Step 2: Find science boundaries
    start = find_science_start(text)
    end = find_science_end(text)

    # Extract
    science = text[start:end].strip()

    # Step 3: Remove author block if it survived
    # Author blocks typically have patterns like "Name Name , PhD" or "Department of"
    lines = science.split(". ")
    cleaned_lines = []
    skip_until_abstract = True

    for line in lines:
        line_lower = line.lower().strip()

        # Skip lines that look like author/affiliation info
        if skip_until_abstract:
            if "abstract" in line_lower[:20]:
                skip_until_abstract = False
                cleaned_lines.append(line)
            elif any(x in line_lower for x in ["department of", "faculty of", "find articles by",
                                                 "author information", "article notes",
                                                 "copyright and license", "accepted for publication",
                                                 "corresponding author", "author contributions",
                                                 "conflict of interest disclosures",
                                                 "funding/support", "role of the funder",
                                                 "data sharing statement"]):
                continue  # Skip this line
            elif re.match(r"^[A-Z][a-z]+ [A-Z]\s+[A-Z][a-z]+", line.strip()):
                continue  # Looks like "Firstname M Lastname" — skip
            else:
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    science = ". ".join(cleaned_lines)

    # Step 4: Apply redactions
    for pattern, replacement in REDACTIONS.items():
        science = re.sub(pattern, replacement, science, flags=re.IGNORECASE)

    # Step 5: Remove any remaining retraction mentions
    science = re.sub(r"(?i)\bretract(ed|ion|ions|ing)?\b", "", science)
    science = re.sub(r"(?i)this article has been\s*\.?\s*", "", science)
    science = re.sub(r"(?i)expression of concern", "", science)

    # Step 6: Clean up
    science = re.sub(r"\s+", " ", science).strip()

    return science


def verify(text):
    """Check for remaining problems."""
    problems = []

    # Check for PMC boilerplate
    for term in ["NCBI", "National Library", "PubMed Central", "PMC Full-Text",
                 "Google Scholar", "courtesy of", "Skip to main content",
                 "official website", "USA.gov"]:
        if term.lower() in text.lower():
            problems.append(f"BOILERPLATE:{term}")

    # Check for retraction
    if re.search(r"(?i)\bretract", text):
        problems.append("RETRACT")

    # Check for obvious author patterns
    if re.search(r"Find articles by", text):
        problems.append("AUTHOR_BLOCK")
    if re.search(r"Corresponding [Aa]uthor", text):
        problems.append("CORRESPONDING")
    if re.search(r"Author [Cc]ontributions", text):
        problems.append("CONTRIBUTIONS")

    # Check for copyright
    if re.search(r"Copyright \d{4}", text):
        problems.append("COPYRIGHT")
    if re.search(r"All Rights Reserved", text):
        problems.append("COPYRIGHT")

    return problems


def main():
    os.makedirs(DST, exist_ok=True)

    total = 0
    clean = 0

    for subdir in SRC_DIRS:
        src_dir = os.path.join(BASE, subdir)
        if not os.path.exists(src_dir):
            continue

        print(f"\n=== Processing {subdir}/ ===")

        for f in sorted(os.listdir(src_dir)):
            if not f.endswith(".txt"):
                continue

            with open(os.path.join(src_dir, f)) as fh:
                raw = fh.read()

            science = extract_science(raw)

            outname = f.replace(".txt", "_anon.txt")
            outpath = os.path.join(DST, outname)
            with open(outpath, "w") as fh:
                fh.write(science)

            problems = verify(science)
            total += 1

            if not problems:
                clean += 1
                status = "CLEAN"
            else:
                status = f"ISSUES: {', '.join(problems)}"

            pct_kept = len(science) * 100 // len(raw) if raw else 0
            print(f"  {f}: {len(raw)} -> {len(science)} ({pct_kept}% kept) [{status}]")

    print(f"\n=== SUMMARY: {clean}/{total} fully clean ===")

    if clean < total:
        print("\nFiles needing manual review:")
        for f in sorted(os.listdir(DST)):
            if not f.endswith(".txt"):
                continue
            with open(os.path.join(DST, f)) as fh:
                text = fh.read()
            problems = verify(text)
            if problems:
                print(f"  {f}: {', '.join(problems)}")


if __name__ == "__main__":
    main()
