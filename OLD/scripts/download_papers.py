#!/usr/bin/env python3
"""
Download full text for all confirmed retracted papers.
Saves raw text to dataset/retracted/
Logs success/failure for each.
"""
import urllib.request
import json
import os
import sys
import time
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RETRACTED_DIR = os.path.join(BASE, "dataset", "retracted")
LOG_FILE = os.path.join(BASE, "dataset", "download_log.txt")

# PMC fetcher
def fetch_pmc(pmcid, label):
    """Fetch full text from PMC via NCBI E-utilities."""
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode"
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "GraduatedDissentBench/1.0")
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())

        # Extract text from BioC format
        texts = []
        for doc in data.get("documents", []):
            for passage in doc.get("passages", []):
                text = passage.get("text", "")
                if text:
                    texts.append(text)

        full_text = "\n\n".join(texts)
        if len(full_text) > 500:
            return full_text
    except Exception as e:
        print(f"  PMC BioC failed for {pmcid}: {e}")

    # Fallback: fetch HTML
    try:
        url2 = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
        req = urllib.request.Request(url2)
        req.add_header("User-Agent", "GraduatedDissentBench/1.0")
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        # Strip HTML tags (rough)
        text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        if len(text) > 1000:
            return text
    except Exception as e:
        print(f"  PMC HTML failed for {pmcid}: {e}")

    return None


def fetch_url(url, label):
    """Fetch text from a URL."""
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "GraduatedDissentBench/1.0")
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8", errors="replace")
        # If HTML, strip tags
        if "<html" in content.lower()[:200]:
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
            content = re.sub(r'<[^>]+>', ' ', content)
            content = re.sub(r'\s+', ' ', content).strip()
        return content if len(content) > 500 else None
    except Exception as e:
        print(f"  URL fetch failed for {label}: {e}")
        return None


# Paper registry
PAPERS = [
    {
        "id": "R01",
        "label": "hahn2023_long_covid",
        "title": "Post-COVID-19 Condition in Children",
        "pmc": "PMC10507591",
        "doi": "10.1001/jamapediatrics.2023.3239",
        "field": "Pediatrics",
        "cutoff": "post",
    },
    {
        "id": "R02",
        "label": "kotz2024_climate_economics",
        "title": "The economic commitment of climate change",
        "pmc": "PMC11023931",
        "doi": "10.1038/s41586-024-07219-0",
        "field": "Economics/Climate",
        "cutoff": "post",
    },
    {
        "id": "R03",
        "label": "protzko2024_replicability",
        "title": "High replicability of social-behavioural findings",
        "pmc": "PMC10896719",
        "doi": "10.1038/s41562-023-01749-9",
        "field": "Psychology",
        "cutoff": "post",
    },
    {
        "id": "R04",
        "label": "acv2024_weight_loss",
        "title": "Apple cider vinegar for weight loss",
        "pmc": "PMC11221284",
        "field": "Nutrition",
        "cutoff": "post",
    },
    {
        "id": "R05",
        "label": "victor2024_cardiac_arrest",
        "title": "IO vs IV vascular access in cardiac arrest",
        "doi": "10.1136/bmj-2024-079530",
        "url": "https://www.bmj.com/content/386/bmj-2024-079530",
        "field": "Emergency Medicine",
        "cutoff": "post",
    },
    {
        "id": "R07",
        "label": "placebo2024_meta_analysis",
        "title": "Placebo effect meta-analysis",
        "field": "Clinical Epidemiology",
        "cutoff": "post",
        "note": "NEEDS MANUAL IDENTIFICATION - title/DOI not confirmed",
    },
    {
        "id": "R10",
        "label": "vitd2022_covid",
        "title": "Vitamin D and COVID-19 morbidity",
        "doi": "10.1371/journal.pone.0263069",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263069",
        "field": "Medicine/COVID-19",
        "cutoff": "post",
    },
    {
        "id": "R11",
        "label": "fortuna2025_burnout_cortisol",
        "title": "Burnout/cortisol mediation analysis",
        "field": "Psychology/Occupational Health",
        "cutoff": "post",
        "note": "Scientific Reports, Open Access - need to find exact DOI",
    },
    {
        "id": "R19",
        "label": "glp1_2024_combo_therapy",
        "title": "GLP-1 combination therapy for weight loss",
        "doi": "10.1038/s41366-024-01526-2",
        "field": "Obesity/Pharmacology",
        "cutoff": "post",
    },
    {
        "id": "R24",
        "label": "together2021_metformin",
        "title": "COVID-19 metformin trial (TOGETHER)",
        "field": "Medicine/COVID-19",
        "cutoff": "post",
        "note": "Lancet Regional Health Americas - need exact DOI",
    },
    {
        "id": "R25",
        "label": "elser2024_wildfire_dementia",
        "title": "Wildfire Smoke Exposure and Incident Dementia",
        "doi": "10.1001/jamaneurol.2024.4058",
        "url": "https://jamanetwork.com/journals/jamaneurology/fullarticle/2826138",
        "field": "Neurology/Environmental Health",
        "cutoff": "post",
    },
]


def main():
    os.makedirs(RETRACTED_DIR, exist_ok=True)
    log = open(LOG_FILE, "w")

    success = 0
    failed = 0
    manual = 0

    for paper in PAPERS:
        pid = paper["id"]
        label = paper["label"]
        outfile = os.path.join(RETRACTED_DIR, f"{label}.txt")

        print(f"\n{'='*60}")
        print(f"{pid}: {paper['title']}")
        print(f"{'='*60}")

        if paper.get("note"):
            print(f"  NOTE: {paper['note']}")

        # Skip if already downloaded
        if os.path.exists(outfile) and os.path.getsize(outfile) > 1000:
            print(f"  Already downloaded: {outfile}")
            log.write(f"{pid}\t{label}\tSKIPPED (already exists)\n")
            success += 1
            continue

        text = None

        # Try PMC first
        if paper.get("pmc"):
            print(f"  Trying PMC: {paper['pmc']}...")
            text = fetch_pmc(paper["pmc"], label)
            if text:
                print(f"  SUCCESS via PMC ({len(text)} chars)")

        # Try direct URL
        if not text and paper.get("url"):
            print(f"  Trying URL: {paper['url'][:60]}...")
            text = fetch_url(paper["url"], label)
            if text:
                print(f"  SUCCESS via URL ({len(text)} chars)")

        # Try DOI redirect
        if not text and paper.get("doi"):
            doi_url = f"https://doi.org/{paper['doi']}"
            print(f"  Trying DOI: {doi_url}...")
            text = fetch_url(doi_url, label)
            if text:
                print(f"  SUCCESS via DOI ({len(text)} chars)")

        if text and len(text) > 1000:
            with open(outfile, "w") as f:
                f.write(text)
            print(f"  SAVED: {outfile} ({len(text)} chars)")
            log.write(f"{pid}\t{label}\tSUCCESS\t{len(text)} chars\n")
            success += 1
        elif paper.get("note") and "NEEDS" in paper.get("note", ""):
            print(f"  MANUAL: Paper needs identification first")
            log.write(f"{pid}\t{label}\tMANUAL\t{paper.get('note','')}\n")
            manual += 1
        else:
            print(f"  FAILED: Could not download")
            log.write(f"{pid}\t{label}\tFAILED\n")
            failed += 1

        time.sleep(1)  # Be polite to servers

    log.close()

    print(f"\n{'='*60}")
    print(f"SUMMARY: {success} downloaded, {failed} failed, {manual} need manual work")
    print(f"Log: {LOG_FILE}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
