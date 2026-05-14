# GD — RW false-positive audit sheet

**Total RW findings:** 77  
**Matched SPOT annotation:** 9  
**Unmatched (this audit):** 68  

## Summary (fill in after manual review)

```
Total non-matching RW findings: 68
Valid severe (SPOT missed): ___
Related (real but overstated): ___
False alarm: ___

Original RW-precision: 9/77 = 11.7%
Adjusted RW-precision: (9 + valid_severe) / 77 = ___%
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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Internal inconsistency between reported energy density (61.05 Wh/kg) and the value derivable from stated capacitance (1502 F/g) and voltage window (0.65 V). Both the standard formula and the paper's own formula yield ~88.2 Wh/kg—a ~31% discrepancy that cannot be explained by rounding.

- **Arbiter justification for RW classification:**  
  > Energy density is the headline metric in the abstract and conclusions. The discrepancy is mathematically undeniable from the paper's own numbers and cannot be attributed to a typo or rounding. It demonstrates either that the capacitance value used for the energy calculation differs from the reported 1502 F/g, or that an incorrect formula was applied. Either way, the central performance claim as published is arithmetically unsupported. This was identified by Review A, strongly endorsed by Review B in steelman, and neither reviewer could explain it away.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Systematic mismatch between gravimetric and areal capacitance values. At 5 mg/cm² loading, 1502 F/g should correspond to ~7.51 F/cm², but the paper reports 4.39 F/cm²—a ~42% discrepancy. Similar mismatches exist for the other electrode materials.

- **Arbiter justification for RW classification:**  
  > This is an independent arithmetic inconsistency in the same core metric, reinforcing that the normalization process is fundamentally flawed. Combined with the energy density error, it establishes a pattern of systematic calculation errors affecting the primary reported values. Both reviewers identified this, and Review B upgraded it to retraction-worthy in steelman. The discrepancy is too large (~42%) to be experimental error and too systematic to be a typo.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Critical lack of vehicle/process control and confounded treatment-time contrast. The experimental design compares cytokine levels before and after exosome addition, but no matched vehicle control (PBS, buffer, or carrier alone) was added to parallel cultures at the same time point. The 'before' measurement is at 24h post-virus and the 'after' is at 96h total, meaning natural cytokine decay, degradation, cell exhaustion, dilution from medium addition, or any non-exosome component could explain the observed reductions.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this as a fundamental design flaw. Reviewer A upgraded this toward RETRACTION-WORTHY after steelmanning B. Reviewer B defended it as RETRACTION-WORTHY throughout. Without a vehicle control, the primary causal claim that exosomes reduce cytokines is not identifiable from the data—this is not a matter of interpretation or overclaiming but a structural inability of the design to support its central conclusion. The rubric states RETRACTION-WORTHY applies when 'the paper's central conclusions CANNOT be supported by the data as presented,' which fits here.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Internally contradictory statistical reporting that prevents verification of primary analyses. Table 4 is labeled as 'paired t-test' but reports medians, IQRs, Z-statistics, and r-values characteristic of Wilcoxon signed-rank tests. Table 5 (Wilcoxon) uses the same data structure. Cohen's d is referenced in table headers but not reported. These contradictions mean readers cannot determine what statistical test was actually performed on the primary endpoints.

- **Arbiter justification for RW classification:**  
  > Both reviewers flagged this. Reviewer A upgraded it toward RETRACTION-WORTHY after steelman exchange, acknowledging that contradictory test labels and output formats could mean the primary analyses are unverifiable. Reviewer B rated it RETRACTION-WORTHY from the start. If the wrong test was applied or the wrong outputs were reported, all significance claims could be invalid. This is not a minor formatting issue—it strikes at the inferential backbone of the paper.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Analytical validation table reports impossible values: negative LOD and LOQ (e.g., kidney LOD = -587.51 µg/kg, LOQ = -1780.34 µg/kg) and R² values exceeding 1.0 (e.g., muscle R² = 6.96), while other matrices show near-zero R² (skin R² = 0.002) yet are still used for quantitation.

- **Arbiter justification for RW classification:**  
  > LOD/LOQ are defined as positive multiples of SD/slope and cannot be negative under any valid calibration. R² is bounded [0,1] by definition. These are mathematical impossibilities that indicate fundamental errors in the calibration/validation procedure. Since all tissue concentration data and all derived PK parameters depend on the validity of the LC-MS/MS assay, these impossible validation metrics invalidate the entire quantitative foundation of the paper.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Elimination half-life values are internally contradictory and biologically implausible. Gill tissue is reported with three mutually exclusive t½ values (0.94 h, 19.39 h, 198.48 h) in different parts of the manuscript. Plasma t½ is reported as 3368.24 h (~140 days), which is biologically implausible and contradicts observed concentration decline within the 128 h observation window.

- **Arbiter justification for RW classification:**  
  > Half-life is a core pharmacokinetic parameter. Three different values for the same tissue in the same study indicate either calculation errors, transcription errors, or data fabrication. A plasma t½ of 140 days estimated from a 128 h sampling window is statistically unjustifiable and biologically nonsensical at 20°C. These contradictions mean the manuscript's central PK conclusions (elimination kinetics, tissue retention, withdrawal recommendations) cannot be trusted.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The trapezoidal AUC formula is stated as (Cᵢ + Cᵢ₊₁)·Δt rather than the correct 0.5·(Cᵢ + Cᵢ₊₁)·Δt, which would double all AUC values if actually applied.

- **Arbiter justification for RW classification:**  
  > AUC is the primary exposure metric and directly informs bioavailability estimates, tissue distribution comparisons, and withdrawal time calculations. If the stated formula was used, all AUC values are inflated by 2×, fundamentally changing PK interpretation. There is a small possibility this is only a typographical error in the equation while the calculation was done correctly, but given the other mathematical impossibilities in the paper, there is no basis to extend this benefit of the doubt.

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

- **GD finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Elimination rate constant and half-life values are internally inconsistent with the stated equations. For example, Ke = 0.01 h⁻¹ should yield t½ = ln(2)/0.01 = 69.3 h, not the 0.94 h reported.

- **Arbiter justification for RW classification:**  
  > This is a direct mathematical inconsistency between reported parameters and the equations used to derive them. It indicates either the equations were not actually applied or the parameters were incorrectly calculated/transcribed. Combined with the other contradictory half-life values, this confirms that the PK parameter estimates are unreliable.

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

- **GD finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > Conflicting Tmax statements for the same tissue: gill peak concentration is reported at 3 h, 6 h, and 8 h in different passages of the manuscript.

- **Arbiter justification for RW classification:**  
  > Tmax is a basic descriptive statistic read directly from concentration-time data. Three different values for the same tissue in the same experiment indicate profound inconsistency in the core data reporting. This, combined with the contradictory half-lives for gill, indicates that the PK results section is unreliable at the most fundamental descriptive level.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Identification of methylene blue and malachite green in real textile wastewater relies solely on visual matching of UV-Vis peaks without chromatographic or standard-addition validation. Real textile effluent contains numerous chromophores with overlapping absorbance bands.

- **Arbiter justification for RW classification:**  
  > The paper's central applied claim is that SBT-AgNPs remove specific named dyes (MB, MG) from textile wastewater. Without selective analytical confirmation (HPLC, LC-MS, spiking/recovery), assigning peaks at ~614 and ~665 nm to those specific dyes in a complex matrix is circular reasoning. If the dyes are not confirmed, the core conclusion collapses. Review A rated this RETRACTION-WORTHY; Review B effectively agreed during steelman. Review A partially softened this during steelman but only if the paper were reframed to 'nonselective decolorization'—which it is not. As written, the named-dye wastewater claim is central and unsupported.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Degradation/removal in wastewater is inferred from raw absorbance decreases at selected wavelengths without controls for nanoparticle scattering, adsorption onto particles, agglomeration/settling, matrix background changes, or dilution effects. No dark control, no catalyst-free light control, no extract-only control.

- **Arbiter justification for RW classification:**  
  > The paper claims photocatalytic degradation as its main outcome, but the experimental design cannot distinguish photocatalysis from adsorption, flocculation, settling, or photolysis. The comparison is AgNPs+room light vs. AgNPs+sunlight (i.e., light vs. more light), with no dark control. Both reviewers flagged this. Review A initially rated it RETRACTION-WORTHY, then softened slightly during steelman; Review B rated the missing controls as MAJOR-REVISION but upgraded the overall mechanistic claim to unsupported during steelman. The combination of no mechanistic controls plus absorbance-only measurement in a complex matrix means the central photocatalytic degradation conclusion cannot be supported by the presented data.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Human schizophrenia vs. control kinome analysis is based on pooled samples (one pool per sex-by-diagnosis group) with only technical triplicates, constituting pseudoreplication that eliminates valid statistical inference about disease effects, sex-specific effects, and all downstream analyses derived from these comparisons.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently rated this RETRACTION-WORTHY. Both steelman exchanges confirmed the severity without downgrade. Pooling removes all biological variance estimation; technical triplicates of a single pooled sample cannot support inferential claims about population-level disease or sex differences. All reported differential phosphorylation, upstream kinase predictions, peptide set enrichment linking dark kinases to schizophrenia, and sex-specific schizophrenia claims are fundamentally unsupported. This infects the paper's central disease-association narrative.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The sole validation experiment (EPHA6/GAB1 co-incubation mass spectrometry) is a single unreplicated experiment lacking FDR control and phosphosite confidence metrics, and the reported EPHA6 autophosphorylation sites (pY259, pY484) appear impossible given the stated recombinant construct spanning residues 683-1130.

- **Arbiter justification for RW classification:**  
  > The paper claims 195 novel kinase-substrate interactions but validates only one pair, and that single validation has no replication, no statistical framework, and a site-numbering problem that suggests either the construct, the numbering, or the MS annotation is wrong. Reviewer A identified the site inconsistency; Reviewer B acknowledged missing it and agreed it was devastating. In steelman, B upgraded the overall validation problem to RETRACTION-WORTHY when combined with the site inconsistency. Without even one credible validation, the entire substrate discovery pipeline lacks ground truth. Confidence is slightly lower than for the pooled-sample finding because the site-numbering issue could conceivably reflect a reporting/isoform numbering error rather than a data error, but even so the validation remains critically inadequate.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Misuse of the Ideal Gas Law as a causal explanation for planetary surface temperatures, used to dismiss the greenhouse effect. PV=nRT is an equation of state, not an energy balance theory; it cannot determine equilibrium temperature without radiative boundary conditions.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as a fundamental physical error. The ideal gas law relates state variables but does not independently explain why a planet has a particular temperature. This error underpins one of the paper's central physical arguments against the greenhouse effect. It is not a matter of interpretation — it is a category error in physics.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Conflation of CO₂ molecular residence time (~3-5 years) with the perturbation lifetime of anthropogenic CO₂ (centuries). The manuscript uses rapid molecular exchange to argue that anthropogenic CO₂ cannot accumulate, ignoring ocean buffering chemistry and multi-reservoir dynamics.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this as a well-known, basic carbon-cycle error. The distinction between individual molecular turnover and net perturbation removal is foundational. This error directly supports the paper's central claim that human CO₂ emissions are inconsequential, and its correction would eliminate that conclusion. Isotopic evidence (δ¹³C, ¹⁴C) independently confirms the anthropogenic origin of the CO₂ increase, which the manuscript ignores.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > No systematic review methodology: no search strategy, databases, inclusion/exclusion criteria, quality assessment, or synthesis protocol. The paper claims to be an evidence-based review but provides no reproducible method.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as fatal for a review article. The paper's conclusions depend entirely on which literature is surveyed and how it is evaluated. Without a transparent methodology, the review is non-reproducible and its conclusions are unsupported by any verifiable process. This is not a minor reporting gap — for a review article, the method IS the study design.

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

- **GD finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Severe selection bias: the manuscript overwhelmingly relies on advocacy organizations (Heartland, GWPF, CO2 Coalition, Net Zero Watch), blogs, self-published books, and low-impact/fringe journals while systematically excluding or dismissing the mainstream peer-reviewed literature without methodological justification.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. For a review article, the evidence base determines the conclusions. A systematically biased source selection toward ideologically aligned, non-peer-reviewed material — while ignoring thousands of peer-reviewed papers from leading journals — means the review's synthesis is fundamentally unreliable. Reviewer B rated this MAJOR-REVISION, but given that it is inseparable from the missing methodology and directly determines all conclusions, the combined effect is retraction-worthy.

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

- **GD finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > Failure to engage with mainstream attribution, carbon-budget, and assessment literature while making sweeping claims that overturn those fields. The paper does not address the strongest contrary evidence (satellite spectral measurements, vertical warming patterns, isotopic constraints, paleoclimate sensitivity estimates).

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this. A review claiming to overturn established science must rigorously engage the strongest opposing evidence. The manuscript simply declares mainstream findings 'non-existent' or 'invalid' without substantive rebuttal. This is not a minor omission — it means the paper's extraordinary claims lack the extraordinary evidence required.

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

- **GD finding (rated RETRACTION-WORTHY, finding #5):**  
  Location:   
  > Invalid inference from annual anthropogenic flux being a small fraction of gross natural fluxes to the claim that human contribution to atmospheric CO₂ is negligible. The relevant quantity is net imbalance, not gross source fraction.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. Natural fluxes are approximately balanced; the anthropogenic addition is a net perturbation to a near-equilibrium system. This is a basic stock-flow accounting error that directly underlies the paper's claim that human CO₂ is too small to matter.

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

- **GD finding (rated RETRACTION-WORTHY, finding #6):**  
  Location:   
  > Claim that logarithmic dependence of radiative forcing on CO₂ concentration means added CO₂ has negligible climatic effect. Logarithmic forcing implies approximately constant forcing per doubling, not negligible effect.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as a non sequitur from the manuscript's own cited formulae. Reviewer B additionally notes that the paper's own Figure 1 shows 0.64-0.81°C warming per doubling, contradicting the 'negligible' characterization in the text. The conclusion drawn is not supported by the mathematics presented.

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

- **GD finding (rated RETRACTION-WORTHY, finding #7):**  
  Location:   
  > Misrepresentation of greenhouse physics: the manuscript states the IPCC explanation 'makes no sense scientifically' and is 'immediately falsified,' but provides no correct radiative-transfer derivation and ignores radiative-convective equilibrium, emission-level arguments, spectroscopy evidence, and the well-verified spectral fingerprint of greenhouse forcing.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this. The paper's central thesis is that greenhouse-gas warming lacks scientific basis. A wholesale mischaracterization of the underlying physics — attacking straw mechanisms rather than the actual theory — invalidates this central conclusion.

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

- **GD finding (rated RETRACTION-WORTHY, finding #8):**  
  Location:   
  > Claim that 'no increase in floods, droughts, hurricanes, or extreme weather events' has been observed, contradicting IPCC AR6 documented increases in extreme precipitation intensity, heatwave frequency, and regional changes in drought and tropical cyclone intensity.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. The claim is presented as established fact using selective citations while ignoring comprehensive assessment reports. However, confidence is slightly lower because the extreme events literature is genuinely complex with regional heterogeneity, and some specific event categories (e.g., normalized hurricane damages) do have legitimate debate. The blanket 'no increase' claim nevertheless misrepresents the overall evidence.

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

- **GD finding (rated RETRACTION-WORTHY, finding #9):**  
  Location:   
  > Use of the seasonal cycle in the Keeling curve and COVID-era emission reductions as evidence against long perturbation lifetimes for anthropogenic CO₂.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. Seasonal exchange around a rising trend tests exchange rates, not perturbation lifetime. COVID-era reductions (~7%) would produce a signal smaller than natural variability against the background trend. These arguments are physically invalid and are used to dismiss mainstream carbon-cycle understanding.

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

- **GD finding (rated RETRACTION-WORTHY, finding #10):**  
  Location:   
  > Confusion of correlation with causation in planetary comparison: cross-planet associations between surface pressure and temperature are treated as proof that pressure causes temperature independently of radiative properties.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this (A explicitly, B as part of the ideal gas law finding). Pressure and temperature co-vary because massive greenhouse atmospheres are both dense and opaque to IR. The manuscript's headline physical argument depends on a causal interpretation that the data do not support.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The final YES-preservation argument cites Claim 4 for a reconfiguration conclusion, but Claim 4 is a size bound and provides no reconfiguration guarantee. The proof literally states 'by Claim 4 the answer is YES' when Claim 4 does not establish any such implication. This is a direct logical disconnect at the theorem's conclusion.

- **Arbiter justification for RW classification:**  
  > This is not a typo or minor citation error—it is invocation of a nonexistent implication at the exact point where the kernel's correctness is concluded. No valid replacement argument is provided. Both reviewers agree after steelman that this is fatal.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Claim 5 (stated for linear forests) is applied to G[J_s ∪ J_t ∪ J_m], but the manuscript never proves this union induces a linear forest. J_s and J_t each induce linear forests and J_m is independent, but their union can have arbitrary additional edges destroying the linear forest property. The key constructive reconfiguration step therefore lacks its required precondition.

- **Arbiter justification for RW classification:**  
  > The entire correctness argument for the kernel reduction depends on being able to reconfigure within this subgraph using a lemma that requires the linear forest property. If the precondition is not met, the lemma does not apply and the equivalence proof fails. Reviewer B upgraded this to RETRACTION-WORTHY after steelman.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Claim 7's proof contains unjustified greedy reconfiguration steps (e.g., 'greedily move all remaining tokens to J_m'). In token jumping, each move must maintain independence of the entire current token set. The manuscript treats this as trivial when it is not—independence of the destination set does not imply legality of the moves, which depends on adjacency to all currently-occupied vertices.

- **Arbiter justification for RW classification:**  
  > Reviewer A rated RETRACTION-WORTHY; Reviewer B initially rated the broader Claim 7 as MAJOR-REVISION but upgraded after steelman. The issue is that the equivalence proof requires a valid sequence of legal token jumps, and the manuscript provides no such argument. This is the substance of the correctness proof, not a peripheral detail. However, there is a small chance the steps could be made rigorous with significant additional argument, so confidence is slightly lower.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The quantum protocol requires orthogonality for confusable pairs (edges of G^(m)), but Lemma 4 and Definition 4 define orthogonal representations on the complement graph Ḡ^(m), where orthogonality is enforced on non-adjacent vertices. This categorical mismatch means Theorem 4's quantum rate formula optimizes the wrong graph parameter, and the claimed quantum advantage (R_quantum(g) < R_classical(g)) is unsupported.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as the central error and rate it RETRACTION-WORTHY. Reviewer A considered downgrading to MAJOR-REVISION in the steelman only if the problem were a globally consistent convention swap, but acknowledged this would still require every cited inequality and product identity to be re-verified under the swapped convention—something the manuscript does not do. Reviewer B's steelman reinforced the severity. The error is not a typo: it inverts which pairs must be orthogonal, changing the feasible set, the relevant ξ-quantity, and the asymptotic rate. Because the quantum advantage demonstration is the paper's primary contribution, this is RETRACTION-WORTHY under the provided standard.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The central claim 'no loss in link budget gain compared to spatial beamforming' rests on an unfair resource comparison. The temporal combining gain (T ≈ 18.375) is compared to N=16 antenna beamforming gain without charging MA-TISK for the proportionally longer integration time or lower effective symbol rate. This is a processing-gain-versus-beamforming-gain conflation.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identified this as the paper's most fundamental flaw. After steelman exchange, both confirmed RETRACTION-WORTHY. The comparison violates basic time-bandwidth-energy conservation: beamforming provides instantaneous power gain in one symbol period, while temporal combining spreads energy over T periods and coherently recombines. Without equal-resource normalization, the claimed equivalence is physically misleading. This is the paper's headline conclusion and it cannot be supported.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Misapplication of the Shannon capacity formula (Eqs. 9-10) to argue that loss in data rate and loss in beamforming gain are equivalent in a fixed-bandwidth system. The low-SNR approximation R ≈ SNR/ln(2) applies only in the wideband/infinite-bandwidth regime, not a fixed 100 MHz channel.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this error. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman, agreeing that this formula is essential to the paper's multiuser equivalence argument. In a fixed-bandwidth system, halving user rate does not halve required SNR in the linear way the paper claims. Since this argument underpins the conclusion that MA-TISK matches beamforming for multiuser scenarios, its invalidity removes support for a central claim.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The manuscript conflates received power gain, SINR gain, processing gain, and beamforming gain, risking systematic double-counting. The 'temporal combining gain' is presented as a replacement for beamforming gain rather than being recognized as processing gain from a lower-rate signaling format.

- **Arbiter justification for RW classification:**  
  > Both reviewers converged on this after steelman exchange. Reviewer A originally flagged it as RETRACTION-WORTHY; Reviewer B acknowledged in steelman that this was 'more coherent' than their scattered observations and elevated related findings. The failure to separate energy spreading, symbol duration expansion, noise bandwidth narrowing, and coherent recombination means the apparent gain may simply reflect resource reallocation rather than genuine link-budget equivalence.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The multi-machine extension (Section 4) claims Õ(n + d_max^m) time for constant m but provides no multidimensional data structure construction, no operation definitions, no complexity proofs. The result is asserted by analogy with the 1D case in a single paragraph.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently classified this as retraction-worthy. Neither downgraded during steelman. The paper claims a distinct theorem without supplying the central algorithmic object needed to state or analyze it. No cited multidimensional dynamic string structure exists with the required properties. This is not an exposition gap — it is a completely unsupported claim that constitutes a headline contribution of the paper.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The central subroutine BFS⁺ is never defined: no pseudocode, no formal detection rule, no specification of what data structures are maintained or what condition triggers triangle detection. The entire correctness and runtime of Theorem 2 depend on this undefined procedure.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently flag this as a critical gap. After steelman exchange, both converge on retraction-worthy severity. An algorithmic paper whose main claimed breakthrough delegates the key step to an unspecified subroutine does not establish its central result. This is not a presentation issue—without BFS⁺, the theorem is a conjecture, not a proven result. All downstream theorems inherit this failure.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The k-clique reduction (Theorem 4) has two independent fatal flaws: (1) the cost of constructing the auxiliary graph (enumerating all ℓ-cliques and checking all pairs for 2ℓ-clique formation) is omitted and can dominate the claimed runtime; (2) the auxiliary graph construction does not enforce disjointness or partition conditions on the three ℓ-cliques forming a triangle, so a triangle in the auxiliary graph may not correspond to a valid 3ℓ-clique in the original graph.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag the k-clique reduction as severely flawed. Review A identifies the construction cost omission; Review B identifies the missing disjointness condition. After steelman exchange, both agree this is retraction-worthy on multiple grounds. The standard Nešetřil-Poljak reduction requires careful partitioning that the manuscript omits, making the reduction potentially semantically incorrect, not just incomplete in runtime accounting.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Double-counting of redshift/flux effects: the paper adds an extra (1+z)^{-2} 'aberration correction' to the solid angle on top of the standard FLRW flux formula, which already includes two factors of (1+z)^{-1} (energy loss and arrival-rate dilation), yielding d_L ∝ (1+z)^2 r instead of the standard d_L ∝ (1+z) r.

- **Arbiter justification for RW classification:**  
  > The standard derivation from first principles (Boltzmann equation, Liouville's theorem, or direct FLRW geodesic computation) yields the correct (1+z)^{-4} surface brightness dimming without any missing beaming term for isotropic emission in the source rest frame. The additional (1+z)^{-2} factor is exactly the paper's novel quantitative result; if it is double-counting, the main conclusion is directly invalidated. Both reviewers identified this independently and both rated it retraction-worthy. Neither downgraded it during steelman.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Use of the SR Doppler formula (Eqs. 4–5) to define a recession speed β from cosmological redshift as if globally meaningful, then building the entire aberration correction from this inferred β.

- **Arbiter justification for RW classification:**  
  > The SR Doppler formula relates frequency shifts to relative velocity between inertial frames in flat spacetime. Cosmological redshift arises from metric expansion along the photon's path in curved spacetime—there is no unique 'velocity' that can be plugged into the SR formula to recover the aberration factor across cosmological distances. Since the rest of the derivation depends on this β, the main quantitative results do not follow. Reviewer A rated this retraction-worthy; Reviewer B subsumed it under the broader SR misapplication. It survived steelman.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The maximum-principle comparison in Proposition 3.1 is not justified. I_A is defined as an infimum over separating curves enclosing area A, not as a smooth scalar field satisfying a parabolic PDE in a spatial variable. The evolution equation (2.5) involves a second-derivative term ∂_r² ln I_A² whose sign is not controlled, and no subsolution/supersolution structure is established that would permit comparison with the spatially constant ODE barrier f(t). This is a categorical misapplication of the maximum principle.

- **Arbiter justification for RW classification:**  
  > Both reviewers flagged this as retraction-worthy. Reviewer B upgraded their confidence after the steelman exchange. Reviewer A's steelman reinforced the point by noting the conceptual mismatch between profile-level infima and pointwise PDE solutions. This proposition is the engine of the entire proof; its failure collapses the main theorem.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The contradiction argument in Theorem 3.2 uses asymptotic tightness of the isoperimetric lower bound (2.4) as A→0 in the wrong logical direction. Tightness means I_A² approaches the lower bound from above as A→0, but the proof requires choosing A small so that the lower bound exceeds an independently prescribed barrier—effectively using tightness to produce an upper bound on I_A², which does not follow. The 'contradiction' in (3.3) is therefore logically invalid.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this as retraction-worthy and maintained that assessment through the steelman exchange. The logical inversion is not a gap that could be filled with additional argument; it is a direct misuse of the asymptotic relationship. Without this step, exponential decay of κ(t) is unproven and the convergence theorem fails.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Theorem 3.3: The proof claims cl(K(βℤ,+)) is a left ideal in (βℤ*,⊙_t), but the key step — that the affine image t(t+1)−tn+(n−t)B is additively piecewise syndetic whenever B is — is unjustified and concretely fails when n=t, where the image collapses to a singleton. This theorem produces the ultrafilter intersection that drives all main partition-regularity results.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this as the critical bottleneck. Reviewer A initially rated it RETRACTION-WORTHY and maintained this through steelman. Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman, explicitly acknowledging the n=t counterexample. The degenerate case is concrete and undeniable, and no alternative argument is provided. Since Theorems 4.10, 4.11, and Corollary 4.12 all require the ultrafilter intersection that this theorem is supposed to produce, the central conclusions are unsupported.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Corollary 4.12 (and 4.14): The stated equation uses ⊙_{l,k} but the proof concludes with ⊕_{l,k}, which is undefined in the manuscript. The flagship partition-regularity claim — the paper's main advertised result — is not actually proved as written.

- **Arbiter justification for RW classification:**  
  > Reviewer A flagged this as RETRACTION-WORTHY and defended it through steelman (downgrading to MAJOR-REVISION in the spirit of charity, but noting it is 'certainly a serious presentation/theorem-statement defect'). Reviewer B identified the Corollary 4.12 operation mismatch as 'the single clearest fatal error.' The mismatch between the stated theorem and what the proof attempts to show means the paper's headline claim is literally unproved. While this could conceivably be a consistent notation error, ⊕_{l,k} is never defined, so the reader cannot determine what was intended.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The protocol's central constructions (bouncing identities, partial transpose implementation, noise polarization in Theorem 5, distillation in Corollary 6) all require ideal infinitely squeezed EPR states. No rigorous finite-squeezing error analysis is provided — no effective finite-r channel is derived, no error bounds (diamond norm, covariance level, or otherwise) are given, and no demonstration that the qualitative advantage survives at any finite resource level is presented. The paper's claims of a physically realizable Gaussian QEC/distillation protocol are therefore unsupported.

- **Arbiter justification for RW classification:**  
  > Both reviews independently identified this as RETRACTION-WORTHY. Review A considered downgrading to MAJOR-REVISION if the paper were reframed as a purely ideal-limit theorem, but as written the paper explicitly claims a protocol and practical circumvention of no-go results. The finite-squeezing discussion (Appendix G) provides only qualitative statements ('fidelity approaches 1 as r→∞') without any quantitative analysis. Since the paper's stated contributions are a protocol and operational circumvention claims — not merely a mathematical identity in an unphysical limit — the gap between what is proven and what is claimed is fundamental.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Lemma 3.7 conflates module-theoretic simplicity (every proper quotient is torsion) with simplicity in the HRS heart. The proof claims a nonzero map F → S must be a monomorphism 'by simplicity of F,' but F is lim→f-simple as a module, not simple in the heart. The deduction that F embeds into the torsionfree almost-torsion module B is the sole bridge from the direct limit construction to a single cogenerating brick, and it fails.

- **Arbiter justification for RW classification:**  
  > Reviewer A initially rated RETRACTION-WORTHY; Reviewer B initially rated MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman after recognizing the conceptual depth of the error. The conflation of two distinct notions of simplicity is structural, not a typo or missing citation. Without a valid embedding F ↪ B, the entire proof pipeline from the direct limit object to a single cogenerating brick collapses.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Theorem 3.2 (main multiplication formula) proof is incomplete and unvalidated for the stated setting. The proof is transplanted from GLS07 (preprojective algebra / 2-CY setting) without verifying that the required hypotheses (constructibility, stratification, Euler characteristic arguments, Ext-symmetry) hold for the infinite-dimensional Jacobian algebra A of a semi-infinite quiver. Critical steps between equations (3.9) and (3.16) are not established.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identify this as the paper's central result and both conclude its proof is not valid as written. This is not a matter of missing minor details—the entire argument framework depends on unverified assumptions about the algebraic and geometric setting. Without this theorem, the paper's main contributions collapse.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Proposition 4.3 (simplicity of L1⊗L2 iff Ext^1=0) contains a logically invalid or circular proof. The proof assumes that vanishing Ext implies the product of F-polynomials equals a single cluster monomial, which is what needs to be proved. The contradiction argument for the 'only if' direction unjustifiably assumes all summands Y in the multiplication formula must equal T.

- **Arbiter justification for RW classification:**  
  > Both reviewers agree the proof is flawed. This proposition is the key bridge between the multiplication formula and the paper's advertised application to quantum affine algebra representations. A logically invalid proof of a central application-level result means the paper's conclusions about tensor product simplicity are unsupported.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Lemma 4.5 is not proved: the proof consists of an unsupported assertion and an editorial placeholder '[AUTHOR_1]'. This lemma is the key technical input to Theorem 2.1, establishing the limiting constant α that determines the explicit eigenvalue formula.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identify this as RETRACTION-WORTHY. Neither downgraded during steelman. The manuscript literally does not contain a proof of the lemma on which the central theorem depends. Without Lemma 4.5, Theorem 2.1's explicit formula is unsubstantiated, and all downstream results (Corollary 2.2, Theorem 2.3) collapse.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The transition from conditioning on {S_n ∈ D} (Lemma 4.4) to conditioning on full path survival {S_k ∈ D for all 1 ≤ k ≤ n} (Lemma 4.5) is unjustified. These are fundamentally different conditioning events, and no bridging argument is provided.

- **Arbiter justification for RW classification:**  
  > Both reviewers identify this gap. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman, recognizing it is the core inferential step identifying the constant α. The path-conditioned law and endpoint-conditioned law are genuinely different objects, and this is not a routine epsilon-delta detail but a change of conditioning sigma-field central to the argument.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The lower bound derivation in the proof of Theorem 2.1 requires uniform convergence (in x and eventually in n) of the conditional probability from Lemma 4.5 to iterate into an exponential bound, but only pointwise convergence is claimed (and not even proved).

- **Arbiter justification for RW classification:**  
  > Reviewer B identifies this initially as MAJOR-REVISION but upgrades to RETRACTION-WORTHY during steelman, since without uniform control the exponential asymptotics cannot be extracted. Reviewer A agrees in steelman. Since the theorem is central, the compounding of this gap with the unproven Lemma 4.5 makes it fatal.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Theorem 6.3 / Proposition 6.2: The noncommutative μ-vanishing result claims μ_G(S(E/K_∞)^∨) = μ_Γ(S(E/K_cyc)^∨) via a restriction map whose kernel is finite and cokernel cofinitely generated. The equality of μ-invariants from such a map is not justified; the cited references ([CSS03b], [Pal14]) address number fields, not function fields, and the required finiteness/cofiniteness is not proven in this setting.

- **Arbiter justification for RW classification:**  
  > Review B rates this retraction-worthy; Review A initially rated it major-revision but upgraded to retraction-worthy after steelman. The μ_G = μ_Γ equality is the sole logical bridge to the main conclusion of Part II (ℓ ≠ p case). Without it, the headline noncommutative result is entirely unsupported. The gap is not a missing detail but a missing proof of the key step, using references whose hypotheses are not verified in the function-field setting.

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

- **GD finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > Theorem 1.5/6.3 contains a contradiction: the abstract and introduction advertise results for a GL₂(Zₗ)-extension, but the theorem statement requires G = Gal(K_∞/K) to be pro-p. An open subgroup of GL₂(Zₗ) is not generally pro-p (for ℓ ≠ p), so the paper does not prove what it claims at the headline level.

- **Arbiter justification for RW classification:**  
  > Review A flags this as retraction-worthy; Review B did not initially catch it but after steelman recognized it as a severe overstatement. The paper's main selling point is extending results to the noncommutative GL₂(Zₗ) setting. If the proof only works for pro-p groups (a drastically more restrictive class), then the claimed result is materially overstated. However, there is some possibility the authors intended a pro-p quotient or open pro-p subgroup, which would make this a major misstatement of generality rather than total invalidity of a restricted result. Retained at retraction-worthy because the discrepancy is between the paper's central advertised contribution and what the proof actually establishes.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The asymptotic gate count is internally self-contradictory. The paper claims O(log(1/ε) log log(1/ε) log log log(1/ε)···) in one place but O(ε log(1/ε) log log(1/ε)···) elsewhere; the latter decreases with smaller ε, which is impossible for a compilation cost. The definition m = ceil(ε / [log(1/ε) log log(1/ε)···]) has the wrong scaling direction (m→0 as ε→0 instead of growing). The iterated-log product is mathematically ill-defined with no specified termination. The precision budget δ ≤ ε/⌈log₂(1/ε)⌉ is inconsistent with the claimed product-of-logs scaling.

- **Arbiter justification for RW classification:**  
  > The paper's principal contribution is a quantitative upper bound on gate count. Both reviewers independently identified that this bound is self-contradictory, and the steelman exchange strengthened rather than weakened this finding. An internally inconsistent complexity formula means the main theorem as stated is not a valid mathematical claim. Neither reviewer downgraded this finding.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The manuscript does not solve the stated problem of approximation from a fixed finite gate set. The theorem explicitly uses a gate set depending on ε (including {P(πℓ/2^m)} where m grows with 1/ε), and the discussion appeals to hardware-native arbitrary phase rotations P(α). This contradicts the introduction's framing as addressing the Nielsen-Chuang challenge for fixed-set approximation complexity.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this issue. Reviewer A initially rated it RETRACTION-WORTHY; Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman exchange. Reviewer A acknowledged in steelman that under an honest reframing (e.g., ε-dependent instruction library) the mathematics might be partially salvageable, suggesting some uncertainty. However, as the paper is written, the central claim addresses a problem it does not actually solve. The mismatch between problem statement and solution is fundamental.

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

- **GD finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The fault-tolerance claim is not established under standard FT assumptions. The recursive scheme requires implementing P(α v_j) transversally on physical qubits for arbitrary non-Clifford angles. These are not available as fault-tolerant operations from a fixed protected gate set in the standard model. The paper's appeal to hardware-native arbitrary rotations undermines the FT compilation framework rather than establishing it. No error propagation, threshold, or concatenation analysis is provided.

- **Arbiter justification for RW classification:**  
  > Reviewer A rated this RETRACTION-WORTHY throughout. Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman, finding Reviewer A's argument about physical rotation availability compelling. However, there is some residual uncertainty: if the work were repositioned as an architecture-specific proposal rather than a standard FT compilation theorem, the underlying idea might survive in weakened form. Given the paper's current claims, the severity is retraction-level.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Method-results mismatch: The only concrete methodology described is a simple elbow-angle calculation and threshold-based curl counter using unmodified MediaPipe landmarks. The paper claims architectural and algorithmic improvements to MediaPipe pose estimation itself, including 20% IoU improvement and enhanced robustness. A downstream rule-based application cannot produce or evidence improvements to the underlying pose estimation model.

- **Arbiter justification for RW classification:**  
  > This is a logical contradiction, not merely a reporting gap. Even if all missing experimental details were supplied, the described method (angle thresholding on existing landmarks) cannot constitute or demonstrate an improvement to MediaPipe's pose estimation architecture. Both reviewers identify this, and both maintained or strengthened this finding through steelman exchange. Reviewer A defended it as RETRACTION-WORTHY; Reviewer B recognized it as the most fundamental problem and elevated its importance.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Primary performance claims (20% IoU improvement, ~30% processing-time reduction) are unsupported by any presented quantitative evidence. No results table, no numerical data points, no sample sizes, no confidence intervals, no variance estimates, and no statistical tests are provided.

- **Arbiter justification for RW classification:**  
  > The paper's central conclusions are headline numerical claims for which zero supporting data is presented. Reviewer A defended this as RETRACTION-WORTHY through steelman; Reviewer B agrees these claims are meaningless without evidence. Under the severity standard, the central conclusions cannot be supported by the data as presented because no data is presented.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The claimed 'novel modifications' and 'advanced neural network architectures' incorporated into MediaPipe are never described. No architecture details, layer modifications, training procedures, loss functions, hyperparameters, or optimization changes are specified.

- **Arbiter justification for RW classification:**  
  > The paper's claimed methodological novelty—the core contribution—is entirely undefined. This is more than a reporting gap: combined with the method-results mismatch, there is no evidence that any architectural modification exists. Reviewer A downgraded this to MAJOR-REVISION in steelman, acknowledging it could theoretically be a reporting omission. However, Reviewer B's steelman correctly notes that the described method (inference-only angle calculation) is logically incompatible with the existence of such modifications, pushing this back toward RETRACTION-WORTHY. On balance, the combination of undefined contribution plus contradictory method description makes this RETRACTION-WORTHY.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The topology proof of Lemma 3 (χ(M^+)=1) is not rigorous. The argument claims coordinate projections induce fibrations with contractible fibers, but no local triviality, continuity of fiber type, or explicit deformation retracts are provided. Fiber descriptions ('quarter of a ring belt,' 'quarter of a circle') are informal and the fiber type changes at boundaries, which is incompatible with a fibration structure.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently rate this retraction-worthy and neither downgrades it during steelman. Lemma 3 is the sole global topological input to the Morse equation; if χ(M^+)≠1, the uniqueness conclusion α₀=1 does not follow. The gaps are not minor omissions but fundamental: the claimed fibrations are not verified, and the informal geometric descriptions do not constitute a proof of contractibility. Reviewer B's steelman observation that fiber type changes at boundaries reinforces that this cannot be trivially repaired.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The manuscript does not prove that critical points of U on the enlarged set M^+ lie within the geometrically realizable planar convex quadrilateral set C. The final step 'Since C ⊂ M^+, U has at most one critical point on C' is logically valid for an upper bound, but the paper does not establish that the unique critical point on M^+ (if it exists) belongs to C, nor does it properly invoke an external existence result to close the argument.

- **Arbiter justification for RW classification:**  
  > Reviewer A rated this retraction-worthy; during steelman, A considered downgrading to major-revision if the paper is read as proving only an upper bound combined with external existence results. However, Reviewer B fully endorsed A's original severity. The issue is that uniqueness on a superset does imply at most one on a subset, which partially works, but the paper's own theorem statement claims existence-and-uniqueness for given angle θ, and the existence part is not established within the paper's framework. Since the theorem as stated is not supported without this step, and the manuscript does not clearly separate 'at most one' from 'exactly one,' this remains retraction-worthy, though with slightly lower confidence.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > The constraint C(r)=0 is only a necessary condition for convex quadrilateral configurations (as the authors acknowledge via Josefsson's relation), not sufficient. The Morse-theoretic uniqueness argument is performed on M^+ = {I=I₀, C=0, r_ij>0}, which is strictly larger than the actual configuration set. The proof does not establish that the critical point structure on this enlarged set faithfully represents the original geometric problem.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this as a core issue. During steelman, Reviewer A considered that this might be major-revision if the authors could prove an exact critical-point correspondence on the realizable locus, but acknowledged this would require a 'nontrivial new argument.' Reviewer B's steelman strengthened this by noting the factorization F₄=C·A is only established on the geometric set where C=0 already holds, making the constraint replacement potentially circular. The combination of the enlargement problem with the circularity of the factorization makes this retraction-worthy.

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

- **GD finding (rated RETRACTION-WORTHY, finding #3):**  
  Location:   
  > The mass-deformation argument ('we can only consider the equal mass case since the Euler characteristic number is invariant under continuous deformations') is invalid as stated. Euler characteristic is invariant under homeomorphism/homotopy equivalence, not under arbitrary continuous parameter changes in defining equations. No deformation retract, homotopy equivalence, or topological triviality of the family is established.

- **Arbiter justification for RW classification:**  
  > Both reviewers initially rated this major-revision, but both upgraded to retraction-worthy during steelman. The argument is essential: without it, the topology calculation (even if correct for equal masses) does not extend to arbitrary positive masses, and the main theorem for general masses is unsupported. Bifurcations or topology changes under mass variation are plausible and not excluded. Since the theorem is stated for 'given four positive masses,' this gap is fatal to the generality claim.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Lemma 2.1.10 (extension lemma): The proof that a holomorphic form extends across the discriminant divisor contains a gap in the pole-order analysis. The argument that h has at worst a simple pole, combined with the pullback calculation f*(dt/t) = k ds/s, does not rule out cancellation that would make the pulled-back form holomorphic even when h has a pole. If this lemma fails, the isomorphism Ω_B^{[1]} ≅ π_*T_{X/B} (Theorem 2.1.11) is unproven, and the entire Shafarevich-Tate group construction and twisting formalism collapse.

- **Arbiter justification for RW classification:**  
  > This isomorphism is the foundational identification used throughout the paper — in defining the Shafarevich-Tate group, in the twisting construction, and in all cohomological calculations about twists. Reviewer B identified this and Reviewer A acknowledged in steelman that this is plausibly retraction-worthy. The pole-order argument as written is genuinely incomplete. However, confidence is 0.80 rather than higher because the correct result might follow from a more careful analysis or alternative argument not presented.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > Theorem 5.2.7 does not prove dim H^0(X^φ, Ω^2) = 1. The proof identifies H^{2,0}(X^φ) with H^0(End'(Ω_B^{[1]})) and argues independence under twisting, but never computes the dimension for any specific twist (including the untwisted hyperkähler X). Independence of dimension across twists is insufficient without an anchor computation.

- **Arbiter justification for RW classification:**  
  > This is the core proof of Theorem B's first assertion (Hodge numbers of twists). Reviewer A identified this; Reviewer B upgraded to RETRACTION-WORTHY during steelman. The logical gap is clear: twist-invariance ≠ computation. The dimension for the untwisted case is known (it's 1 for hyperkähler), so the fix may be straightforward — but as written, the theorem's conclusion does not follow from its proof. The high severity reflects that Theorem B is a headline result and this gap is not merely expository.

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

- **GD finding (rated RETRACTION-WORTHY, finding #2):**  
  Location:   
  > Theorem D (5.3.12): The proof confuses 'Fujiki class C' (bimeromorphic to a Kähler manifold) with 'admits a rational map to a Kähler manifold' and then attempts to pull back a Kähler form along such a rational map. This is a category error: pullback of a Kähler form under a rational map is not defined without resolving indeterminacies, and the subsequent claim that the restriction to a general fiber of π^φ is birational onto its image is unjustified.

- **Arbiter justification for RW classification:**  
  > Reviewer A identified this as retraction-worthy; Reviewer B upgraded to the same during steelman, acknowledging the conceptual error. The proof of Theorem D as written does not establish the theorem from its hypothesis. This is not a gap that can be filled by adding a sentence — the entire proof strategy is based on a mischaracterization of Fujiki class C. Theorem D is one of the paper's four headline results.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The proof that m(x'Q(x),∞) = O(1) for algebraic integers (Theorem 1.4) and simple numbers (Theorem 1.5) is mathematically incoherent. The argument conflates m(y,0), h(y), N(y,0), and m(y,∞) in an invalid identity chain, and the appeal to Dirichlet's unit theorem to bound Archimedean absolute values of an arbitrary algebraic integer y is unjustified. Without this bound, the main error term in inequality (14)/(19) is uncontrolled and Theorems 1.4 and 1.5 are unproved.

- **Arbiter justification for RW classification:**  
  > Both reviewers independently identified this as the single most critical failure. This step is the lynchpin of the entire proof chain — if it fails, the paper's central claimed inequalities (11) and (12) have no valid derivation. The reasoning presented is not a gap that could be filled; it is logically incoherent as written.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The construction of x' is not rigorously specified to be independent of x, yet the proof framework requires a fixed x'. The manuscript's own Remark reveals that the construction depends on the factorization of x and x−a_j, making x' depend on x. Without a valid x-independent construction ensuring the required integrality and valuation properties, the deduction of the main theorems from Theorem 2.1 collapses.

- **Arbiter justification for RW classification:**  
  > Both reviewers flag this. If x' depends on x, inequality (14) is not the fixed inequality it purports to be, and the entire argument structure is invalidated. Review A provides the more detailed analysis showing the dependency, while Review B notes the missing link between the algebraic construction and the analytic estimate. Neither reviewer sees a way to repair this within the manuscript's framework.

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

- **GD finding (rated RETRACTION-WORTHY, finding #4):**  
  Location:   
  > The derivation of inequality (15) contains an indexing/aggregation error where the right-hand side depends on a single j while the left-hand side sums over all j. The subsequent averaging to define S_{x'}(x) does not resolve this mismatch.

- **Arbiter justification for RW classification:**  
  > Review A identifies this specifically; Review B covers it implicitly under general proof incompleteness. This is inside the core derivation chain. However, there is some possibility this is a notational/expository error that could be clarified (e.g., the inequality might hold for each j separately and then be summed). Given some residual uncertainty about whether this is a true logical error versus a presentation error, confidence is slightly lower, but it is still classified as retraction-worthy because as written the derivation does not work.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > The manuscript conflates two distinct methods (MSP-MVS and TSAR-MVS) with different pipelines, different contributions, and different algorithmic components, making it impossible to determine what method was actually implemented, evaluated, and reported on.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this independently. Review A upgraded to RETRACTION-WORTHY after steelmanning. The title/abstract/conclusion describe MSP-MVS (segmentation prior, anchor equidistribution, ILS), while a substantial central section describes TSAR-MVS (confidence filtering, superpixel-RANSAC, Roberts+Hough segmentation). This is not a local typo or naming inconsistency — it represents an identity failure of the object under study. The central conclusions ('our method achieves SOTA') cannot be supported because the manuscript does not establish which method produced the data. This meets the RETRACTION-WORTHY definition: the paper's central conclusions cannot be supported by the data as presented.

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

- **GD finding (rated RETRACTION-WORTHY, finding #1):**  
  Location:   
  > The ablation study components (w/o. SAM, w/o. Her, w/o. Agr., w/o. CRF., w/o. Equ., etc.) do not map cleanly onto either method description, making the causal evidence for the paper's claimed contributions uninterpretable.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this. The ablations are supposed to establish which components drive performance, but if the evaluated system includes modules from both MSP-MVS and TSAR-MVS pipelines (or only one, but it's unclear which), the ablation evidence is logically disconnected from the stated contributions. Review A upgraded this to borderline RETRACTION-WORTHY after steelmanning. Combined with the identity-confusion finding, this collapses the paper's mechanistic claims.

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

- **GD finding (rated RETRACTION-WORTHY, finding #0):**  
  Location:   
  > Lemma 2.3 contradiction step: The proof conflates set sums and intersections. The claim '((x+V') + (y+V')) = ∅' for distinct x,y in L is mathematically impossible (sums of nonempty subsets are never empty); the intended statement should involve intersections. This occurs at the exact step where the disjointness of translates must be established for the Zorn's lemma / maximality argument to work. Without a valid proof of this lemma, the special neighborhood U with the required separation and density properties is not constructed.

- **Arbiter justification for RW classification:**  
  > Both reviewers identified this as the central fatal error. Both maintained RETRACTION-WORTHY severity through steelman. The error is not merely typographical—it occurs at the critical logical step of the key lemma, and the surrounding argument does not make the intended reasoning recoverable. Since Theorem 1.1 depends entirely on Lemma 2.3, the paper's main conclusion is unsupported. Reviewer B acknowledged in steelman that this could conceivably be MAJOR-REVISION if the authors can supply a corrected proof, but as written the argument is broken.

- **Human verdict** (mark one):  
  - [ ] VALID SEVERE — genuine error, SPOT missed it  
  - [ ] RELATED — real issue but severity overstated  
  - [ ] FALSE ALARM — not a genuine severe error  

- **Notes:** _______________________________________________

---

