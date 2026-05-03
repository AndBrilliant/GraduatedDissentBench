# Anonymization Methodology Note

## What is removed:
- Author names
- Institutional names (universities, hospitals, research institutes)
- Journal names
- DOIs, PMC IDs, PMIDs
- Email addresses
- Dates of publication/acceptance
- Retraction notices and mentions
- References sections
- Acknowledgments, funding, conflicts of interest, author contributions
- PMC/publisher boilerplate (headers, footers, navigation)
- Supplementary material links

## What is KEPT (by design):
- Country and region names when scientifically relevant to the study population
  (e.g., "Israel" for a study of Israeli health records, "California" for a
  study of California wildfire exposure). These are part of the methodology
  and removing them would alter the scientific content.
- Generic tool/software names (Stata, R, Python)
- Generic guideline names (STROBE, CONSORT)
- Study acronyms that are NOT the paper title (kept if they appear in methods)

## Rationale for keeping country names:
Country names identify the study population, which is relevant to
methodological evaluation (e.g., generalizability, healthcare system context).
Removing them would remove information that a reviewer needs to assess the
methodology. A model that correctly identifies a study population problem
should not be penalized because the country name was stripped.

However, country names can help identify specific papers. This is an
acknowledged limitation. The anonymization prioritizes preserving scientific
content over perfect de-identification.
