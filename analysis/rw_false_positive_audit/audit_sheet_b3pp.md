# B3++ — RW false-positive audit sheet

**Total RW findings:** 112  
**Matched SPOT annotation:** 7  
**Unmatched (this audit):** 105  

## Summary (fill in after manual review)

```
Total non-matching RW findings: 105
Valid severe (SPOT missed): ___
Related (real but overstated): ___
False alarm: ___

Original RW-precision: 7/112 = 6.2%
Adjusted RW-precision: (7 + valid_severe) / 112 = ___%
```

## How to fill in `human_verdict`

- **VALID**: Reading the finding alongside the paper, this is a genuine severe methodological error that, if confirmed, would warrant retraction. SPOT didn't annotate it because SPOT lists only the single retraction-causing error per paper.
- **RELATED**: The finding identifies a real issue, but the severity rating is too high (should have been MAJOR-REVISION).
- **FALSE**: Not a real error, or an error that does not rise to retraction-worthy severity.

---

### 10.1016_j.jpcs.2024.112058 — Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications

- **Paper category:** Materials Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Specific capacitance equations are internally inconsistent and at least one is dimensionally incorrect. Eq. (3) for CV-derived gravimetric capacitance has incorrect variable arrangement; Eq. (4) is labeled as specific capacitance but computes areal capacitance. The text conflates these throughout, making the derivation of the headline 1502 F/g value unverifiable and likely incorrect.

- **Arbiter justification for RW classification:**  
  > The paper's central claim is a specific capacitance value. If the equations used to derive that value are dimensionally wrong or confuse gravimetric and areal normalization, then the flagship number is not a valid measurement of the claimed quantity. This is not a presentation issue—it means the primary result cannot be supported as presented. Both reviewers flagged formula problems; Reviewer A rated this retraction-worthy and Reviewer B rated it major-revision but acknowledged the formulas could invalidate reported numbers. On balance, the direct link between broken equations and the headline metric meets the retraction-worthy threshold.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.jpcs.2024.112058 — Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications

- **Paper category:** Materials Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The reported energy density (61.05 Wh/kg) is arithmetically inconsistent with the manuscript's own stated formula and inputs. Using SE = Cs×ΔV²/7.2 with Cs = 1502 F/g and ΔV = 0.65 V yields ~88 Wh/kg, not 61.05 Wh/kg. No corrected voltage window or IR-drop adjustment is disclosed.

- **Arbiter justification for RW classification:**  
  > A headline quantitative result fails a direct substitution check using the paper's own equation and stated parameters. The ~44% discrepancy is far too large for rounding. This means the promoted energy density value is either calculated with undisclosed inputs or is simply wrong. Either way, a central claim in the abstract is numerically unsupported. Reviewer A identified this; Reviewer B acknowledged it as a critical arithmetic error in reflection. This independently breaks a headline claim.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.jpcs.2024.112058 — Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications

- **Paper category:** Materials Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Energy density and power density are derived from a three-electrode half-cell measurement but presented as supercapacitor device performance metrics (61.05 Wh/kg, 270.5 W/kg). No two-electrode device was constructed or tested.

- **Arbiter justification for RW classification:**  
  > Half-cell electrode data systematically overstate device-level energy and power density. The manuscript foregrounds these values in the abstract and conclusion as evidence of practical supercapacitor performance. Since no full device was tested, these application-level claims are methodologically invalid regardless of whether the underlying electrode material is good. Reviewer A rated this retraction-worthy; Reviewer B recognized it as a separate fundamental error in reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.jpcs.2024.112058 — Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications

- **Paper category:** Materials Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The reported specific capacitance of 1502 F/g at 1.0 A/g in a 0.65 V window in aqueous KOH is physically implausible. This corresponds to ~271 mAh/g equivalent capacity, exceeding known pseudocapacitive material limits in such a narrow window. Combined with a moderate BET surface area (61.43 m²/g), the implied areal capacitance (~24.4 F/m²) is far beyond established double-layer or pseudocapacitive limits.

- **Arbiter justification for RW classification:**  
  > While plausibility arguments alone can be debatable, here the implausibility is extreme and is corroborated by multiple independent calculation errors (broken formulas, arithmetic inconsistency). The convergence of an implausible number with demonstrably flawed calculation methods strongly indicates the value is erroneous. Reviewer B rated this retraction-worthy; Reviewer A's formula-error findings provide the mechanistic explanation for why the number is wrong. Together this meets the threshold.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.scenv.2024.100142 — Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes

- **Paper category:** Environmental Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > No statistical analysis reported for cell viability data (no replicates, no variance, no p-values, no statistical test identified), yet the manuscript makes explicit claims of 'no significant adverse effects' and 'significantly higher viability.'

- **Arbiter justification for RW classification:**  
  > The biomedical conclusion depends on statistical inference, but no inferential substrate exists in the paper. A single percentage (92%) with no n, no error, and no test cannot support claims of significance. This is not a reporting gap—it is the absence of the evidence required for the stated conclusion. Both reviewers independently rated this retraction-worthy and defended it through reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.scenv.2024.100142 — Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes

- **Paper category:** Environmental Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > MTT assay on particulate hydroxyapatite lacks essential interference controls (particle-only blanks, optical correction for scattering/absorption by HAp, dye adsorption checks). The reported absorbance values may reflect material artifacts rather than cell viability.

- **Arbiter justification for RW classification:**  
  > Calcium phosphate particles are well-known to interfere with colorimetric assays. Without particle-only wells and interference validation, the optical density readout is uninterpretable. Since the entire biocompatibility claim rests on this single assay, the conclusion is fundamentally unsupported. Reviewer A identified and strongly defended this; Reviewer B recognized it as an additional independent retraction rationale during reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1016_j.scenv.2024.100142 — Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes

- **Paper category:** Environmental Science
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Text fragments from an unrelated materials science study (Fe-Al-based mesoporous metal oxides 'BMO', Cu Kα peaks, HRTEM discussion) appear to have been inserted into the manuscript's characterization narrative.

- **Arbiter justification for RW classification:**  
  > If confirmed, this means parts of the analytical interpretation were copied from another manuscript rather than derived from the authors' own data. This is a core integrity failure that undermines confidence in whether the presented characterization accurately describes the authors' actual experiments. Both reviewers escalated this to retraction-worthy during reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-56334-5 — The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation

- **Paper category:** Multidisciplinary
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The manuscript's central claim that exosomes significantly reduce pro-inflammatory cytokines is directly contradicted by its own reported p-values: three of four cytokines (TNF-α, IFN-γ, IL-17) show non-significant differences (p=0.055, 0.327, 0.627) in the key exosome-treatment condition, yet the text claims 'all our results demonstrated a significant difference.'

- **Arbiter justification for RW classification:**  
  > This is not overstatement or spin — it is a direct logical contradiction between the narrative conclusion and the reported statistical results. If 75% of the primary outcome comparisons are non-significant by the paper's own analysis, the central conclusion that exosomes suppress hyperinflammation is unsupported. This meets the retraction threshold: the paper's central conclusions cannot be supported by the data as presented.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-56334-5 — The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation

- **Paper category:** Multidisciplinary
- **SPOT error category:** Data Inconsistency (figure-text) (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The study draws therapeutic efficacy and safety conclusions about exosome treatment for COVID-19 patients from an in vitro PBMC stimulation assay with n=5 patients and n=5 controls — a fundamental mismatch between evidence and claims.

- **Arbiter justification for RW classification:**  
  > The manuscript's stated conclusions concern clinical treatment efficacy and safety, but the study design is a small ex vivo laboratory experiment with no patient administration, clinical endpoints, pharmacology, or adverse-event data. Reviewer A upgraded this to retraction-worthy on reflection when the headline conclusion is taken as the paper's core contribution, and the data fundamentally cannot support it. The overclaim is not stylistic — it is a category error between study design and stated conclusions that cannot be fixed by reanalysis alone.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Analytical method validation reports mathematically impossible values: negative LOD/LOQ (e.g., kidney LOD = −587.51 µg/kg, LOQ = −1780.34 µg/kg) and R² values outside [0,1] (muscle R² = 6.96, skin R² = 0.002).

- **Arbiter justification for RW classification:**  
  > LOD/LOQ computed as 3.3σ/slope and 10σ/slope cannot be negative under standard calibration, and R² is bounded [0,1] by definition. These are not debatable analytical choices—they are mathematical impossibilities indicating either catastrophic calculation errors or fundamental misunderstanding of validation statistics. Because the analytical assay underpins every concentration measurement in both the PK and residue-depletion studies, invalid validation severs the evidentiary chain from sample to PK conclusion. Both reviewers rated this RETRACTION-WORTHY; neither downgraded after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The trapezoidal AUC formula is stated as AUC = Σ(Ci + Ci+1)·Δt instead of the correct 0.5·(Ci + Ci+1)·Δt.

- **Arbiter justification for RW classification:**  
  > AUC is the central metric of drug exposure in the PK study. If this formula was actually used as written, all AUC values would be doubled, invalidating exposure estimates, tissue comparisons, and any downstream parameter dependent on AUC. It is possible this is only a typographical error in the methods text while correct computation was performed, but the paper as presented asks readers to accept an explicitly wrong formula for its primary endpoint. Reviewer A identified this; Reviewer B acknowledged missing it and upgraded to RETRACTION-WORTHY on reflection. The slight uncertainty is whether it was actually applied or is merely a writing error, but as presented it is fundamentally broken.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Pharmacokinetic parameters are internally contradictory and violate basic PK identities: e.g., gill kel = 0.01 h⁻¹ implies t1/2 ≈ 69.3 h but reported half-lives are 0.94 h, 19.39 h, and 198.48 h; liver t1/2 is reported as both 238.68 h and 420.28 h; plasma Tmax is 24 h in the abstract but 3 h in text; gill Cmax timing is reported as 3 h, 6 h, and 8 h in different sections.

- **Arbiter justification for RW classification:**  
  > These are not ambiguities or matters of interpretation—they are direct numerical contradictions within the same manuscript for primary PK descriptors (half-lives, Tmax, Cmax timing). When the reported rate constant and corresponding half-life violate t1/2 = ln(2)/k, the results table is arithmetically self-contradictory. A reader cannot determine which values, if any, are correct. Since tissue-specific PK characterization is the paper's central contribution, irreconcilable contradictions in these parameters make the core conclusions unsupportable. Both reviewers rated these contradictions RETRACTION-WORTHY; both defended this after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The paper claims non-compartmental analysis (NCA) but reports absorption rate constants (Ka), absorption half-lives (t1/2a), distribution half-lives, and interprets biphasic kinetics—parameters that require compartmental modeling assumptions.

- **Arbiter justification for RW classification:**  
  > Standard NCA does not estimate Ka, absorption half-life, or separate distribution/elimination phases from oral data. If NCA was truly performed, these parameters are fabricated or meaningless. If compartmental modeling was performed, the methods are misreported and the analysis is irreproducible. Either way, the central PK parameters that form the paper's main conclusions are not supported by the stated analytical method. Reviewer A rated RETRACTION-WORTHY throughout; Reviewer B initially rated MAJOR-REVISION but explicitly upgraded to RETRACTION-WORTHY on reflection, noting that invalid parameters invalidate conclusions rather than merely needing clarification.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > Biosafety data show identical baseline (Day 0) values across all five groups (Control, 1×, 3×, 5×, 10×) for ALP (5 U/L), AST (100 U/L), ALT (20 U/L), and Creatinine (0.2 mg/L), with significance annotations placed on these identical values.

- **Arbiter justification for RW classification:**  
  > Identical values to 1–3 significant digits across five independent biological groups is biologically implausible. Real biological variation in fish enzyme and metabolite measurements precludes exact agreement across groups. Significance markers on identical values are nonsensical. This pattern strongly suggests either data fabrication, template copying, or extreme rounding that renders the presented data non-representative of actual measurements. Reviewer B rated RETRACTION-WORTHY; Reviewer A initially rated MAJOR-REVISION but upgraded on reflection after considering the combined evidence of identical values plus significance annotations. The slight uncertainty reflects the possibility that extreme rounding or figure-generation artifacts could partially explain the pattern, though this would still mean the data as presented do not support the biosafety conclusions.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-024-73921-8 — Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)

- **Paper category:** Multidisciplinary
- **SPOT error category:** Statistical reporting (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

- **B3++ finding (rated RETRACTION-WORTHY, finding #5):**  
  Location:   
  > Elimination half-lives vastly exceed the 128-hour observation window (plasma 3368 h, liver 420 h), and Ka values near zero (0.0002 h⁻¹ in plasma) imply absorption half-lives of thousands of hours.

- **Arbiter justification for RW classification:**  
  > While terminal half-life overestimation from short sampling windows is a known limitation, the magnitude here (3368 h from 128 h sampling = 26× the observation period) goes beyond 'unstable estimate' to 'meaningless parameter.' A Ka of 0.0002 h⁻¹ implies absorption would take years for OTC in fish, which is biophysically absurd. Reviewer B rated RETRACTION-WORTHY; Reviewer A rated MAJOR-REVISION for the half-life issue alone but rated related contradictions as RETRACTION-WORTHY. On balance, these extreme values—combined with the NCA/compartmental mismatch and internal contradictions—are not independently remediable by restricting terminal-phase estimation because they reflect a fundamentally broken analytical pipeline.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-025-85894-3 — Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles

- **Paper category:** Multidisciplinary
- **SPOT error category:** Data inconsistency (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Specific dyes (methylene blue, malachite green) in real textile wastewater are identified and quantified solely from broad UV-Vis absorbance features without chromatographic separation, standard addition, spiking recovery, or matrix-validated calibration.

- **Arbiter justification for RW classification:**  
  > The paper's headline applied conclusion—removal of named dyes from real textile wastewater—depends entirely on assigning broad UV-Vis peaks at ~614 and ~665 nm to malachite green and methylene blue in a complex, multicomponent matrix. Without any orthogonal analytical confirmation, the analyte identity is unestablished. If the identity is wrong, the central wastewater conclusion collapses. New primary data (e.g., HPLC/LC-MS) would be required, not just reanalysis.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-025-85894-3 — Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles

- **Paper category:** Multidisciplinary
- **SPOT error category:** Data inconsistency (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The degradation experiments lack all essential controls: no dye + sunlight without catalyst (photolysis control), no dye + catalyst in dark (adsorption control), no tea-extract-only control, and no nanoparticle optical blank subtraction.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identified this and both maintained or strengthened it on reflection. The paper claims photocatalytic degradation by SBT-AgNPs, but the design cannot distinguish photocatalysis from direct photolysis, adsorption, scattering artifacts, or extract effects. The causal claim is untestable from the presented experiments. New experiments, not editorial corrections, would be needed.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1038_s41598-025-85894-3 — Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles

- **Paper category:** Multidisciplinary
- **SPOT error category:** Data inconsistency (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Reported dye standard concentrations are physically impossible or internally inconsistent: malachite green at 100–500 mg in 10 mL (10,000–50,000 mg/L) far exceeds aqueous solubility (~4,000 mg/L); methylene blue listed masses do not match stated working concentrations; textile wastewater described as both '1 µl/ml' and '0.001 mg/ml'.

- **Arbiter justification for RW classification:**  
  > Reviewer B identified this as the primary quantitative defect, and Reviewer A upgraded it upon reflection. If the starting dye concentrations are undefined or physically impossible, every calculated degradation percentage is meaningless. This is not a unit-labeling problem that could be resolved by a corrigendum; the actual experimental conditions are unknowable from the manuscript, invalidating all quantitative removal claims.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1186_s12964-024-01868-4 — Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases

- **Paper category:** Biology
- **SPOT error category:** Reagent identity (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Schizophrenia kinome analysis is based on pooled postmortem samples (one pool per sex-by-diagnosis cell) with technical triplicates treated as the basis for biological inference about disease and sex effects.

- **Arbiter justification for RW classification:**  
  > Pooling collapses all subject-level biological variability into a single composite per group. Technical triplicates measure assay reproducibility on the same pooled material, not between-subject variation. There is effectively n=1 biologically per group. No valid statistical inference about disease effects or sex differences is possible. This is not low power—it is zero valid inferential degrees of freedom for the biological question. The paper's central disease-related conclusions (disease separation, global phosphorylation reduction, upstream kinase changes, sex-specific enrichment) cannot be supported by these data. Both reviewers independently identified this as retraction-worthy and defended it through reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1186_s12964-024-01868-4 — Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases

- **Paper category:** Biology
- **SPOT error category:** Reagent identity (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Sex-specific schizophrenia kinase perturbation claims are unsupported because there is one pooled sample per sex-by-diagnosis cell, making interaction or sex-stratified disease effects impossible to estimate.

- **Arbiter justification for RW classification:**  
  > Establishing a sex-specific disease effect requires replication within each sex-by-diagnosis cell or a model with subject-level data. One pool per cell (female control, female SCZ, male control, male SCZ) cannot support such claims. These sex-specific findings are highlighted prominently in figures, results, and discussion, making them central rather than peripheral conclusions. This is a direct corollary of the pooling design flaw but targets a particularly emphasized and especially untenable claim category.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.1186_s12964-024-01868-4 — Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases

- **Paper category:** Biology
- **SPOT error category:** Reagent identity (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Technical replicates of pooled material are used to compute fold changes, clustering, and upstream kinase predictions, creating pseudoreplication throughout the disease-analysis pipeline.

- **Arbiter justification for RW classification:**  
  > Using technical replicates as if they were independent biological observations grossly underestimates uncertainty. Apparent clustering and separation of groups may reflect high assay precision on the same pooled lysate rather than reproducible disease biology across individuals. All downstream analyses (differential peptides, kinase inference, pathway enrichment, connectivity) inherit this invalid variance structure. Both reviewers recognized this mechanism; Reviewer A articulated it as a distinct finding from the pooling design itself.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.34172_bi.2023.30064 — Unveiling the biological effects of radio-frequency and extremely-low frequency electromagnetic fields on the central nervous system performance

- **Paper category:** Medicine
- **SPOT error category:** Reagent identity (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the manuscript incorrectly refers to "C57BL/6 rats," but C57BL/6 is a strain of mice, not rats; thus, there is a misidentification of the animal model used.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Complete absence of review methodology. The Methods section is a single sentence fragment containing a template placeholder ('[JOURNAL]'). No search strategy, databases, date ranges, keywords, inclusion/exclusion criteria, study selection process, data extraction procedure, or synthesis method is described.

- **Arbiter justification for RW classification:**  
  > For a review article, the methodology for identifying, selecting, and synthesizing evidence IS the scientific method. Its total absence means the central conclusions — which purport to summarize a field — are built on an opaque, unreproducible, and potentially biased author-selected literature set. This is not a gap that can be patched; the entire review would need to be reconstructed from scratch. The paper's core scientific product (a synthesized evidence summary) cannot be supported by the paper as presented. Both reviewers rated or upgraded this to RETRACTION-WORTHY after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The manuscript treats the ideal gas law (PV=nRT) as a predictive theory of planetary surface temperature and uses it to argue that the greenhouse effect is 'very small or non-existent.' The ideal gas law is an equation of state, not an energy-balance equation, and cannot determine equilibrium temperature without independent radiative and thermodynamic constraints.

- **Arbiter justification for RW classification:**  
  > This is a foundational category error in atmospheric physics. The manuscript uses it as the core mechanistic basis for rejecting the greenhouse effect. Both reviewers independently rate this RETRACTION-WORTHY and defend the rating through reflection. The error is not a simplification or approximation—it is the application of the wrong physical framework to the central question. No revision can rescue a conclusion built on this premise without abandoning the premise itself.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The manuscript claims Venus's high surface temperature is explained 'simply because the atmospheric pressure is so great,' presenting this as flagship evidence that greenhouse physics is unnecessary. Pressure alone cannot create or sustain high temperatures without an energy source and radiative constraints.

- **Arbiter justification for RW classification:**  
  > This is used as a principal empirical demonstration supporting the rejection of greenhouse warming. Pressure profiles redistribute temperature vertically via the adiabatic lapse rate but do not independently set the total energy content of a planetary atmosphere. The example is physically non-responsive to the energy-balance question it purports to settle. Reviewer A flags this as a separate RETRACTION-WORTHY finding; Reviewer B subsumes it under the ideal gas law error. Both agree the underlying physics is wrong and central to the paper's argument.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The manuscript argues that because CO2 radiative forcing is logarithmic, additional CO2 must produce negligible warming, and presents ~0.64–0.81°C for a doubling from 400 to 800 ppm as a definitive or upper-bound estimate. This is derived using a fixed low climate sensitivity parameter (lambda) while omitting all feedback processes.

- **Arbiter justification for RW classification:**  
  > Logarithmic forcing does not imply negligible temperature response; the temperature outcome depends critically on feedbacks (water vapor, albedo, lapse rate, clouds) which the manuscript ignores entirely. Presenting a no-feedback estimate as an upper bound forecloses the actual uncertainty space and converts an unjustified assumption into a false impossibility claim. Both reviewers rate this or closely related findings as RETRACTION-WORTHY and defend through reflection. The manuscript's central quantitative policy argument (that warming from further CO2 is too small to justify mitigation) depends directly on this invalid inference.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The manuscript conflates atmospheric CO2 residence time (the average time an individual molecule stays in the atmosphere) with the perturbation adjustment time (the timescale for an excess concentration to decay). It uses seasonal exchange and short residence times to argue that anthropogenic CO2 cannot persist long enough to matter.

- **Arbiter justification for RW classification:**  
  > This is a well-documented category error in carbon-cycle science. A short molecular residence time does not imply rapid removal of a concentration perturbation when gross fluxes are approximately balanced. The manuscript uses this conflation to claim human CO2 contributions are transient and inconsequential—a claim that directly supports its conclusion that anthropogenic climate change is negligible. Reviewer A rates this RETRACTION-WORTHY and defends it; Reviewer B acknowledges and upgrades to RETRACTION-WORTHY in reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > The manuscript calculates that anthropogenic CO2 is only ~4.3% of atmospheric CO2 (~18 ppm) by dividing annual human emissions (32.7 Pg C/yr) by total gross carbon flux (~760 Pg C/yr). This is an invalid mass-balance calculation because natural gross fluxes are approximately balanced; the correct comparison is net anthropogenic emissions versus the net change in atmospheric concentration.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identify this as a fundamental carbon-cycle accounting error. The observed rise in atmospheric CO2 from ~280 to ~420 ppm is quantitatively consistent with cumulative anthropogenic emissions (confirmed by isotopic and mass-balance evidence). Dividing emissions by gross throughput rather than comparing to the net atmospheric increase uses the wrong denominator and the wrong accounting identity. This error directly supports the manuscript's central claim that human CO2 is negligible, and its correction demolishes that claim.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #5):**  
  Location:   
  > The manuscript claims 'the increase in temperature from 1880 through 2000 is statistically indistinguishable from 0 K' and that 'recent global average surface temperatures remain relatively stable,' without presenting a transparent or reproducible statistical analysis.

- **Arbiter justification for RW classification:**  
  > Multiple independent observational datasets (HadCRUT, GISTEMP, Berkeley Earth, ERA5, satellite records) show approximately 1.0–1.2°C warming over this period, with statistical significance far exceeding conventional thresholds. The manuscript's claim is incompatible with the observational record as ordinarily understood and is presented without any valid supporting analysis. Both reviewers rate this RETRACTION-WORTHY. This is a central empirical premise of the paper; if observed warming is not effectively zero, the paper's argument that there is no warming to explain collapses.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 10.5539_jsd.v17n6p137 — The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis

- **Paper category:** Environmental Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

- **B3++ finding (rated RETRACTION-WORTHY, finding #6):**  
  Location:   
  > The manuscript treats human breathing as a net source of atmospheric CO2 (~0.1638 ppmv), comparing it to fossil fuel emissions to argue the latter are trivial. Human respiration is part of a closed biogenic carbon loop and represents zero net addition to atmospheric CO2.

- **Arbiter justification for RW classification:**  
  > Reviewer B identifies this as a 'high-school level error' and rates it RETRACTION-WORTHY; Reviewer A addresses it under the broader category of unsupported sector-level conversions (MAJOR-REVISION). The error is elementary: carbon in food originates from recent atmospheric CO2 via photosynthesis, so exhaling it returns it to the atmosphere with no net change. Using this as a comparator to minimize fossil fuel emissions (which release geologically sequestered carbon) demonstrates a fundamental misunderstanding of the carbon cycle. Given that it directly supports the paper's claim of anthropogenic insignificance, RETRACTION-WORTHY is appropriate.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.09543v2 — Token Jumping in Planar Graphs has Linear Sized Kernels

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The final equivalence argument misapplies Claim 4 (a size-bound claim) where it needs a reconfigurability result. Even substituting Claim 5 does not work because its premises (that J_s and J_t are independent sets in a linear forest) are not established—the text itself admits J_s and J_t are 'not necessarily independent.'

- **Arbiter justification for RW classification:**  
  > The proof's terminal inferential step invokes a claim that does not entail the needed conclusion, and no available substitute has its hypotheses satisfied. This leaves the main theorem without a logically valid final step. Both reviewers identify this independently.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.09543v2 — Token Jumping in Planar Graphs has Linear Sized Kernels

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The manuscript asserts G[J_s ∪ J_t ∪ J_m] is a linear forest without proof. J_s and J_t individually inducing linear forests and J_m being independent does not imply their union induces a linear forest—cross-edges can create cycles or high-degree vertices.

- **Arbiter justification for RW classification:**  
  > This is a necessary structural premise for the final reconfiguration step. Without it, the entire YES-preservation direction of the kernel equivalence collapses. Both reviewers flag this; neither finds any argument in the text that could establish it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.09543v2 — Token Jumping in Planar Graphs has Linear Sized Kernels

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Claim 7's induction proof does not verify that each proposed token jump preserves independence globally. The assumption 'no token appears on the closed neighborhood of z''_{i-1}' is stated without justification, effectively assuming what needs to be proved.

- **Arbiter justification for RW classification:**  
  > Claim 7 is the core equivalence proof for the kernel. Token jumping requires every intermediate configuration to be independent. The proof does not check this, making the reduction's correctness unestablished. Both reviewers identify this; Reviewer A calls it retraction-worthy, Reviewer B calls the equivalence proof retraction-worthy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.09543v2 — Token Jumping in Planar Graphs has Linear Sized Kernels

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Claim 3 (interior vertices from different X-pairs are non-adjacent) relies on planar embedding arguments with 'cycles' that are not guaranteed to exist as cycles in the graph. The proof conflates geometric embedding intuition with combinatorial graph structure without a rigorous Jordan-curve-type argument.

- **Arbiter justification for RW classification:**  
  > This claim is repeatedly invoked to guarantee that different X-pair classes are independent, which underpins the decomposition into a linear forest structure and the counting arguments. Both reviewers flag it as seriously flawed. Reviewer A upgraded to RETRACTION-WORTHY on reflection; Reviewer B rated it RETRACTION-WORTHY throughout. The claim is central enough that its failure cascades through multiple later arguments.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.16191v2 — From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof of Theorem 4.9 (the key 38-queue bound) is incomplete, containing explicit draft markers, duplicated/reordered proof fragments, undefined queue families, and no finished queue assignment or non-nesting verification. The manuscript's headline numerical claim is therefore unsupported.

- **Arbiter justification for RW classification:**  
  > Both reviewers agree the proof is unfinished. Reviewer A identified draft markers, corrupted text, and undefined objects; Reviewer B acknowledged in reflection that the 'DRAFT' marker makes the 38-queue claim unverifiable. A queue-number proof requires an exact partition of edges into queues and a complete non-nesting argument for each queue class. Neither is present. This is not a gap in an otherwise complete argument—it is an absent proof of the central claim. Under the key test, confirmation of this finding means the paper's headline result requires complete re-proving, which meets the RETRACTION-WORTHY standard.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2401.16191v2 — From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The local machinery around Claim 4.10 / Theorem 4.9 (1-queue layouts for bipods, global queue assembly) is internally corrupted: interleaved incompatible proof branches, malformed inequalities, references to undefined queue families, and notation switches mid-argument.

- **Arbiter justification for RW classification:**  
  > Reviewer A identified this as a separate fatal defect from the incompleteness of Theorem 4.9. The local non-nesting lemmas are the engine of any queue-layout proof; if they are textually garbled to the point of being mathematically unreadable, the global bound cannot be assembled. Reviewer B's reflection acknowledged the corrupted text blocks verification. This independently prevents support of the 38-queue claim even if one attempted to reconstruct intent from the fragments.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.01549v2 — Quantum advantage in zero-error function computation with side information

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Lemma 4/Theorem 4: The converse direction — from an arbitrary zero-error quantum protocol with mixed states to an orthogonal representation of the complement graph — is invalid. The proof selects an arbitrary eigenvector from each mixed state and claims the resulting vectors form an orthogonal representation. This fails because: (a) zero-error function computation only requires distinguishability conditioned on Bob's side information y and differing outputs, not global pairwise orthogonality of code states; (b) orthogonality of supports for adjacent pairs does not imply that arbitrary eigenvector selections yield orthogonal vectors; (c) no equivalence between the operational zero-error criterion and orthogonal rank is established for the mixed-state model. This invalidates the claimed formula R_quantum = inf_m (1/m) log ξ(G^(m)).

- **Arbiter justification for RW classification:**  
  > This lemma is the indispensable bridge between operational quantum protocols and the graph parameter (orthogonal rank) that powers the paper's main quantum/classical separation. Without a valid converse, the exact quantum rate formula is unsupported, and all downstream separation claims collapse. The error is structural and not a matter of missing detail that could be easily patched.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.01549v2 — Quantum advantage in zero-error function computation with side information

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Proposition 1 asserts G ⊠ H = G̅ ∨ H̅ (or equivalently that the strong product equals the OR product). This is false under the manuscript's own definitions. In the OR product, adjacency in one coordinate suffices regardless of the other; in the strong product, the non-adjacent coordinate must satisfy equality or adjacency. These are distinct graph products with different edge sets in general.

- **Arbiter justification for RW classification:**  
  > This is not a typo but a fundamental graph-theoretic misidentification. The paper's framework distinguishes between G^(m), G^{⊠m}, and G^{∨m} and uses containment relations among them to derive bounds and equalities. If the paper simultaneously claims two of these benchmark products are identical when they are not, the entire product-based proof architecture becomes internally inconsistent. All subsequent inclusion-based arguments, parameter bounds, and rate calculations that depend on distinguishing these products are compromised.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.10307v2 — A New Radio to Overcome Critical Link Budgets

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The central equivalence between temporal/frequency combining gain and transmit beamforming gain is not established under consistent power, rate, and bandwidth normalization. The paper treats T-fold matched-filter integration over time-frequency degrees of freedom as a no-loss replacement for N-antenna spatial beamforming gain, without specifying or enforcing equal total energy, equal average power, equal throughput, equal bandwidth, and equal latency. Under standard communication-theoretic normalization, temporal processing gain and spatial array gain are distinct quantities; the claimed equivalence collapses into a trivial resource tradeoff.

- **Arbiter justification for RW classification:**  
  > This is the paper's headline claim. Both reviewers independently identified this as the most critical flaw. Reviewer A rated it RETRACTION-WORTHY from the start and defended it vigorously in reflection. Reviewer B's finding #10 evolved toward RETRACTION-WORTHY during reflection. If the normalization is corrected, the paper's central conclusion—'no loss in link budget gain compared to spatial beamforming'—is either false or becomes a trivially obvious time-bandwidth tradeoff, which is not the claimed contribution. This is not fixable by adding experiments; it requires abandoning or fundamentally reformulating the core thesis.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.10307v2 — A New Radio to Overcome Critical Link Budgets

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The numerical examples compare MA-TISK with T > N (e.g., T = 18.375 versus N = 16) against N-antenna beamforming and report combining gains meeting or exceeding beamforming gain. This comparison is unfair because MA-TISK uses more time-frequency resources per symbol than the beamforming baseline. The benchmark could trivially be matched by allowing beamforming to also use longer integration windows or more subcarriers.

- **Arbiter justification for RW classification:**  
  > This is the empirical instantiation of the normalization error above. The paper's primary numerical evidence (gains of 12.2–12.6 dB versus 12.0 dB for 16-antenna beamforming) is invalid because the two schemes are not compared under equal resource usage. Both reviewers flagged this. Reviewer A rated it RETRACTION-WORTHY from the start. Reviewer B initially rated the unfair comparison as MAJOR-REVISION but moved toward RETRACTION-WORTHY in reflection, recognizing it is not a 'fixable' issue but a logical invalidation of the reported results. Because this is the paper's main quantitative evidence for its headline claim, it is retraction-worthy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.10318v2 — Multi-Antenna Towards Inband Shift Keying

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The error is that the paper underestimates the beamforming gain for transmit beamforming with N antennas, stating it as N when the correct value is N^2.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The central claim that transmit beamforming can be replaced by temporal repetition coding 'without reducing the data rate or the link budget' is unsupported by any valid comparative analysis under matched resource constraints (same bandwidth, time, energy, latency, channel model).

- **Arbiter justification for RW classification:**  
  > Spatial beamforming gain arises from coherent combining across antennas at fixed time/frequency resources and provides directional array gain. Temporal repetition consumes additional time resources, changes latency, and does not produce directional gain. The paper asserts equivalence by invoking a scalar AWGN capacity formula, but this does not establish operational equivalence in multi-antenna mmWave/THz systems. No end-to-end link budget, channel simulation, or fair comparison is provided. Since this is the paper's title-level and conclusion-level claim, and the reasoning is logically flawed (not just empirically incomplete), the central conclusion cannot be supported by the presented data. Reviewer A rated this RETRACTION-WORTHY and defended it vigorously; Reviewer B acknowledged the conflation as a logical error (MAJOR-REVISION) but argued the modulation might survive independently. However, the paper's framing, motivation, and conclusions all rest on this replacement claim, making it the paper's core thesis rather than a peripheral point.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.14546v2 — Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The main theorem (Theorem 2.3) appears to state equality φ_C([y^i f_{j_i}(x)]) = φ_C([y^{n-1-i} f̃_{j_i}(x)]) rather than asserting that the right-hand side is the complex conjugate of the left-hand side. Since the two sides lie in different Hodge summands H^{n-1-i,i} and H^{i,n-1-i}, literal equality is impossible unless both classes are zero.

- **Arbiter justification for RW classification:**  
  > If the theorem genuinely asserts equality rather than conjugation, it is a false statement for generic non-zero classes in distinct Hodge types. This is not a minor notational slip—it changes the mathematical content of the theorem from 'description of conjugation' to 'assertion that two generally distinct classes are equal,' which is wrong. Reviewer A identified this clearly; Reviewer B acknowledged in reflection that this is an independent fatal error they had missed. The confidence is 0.80 rather than higher because there remains some possibility that the manuscript's full context or notation makes the conjugation implicit in a way not captured by the excerpts.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.14546v2 — Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The proof of Theorem 2.3 reconstructs an element via the pairing C(φ_C(U_k), φ_C(U_k)) rather than C(φ_C(U_k), conjugate of φ_C(U_k)), thereby solving for the original class or an element with a prescribed self-pairing rather than the conjugate class.

- **Arbiter justification for RW classification:**  
  > The reconstruction of conjugation from a bilinear/sesquilinear pairing requires using the conjugated argument. If the proof computes a self-pairing and then inverts to find an algebraic representative, it has not established conjugation. This is logically independent of the theorem-statement error. Both reviewers agree after reflection. Confidence is slightly lower because the proof details may contain implicit conjugation steps not visible in the excerpt.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.14546v2 — Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The definition of f̃_{j_i}(x) in equation (2.10) depends on U_{k,γ}, which is constructed from period integrals of φ_C(U_k). The claimed 'explicit algebraic description' of complex conjugation therefore depends on the very transcendental periods it purports to describe algebraically, creating a vicious circle.

- **Arbiter justification for RW classification:**  
  > The paper's central contribution is an explicit algebraic formula for complex conjugation on de Rham cohomology. If that formula requires knowing the periods first, it is not algebraic in any meaningful sense—it reduces to a formal tautology. Reviewer B identified this as the core structural flaw; Reviewer A acknowledged it as a new error in reflection. This is independently fatal: even if the equality-vs-conjugation issue were resolved, the formula would still fail to deliver what is promised.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.14546v2 — Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The elliptic curve example defines a coefficient μ as (∫_{γ_1}ω · ∫_{γ_2}ω − ∫_{γ_2}ω · ∫_{γ_1}ω)/(24πi), which is identically zero because multiplication of complex numbers is commutative.

- **Arbiter justification for RW classification:**  
  > An illustrative example that reduces to zero by tautology is a concrete demonstration that the formula does not work as claimed, at least in the simplest case. This is not merely a typo—it suggests either the formula is wrong or the specialization procedure is flawed. Both reviewers converge on this being retraction-worthy after reflection. Confidence is 0.78 because there is some chance the formula involves quantities (e.g., matrix entries, different differential forms) that are not commutative in a way obscured by the notation or OCR.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2402.16847v2 — The Art of Staying Ahead of Deadlines: Improved Algorithms for the Minimum Tardy Processing Time

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the runtime analysis omits the contribution of the processing times within the interval [d_j - p_j, d_{j - 1}], which leads to an incomplete and therefore incorrect calculation of the total processing time.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The bitwise OR (merge) operation required to compute S_j = L_{j-1} shifted ∪ R_{j-1} is not implementable with the listed dynamic string data structure operations (split, concatenate, make_string). The manuscript defers to Fischer and Wennmann without explaining how OR is performed in the new setting where strings have length d_max+1 rather than P. Split and concatenation alone cannot implement bitwise OR on indicator strings. Without this operation, the algorithm cannot compute its central recurrence.

- **Arbiter justification for RW classification:**  
  > The OR merge is the step that combines the shifted left part with the right part to produce S_j. If this operation cannot be performed within the data structure, the algorithm is fundamentally incomplete. The manuscript's only justification is a reference to prior work that operated in a different setting (strings of length P, not d_max). This is not a missing detail—it is a missing core algorithm. However, there is some possibility that the referenced Fischer-Wennmann machinery does contain a transferable OR implementation that works in this context and the authors simply failed to explain the adaptation. This slight uncertainty prevents full confidence, but the burden of proof is on the manuscript, and it fails to meet it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.01085v2 — A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The core subroutine BFS+ is never formally defined. All correctness and runtime analyses depend on its exact behavior, but the manuscript provides only informal prose references to a 'slightly modified BFS' without pseudocode, data-structure specifications, or algorithmic rules.

- **Arbiter justification for RW classification:**  
  > An algorithm paper claiming a breakthrough must specify the algorithm. The entire detection mechanism is this undefined subroutine. Without it, there is no algorithm to verify, and the main theorem is an unsupported existence claim. Both reviewers independently rated this RETRACTION-WORTHY and defended the rating through reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.01085v2 — A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The claimed O(m) time per BFS+ trial is unjustified. Detecting triangles during BFS as described requires checking non-tree edges among vertices at the same or adjacent levels, which standard BFS does not perform without additional adjacency queries whose cost is not analyzed.

- **Arbiter justification for RW classification:**  
  > The headline O(n^{7/3}) bound is the product of the number of trials and the per-trial cost. If the per-trial cost exceeds O(m) due to the unanalyzed detection checks, the main runtime claim fails. This is not an accounting refinement but a structural incompatibility between what the correctness argument needs and what O(m) BFS provides. Reviewer A rated this RETRACTION-WORTHY; Reviewer B's parallel findings support this.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.01085v2 — A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The probability-of-success argument only establishes that a random sample lands in A = N+(T) with sufficient probability. It does not establish that this event implies algorithmic detection of a triangle, because the implication depends on the unproved correctness of BFS+. The advertised error bound (e.g., ≤ 10^{-30}) is therefore unsupported.

- **Arbiter justification for RW classification:**  
  > The paper amplifies the probability of the wrong event. The sampling calculation may be correct, but it is irrelevant unless landing in N+(T) deterministically triggers detection—an implication that is not proved. The formal guarantee of the theorem is thus unsubstantiated. Both reviewers identified this; Reviewer A rated it RETRACTION-WORTHY and defended it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.01085v2 — A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > All downstream theorems (BMM via Theorem 3, k-clique via Theorem 4, Max-Cut via Theorem 5, and numerous other applications) are explicitly derived from Theorem 2 and are presented as established results, but they collapse if Theorem 2 is unsupported.

- **Arbiter justification for RW classification:**  
  > These are not independent results; they are corollaries of the broken core theorem. The manuscript presents them as proved consequences, including claims to invalidate major open conjectures. Since the foundation is unsupported, none of these conclusions can stand as presented. Reviewer A rated this RETRACTION-WORTHY; Reviewer B's analysis supports it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.06831v2 — HDRTransDC: High Dynamic Range Image Reconstruction with Transformer Deformation Convolution

- **Paper category:** Computer Science
- **SPOT error category:** Statistical reporting (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is related to potentially incorrect metric calculations in Sections 4.2 and 4.3, meaning the statistical results reported in these sections may be inaccurate or misleading and require further validation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The primary quantitative comparison table omits the most directly relevant state-of-the-art baseline (Liu et al. 2022, 'Context-Aware Transformer'), while the text explicitly claims superiority over it by specific margins (0.34 dB, 0.33 dB, 0.07). The baseline's actual numbers are nowhere in the manuscript, making the central 'state-of-the-art' claim unverifiable.

- **Arbiter justification for RW classification:**  
  > The paper's primary contribution claim is achieving state-of-the-art performance. If the most relevant competitor's results are absent from the comparison table while the paper claims to beat it, this is not merely incomplete reporting—it means the paper's central conclusion cannot be supported by the data as presented. Readers cannot verify the claimed margins, cannot assess whether the comparison was conducted fairly, and cannot determine if Liu et al.'s method was evaluated under the same protocol. This crosses from 'could be improved' to 'fundamentally broken' as an evidentiary basis for the main claim.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The paper double-counts propagation effects already incorporated in standard FLRW distance theory by adding an extra aberration factor of (1+z)^{-2} to the observed flux, yielding modified d_L and d_A relations (Eqs. 16, 24, 29).

- **Arbiter justification for RW classification:**  
  > Standard cosmological radiative transfer, derived from null geodesic congruences, phase-space invariants (I_ν/ν^3), and photon number conservation, already yields the correct (1+z)^4 surface brightness dimming and the standard luminosity distance d_L = (1+z)R_0 r_1. The claimed additional (1+z)^{-2} factor from aberration is not missing; inserting it violates Liouville's theorem and photon number conservation. The paper's headline equations are products of this double count, and all downstream cosmological implications inherit the error.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The paper claims standard cosmology omitted relativistic aberration from its distance-redshift framework, but this is factually false. Standard FLRW distance theory fully incorporates all relevant geometric and kinematic effects.

- **Arbiter justification for RW classification:**  
  > The paper's entire novelty rests on correcting a purported omission in the standard framework. If that omission does not exist—and it does not, as the standard derivation accounts for beam geometry, redshift, time dilation, and solid-angle evolution covariantly—then the paper's central contribution is void. This is not merely a misrepresentation of the literature; it is the false premise upon which the entire manuscript is constructed. Both reviewers converged on RETRACTION-WORTHY for this finding after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The paper uses the equivalence principle to justify replacing the global FLRW light-propagation problem with chained local inertial frames and then extracts a global observable flux correction from this local construction.

- **Arbiter justification for RW classification:**  
  > The equivalence principle permits local Minkowski approximations over scales much smaller than the Hubble radius. It does not license replacing a global null-geodesic propagation calculation with a single SR aberration transformation between cosmologically separated endpoints. The paper itself acknowledges FLRW quasi-translations are not Lorentz transformations, yet proceeds to use SR beaming formulas globally. This methodological error is the bridge that enables the invalid derivation.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > The paper confuses frame-dependent aberration of ray direction with a new independent physical photon-loss mechanism, treating the angular redistribution under frame change as an additional dimming beyond what is already encoded by angular-diameter distance and reciprocity.

- **Arbiter justification for RW classification:**  
  > Changing frames changes the angular description of a ray bundle but does not create additional photon loss. Once beam area, solid angle, and redshift are treated covariantly, there is no extra cosmological dimming term. Etherington reciprocity and Liouville's theorem already connect these quantities consistently. The paper's interpretation of its Eqs. 11-13 as a new photon-loss factor is a conceptual error that directly generates the incorrect central result.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #5):**  
  Location:   
  > The angular-diameter distance derivation (Eq. 29: d_A = (1+z)r_O) is not independently derived from geodesic deviation or ray bundle geometry but is back-solved to preserve the Etherington relation after the luminosity distance has been modified by the spurious aberration factor.

- **Arbiter justification for RW classification:**  
  > In standard cosmology, d_A is determined by the transverse physical size at emission divided by observed angle and is derived from the geodesic deviation equation. The paper's d_A is not obtained this way; it is adjusted to force d_L = (1+z)^2 d_A after d_L has been altered. This circular reasoning means one of the paper's two principal observables is not grounded in physics. Both reviewers identify this circularity, and Reviewer B upgraded it to RETRACTION-WORTHY after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2403.18567v2 — The effect of Relativistic Aberration on Cosmological Distances

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

- **B3++ finding (rated RETRACTION-WORTHY, finding #6):**  
  Location:   
  > The paper's CMB prediction—that aberration spreads small-scale anisotropies by a factor ~(1+z)^2 ≈ 10^6 for z~1000, making the CMB appear more homogeneous—is directly contradicted by Planck observations of sharp acoustic peaks up to ℓ ~ 2500.

- **Arbiter justification for RW classification:**  
  > This is a specific, quantitative prediction that is falsified by observational data. A factor 10^6 spread in solid angle would completely wash out the observed acoustic peak structure of the CMB power spectrum. Reviewer B correctly identifies this as observational falsification. Reviewer A initially rated this MINOR (as downstream of the already-fatal core error) but acknowledged potential upgrade. As the paper presents this claim as physical support for its mechanism rather than pure speculation, it constitutes an independently falsifiable prediction that fails.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.01980v6 — A Simple Ricci Flow Proof of the Uniformization Theorem

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The maximum principle argument in Proposition 3.1 is structurally invalid: I_A is an infimum-defined isoperimetric profile, not a classical smooth solution of a parabolic PDE, and the paper applies a standard comparison principle without establishing the required smoothness, regularity, or viscosity/barrier framework.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identify this as the fatal core defect. Hamilton-style isoperimetric arguments require delicate viscosity or barrier arguments precisely because the profile is defined as an infimum and is generally nonsmooth. The manuscript treats I_A^2 as a classical PDE solution and invokes the maximum principle directly, which is a category error, not a missing lemma. Since Proposition 3.1 is the engine of the entire proof and no alternative argument exists in the paper, its failure collapses the main theorem.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.01980v6 — A Simple Ricci Flow Proof of the Uniformization Theorem

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Equation (2.5) uses second derivatives with respect to a spatial/normal variable r, but I_A is defined as a function of enclosed area A, not of r. The PDE is not well-posed for the stated unknown because the independent-variable structure is undefined.

- **Arbiter justification for RW classification:**  
  > Reviewer A identifies this as a separate structural flaw from the maximum principle issue: the manuscript never defines how I_A depends on r, never establishes a parametrization through minimizers, and never justifies differentiability in the requisite variables. Reviewer B, upon reflection, acknowledges this as an additional structural flaw reinforcing the retraction-level assessment. A PDE with undefined independent variables is not a correctable notational issue—it means the core evolution formula is not mathematically meaningful as written.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.01980v6 — A Simple Ricci Flow Proof of the Uniformization Theorem

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The contradiction argument in Theorem 3.2 misuses the 'tightness' of the small-area asymptotic: having two lower bounds on I_A^2 that both approach the true value as A→0 does not produce the inequality in the direction needed for contradiction.

- **Arbiter justification for RW classification:**  
  > Reviewer A identifies this as an independent logical error in the paper's main theorem: tightness of one lower bound does not imply it dominates another lower bound. Reviewer B corroborates by noting the inequality direction is wrong. Since Theorem 3.2 is the paper's central result and this step is the only bridge from the profile estimate to curvature decay, its failure is independently fatal even if Proposition 3.1 were somehow rescued.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.01980v6 — A Simple Ricci Flow Proof of the Uniformization Theorem

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The constants B and C in Proposition 3.1 depend on A, with B diverging as A→0, yet the proof fixes A for the ODE comparison and then sends A→0 in the contradiction argument. This makes the limiting manipulation invalid.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY upon reflection, noting that the A-dependence independently destroys the final contradiction step. Reviewer B initially rated the B-divergence as the primary mechanism breaking the contradiction. Since the proof's terminal step requires a limit that is mathematically impossible as written (B→∞ makes e^{-BT}→0, not the intended comparison), and no alternative argument is supplied, this defect independently invalidates Theorem 3.2.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The claim '(Z, ⊙_{l,k}) is an abelian group when l | k(k−1)' is false in general. The map x ↦ lx+k transports ⊙_{l,k} into ordinary integer multiplication, but Z under multiplication is not a group (only ±1 are units). A concrete counterexample with l=1, k=1 shows the identity is 0 but element 1 has no inverse. Later sections explicitly rely on group/ideal behavior of this structure.

- **Arbiter justification for RW classification:**  
  > This is a foundational structural claim on which the generalized machinery (Theorems 4.8–4.14) is built. It is demonstrably false by elementary counterexample. The paper's generalized partition-regularity results cannot stand on a non-existent group structure.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Theorem 4.3's proof contains algebraically incorrect manipulations. From A ∈ p ⊙_t q one gets {n : n^{-1}A ∈ q} ∈ p, not '⊆ p'. The transport step with F'={1/(n−t)f : f∈F} and claims about a + (1/n)P(d) ∈ n^{-1}A mixes additive polynomial patterns, scalar division, and the nonstandard semigroup law incorrectly. This theorem is a main technical engine for polynomial/symmetric partition results.

- **Arbiter justification for RW classification:**  
  > The proof mechanism is not merely incomplete but algebraically wrong in type and substance. Since Theorem 4.3 feeds later polynomial pattern claims (the paper's advertised new results), the derived conclusions are unsupported.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Theorem 4.11 invokes Theorem 3.3 to obtain an ultrafilter in cl(K(βZ,+)) ∩ E(K(βZ, ⊙_{l,k})), but Theorem 3.3 concerns only ⊙_t (the special case), not the generalized operation ⊙_{l,k}. No analogue for the generalized operation is proved anywhere.

- **Arbiter justification for RW classification:**  
  > This is a direct logical gap: the main generalized theorem starts from a premise not established in the paper. Corollary 4.12 (the headline answer to Di Nasso's question) and Corollary 4.14 depend on this theorem, so the central generalized conclusions collapse.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Corollaries 4.12 and 4.14 state equations involving the operation ⊕_{l,k}, which is never defined anywhere in the manuscript. The proof of Corollary 4.12 concludes with ⊕_{l,k} rather than ⊙_{l,k}. Since the paper's contribution is precisely new partition-regular equations under a specifically defined operation, using an undefined operation in the final stated results renders them mathematically meaningless.

- **Arbiter justification for RW classification:**  
  > These are the paper's highlighted end-products (Corollary 4.12 is the abstract's main claim answering Di Nasso's question). The conclusions are literally stated using an undefined mathematical object. Combined with the upstream proof failures, this cannot be dismissed as a harmless typo.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > Misapplication of Theorem 4.9 (cited as [8, Lemma 2.1]) in Theorem 4.10. The lemma allows identifying one free variable (x_1 = y_1) across two ultrafilter-realized equations, but the proof uses it to equate results/configurations across different equation forms (e.g., deriving (a+b)/2 = c ⊙ d). This misinterpretation of the logical statement invalidates the proof of Theorem 4.10.

- **Arbiter justification for RW classification:**  
  > Theorem 4.10 is a flagship new partition-regular equation, and Corollary 4.12 depends on it. The misapplication is a fundamental logical error, not a gap that can be filled. However, confidence is slightly lower because the precise scope of what the lemma allows may depend on the exact formulation in the cited source.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.04502v2 — The interplay between additive and symmetric large sets and their combinatorial applications

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

- **B3++ finding (rated RETRACTION-WORTHY, finding #5):**  
  Location:   
  > Section 4.8's generalization to ⊙_{l,k} silently changes the hypothesis from l | k(k−1) to l | (k−1) without justification. The generalized partition-regularity theorems (4.10–4.14) are stated under the different condition, and there is no coherent reconciliation.

- **Arbiter justification for RW classification:**  
  > Combined with the false group claim above, this means the generalized framework has no stable, coherent set of hypotheses. The later theorems cannot be evaluated because it is unclear under what conditions they are even intended to hold.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.18586v2 — How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The protocol purports to implement the partial transpose of a Gaussian channel via CV gate teleportation, but partial transpose is not a completely positive map. The paper never rigorously proves that the overall physically realized protocol (composition of beam splitters, squeezers, homodyne measurements, displacements, and entangled ancillae) yields a CPTP map on arbitrary input states. Without this proof, Theorem 5 and all downstream conclusions (noise polarization, entanglement distillation) are not established as statements about physical quantum operations.

- **Arbiter justification for RW classification:**  
  > The entire paper's contribution hinges on physically realizing a channel transformation that corresponds to partial transposition. If this step is not proven to yield a valid quantum channel, the central theorem is unsupported. This is not a missing robustness check — it is an absent proof of the principal construction's physical validity. Both reviewers flagged this and both strengthened their assessment upon reflection. The slight residual uncertainty is because the composition of physical operations is inherently CPTP, so the real question is whether the effective channel matches the claimed form; but this matching is exactly what the paper fails to demonstrate rigorously.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.18586v2 — How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Lemma 4 provides only a covariance-matrix-level transformation (M → Z_i M Z_i, N → Z_i N Z_i) for the 'partial transpose of a Gaussian operation' but does not verify that the transformed parameters satisfy the Gaussian complete positivity condition (involving the symplectic form Ω). Conjugation by the non-symplectic Z_i does not automatically preserve the Gaussian CP constraint. Since Theorem 5 is built directly on this lemma, the central result lacks a valid channel-theoretic foundation.

- **Arbiter justification for RW classification:**  
  > The Gaussian CP condition is N + iΩ - iM^T Ω M ≥ 0 (or similar, depending on convention). Conjugating M and N by Z_i does not obviously preserve this inequality since Z_i is not symplectic. If the transformed parameters violate this condition, the 'channel' B_i(G^{M,N}) is not a valid quantum channel. The paper omits this verification entirely. Both reviewers identified this, and Reviewer B upgraded this to RETRACTION-WORTHY upon reflection. The confidence is slightly lower because for specific channels (e.g., thermal/amplifier channels with particular symmetry), the CP condition might happen to be preserved, but the paper claims generality.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2404.18586v2 — How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The protocol requires ideal infinitely squeezed EPR states (infinite energy, non-normalizable), yet the paper frames its construction as relying on 'local Gaussian resources' and draws practical conclusions about Gaussian QEC and entanglement distillation. The finite-squeezing analysis (Appendix G) provides only state-level fidelity bounds, not channel-level error analysis (e.g., diamond norm, induced noise parameters), and does not demonstrate that noise polarization or distillation survives with realistic squeezing levels.

- **Arbiter justification for RW classification:**  
  > The key lemmas (2, 3) and the resulting noise-polarization theorem hold exactly only in the unphysical infinite-squeezing limit. For any finite squeezing, the protocol introduces additional noise that is never quantified at the channel level. Since the paper's headline claim is about circumventing Gaussian QEC no-go results with physical resources, and this circumvention is only demonstrated in an unphysical limit, the central practical conclusions are unsupported. Both reviewers agree this is at minimum a devastating flaw. The confidence is somewhat lower because a sufficiently careful finite-squeezing analysis might rescue a weaker version of the result, but such analysis is entirely absent.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.01133v3 — A missing theorem on dual spaces

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The issue is that an error in Proposition 2.3 undermines the validity of Lemmas 3 and 4, and Theorem 4.1 depends on results from Proposition 2.3; therefore, Lemmas 3 and 4 are only valid if the conclusions of Proposition 2.3 hold for the map q used in Theorem 4.1.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > In the proof of Theorem 3.3(1), the manuscript states J² = I and invokes a criterion for complex structure that requires J² = -I. Moreover, the manuscript's own calculation (J²)* = -I implies J² = -I by elementary duality, directly contradicting the stated J² = I. This is an internal contradiction at the algebraic core of the proof that X acquires complex structure, and Theorem 4.1 explicitly depends on this construction.

- **Arbiter justification for RW classification:**  
  > This is not a typo that can be fixed by changing one symbol — the manuscript simultaneously asserts (J²)* = -I and J² = I, which are mutually contradictory by elementary duality. If J² = -I is what is intended, the authors need to supply a correct derivation showing this, because the currently written argument is self-negating. The conclusion (complex structure on X) depends entirely on this step. Theorem 4.1 and Theorem 1.2 inherit this defect. Without a valid proof of this step, the paper's central conclusions are unsupported.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.05635v2 — Large Bricks and Join-irreducible torsionfree classes

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** There is a logical gap in the proof of Proposition 3.9, meaning that a necessary step or justification is missing, so the conclusion does not properly follow from the premises given.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The construction of a directed system from a spanning tree of the Hasse quiver in Proposition 3.9 is mathematically invalid. A spanning tree does not define a directed/filtered index category, and the paper's explicit claim that 'we don't have any compatibility condition to check on the maps as the underlying graph is a tree' is false. A direct limit requires a directed indexing category with coherent transition maps for all composable pairs. Without a properly defined directed system, the central object F (whose existence drives the entire main proof) is not well-defined.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this as the most critical error. Reviewer A calls it MAJOR-REVISION on the grounds that the result might be salvageable by a different construction, but Reviewer B correctly argues that this is not a mere gap in exposition — it is an error in the definition of a fundamental categorical construction. The paper explicitly asserts that no compatibility check is needed, which is mathematically wrong. The direct limit F is the sole vehicle for the main theorem's proof, and without it the entire argument collapses. While a different proof strategy might exist, the proof as presented is fundamentally broken at this step. Under the key test: if confirmed, this finding alone means the paper's central conclusion is not supported by the argument as given, which is retraction-worthy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.11232v2 — Multiplication formula for Hernandez and Leclerc's quivers with potentials

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof of Theorem 3.2 (the central multiplication formula) imports GLS07-style geometric arguments (Euler characteristics of constructible strata, fiber descriptions, Grassmannian decompositions) into the setting of modules over an infinite-dimensional Jacobian algebra A without establishing that the required geometric prerequisites (algebraicity, finite type, constructibility, affine fiber properties) hold in this new context.

- **Arbiter justification for RW classification:**  
  > This is the paper's core theorem. The entire proof strategy depends on geometric properties that are highly setting-sensitive and known to hold in 2-CY/Frobenius/finite-type contexts but are not verified here. Both reviewers independently identify this as fatal. Reviewer A emphasizes the categorical transfer failure; Reviewer B emphasizes undefined objects and non sequiturs. Together they establish that the proof is not a sketch with gaps but rather a wholesale unverified import of methodology. Under the prompt's key test, if confirmed, this requires retraction because the paper's primary contribution is unsupported.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.11232v2 — Multiplication formula for Hernandez and Leclerc's quivers with potentials

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Internal to the proof of Theorem 3.2, multiple essential steps are undefined, unjustified, or logically disconnected: the set C in (3.12), the projection/fiber arguments, the notation ⊥d', equation (3.13) cited without hypothesis verification, the decomposition over an unspecified index set Y, and the conclusion that certain fibers are affine spaces—all asserted rather than derived.

- **Arbiter justification for RW classification:**  
  > Even setting aside the ambient-setting transfer problem, the proof does not go through on its own terms. The steps needed to derive equation (3.16) from the preceding manipulations are missing. This is an independent fatal flaw in the same theorem. Both reviewers identify these gaps; Reviewer A separates them as a distinct finding while Reviewer B folds them into the same finding. Either way, the proof has no valid derivation chain.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.11232v2 — Multiplication formula for Hernandez and Leclerc's quivers with potentials

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Proposition 4.3's proof is logically invalid. The contradiction argument claiming F_T = 2F_T does not follow from Theorem 3.2 (even if that theorem were valid). The right-hand side of the multiplication formula is a sum over multiple Y with different Euler-characteristic coefficients, and there is no mechanism shown to collapse it to a single term with coefficient 2. Additionally, the proposition uses Ext over 𝒜 (a cluster algebra) rather than Ext over A (the Jacobian algebra), making the statement formally ill-posed.

- **Arbiter justification for RW classification:**  
  > This proposition is the essential bridge from the multiplication formula to all representation-theoretic conclusions about tensor product simplicity and heads. Both reviewers identify the contradiction argument as a non sequitur. Reviewer A additionally identifies the category error (Ext over 𝒜 vs A). Reviewer B's second pass upgrades severity even further. Since this proposition is indispensable for Theorems 4.5 and 2.3, its failure propagates to all main applications. The logical error is elementary and cannot be repaired by minor revision—it requires a completely new argument.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.11232v2 — Multiplication formula for Hernandez and Leclerc's quivers with potentials

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Theorem 4.5 (linking heads of tensor products of simple modules to generic extensions, and claiming to prove Conjecture 5.1 of [LM21]) is not proved. The proof depends on the invalid Proposition 4.3 and unproved Theorem 3.2, and independently fails at its final step where the existence of the required exact sequence is dismissed with 'It is easy to see' without derivation.

- **Arbiter justification for RW classification:**  
  > This is one of the paper's principal advertised applications. Both reviewers agree the proof is incomplete and depends on earlier broken results. Reviewer A rates it RETRACTION-WORTHY; Reviewer B initially rated it MAJOR-REVISION but effectively treats it as fatal in the second pass by noting the cascading dependency on invalid prior results. Since the paper explicitly claims to prove an open conjecture via this theorem, its failure means a headline claim of the paper is unsupported.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.11232v2 — Multiplication formula for Hernandez and Leclerc's quivers with potentials

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

- **B3++ finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > Theorem 2.3 (a structural result about the Gabriel quiver) is essentially unproved. The manuscript promises a computation but does not carry it out, instead invoking BIRS09 from a different (2-CY) framework without verifying that its hypotheses apply to the present setting.

- **Arbiter justification for RW classification:**  
  > Reviewer A identifies this as RETRACTION-WORTHY; Reviewer B does not separately flag it but the concern is implicitly covered by the cascading dependency analysis. The proof as written consists of an unverified citation transfer and an absent calculation for an advertised structural result. However, I note slightly lower confidence because it is conceivable that the BIRS09 result does apply with additional checking—the gap is more clearly one of missing verification than of demonstrated impossibility. Still, as a flagship theorem with no valid proof in the manuscript, it meets the retraction threshold.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.20571v2 — On the principal eigenvalue for compound Poisson processes

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Lemma 4.4's proof contains a mathematical error in the CLT-based density argument: it evaluates the density j_n of the standardized sum S_n/(σ√n) at points v/(σ√n) that shrink to zero and claims convergence to γ(0), but this confuses the density of the standardized sum with its value at a vanishing argument. The scaling is mishandled.

- **Arbiter justification for RW classification:**  
  > This is a separate mathematical error from the conditioning issue. If the density convergence argument is invalid, Lemma 4.4 is unproven, breaking the proof chain at an even earlier stage. However, there is some possibility that a corrected local CLT argument could salvage Lemma 4.4 itself (though not the downstream conditioning error in Lemma 4.5). Given that even a correct Lemma 4.4 is insufficient for the main theorem due to the conditioning error, the combined effect is definitively retraction-worthy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2405.20571v2 — On the principal eigenvalue for compound Poisson processes

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Lemma 4.4, even if technically correct, proves only convergence of the law of S_n conditioned on {S_n∈D} to uniformity on D—not convergence under the path-survival conditioning {S_1∈D,...,S_n∈D} that the subsequent proof requires.

- **Arbiter justification for RW classification:**  
  > This is logically independent of whether the CLT computation in Lemma 4.4 is correct. The lemma addresses the wrong conditional law. Path-survival conditioning biases the endpoint distribution toward the interior of D (quasi-stationary behavior), which generally differs from endpoint conditioning. No argument bridging these two conditioning regimes is provided. This gap is structural and cannot be fixed by minor revision of the existing proof strategy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.03201v2 — Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Proof of Theorem 5.1 uses the nonsensical group Gal(K_{∞,w}/K_{∞,w}) ≅ ∏_{ℓ≠p} Z_ℓ to conclude ker f₄ = coker f₄ = 0. This group is trivially the identity, and the intended local comparison is fundamentally misidentified.

- **Arbiter justification for RW classification:**  
  > This step is used to eliminate local terms in the snake-lemma comparison that yields the isogeny formula. The statement is mathematically impossible — the Galois group of a field over itself is trivial. This is not a gap that could be filled; it indicates the authors lost track of the relevant local extension. The proof collapses at this point. Reviewer A identified this; Reviewer B's concerns about the Euler characteristic derivation are complementary and reinforce the conclusion that the proof is broken at multiple points.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.03201v2 — Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The derivation of equation (11) in the proof of Theorem 5.1 relies on unjustified multiplicativity of Euler characteristics from the flat cohomology long exact sequence. The claimed ratio of Euler characteristics does not follow from the provided setup without additional finiteness/vanishing hypotheses that are not established.

- **Arbiter justification for RW classification:**  
  > This is a third independent failure point in the proof of Theorem 5.1, identified primarily by Reviewer B and acknowledged by Reviewer A in reflection. The algebraic manipulation assumes properties of Euler characteristics that are not generally valid for arbitrary Λ-modules. Combined with the hypothesis mismatch and the local Galois group error, this makes the proof of Theorem 5.1 triply broken. Any one of these errors alone would be sufficient; together they are decisive.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.03201v2 — Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Theorem 1.5/6.3 has an internal contradiction: the Galois group of the trivializing extension is described as an open subgroup of GL₂(Z_ℓ) but then stated to be pro-p, while working over Z_ℓ with ℓ-adic μ-invariants. An open subgroup of GL₂(Z_ℓ) is pro-ℓ (up to finite index), not pro-p for p ≠ ℓ.

- **Arbiter justification for RW classification:**  
  > The entire noncommutative Iwasawa-theoretic framework of Part II depends on the correct identification of the ambient prime and group structure. If G is pro-ℓ rather than pro-p, then Λ(G) is the wrong Iwasawa algebra, the μ-invariant is defined over the wrong prime, and all cohomological/Nakayama arguments are in the wrong category. However, there is a small possibility this is a systematic notational confusion (consistently swapping p and ℓ) that could be mechanically corrected without changing the mathematical content, which introduces slight uncertainty. Nevertheless, as printed, the theorem specifies mutually incompatible hypotheses and the main result of Part II is incoherent.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.04846v2 — Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The main gate-count complexity claim is internally inconsistent and mathematically impossible. The paper states a gate count of O(ε log(1/ε) log log(1/ε) ···) which decreases as ε→0, and the recursion structure (angle-doubling with constant gates per level) yields at most O(m) = O(log(1/ε)) gates, not the iterated-log product claimed. The choice of m and the precision allocation are mutually contradictory.

- **Arbiter justification for RW classification:**  
  > The paper's sole headline contribution is an asymptotic scaling theorem. Both reviewers independently identify that the scaling formula is impossible (gate count decreasing with accuracy demand) and that the recursion structure cannot produce the claimed complexity. The derivation contains contradictory precision budgets (δ ≤ ε/⌈log₂(1/ε)⌉ vs. later claiming error ε·log(1/ε)·loglog(1/ε)···) and an asymptotically nonsensical choice of m. These are not isolated typos but pervasive failures in the proof of the central result. Without a valid derivation, the main theorem is unsupported.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.04846v2 — Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The core construction for implementing logical phase gates P(α)_L transversally via solving Hv = w over ℝ (Eq. 4) is mathematically unjustified and likely invalid. The claim that full row rank over F₂ implies full row rank over ℝ is false, and even when a real solution exists, no proof is given that the resulting tensor product of physical phase gates preserves the code space and induces the correct logical action.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as the indispensable primitive enabling the entire recursive scheme. Reviewer B provides a concrete counterexample class (even-weight row dependencies). Reviewer A emphasizes the missing proof of logical action on all codewords/cosets and compatibility with stabilizer structure. If this construction fails, the recursion has no valid starting point and the entire method collapses. The Steane code example is stated without derivation and does not constitute a general proof.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.04846v2 — Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The manuscript uses an ε-dependent finite gate set while framing its contribution as addressing the fixed finite universal gate-set approximation problem (Nielsen–Chuang challenge / Solovay-Kitaev improvement). An ε-indexed family of finite sets is fundamentally different from a single fixed finite set.

- **Arbiter justification for RW classification:**  
  > This is a problem-definition error, not a presentation issue. The paper explicitly states gates are 'chosen from a finite set depending on the value of ε.' Standard lower bounds and comparisons to Solovay-Kitaev do not apply when the generating set changes with target precision. Reviewer A identified this; Reviewer B acknowledged it as a missed finding they would rate RETRACTION-WORTHY. The paper does not solve the problem it claims to address.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.04846v2 — Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The fault-tolerance claim assumes availability of arbitrary physical phase rotations P(α) on each qubit to realize logical P(α)_L transversally, thereby presupposing the very continuous rotations the paper claims to synthesize fault-tolerantly from a finite discrete set.

- **Arbiter justification for RW classification:**  
  > This collapses the distinction between physical analog control and fault-tolerant logical gate synthesis, which is the entire point of the FT synthesis problem. Reviewer A identified this as a category error that voids the claimed novelty. Reviewer B acknowledged this as a missed finding they would rate RETRACTION-WORTHY. If arbitrary-angle physical rotations are assumed at the encoded level, the claimed approximation breakthrough is vacated.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.11623v4 — Nevanlinna Theory on Geodesic Balls of Complete K√§hler Manifolds

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the Green function $G_R(o,x)$ for the geodesic ball $B(R)$ was incorrectly stated to satisfy the Dirichlet boundary condition on the geodesic sphere $\partial B(R)$, when in fact it does not necessarily vanish on the boundary as required by the Dirichlet condition.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Probable sign error in the genus term derivation of Theorem 4.1. The proof moves from -∫N_f(r,ζ)K'(ζ)ω(ζ) to a lower bound involving +(2-2g)T_f(r), but Gauss-Bonnet gives ∫K'ω = 2-2g, so the negative sign should yield -(2-2g)T_f = (2g-2)T_f. The resulting coefficient (q-2+2g) in the main Second Main Theorem may be incorrect.

- **Arbiter justification for RW classification:**  
  > The coefficient in front of the characteristic function is the quantitative heart of any Second Main Theorem. If the sign handling is wrong, the stated theorem is numerically false, not merely incompletely proved. This directly affects Theorem II and all downstream defect relations for genus g targets. Both reviewers acknowledged this error; Reviewer A rated it RETRACTION-WORTHY and defended this strongly in reflection. Reviewer B acknowledged it as genuine but considered it secondary to the Lemma 3.6 issue. The sign tracking in the displayed computation is specific enough to evaluate: the intermediate inequality appears directionally inconsistent with Gauss-Bonnet, and this is not a gap that can be filled—it would require changing the theorem statement or the proof strategy.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.15649v2 — Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe

- **Paper category:** Computer Science
- **SPOT error category:** Statistical reporting (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Referenced Table 1 and Figures 1–3 containing experimental results are absent from the manuscript. No quantitative data, numerical comparisons, variance estimates, or statistical outputs are actually presented, yet the paper makes specific claims (20% IoU improvement, 30% speed reduction).

- **Arbiter justification for RW classification:**  
  > The paper's central conclusions are empirical and comparative. The complete absence of results data means there is zero evidential support for the headline claims within the manuscript. This is not a formatting gap—it is an empty results section with unsupported assertions. Both reviewers rated this RETRACTION-WORTHY and defended it through reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.15649v2 — Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe

- **Paper category:** Computer Science
- **SPOT error category:** Statistical reporting (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > No experimental dataset is described: no dataset name, number of subjects, number of frames, annotation protocol, ground-truth source, train/test split, resolution, frame rate, or ethical approval for human subjects.

- **Arbiter justification for RW classification:**  
  > Pose-estimation accuracy metrics (MSE, IoU) are defined relative to ground-truth annotations. Without any specification of the dataset or reference standard, the reported metrics are not merely irreproducible—they are uninterpretable. The central accuracy claims have no scientific meaning. Both reviewers rated this RETRACTION-WORTHY and strongly defended it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.15649v2 — Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe

- **Paper category:** Computer Science
- **SPOT error category:** Statistical reporting (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The proposed 'enhancements' to MediaPipe are never concretely described. The paper uses vague phrases ('refined algorithms,' 'advanced neural network architectures') but provides no architecture modifications, training procedures, hyperparameters, loss functions, or optimization details. The only concrete processing described is a rule-based angle threshold for curl counting.

- **Arbiter justification for RW classification:**  
  > The paper's central novelty claim is that specific enhancements to MediaPipe produced measurable improvements. If the enhancements are undefined, there is no identifiable intervention to evaluate, attribute gains to, or replicate. The central scientific contribution is untestable. Reviewer A rated this RETRACTION-WORTHY and defended it vigorously; Reviewer B initially rated a related finding as MAJOR-REVISION but in reflection concurred that the absence of any described modification may indicate the claimed innovation does not exist.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2406.15649v2 — Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe

- **Paper category:** Computer Science
- **SPOT error category:** Statistical reporting (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The baseline comparison is completely undefined. The paper claims superiority over 'traditional models' and the 'baseline MediaPipe model' but specifies no version, configuration, hardware, thresholds, or matched conditions for comparison.

- **Arbiter justification for RW classification:**  
  > The paper's core claim is comparative improvement. Without an identified and specified comparator under matched conditions, the claim of superiority is logically empty. Both reviewers identified this as a critical defect; Reviewer A rated it RETRACTION-WORTHY, and Reviewer B's findings 3 and related reasoning support the same conclusion.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.02110v2 — On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof that M^+ is contractible (Lemma 3), hence χ(M^+)=1, is invalid. The manuscript invokes 'fibration' language without establishing fibrations or local triviality, describes fibers incorrectly (e.g., quarter-circle arcs claimed contractible without justification, variable-plane inconsistencies), and draws contractibility conclusions that do not follow from the stated constructions. The topology of M^+ as a nonlinear algebraic set in the positive orthant is non-trivial and is not established by the given argument.

- **Arbiter justification for RW classification:**  
  > The Morse counting relation Σ(-1)^q α_q = χ(M^+) = 1 is the sole mechanism yielding uniqueness. If χ(M^+) is not established, the main theorem has no proof. Both reviewers agree this is a fundamental failure after reflection. Reviewer A identified it as retraction-worthy from the start; Reviewer B upgraded it to retraction-worthy in reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.02110v2 — On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The Morse-theoretic argument is performed on M^+ (defined by I=I₀ and C=0 in the positive orthant), which is strictly larger than the space of planar realizable strictly convex quadrilateral configurations. The manuscript never proves that every critical point of U on M^+ corresponds to a realizable planar convex central configuration, nor that spurious algebraic critical points outside the geometric domain cannot occur. Uniqueness on M^+ does not imply uniqueness of geometric central configurations without such an equivalence.

- **Arbiter justification for RW classification:**  
  > This is a theorem-domain mismatch at the heart of the paper. The stated theorem concerns planar convex central configurations, but the proof counts critical points on a larger algebraic set. Without proving the domains share the same critical-point structure, the central inference is invalid. Reviewer A identified this as retraction-worthy and defended it in reflection; Reviewer B raised related concerns about M^+ containing non-geometric points.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.02110v2 — On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Lemma 2 establishes positive definiteness of the ambient Hessian D²W(r) in all six distance variables and concludes that constrained critical points are non-degenerate minima of Morse index 0 on M^+. However, for constrained Morse theory, non-degeneracy must be verified for the Hessian of U restricted to the tangent space of M^+, which is a different object. The manuscript does not compute the restricted/bordered Hessian, nor does it establish that M^+ is a smooth manifold at critical points (requiring regularity of the constraint map).

- **Arbiter justification for RW classification:**  
  > The Morse index assignment (all critical points have index 0) is directly used in the counting formula. If the constrained Hessian has different signature, the count changes and uniqueness fails. Reviewer B rated this retraction-worthy; Reviewer A rated it major-revision. The argument is that while ambient positive definiteness is suggestive, the constrained Morse analysis is entirely absent, not merely incomplete. Given that the smooth-manifold hypothesis for M^+ is also unverified, the entire Morse-theoretic framework is unsubstantiated. However, because positive definiteness of the full Hessian often does imply positivity on tangent subspaces, there is some probability this could be repaired, placing this at the boundary. I classify it as retraction-worthy because the needed smooth-manifold and tangent-space arguments are absent, not merely incomplete.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.06913v2 — A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Incorrect use of advanced composition in all (ε,δ)-DP results. The per-mechanism privacy parameters used in Theorems 3.2, 4.2, and 4.4 do not satisfy the paper's own composition lemma (Lemma 2.2). The denominators are missing a factor of approximately √m, and the δ/(2k) allocation is omitted. This means all approximate-DP guarantees are unproven and generally false under the stated parameters.

- **Arbiter justification for RW classification:**  
  > This is a systematic, global error affecting every approximate-DP theorem in the paper. The stated (ε,δ)-DP guarantees do not follow from the paper's own privacy lemma, and the parameters are materially wrong (not just slightly loose). Since the approximate-DP results are presented as central contributions, this invalidates the paper's main claims as written. Both reviewers agree on the severity after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.06913v2 — A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances

- **Paper category:** Computer Science
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Unjustified sensitivity claim in Lemma 3.2 / Appendix A for the tree-release primitive. The proof claims that releasing distances from root to centroid and centroid to children has global ℓ1 sensitivity 1 because subtrees are disjoint. However, disjoint subtrees do not imply edge-disjoint paths: a single edge perturbation can affect multiple released distances simultaneously. The true sensitivity could be O(log n) or more.

- **Arbiter justification for RW classification:**  
  > This primitive is used in every main theorem (Theorems 3.1, 3.2, 4.1–4.4). The paper's own proof is clearly invalid—the logical step from subtree disjointness to sensitivity 1 does not hold. If the true sensitivity is higher, the required noise scale increases, which would change both the privacy guarantees and the error bounds. While Reviewer A suggested this might be salvageable by importing an external result, the paper as written provides no valid privacy analysis for its most fundamental building block, and any fix could change the quantitative conclusions. This crosses the retraction threshold because every main theorem depends on it.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.09178v2 — Shafarevich-Tate groups of holomorphic Lagrangian fibrations II

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** There is likely a mistake in the formulation or derivation of equations related to Kähler twists, such as an incorrect application of properties of Kähler manifolds or errors in twisting procedures within the proof.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Theorem D uses an incorrect criterion for Fujiki class C. The proof assumes that if X^φ is of Fujiki class C, there exists a rational map f: X^φ → Y to a Kähler manifold Y with a pullback Kähler class h on X^φ. In reality, Fujiki class C means bimeromorphic to a compact Kähler manifold via a modification μ: Z → X^φ from a Kähler Z, not a rational map from X^φ to a Kähler target. This is a category error that destroys the contradiction strategy.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identified this as retraction-worthy. The error is not a gap but a fundamental misunderstanding of the geometric criterion being applied. The entire proof mechanism for Theorem D collapses. No local repair is possible—a completely new argument would be needed.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.18406v2 — A form of refined Roth's theorem and its application to the $abc$-conjecture

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof of Theorem 1.4 invokes Dirichlet's unit theorem to claim that for an arbitrary algebraic integer y, there exists a field-dependent constant c(κ) such that |y|_v ≤ c(κ)|y|_w for any two Archimedean places v, w, and hence m(y,0)=O(1). This is not a consequence of Dirichlet's unit theorem and is false in general: algebraic integers can have wildly unbalanced Archimedean absolute values. This step is the sole mechanism used to eliminate the term 2m(x'Q(x),∞) from Theorem 2.1 and obtain the main inequality of Theorem 1.4.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identify this as a fatal error. The invoked principle is mathematically incorrect for arbitrary algebraic integers. Without this step, Theorem 1.4's proof collapses entirely. No minor revision can repair a proof that rests on a false mathematical claim at its decisive step.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.18406v2 — A form of refined Roth's theorem and its application to the $abc$-conjecture

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The proof of Theorem 1.4 asserts that y = 1/(x'Q(x)) is an algebraic integer when x is an algebraic integer, but never supplies the required valuation argument. The ideals a_0 and a_∞ used in the construction of x' are undefined, and the divisor bookkeeping needed to verify ord_v(x') ≤ Σ_j ord_v(x−a_j) at all finite places is absent. The same unsupported integrality claim is reused in the proof of Theorem 1.5.

- **Arbiter justification for RW classification:**  
  > Both reviewers agree this is a critical unsupported claim. The integrality of y is a prerequisite for the subsequent Archimedean argument. Without it, the passage from Theorem 2.1 to Theorem 1.4 does not function, and Theorem 1.5 (and hence the abc corollary) also fails. The manuscript provides no basis to believe the claim is even true as stated.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.18406v2 — A form of refined Roth's theorem and its application to the $abc$-conjecture

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Equation (19) in the proof of Theorem 2.1 replaces full counting functions N(x, a_j) with truncated counting functions N̄(x, a_j) without justification. Since N̄ ≤ N, this is a one-directional inequality being used in the wrong direction—it strengthens the bound and cannot be done without a separate multiplicity estimate that is not provided.

- **Arbiter justification for RW classification:**  
  > Reviewer A identifies this as a direct logical error; Reviewer B acknowledges it as a missed fatal error in reflection. Theorem 2.1 is the engine for all subsequent results; if its statement involves truncated counts but the proof only establishes the inequality for full counts, the theorem is not proved as stated.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.19061v3 — A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > CHSH nonlocality (Horodecki quantity M) is invariant under qubit swap. Swapping subsystems sends the correlation matrix T to T^T, and the Horodecki quantity depends on eigenvalues of T^T T (equivalently T T^T), which have identical spectra. Therefore 'swap-intolerant nonlocality'—where a state is CHSH-nonlocal but becomes local after swap—cannot exist for any Hermitian trace-1 operator, regardless of positive semidefiniteness.

- **Arbiter justification for RW classification:**  
  > This is a clean linear-algebraic invariance that directly contradicts the paper's central definition and theorem. It is not a matter of interpretation or proof technique—the claimed phenomenon is mathematically impossible. Both reviewers agree after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.19061v3 — A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

- **B3++ finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Proposition 3.1's geometric argument that semi-trivial perp states cannot be simultaneously positive-semidefinite and nonlocal is incorrect. The inequality |E| > 1 does not force the smallest eigenvalue negative because the radii r_+ and r_- depend on adjustable parameters τ_p. Appropriate choices of τ_p can yield |E| > 1 with nonnegative eigenvalues.

- **Arbiter justification for RW classification:**  
  > This proposition is a key logical pillar: it motivates the necessity of leaving the PSD set and aligns the positivity boundary with the nonlocality boundary. If it is false, the entire constructive strategy collapses independently of the swap-invariance issue. Reviewer B identified this clearly; Reviewer A flagged the unverified optimization. Both agree it is fatal after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.19061v3 — A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity

- **Paper category:** Physics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

- **B3++ finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Theorem 1.4's constructive rotation step ('rotate E into region (9)') cannot produce swap-intolerant nonlocality because (a) CHSH is swap-invariant, and (b) the rotation changes the relationship between the β-vector and τ-vector, altering eigenvalues and positivity conditions in ways the proof does not account for.

- **Arbiter justification for RW classification:**  
  > Even granting all auxiliary results, the final constructive step aims to produce an effect that is mathematically forbidden. Two independent problems (swap invariance from Reviewer A, uncontrolled eigenvalue changes from Reviewer B) each independently invalidate the construction. Both reviewers rate this retraction-worthy after reflection.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.19323v3 — MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo

- **Paper category:** Computer Science
- **SPOT error category:** Experiment setup (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The manuscript describes two incompatible methods—MSP-MVS (deformable-patch MVS with multi-granularity segmentation prior, anchor equidistribution, iterative local search) and TSAR-MVS (post-processing pipeline with confidence filtering, superpixel/RANSAC refinement, WMF propagation, textureless-aware segmentation)—under one paper. The evaluated algorithm cannot be uniquely identified, breaking the method-to-results correspondence required for any scientific claim.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identified this as retraction-worthy and neither downgraded upon reflection. This is not a naming typo—the two described pipelines operate at different stages (full MVS vs. post-processing), have different inputs, different module architectures, and different contribution claims. If confirmed, no reader can determine what algorithm generated the benchmark numbers, making the central SOTA claims scientifically unsupported. This meets the retraction test: the paper's central conclusions cannot be supported by the data as presented because the method generating those data is undefined.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2407.19323v3 — MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo

- **Paper category:** Computer Science
- **SPOT error category:** Experiment setup (severity tier: `errata`)
- **SPOT annotation (the one annotated error):** The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

- **B3++ finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The manuscript explicitly proposes TSAR-MVS ('Therefore, we propose TSAR-MVS') while simultaneously citing 'TSAR-MVS (Yuan et al. 2024b)' as prior work in the related work section, creating a direct contradiction about whether the core contribution is novel or previously published.

- **Arbiter justification for RW classification:**  
  > Reviewer A rated this retraction-worthy and defended it strongly in reflection; Reviewer B identified it as a new error in reflection that strengthened the retraction case. If confirmed, this collapses the novelty claim—a methods paper's central contribution is that a new method is being proposed. However, there is some residual possibility this reflects careless editing of a revision/extension of the authors' own prior work rather than deliberate misrepresentation. Even so, the manuscript as submitted cannot support its novelty claims. The severity remains retraction-worthy because the paper in its current form misrepresents originality at the most fundamental level.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

### 2408.16162v2 — Every Polish group has a non-trivial topological group automorphism

- **Paper category:** Mathematics
- **SPOT error category:** Equation / proof (severity tier: `retract`)
- **SPOT annotation (the one annotated error):** The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

- **B3++ finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof of Lemma 2.3 contains an invalid maximality contradiction: the argument constructs W:=U∪V' and claims W∈𝒫 by asserting disjointness of translates x+W and y+W for distinct x,y∈L. However, only same-type disjointness ((x+U)∩(y+U)=∅ and (x+V')∩(y+V')=∅) is established. The mixed intersections (x+U)∩(y+V') and (x+V')∩(y+U) are never shown empty, so the disjointness of x+W and y+W does not follow. Without this, the contradiction to maximality fails and item (2) of the lemma (that the complement of L+U has empty interior) is unproved.

- **Arbiter justification for RW classification:**  
  > This is a definitive logical non sequitur internal to the written proof, not a mere gap or missing citation. Lemma 2.3 is the sole mechanism for producing the dense subgroup in the main theorem's only nontrivial case. Both reviewers independently flagged this lemma as fatally flawed. Reviewer A's specific identification of the mixed-intersection failure is a clean, precise error that survives charitable reconstruction—even granting V' is non-empty and open, the proof still does not establish what it needs. The manuscript's central conclusion cannot be supported without this lemma.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

