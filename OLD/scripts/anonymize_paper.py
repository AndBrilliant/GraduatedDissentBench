#!/usr/bin/env python3
"""Anonymize a paper text file for the Graduated Dissent Benchmark.

Strips author names, journal names, dates, affiliations, acknowledgments,
funding sections, retraction notices, and errata references. Replaces
identifiable information with bracketed placeholders.

Usage: python3 anonymize_paper.py input.txt output.txt
"""

import argparse
import re
import sys


# Common affiliation markers
AFFILIATION_PATTERNS = [
    r"(?i)^.*(?:department|dept\.?|school|faculty|institute|center|centre|laboratory|lab|college|university|univ\.?|hospital|medical center|research group)\b.*$",
]

# Section headers to remove entirely (case-insensitive)
REMOVE_SECTIONS = [
    r"acknowledgment",
    r"acknowledgement",
    r"acknowledgments",
    r"acknowledgements",
    r"funding",
    r"financial support",
    r"grant support",
    r"competing interests",
    r"conflict of interest",
    r"author contributions",
    r"author information",
]

# Retraction / errata patterns
RETRACTION_PATTERNS = [
    r"(?i)\bretraction\b.*(?:notice|statement|note)?\b",
    r"(?i)\berrat(?:um|a)\b",
    r"(?i)\bcorrection notice\b",
    r"(?i)\bthis (?:article|paper) has been retracted\b",
    r"(?i)\bexpression of concern\b",
]

# Date patterns
DATE_PATTERNS = [
    # "January 2024", "Jan 2024", "Jan. 2024"
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan\.?|Feb\.?|Mar\.?|Apr\.?|Jun\.?|Jul\.?|Aug\.?|Sep(?:t)?\.?|Oct\.?|Nov\.?|Dec\.?)\s+\d{4}\b",
    # "12 January 2024", "12 Jan 2024"
    r"\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan\.?|Feb\.?|Mar\.?|Apr\.?|Jun\.?|Jul\.?|Aug\.?|Sep(?:t)?\.?|Oct\.?|Nov\.?|Dec\.?)\s+\d{4}\b",
    # "2024-01-15", "2024/01/15"
    r"\b\d{4}[-/]\d{2}[-/]\d{2}\b",
    # "01/15/2024", "01-15-2024"
    r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",
    # Received/Accepted/Published date lines
    r"(?i)(?:received|accepted|published|submitted|revised|online)\s*:?\s*\d{1,2}\s+\w+\s+\d{4}",
    r"(?i)(?:received|accepted|published|submitted|revised|online)\s*:?\s*\w+\s+\d{1,2},?\s+\d{4}",
]

# Journal name patterns (common contexts where journal names appear)
JOURNAL_PATTERNS = [
    # "Published in <Journal Name>"
    r"(?i)published\s+in\s+[A-Z][A-Za-z\s&:]+",
    # Common journal name patterns in references
    r"(?i)(?:journal of|annals of|proceedings of|transactions on|reviews? of|archives of|bulletin of)\s+[A-Za-z\s&]+",
    # Italicized or quoted journal names in references (simple heuristic)
    r"(?i)(?:Nature|Science|JAMA|BMJ|Lancet|PNAS|NEJM|Cell|PLoS\s+\w+)\b",
]


def find_author_block(lines):
    """Heuristic: find the author block near the top of the paper.

    Looks for lines after the title (first non-empty line) that contain
    comma-separated names, email addresses, or superscript markers before
    the abstract or introduction.
    """
    author_line_indices = []
    found_title = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            if found_title and author_line_indices:
                # blank line after author block -- stop
                break
            continue

        # Skip the title (first substantial line)
        if not found_title:
            found_title = True
            continue

        # Stop at abstract/introduction
        if re.match(r"(?i)^\s*(abstract|introduction|1[\.\s])", stripped):
            break

        # Heuristic: author lines often have commas, "and", superscripts,
        # or email-like patterns, and are relatively short
        if len(stripped) < 200:
            has_name_pattern = bool(re.search(r"[A-Z][a-z]+\s+[A-Z][a-z]+", stripped))
            has_email = bool(re.search(r"\S+@\S+", stripped))
            has_superscript = bool(re.search(r"[\d*†‡§¶]+", stripped))
            has_comma_names = bool(re.search(r"[A-Z][a-z]+.*,.*[A-Z][a-z]+", stripped))

            if has_email or (has_name_pattern and (has_comma_names or has_superscript)):
                author_line_indices.append(i)
            elif author_line_indices and re.match(r"(?i)^\s*and\s+", stripped):
                author_line_indices.append(i)

    return author_line_indices


def extract_author_names(lines, author_indices):
    """Extract individual author names from author block lines."""
    names = []
    for i in author_indices:
        text = lines[i].strip()
        # Remove emails
        text = re.sub(r"\S+@\S+", "", text)
        # Remove superscripts/markers
        text = re.sub(r"[*†‡§¶]+", "", text)
        # Remove numbers that look like affiliations
        text = re.sub(r"\d+", "", text)
        # Split on commas and "and"
        parts = re.split(r",|\band\b", text)
        for part in parts:
            part = part.strip()
            # A name is typically 2-4 capitalized words
            if re.match(r"^[A-Z][a-z]+(?:\s+[A-Z]\.?)?(?:\s+[A-Z][a-z]+){1,3}$", part):
                names.append(part)
    return names


def remove_section(lines, header_pattern):
    """Remove a section from its header to the next section header."""
    result = []
    in_removed_section = False
    section_header_re = re.compile(
        r"^\s*(?:\d+[\.\s]*)?(" + header_pattern + r")\s*$", re.IGNORECASE
    )
    # Generic section header: starts with a number or all-caps or title-case short line
    next_section_re = re.compile(
        r"^\s*(?:\d+[\.\s]+[A-Z]|[A-Z][A-Z\s]{2,}$|References$|Bibliography$)", re.IGNORECASE
    )

    for line in lines:
        if in_removed_section:
            if next_section_re.match(line.strip()) and not section_header_re.match(line.strip()):
                in_removed_section = False
                result.append(line)
        else:
            if section_header_re.match(line.strip()):
                in_removed_section = True
            else:
                result.append(line)
    return result


def anonymize(text):
    """Main anonymization pipeline."""
    lines = text.splitlines()

    # --- Step 1: Find and replace author names ---
    author_indices = find_author_block(lines)
    author_names = extract_author_names(lines, author_indices)

    # Replace author block lines with placeholders
    if author_indices:
        placeholder_line = "  ".join(
            f"[AUTHOR_{i+1}]" for i in range(max(len(author_names), 1))
        )
        # Replace first author line with placeholder, remove rest
        lines[author_indices[0]] = placeholder_line
        for i in sorted(author_indices[1:], reverse=True):
            lines.pop(i)

    # Replace author names throughout the text (longer names first to avoid partial matches)
    author_names_sorted = sorted(author_names, key=len, reverse=True)
    name_map = {}
    for idx, name in enumerate(author_names_sorted):
        tag = f"[AUTHOR_{idx+1}]"
        name_map[name] = tag
        # Also handle last-name-only references
        parts = name.split()
        if len(parts) >= 2:
            lastname = parts[-1]
            if lastname not in name_map:
                name_map[lastname] = tag

    text = "\n".join(lines)
    for name, tag in name_map.items():
        text = re.sub(r"\b" + re.escape(name) + r"\b", tag, text)

    lines = text.splitlines()

    # --- Step 2: Remove affiliation lines near the top ---
    # Only check the first ~30 lines (header area)
    for i in range(min(30, len(lines))):
        for pat in AFFILIATION_PATTERNS:
            if re.match(pat, lines[i].strip()):
                lines[i] = ""
                break

    # --- Step 3: Remove sections (acknowledgments, funding, etc.) ---
    for section_pat in REMOVE_SECTIONS:
        lines = remove_section(lines, section_pat)

    # --- Step 4: Remove retraction/errata notices ---
    filtered = []
    for line in lines:
        is_retraction = False
        for pat in RETRACTION_PATTERNS:
            if re.search(pat, line):
                is_retraction = True
                break
        if not is_retraction:
            filtered.append(line)
    lines = filtered

    text = "\n".join(lines)

    # --- Step 5: Replace dates ---
    for pat in DATE_PATTERNS:
        text = re.sub(pat, "[DATE]", text)

    # --- Step 6: Replace journal names ---
    for pat in JOURNAL_PATTERNS:
        text = re.sub(pat, "[JOURNAL]", text)

    # Clean up multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


def main():
    parser = argparse.ArgumentParser(
        description="Anonymize a paper text file for the Graduated Dissent Benchmark."
    )
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output anonymized text file")
    parser.add_argument(
        "--extra-names",
        nargs="*",
        default=[],
        help="Additional author names to strip (e.g. 'John Smith' 'Jane Doe')",
    )
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    result = anonymize(text)

    # Handle any extra names provided on the command line
    for i, name in enumerate(args.extra_names):
        tag = f"[AUTHOR_EXTRA_{i+1}]"
        result = re.sub(r"\b" + re.escape(name) + r"\b", tag, result)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Anonymized output written to {args.output}")


if __name__ == "__main__":
    main()
