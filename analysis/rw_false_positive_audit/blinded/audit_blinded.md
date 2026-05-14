# Blinded peer-review audit

264 candidate findings, randomly shuffled.

See the cover page of the PDF for instructions, or the README for context. Record verdicts in `audit_blinded.csv`.

---

### F001

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The application of Dirichlet's unit theorem to conclude m(y, 0) = O(1) is invalid as presented. The claimed uniform comparability |y|_v ≤ c(κ)|y|_w for arbitrary algebraic integers y and Archimedean places v, w does not hold without unit normalization. Even with such normalization, the bound would depend on y, not just on κ. This is the final step in proving Theorem 1.4.

**Arbiter's justification:**
> Both reviewers flag this independently. This is the concluding step that converts auxiliary estimates into the main theorem. Without a valid argument here, the proof of Theorem 1.4 fails at its conclusion.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F002

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> The converse direction of Lemma 4 incorrectly derives an orthogonal representation from a zero-error quantum protocol by selecting an arbitrary eigenvector from each mixed state.

**Arbiter's justification:**
> Zero-error distinguishability requires orthogonal supports only for confusable pairs (edges of G^(m)), not for all edges of the complement graph as claimed. Furthermore, extracting a single eigenvector from each mixed state does not preserve the pairwise orthogonality structure needed for an orthogonal representation. This gap invalidates the converse of Lemma 4, which is the basis for the quantum rate characterization R_quantum = inf_m (1/m) log ξ(G^(m)) in Theorem 4. Reviewer A provides detailed technical justification; Reviewer B concurs there is a gap. While there might exist a correct proof via a different argument (e.g., Nayak-type arguments or purification), the proof as written is invalid.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F003

- Paper: *Shafarevich-Tate groups of holomorphic Lagrangian fibrations II*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> There is likely a mistake in the formulation or derivation of equations related to Kähler twists, such as an incorrect application of properties of Kähler manifolds or errors in twisting procedures within the proof.

**Candidate finding (rated retraction-worthy):**
> Lemma 2.1.10 (extension lemma): The proof that a holomorphic form extends across the discriminant divisor contains a gap in the pole-order analysis. The argument that h has at worst a simple pole, combined with the pullback calculation f*(dt/t) = k ds/s, does not rule out cancellation that would make the pulled-back form holomorphic even when h has a pole. If this lemma fails, the isomorphism Ω_B^{[1]} ≅ π_*T_{X/B} (Theorem 2.1.11) is unproven, and the entire Shafarevich-Tate group construction and twisting formalism collapse.

**Arbiter's justification:**
> This isomorphism is the foundational identification used throughout the paper — in defining the Shafarevich-Tate group, in the twisting construction, and in all cohomological calculations about twists. Reviewer B identified this and Reviewer A acknowledged in steelman that this is plausibly retraction-worthy. The pole-order argument as written is genuinely incomplete. However, confidence is 0.80 rather than higher because the correct result might follow from a more careful analysis or alternative argument not presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F004

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> Theorem 1.5 uses the undefined notion of 'simple number' and claims, for q = 2, that y = 1/(x'Q(x)) is an algebraic integer by the same (already unproved) argument. The definition is not shown to be preserved under the relevant transformations, making Theorem 1.5 unverifiable.

**Arbiter's justification:**
> Theorem 1.5 is the bridge to the abc-conjecture corollary (Theorem 1.6). Both reviewers note the undefined terminology and the reliance on the same flawed integrality argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F005

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The paper's CMB prediction—that aberration spreads small-scale anisotropies by a factor ~(1+z)^2 ≈ 10^6 for z~1000, making the CMB appear more homogeneous—is directly contradicted by Planck observations of sharp acoustic peaks up to ℓ ~ 2500.

**Arbiter's justification:**
> This is a specific, quantitative prediction that is falsified by observational data. A factor 10^6 spread in solid angle would completely wash out the observed acoustic peak structure of the CMB power spectrum. Reviewer B correctly identifies this as observational falsification. Reviewer A initially rated this MINOR (as downstream of the already-fatal core error) but acknowledged potential upgrade. As the paper presents this claim as physical support for its mechanism rather than pure speculation, it constitutes an independently falsifiable prediction that fails.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F006

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> In Part II (Theorem 1.5/6.3 and §6), the Galois group G=Gal(K_∞/K) is simultaneously described as an open subgroup of GL_2(Z_ℓ) and as pro-p, which is incompatible when ℓ≠p. This misidentification affects the Iwasawa algebra Λ(G), the definition of μ_G, and all transfer arguments.

**Arbiter's justification:**
> The entire noncommutative Iwasawa-theoretic framework in Part II is built on the structure of G. If G is misidentified, the completed group ring, the M_H(G) condition, and the μ-invariant comparisons are set in the wrong category. This directly invalidates Theorem 1.5/6.3.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F007

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 1.4 claims that y = 1/(x'Q(x)) is an algebraic integer for algebraic integer x. This integrality claim is not established: the construction of x' via ideals a_0 and a_∞ is incomplete, and the divisibility x' | ∏_j(x − a_j) in the ring of integers is never verified. Without integrality, the crucial conclusion m(x'Q(x),∞) = O(1) does not follow.

**Arbiter's justification:**
> Both reviewers identify this as essential to the proof of Theorem 1.4. The integrality claim is what eliminates the extra error term and yields the main result. Reviewer A provides a detailed explanation of why the claim is unproved; Reviewer B notes the circularity when attempting to extend to all algebraic numbers.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F008

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The probabilistic analysis claiming error probability ≤ 10^{-30} is unsupported. The sampling calculation (exp(-70)) is mathematically valid in isolation, but it is irrelevant because it only bounds the probability of landing in A, not the probability of detecting a triangle given landing in A. The latter probability is unproved.

**Arbiter's justification:**
> Both reviewers note that the error bound depends on the unproved detection guarantee. Reviewer B additionally raises concerns about the independence assumptions and parameter regimes. The advertised high-probability guarantee is the basis for the algorithm's claimed correctness, so its failure is fatal to the main theorem.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F009

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> Lemma 2.3 contains incorrect or incoherent set-theoretic/group-theoretic computations: sums and intersections are conflated, and the claimed disjointness (x+V')∩(y+V')=∅ is not correctly derived from the preceding expressions involving x+x+U_x and y+y+U_y in a Boolean group.

**Arbiter's justification:**
> Reviewer A identifies that the displayed computation is internally inconsistent. While in a Boolean group x+x=0, so x+x+U_x = U_x, the leap to the claimed disjointness of translated sets is not logically justified. This compounds the other errors in Lemma 2.3. Confidence is slightly lower because some of this might be a notational issue, but the mathematical content as written is incorrect.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F010

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> Lemma 2.3 contradiction step: The proof conflates set sums and intersections. The claim '((x+V') + (y+V')) = ∅' for distinct x,y in L is mathematically impossible (sums of nonempty subsets are never empty); the intended statement should involve intersections. This occurs at the exact step where the disjointness of translates must be established for the Zorn's lemma / maximality argument to work. Without a valid proof of this lemma, the special neighborhood U with the required separation and density properties is not constructed.

**Arbiter's justification:**
> Both reviewers identified this as the central fatal error. Both maintained RETRACTION-WORTHY severity through steelman. The error is not merely typographical—it occurs at the critical logical step of the key lemma, and the surrounding argument does not make the intended reasoning recoverable. Since Theorem 1.1 depends entirely on Lemma 2.3, the paper's main conclusion is unsupported. Reviewer B acknowledged in steelman that this could conceivably be MAJOR-REVISION if the authors can supply a corrected proof, but as written the argument is broken.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F011

- Paper: *Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

**Candidate finding (rated retraction-worthy):**
> MTT assay on particulate hydroxyapatite lacks essential interference controls (particle-only blanks, optical correction for scattering/absorption by HAp, dye adsorption checks). The reported absorbance values may reflect material artifacts rather than cell viability.

**Arbiter's justification:**
> Calcium phosphate particles are well-known to interfere with colorimetric assays. Without particle-only wells and interference validation, the optical density readout is uninterpretable. Since the entire biocompatibility claim rests on this single assay, the conclusion is fundamentally unsupported. Reviewer A identified and strongly defended this; Reviewer B recognized it as an additional independent retraction rationale during reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F012

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> The Horodecki CHSH nonlocality criterion is invariant under party exchange (A↔B swap), making 'swap-intolerant nonlocality' impossible within the standard bipartite formalism. Swapping parties sends T→T^T, but the eigenvalues of T^T T are identical to those of TT^T, so the Horodecki quantity M is unchanged. The paper's central concept is therefore mathematically incoherent.

**Arbiter's justification:**
> This is a theorem-level impossibility result: no 2-qubit operator (positive or not) can have its CHSH nonlocality status change under party relabelling when assessed via the Horodecki criterion. The paper's main theorem directly contradicts this mathematical fact. This is not a matter of interpretation or methodology—it is a fundamental error that renders the central conclusion unsupportable.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F013

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript treats the ideal gas law (PV=nRT) as a predictive theory of planetary surface temperature and uses it to argue that the greenhouse effect is 'very small or non-existent.' The ideal gas law is an equation of state, not an energy-balance equation, and cannot determine equilibrium temperature without independent radiative and thermodynamic constraints.

**Arbiter's justification:**
> This is a foundational category error in atmospheric physics. The manuscript uses it as the core mechanistic basis for rejecting the greenhouse effect. Both reviewers independently rate this RETRACTION-WORTHY and defend the rating through reflection. The error is not a simplification or approximation—it is the application of the wrong physical framework to the central question. No revision can rescue a conclusion built on this premise without abandoning the premise itself.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F014

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Identification of methylene blue and malachite green in real textile wastewater relies solely on visual matching of UV-Vis peaks without chromatographic or standard-addition validation. Real textile effluent contains numerous chromophores with overlapping absorbance bands.

**Arbiter's justification:**
> The paper's central applied claim is that SBT-AgNPs remove specific named dyes (MB, MG) from textile wastewater. Without selective analytical confirmation (HPLC, LC-MS, spiking/recovery), assigning peaks at ~614 and ~665 nm to those specific dyes in a complex matrix is circular reasoning. If the dyes are not confirmed, the core conclusion collapses. Review A rated this RETRACTION-WORTHY; Review B effectively agreed during steelman. Review A partially softened this during steelman but only if the paper were reframed to 'nonselective decolorization'—which it is not. As written, the named-dye wastewater claim is central and unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F015

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The mass-deformation argument ('we can only consider the equal mass case since the Euler characteristic number is invariant under continuous deformations') is invalid as stated. Euler characteristic is invariant under homeomorphism/homotopy equivalence, not under arbitrary continuous parameter changes in defining equations. No deformation retract, homotopy equivalence, or topological triviality of the family is established.

**Arbiter's justification:**
> Both reviewers initially rated this major-revision, but both upgraded to retraction-worthy during steelman. The argument is essential: without it, the topology calculation (even if correct for equal masses) does not extend to arbitrary positive masses, and the main theorem for general masses is unsupported. Bifurcations or topology changes under mass variation are plausible and not excluded. Since the theorem is stated for 'given four positive masses,' this gap is fatal to the generality claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F016

- Paper: *Shafarevich-Tate groups of holomorphic Lagrangian fibrations II*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> There is likely a mistake in the formulation or derivation of equations related to Kähler twists, such as an incorrect application of properties of Kähler manifolds or errors in twisting procedures within the proof.

**Candidate finding (rated retraction-worthy):**
> Theorem 5.2.7 does not prove dim H^0(X^φ, Ω^2) = 1. The proof identifies H^{2,0}(X^φ) with H^0(End'(Ω_B^{[1]})) and argues independence under twisting, but never computes the dimension for any specific twist (including the untwisted hyperkähler X). Independence of dimension across twists is insufficient without an anchor computation.

**Arbiter's justification:**
> This is the core proof of Theorem B's first assertion (Hodge numbers of twists). Reviewer A identified this; Reviewer B upgraded to RETRACTION-WORTHY during steelman. The logical gap is clear: twist-invariance ≠ computation. The dimension for the untwisted case is known (it's 1 for hyperkähler), so the fix may be straightforward — but as written, the theorem's conclusion does not follow from its proof. The high severity reflects that Theorem B is a headline result and this gap is not merely expository.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F017

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript claims the greenhouse effect is 'fictitious' and that planetary surface temperatures are explained by the ideal gas law alone, without radiative transfer considerations.

**Arbiter's justification:**
> This contradicts over a century of experimentally verified atmospheric physics. The ideal gas law relates state variables and cannot determine a planet's energy balance or equilibrium temperature without radiative constraints. This error is central to the paper's thesis and invalidates its core physical argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F018

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Specific dyes (methylene blue, malachite green) in real textile wastewater are identified and quantified solely from broad UV-Vis absorbance features without chromatographic separation, standard addition, spiking recovery, or matrix-validated calibration.

**Arbiter's justification:**
> The paper's headline applied conclusion—removal of named dyes from real textile wastewater—depends entirely on assigning broad UV-Vis peaks at ~614 and ~665 nm to malachite green and methylene blue in a complex, multicomponent matrix. Without any orthogonal analytical confirmation, the analyte identity is unestablished. If the identity is wrong, the central wastewater conclusion collapses. New primary data (e.g., HPLC/LC-MS) would be required, not just reanalysis.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F019

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Pharmacokinetic parameters are internally contradictory and mathematically inconsistent. Elimination half-lives do not match reported elimination rate constants via t½ = ln(2)/k (e.g., k = 0.01 h⁻¹ should give t½ ≈ 69 h, not 0.94 h). Reported half-lives include physiologically implausible values (plasma t½ = 3368.24 h ≈ 140 days). The same tissue (gill) appears with contradictory half-life values (0.94 h, 198.48 h, 19.39 h) in different sections. Tmax/Cmax values contradict between abstract, tables, and text.

**Arbiter's justification:**
> The pharmacokinetic characterization is the manuscript's primary contribution. When half-lives, rate constants, Tmax, and Cmax values are mutually contradictory and mathematically inconsistent, no reliable PK profile can be extracted. These are not borderline discrepancies but order-of-magnitude contradictions that cannot be resolved by the reader. Both reviewers identified this as retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F020

- Paper: *From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

**Candidate finding (rated retraction-worthy):**
> The degenerate step augmentation (Section 3.2) does not rigorously justify that BFS-layering properties are preserved after adding new vertices and edges, and does not explain how augmented vertices are removed to obtain results for the original graph.

**Arbiter's justification:**
> Both reviewers flag this independently. Reviewer B notes that adding edges (t2,vy) and (t3,vy) where t2,t3 are on higher layers can violate BFS-layering span requirements. Reviewer A notes the lack of a projection argument back to the original graph. The degenerate step is part of the iterative construction for Theorem 1.2, the core structural result. If augmentation breaks the BFS-layering or if results cannot be transferred back to the original graph, the main theorem is unsupported. However, such augmentation techniques are standard in the graph structure literature and may be justifiable with more careful exposition, so there is some chance this is repairable.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F021

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Use of the seasonal cycle in the Keeling curve and COVID-era emission reductions as evidence against long perturbation lifetimes for anthropogenic CO₂.

**Arbiter's justification:**
> Both reviewers flag this. Seasonal exchange around a rising trend tests exchange rates, not perturbation lifetime. COVID-era reductions (~7%) would produce a signal smaller than natural variability against the background trend. These arguments are physically invalid and are used to dismiss mainstream carbon-cycle understanding.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F022

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> Lemma 2.3 contradiction step: W := U ∪ V' is claimed to be an identity neighborhood in the poset, but V' is constructed as a nonempty open subset of V, not necessarily containing 0_G. Thus W need not be an identity neighborhood, and the maximality contradiction collapses.

**Arbiter's justification:**
> This is a distinct error within the same lemma. The contradiction that would establish property (2) depends on W being in the poset, which requires W to be a neighborhood of 0. If V' does not contain 0, this fails. Reviewer A's analysis is specific and convincing.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F023

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript treats human breathing as a net source of atmospheric CO2 (~0.1638 ppmv), comparing it to fossil fuel emissions to argue the latter are trivial. Human respiration is part of a closed biogenic carbon loop and represents zero net addition to atmospheric CO2.

**Arbiter's justification:**
> Reviewer B identifies this as a 'high-school level error' and rates it RETRACTION-WORTHY; Reviewer A addresses it under the broader category of unsupported sector-level conversions (MAJOR-REVISION). The error is elementary: carbon in food originates from recent atmospheric CO2 via photosynthesis, so exhaling it returns it to the atmosphere with no net change. Using this as a comparator to minimize fossil fuel emissions (which release geologically sequestered carbon) demonstrates a fundamental misunderstanding of the carbon cycle. Given that it directly supports the paper's claim of anthropogenic insignificance, RETRACTION-WORTHY is appropriate.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F024

- Paper: *A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

**Candidate finding (rated retraction-worthy):**
> Unjustified sensitivity claim in Lemma 3.2 / Appendix A for the tree-release primitive. The proof claims that releasing distances from root to centroid and centroid to children has global ℓ1 sensitivity 1 because subtrees are disjoint. However, disjoint subtrees do not imply edge-disjoint paths: a single edge perturbation can affect multiple released distances simultaneously. The true sensitivity could be O(log n) or more.

**Arbiter's justification:**
> This primitive is used in every main theorem (Theorems 3.1, 3.2, 4.1–4.4). The paper's own proof is clearly invalid—the logical step from subtree disjointness to sensitivity 1 does not hold. If the true sensitivity is higher, the required noise scale increases, which would change both the privacy guarantees and the error bounds. While Reviewer A suggested this might be salvageable by importing an external result, the paper as written provides no valid privacy analysis for its most fundamental building block, and any fix could change the quantitative conclusions. This crosses the retraction threshold because every main theorem depends on it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F025

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> Evaluation metrics are inappropriate or inadequately defined for human pose estimation. IoU and MSE are used without defining what is being compared (keypoints, bounding boxes, skeleton masks), and standard pose estimation metrics (PCK, OKS/mAP, MPJPE) are absent.

**Arbiter's justification:**
> The 20% IoU improvement headline claim is uninterpretable because it is unclear what IoU measures in this context. If the metric does not correspond to the actual task, the central accuracy claim is meaningless even if numbers were provided.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F026

- Paper: *Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

**Candidate finding (rated retraction-worthy):**
> The main theorem (Theorem 2.3) appears to state equality φ_C([y^i f_{j_i}(x)]) = φ_C([y^{n-1-i} f̃_{j_i}(x)]) rather than asserting that the right-hand side is the complex conjugate of the left-hand side. Since the two sides lie in different Hodge summands H^{n-1-i,i} and H^{i,n-1-i}, literal equality is impossible unless both classes are zero.

**Arbiter's justification:**
> If the theorem genuinely asserts equality rather than conjugation, it is a false statement for generic non-zero classes in distinct Hodge types. This is not a minor notational slip—it changes the mathematical content of the theorem from 'description of conjugation' to 'assertion that two generally distinct classes are equal,' which is wrong. Reviewer A identified this clearly; Reviewer B acknowledged in reflection that this is an independent fatal error they had missed. The confidence is 0.80 rather than higher because there remains some possibility that the manuscript's full context or notation makes the conjugation implicit in a way not captured by the excerpts.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F027

- Paper: *How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

**Candidate finding (rated retraction-worthy):**
> Lemma 4 provides only a covariance-matrix-level transformation (M → Z_i M Z_i, N → Z_i N Z_i) for the 'partial transpose of a Gaussian operation' but does not verify that the transformed parameters satisfy the Gaussian complete positivity condition (involving the symplectic form Ω). Conjugation by the non-symplectic Z_i does not automatically preserve the Gaussian CP constraint. Since Theorem 5 is built directly on this lemma, the central result lacks a valid channel-theoretic foundation.

**Arbiter's justification:**
> The Gaussian CP condition is N + iΩ - iM^T Ω M ≥ 0 (or similar, depending on convention). Conjugating M and N by Z_i does not obviously preserve this inequality since Z_i is not symplectic. If the transformed parameters violate this condition, the 'channel' B_i(G^{M,N}) is not a valid quantum channel. The paper omits this verification entirely. Both reviewers identified this, and Reviewer B upgraded this to RETRACTION-WORTHY upon reflection. The confidence is slightly lower because for specific channels (e.g., thermal/amplifier channels with particular symmetry), the CP condition might happen to be preserved, but the paper claims generality.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F028

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript derives or endorses a hard upper limit on CO₂-driven warming (~0.5–0.81°C) by misusing the logarithmic forcing relationship and ignoring climate feedbacks.

**Arbiter's justification:**
> Logarithmic forcing is the standard formulation and does not imply negligible warming; it is consistent with substantial warming per CO₂ doubling when feedbacks are included. The paper's central quantitative conclusion about climate sensitivity is built on this misinterpretation. If corrected, the main policy conclusion collapses.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F029

- Paper: *A missing theorem on dual spaces*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The issue is that an error in Proposition 2.3 undermines the validity of Lemmas 3 and 4, and Theorem 4.1 depends on results from Proposition 2.3; therefore, Lemmas 3 and 4 are only valid if the conclusions of Proposition 2.3 hold for the map q used in Theorem 4.1.

**Candidate finding (rated retraction-worthy):**
> In the proof of Theorem 3.3(1), the manuscript states J² = I and invokes a criterion for complex structure that requires J² = -I. Moreover, the manuscript's own calculation (J²)* = -I implies J² = -I by elementary duality, directly contradicting the stated J² = I. This is an internal contradiction at the algebraic core of the proof that X acquires complex structure, and Theorem 4.1 explicitly depends on this construction.

**Arbiter's justification:**
> This is not a typo that can be fixed by changing one symbol — the manuscript simultaneously asserts (J²)* = -I and J² = I, which are mutually contradictory by elementary duality. If J² = -I is what is intended, the authors need to supply a correct derivation showing this, because the currently written argument is self-negating. The conclusion (complex structure on X) depends entirely on this step. Theorem 4.1 and Theorem 1.2 inherit this defect. Without a valid proof of this step, the paper's central conclusions are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F030

- Paper: *A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

**Candidate finding (rated retraction-worthy):**
> Section 4.2, Lemma 4.4: |A_i| is modeled as Binomial(n, p_i), but A_i is a union of fixed-size subsets sampled without replacement, so the vertex indicators are dependent and the binomial model is invalid.

**Arbiter's justification:**
> This lower bound on |A_i| feeds into Lemma 4.5 and the subsequent stretch analysis for the Thorup-Zwick-style oracle. The probabilistic foundation for the 2k−1 stretch guarantee is therefore unsupported. Reviewer A identifies this clearly as retraction-worthy; Reviewer B flags it as a major concern though with slightly less certainty. The dependence issue is real and not easily hand-waved away, though it might be repairable with a more careful analysis (e.g., negative association arguments). Given that no such repair is present, the current proof is invalid.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F031

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> Proof of Theorem 5.1 uses the nonsensical group Gal(K_{∞,w}/K_{∞,w}) ≅ ∏_{ℓ≠p} Z_ℓ to conclude ker f₄ = coker f₄ = 0. This group is trivially the identity, and the intended local comparison is fundamentally misidentified.

**Arbiter's justification:**
> This step is used to eliminate local terms in the snake-lemma comparison that yields the isogeny formula. The statement is mathematically impossible — the Galois group of a field over itself is trivial. This is not a gap that could be filled; it indicates the authors lost track of the relevant local extension. The proof collapses at this point. Reviewer A identified this; Reviewer B's concerns about the Euler characteristic derivation are complementary and reinforce the conclusion that the proof is broken at multiple points.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F032

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The central claim 'no loss in link budget gain compared to spatial beamforming' rests on an unfair resource comparison. The temporal combining gain (T ≈ 18.375) is compared to N=16 antenna beamforming gain without charging MA-TISK for the proportionally longer integration time or lower effective symbol rate. This is a processing-gain-versus-beamforming-gain conflation.

**Arbiter's justification:**
> Both reviewers independently identified this as the paper's most fundamental flaw. After steelman exchange, both confirmed RETRACTION-WORTHY. The comparison violates basic time-bandwidth-energy conservation: beamforming provides instantaneous power gain in one symbol period, while temporal combining spreads energy over T periods and coherently recombines. Without equal-resource normalization, the claimed equivalence is physically misleading. This is the paper's headline conclusion and it cannot be supported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F033

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript conflates CO₂ residence time with adjustment time, and calculates that anthropogenic CO₂ is only ~4.3% of atmospheric CO₂ by comparing human emissions to gross natural fluxes, ignoring net imbalance and stock-flow accounting.

**Arbiter's justification:**
> This is a well-known carbon-cycle error. Natural gross fluxes are largely balanced; the anthropogenic perturbation is the net addition causing the observed CO₂ rise. The paper's claim that human emissions are negligible depends entirely on this confusion. Both reviewers identify this error.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F034

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Severe selection bias: the manuscript overwhelmingly relies on advocacy organizations (Heartland, GWPF, CO2 Coalition, Net Zero Watch), blogs, self-published books, and low-impact/fringe journals while systematically excluding or dismissing the mainstream peer-reviewed literature without methodological justification.

**Arbiter's justification:**
> Both reviewers flag this. For a review article, the evidence base determines the conclusions. A systematically biased source selection toward ideologically aligned, non-peer-reviewed material — while ignoring thousands of peer-reviewed papers from leading journals — means the review's synthesis is fundamentally unreliable. Reviewer B rated this MAJOR-REVISION, but given that it is inseparable from the missing methodology and directly determines all conclusions, the combined effect is retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F035

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The source base is dominated by advocacy organizations, blogs, opinion books, think-tank reports, YouTube videos, and preprints, treated as equivalent to peer-reviewed primary literature.

**Arbiter's justification:**
> For a review article making sweeping scientific claims that reject mainstream physics, the evidentiary base must be robust. Systematic reliance on non-scholarly and partisan sources to reject established science fatally compromises the review's validity. Both reviewers note this, though Reviewer B initially classified it as minor before acknowledging the scale makes it more serious.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F036

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> Claim 5 (stated for linear forests) is applied to G[J_s ∪ J_t ∪ J_m], but the manuscript never proves this union induces a linear forest. J_s and J_t each induce linear forests and J_m is independent, but their union can have arbitrary additional edges destroying the linear forest property. The key constructive reconfiguration step therefore lacks its required precondition.

**Arbiter's justification:**
> The entire correctness argument for the kernel reduction depends on being able to reconfigure within this subgraph using a lemma that requires the linear forest property. If the precondition is not met, the lemma does not apply and the equivalence proof fails. Reviewer B upgraded this to RETRACTION-WORTHY after steelman.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F037

- Paper: *How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

**Candidate finding (rated retraction-worthy):**
> The protocol's central constructions (bouncing identities, partial transpose implementation, noise polarization in Theorem 5, distillation in Corollary 6) all require ideal infinitely squeezed EPR states. No rigorous finite-squeezing error analysis is provided — no effective finite-r channel is derived, no error bounds (diamond norm, covariance level, or otherwise) are given, and no demonstration that the qualitative advantage survives at any finite resource level is presented. The paper's claims of a physically realizable Gaussian QEC/distillation protocol are therefore unsupported.

**Arbiter's justification:**
> Both reviews independently identified this as RETRACTION-WORTHY. Review A considered downgrading to MAJOR-REVISION if the paper were reframed as a purely ideal-limit theorem, but as written the paper explicitly claims a protocol and practical circumvention of no-go results. The finite-squeezing discussion (Appendix G) provides only qualitative statements ('fidelity approaches 1 as r→∞') without any quantitative analysis. Since the paper's stated contributions are a protocol and operational circumvention claims — not merely a mathematical identity in an unphysical limit — the gap between what is proven and what is claimed is fundamental.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F038

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> Unsupported safety claims: The paper explicitly states findings 'underscore the potential safety and efficacy' of exosomes as a therapeutic strategy, but no toxicity, safety, or tolerability evaluation was performed in patients or animals. An MTT viability assay on PBMCs does not constitute evidence of clinical safety.

**Arbiter's justification:**
> This is a specific and egregious instance of the design-conclusion mismatch. Safety in humans cannot be inferred from PBMC viability data. Since safety is explicitly part of the paper's stated conclusion, this claim is fundamentally unsupported. This compounds the first finding and reinforces the retraction-worthy assessment.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F039

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The manuscript conflates received power gain, SINR gain, processing gain, and beamforming gain, risking systematic double-counting. The 'temporal combining gain' is presented as a replacement for beamforming gain rather than being recognized as processing gain from a lower-rate signaling format.

**Arbiter's justification:**
> Both reviewers converged on this after steelman exchange. Reviewer A originally flagged it as RETRACTION-WORTHY; Reviewer B acknowledged in steelman that this was 'more coherent' than their scattered observations and elevated related findings. The failure to separate energy spreading, symbol duration expansion, noise bandwidth narrowing, and coherent recombination means the apparent gain may simply reflect resource reallocation rather than genuine link-budget equivalence.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F040

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> No actual experimental results are reported. The claimed quantitative improvements (20% IoU, 30% speed reduction) appear only as summary assertions in the text with no supporting tables, figures, confidence intervals, p-values, or any analyzable data.

**Arbiter's justification:**
> The paper's central conclusions rest entirely on quantitative performance claims, yet no numerical evidence is provided anywhere in the manuscript. This is not a matter of incomplete reporting—the evidence is wholly absent, rendering the conclusions baseless.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F041

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The central subroutine BFS⁺ is never defined: no pseudocode, no formal detection rule, no specification of what data structures are maintained or what condition triggers triangle detection. The entire correctness and runtime of Theorem 2 depend on this undefined procedure.

**Arbiter's justification:**
> Both reviewers independently flag this as a critical gap. After steelman exchange, both converge on retraction-worthy severity. An algorithmic paper whose main claimed breakthrough delegates the key step to an unspecified subroutine does not establish its central result. This is not a presentation issue—without BFS⁺, the theorem is a conjecture, not a proven result. All downstream theorems inherit this failure.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F042

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> The claimed 'novel modifications' and 'advanced neural network architectures' incorporated into MediaPipe are never described. No architecture details, layer modifications, training procedures, loss functions, hyperparameters, or optimization changes are specified.

**Arbiter's justification:**
> The paper's claimed methodological novelty—the core contribution—is entirely undefined. This is more than a reporting gap: combined with the method-results mismatch, there is no evidence that any architectural modification exists. Reviewer A downgraded this to MAJOR-REVISION in steelman, acknowledging it could theoretically be a reporting omission. However, Reviewer B's steelman correctly notes that the described method (inference-only angle calculation) is logically incompatible with the existence of such modifications, pushing this back toward RETRACTION-WORTHY. On balance, the combination of undefined contribution plus contradictory method description makes this RETRACTION-WORTHY.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F043

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> Theorem 6.3 / Proposition 6.2: The noncommutative μ-vanishing result claims μ_G(S(E/K_∞)^∨) = μ_Γ(S(E/K_cyc)^∨) via a restriction map whose kernel is finite and cokernel cofinitely generated. The equality of μ-invariants from such a map is not justified; the cited references ([CSS03b], [Pal14]) address number fields, not function fields, and the required finiteness/cofiniteness is not proven in this setting.

**Arbiter's justification:**
> Review B rates this retraction-worthy; Review A initially rated it major-revision but upgraded to retraction-worthy after steelman. The μ_G = μ_Γ equality is the sole logical bridge to the main conclusion of Part II (ℓ ≠ p case). Without it, the headline noncommutative result is entirely unsupported. The gap is not a missing detail but a missing proof of the key step, using references whose hypotheses are not verified in the function-field setting.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F044

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> Method-results mismatch: The only concrete methodology described is a simple elbow-angle calculation and threshold-based curl counter using unmodified MediaPipe landmarks. The paper claims architectural and algorithmic improvements to MediaPipe pose estimation itself, including 20% IoU improvement and enhanced robustness. A downstream rule-based application cannot produce or evidence improvements to the underlying pose estimation model.

**Arbiter's justification:**
> This is a logical contradiction, not merely a reporting gap. Even if all missing experimental details were supplied, the described method (angle thresholding on existing landmarks) cannot constitute or demonstrate an improvement to MediaPipe's pose estimation architecture. Both reviewers identify this, and both maintained or strengthened this finding through steelman exchange. Reviewer A defended it as RETRACTION-WORTHY; Reviewer B recognized it as the most fundamental problem and elevated its importance.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F045

- Paper: *Shafarevich-Tate groups of holomorphic Lagrangian fibrations II*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> There is likely a mistake in the formulation or derivation of equations related to Kähler twists, such as an incorrect application of properties of Kähler manifolds or errors in twisting procedures within the proof.

**Candidate finding (rated retraction-worthy):**
> Theorem D (5.3.12): The proof confuses 'Fujiki class C' (bimeromorphic to a Kähler manifold) with 'admits a rational map to a Kähler manifold' and then attempts to pull back a Kähler form along such a rational map. This is a category error: pullback of a Kähler form under a rational map is not defined without resolving indeterminacies, and the subsequent claim that the restriction to a general fiber of π^φ is birational onto its image is unjustified.

**Arbiter's justification:**
> Reviewer A identified this as retraction-worthy; Reviewer B upgraded to the same during steelman, acknowledging the conceptual error. The proof of Theorem D as written does not establish the theorem from its hypothesis. This is not a gap that can be filled by adding a sentence — the entire proof strategy is based on a mischaracterization of Fujiki class C. Theorem D is one of the paper's four headline results.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F046

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The constraint C(r) = 2r₁₂r₃₄cosθ + r₂₃² + r₁₄² - r₂₄² - r₁₃² = 0 involves the angle θ between opposite sides, which is itself a function of the mutual distances r. The manuscript treats cosθ as if it were a fixed external parameter throughout the Morse-theoretic analysis and the Euler characteristic computation (Lemma 3). This means M⁺ is not a well-defined fixed submanifold of ℝ⁶ — it changes with the point r. The topological analysis (contractibility, fibration structure, χ=1) is performed on an object that is not properly defined.

**Arbiter's justification:**
> Reviewer B's central finding. If θ is not a fixed parameter but depends on r, then M⁺ as defined is not a standard level set of a smooth function, and the entire Morse-theoretic framework (which requires a fixed constraint manifold) breaks down. This interacts with and compounds the domain issue above. There is some possibility that the authors intend to fix θ as a parameter and study the family of central configurations at each θ, but even under that charitable reading the arguments are not valid because the constraint C depends on θ in a way that was not properly handled.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F047

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The CMB argument—that aberration at z~1000 would catastrophically smooth anisotropies—contradicts standard treatment and observations. The standard CMB dipole aberration from our peculiar velocity is small and well-measured, not a factor of ~10^6 smoothing.

**Arbiter's justification:**
> This is a major downstream conclusion of the paper. It follows from the same invalid global-aberration reasoning applied to the last-scattering surface. The prediction is flatly contradicted by observed CMB anisotropies and their successful modeling in standard cosmology.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F048

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> Use of the SR Doppler formula (Eqs. 4–5) to define a recession speed β from cosmological redshift as if globally meaningful, then building the entire aberration correction from this inferred β.

**Arbiter's justification:**
> The SR Doppler formula relates frequency shifts to relative velocity between inertial frames in flat spacetime. Cosmological redshift arises from metric expansion along the photon's path in curved spacetime—there is no unique 'velocity' that can be plugged into the SR formula to recover the aberration factor across cosmological distances. Since the rest of the derivation depends on this β, the main quantitative results do not follow. Reviewer A rated this retraction-worthy; Reviewer B subsumed it under the broader SR misapplication. It survived steelman.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F049

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Corollary 2.2 (Faber–Krahn inequality: balls uniquely minimize the principal eigenvalue among domains of given volume) depends entirely on Theorem 2.1. Since the theorem's formula is unsupported, the Faber–Krahn result is also unsupported. The rearrangement argument at most proves an inequality for the averaged escape integral, not for the principal eigenvalue.

**Arbiter's justification:**
> This is a central advertised result of the paper. Its validity is entirely derivative of Theorem 2.1, which is itself unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F050

- Paper: *Nevanlinna Theory on Geodesic Balls of Complete K√§hler Manifolds*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the Green function $G_R(o,x)$ for the geodesic ball $B(R)$ was incorrectly stated to satisfy the Dirichlet boundary condition on the geodesic sphere $\partial B(R)$, when in fact it does not necessarily vanish on the boundary as required by the Dirichlet condition.

**Candidate finding (rated retraction-worthy):**
> Probable sign error in the genus term derivation of Theorem 4.1. The proof moves from -∫N_f(r,ζ)K'(ζ)ω(ζ) to a lower bound involving +(2-2g)T_f(r), but Gauss-Bonnet gives ∫K'ω = 2-2g, so the negative sign should yield -(2-2g)T_f = (2g-2)T_f. The resulting coefficient (q-2+2g) in the main Second Main Theorem may be incorrect.

**Arbiter's justification:**
> The coefficient in front of the characteristic function is the quantitative heart of any Second Main Theorem. If the sign handling is wrong, the stated theorem is numerically false, not merely incompletely proved. This directly affects Theorem II and all downstream defect relations for genus g targets. Both reviewers acknowledged this error; Reviewer A rated it RETRACTION-WORTHY and defended this strongly in reflection. Reviewer B acknowledged it as genuine but considered it secondary to the Lemma 3.6 issue. The sign tracking in the displayed computation is specific enough to evaluate: the intermediate inequality appears directionally inconsistent with Gauss-Bonnet, and this is not a gap that can be filled—it would require changing the theorem statement or the proof strategy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F051

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> The existence proof in Theorem 1.4 (construction of SIN states via rotation into the region described by Eq. (9)) is unsupported because it relies on both the erroneous Eq. (8)/(9) target region and on an unjustified claim that the relevant properties are preserved under the prescribed rotation.

**Arbiter's justification:**
> The constructive heart of the paper's theorem depends on a target region derived from an algebraic error. Since the target region does not actually differ between original and swapped states (per the swap-invariance argument), there are no SIN states to construct. The existence proof is void.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F052

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Lemma 4.5 is incorrectly proved: the proof conflates conditioning on {S_n ∈ D} with conditioning on the full path survival event ∩_{k=1}^n {S_k ∈ D}. The conditional distribution of S_n given the entire path stays in D is not uniform on D and depends on path history. The bounded convergence theorem is applied to a ratio whose denominator involves the full survival event, not merely the marginal event {S_n ∈ D}. The claimed uniform limit is unsubstantiated.

**Arbiter's justification:**
> Both reviewers independently identify this as the critical error. Lemma 4.5 is the key technical input converting the jump-chain survival probabilities into the explicit eigenvalue formula of Theorem 2.1. Without it, the entire derivation collapses. The error is not a gap that can be filled by adding a sentence — the conditional distribution given full survival is fundamentally different from the conditional distribution given the marginal event, especially for bounded jumps.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F053

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The paper uses the equivalence principle to justify replacing the global FLRW light-propagation problem with chained local inertial frames and then extracts a global observable flux correction from this local construction.

**Arbiter's justification:**
> The equivalence principle permits local Minkowski approximations over scales much smaller than the Hubble radius. It does not license replacing a global null-geodesic propagation calculation with a single SR aberration transformation between cosmologically separated endpoints. The paper itself acknowledges FLRW quasi-translations are not Lorentz transformations, yet proceeds to use SR beaming formulas globally. This methodological error is the bridge that enables the invalid derivation.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F054

- Paper: *From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

**Candidate finding (rated retraction-worthy):**
> Theorem 4.9 proof is explicitly marked as DRAFT and is incomplete, with undefined notation, inconsistent queue class names, and no verifiable derivation of the 38-queue bound.

**Arbiter's justification:**
> Theorem 4.9 is the direct basis for the headline result (Theorem 1.5: 38-queue bound for planar graphs). Both reviewers note that the proof is incomplete and the notation is inconsistent. An incomplete draft proof with undefined terms means the central claimed bound is simply not established. This is not a matter of a gap that could be filled—the proof is openly unfinished.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F055

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> The baseline comparison is completely undefined. The paper claims superiority over 'traditional models' and the 'baseline MediaPipe model' but specifies no version, configuration, hardware, thresholds, or matched conditions for comparison.

**Arbiter's justification:**
> The paper's core claim is comparative improvement. Without an identified and specified comparator under matched conditions, the claim of superiority is logically empty. Both reviewers identified this as a critical defect; Reviewer A rated it RETRACTION-WORTHY, and Reviewer B's findings 3 and related reasoning support the same conclusion.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F056

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Claim that logarithmic dependence of radiative forcing on CO₂ concentration means added CO₂ has negligible climatic effect. Logarithmic forcing implies approximately constant forcing per doubling, not negligible effect.

**Arbiter's justification:**
> Both reviewers identify this as a non sequitur from the manuscript's own cited formulae. Reviewer B additionally notes that the paper's own Figure 1 shows 0.64-0.81°C warming per doubling, contradicting the 'negligible' characterization in the text. The conclusion drawn is not supported by the mathematics presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F057

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> The transition from conditioning on {S_n ∈ D} (Lemma 4.4) to conditioning on full path survival {S_k ∈ D for all 1 ≤ k ≤ n} (Lemma 4.5) is unjustified. These are fundamentally different conditioning events, and no bridging argument is provided.

**Arbiter's justification:**
> Both reviewers identify this gap. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman, recognizing it is the core inferential step identifying the constant α. The path-conditioned law and endpoint-conditioned law are genuinely different objects, and this is not a routine epsilon-delta detail but a change of conditioning sigma-field central to the argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F058

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> Theorem 1.5/6.3 contains a contradiction: the abstract and introduction advertise results for a GL₂(Zₗ)-extension, but the theorem statement requires G = Gal(K_∞/K) to be pro-p. An open subgroup of GL₂(Zₗ) is not generally pro-p (for ℓ ≠ p), so the paper does not prove what it claims at the headline level.

**Arbiter's justification:**
> Review A flags this as retraction-worthy; Review B did not initially catch it but after steelman recognized it as a severe overstatement. The paper's main selling point is extending results to the noncommutative GL₂(Zₗ) setting. If the proof only works for pro-p groups (a drastically more restrictive class), then the claimed result is materially overstated. However, there is some possibility the authors intended a pro-p quotient or open pro-p subgroup, which would make this a major misstatement of generality rather than total invalidity of a restricted result. Retained at retraction-worthy because the discrepancy is between the paper's central advertised contribution and what the proof actually establishes.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F059

- Paper: *Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 2.3 reconstructs an element via the pairing C(φ_C(U_k), φ_C(U_k)) rather than C(φ_C(U_k), conjugate of φ_C(U_k)), thereby solving for the original class or an element with a prescribed self-pairing rather than the conjugate class.

**Arbiter's justification:**
> The reconstruction of conjugation from a bilinear/sesquilinear pairing requires using the conjugated argument. If the proof computes a self-pairing and then inverts to find an algebraic representative, it has not established conjugation. This is logically independent of the theorem-statement error. Both reviewers agree after reflection. Confidence is slightly lower because the proof details may contain implicit conjugation steps not visible in the excerpt.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F060

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The constraint C(r)=0 is only a necessary condition for convex quadrilateral configurations (as the authors acknowledge via Josefsson's relation), not sufficient. The Morse-theoretic uniqueness argument is performed on M^+ = {I=I₀, C=0, r_ij>0}, which is strictly larger than the actual configuration set. The proof does not establish that the critical point structure on this enlarged set faithfully represents the original geometric problem.

**Arbiter's justification:**
> Both reviewers flag this as a core issue. During steelman, Reviewer A considered that this might be major-revision if the authors could prove an exact critical-point correspondence on the realizable locus, but acknowledged this would require a 'nontrivial new argument.' Reviewer B's steelman strengthened this by noting the factorization F₄=C·A is only established on the geometric set where C=0 already holds, making the constraint replacement potentially circular. The combination of the enlargement problem with the circularity of the factorization makes this retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F061

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> No ground truth measurement procedure is described. It is unclear how reference pose labels were obtained for accuracy evaluation.

**Arbiter's justification:**
> Accuracy metrics require reference labels. Without knowing the source and quality of ground truth, reported accuracy improvements are unvalidatable. Combined with the absence of dataset details, this confirms the empirical claims are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F062

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> Primary performance claims (20% IoU improvement, ~30% processing-time reduction) are unsupported by any presented quantitative evidence. No results table, no numerical data points, no sample sizes, no confidence intervals, no variance estimates, and no statistical tests are provided.

**Arbiter's justification:**
> The paper's central conclusions are headline numerical claims for which zero supporting data is presented. Reviewer A defended this as RETRACTION-WORTHY through steelman; Reviewer B agrees these claims are meaningless without evidence. Under the severity standard, the central conclusions cannot be supported by the data as presented because no data is presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F063

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The contradiction argument in Theorem 3.2 uses asymptotic tightness of the isoperimetric lower bound (2.4) as A→0 in the wrong logical direction. Tightness means I_A² approaches the lower bound from above as A→0, but the proof requires choosing A small so that the lower bound exceeds an independently prescribed barrier—effectively using tightness to produce an upper bound on I_A², which does not follow. The 'contradiction' in (3.3) is therefore logically invalid.

**Arbiter's justification:**
> Both reviewers identified this as retraction-worthy and maintained that assessment through the steelman exchange. The logical inversion is not a gap that could be filled with additional argument; it is a direct misuse of the asymptotic relationship. Without this step, exponential decay of κ(t) is unproven and the convergence theorem fails.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F064

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The recursive construction for implementing P(πℓ/2^m) fault-tolerantly is not properly specified. The recursion direction is ambiguous (doubling vs. halving angles), no explicit base case is given, the referenced circuit figures (Figs. 1 and 2) are missing from the manuscript, and the resource analysis (claimed O(n) overhead) is unsupported with no accounting for state preparation, verification, rejection sampling, or teleportation costs.

**Arbiter's justification:**
> Reviewer B identifies the mathematical impossibility of the doubling recursion as described; Reviewer A identifies the missing resource analysis. Together, these mean the constructive procedure—the paper's main algorithmic contribution—is both untestable (missing figures) and logically inconsistent (recursion direction). The paper cannot be evaluated or reproduced.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F065

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Corollary 4.12 states that x + P(y−x) = z ⊙_{l,k} w is partition regular, but the proof concludes with x + P(y−x) = z ⊕_{l,k} w, which is a different operation. The statement and proof are mismatched.

**Arbiter's justification:**
> This is the paper's headline result. A mismatch between the operation in the statement and the operation in the proof means the theorem as stated is not proved. If ⊕_{l,k} was intended, the result is less novel; if ⊙_{l,k} was intended, a different proof is needed.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F066

- Paper: *A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

**Candidate finding (rated retraction-worthy):**
> Incorrect use of advanced composition in all (ε,δ)-DP results. The per-mechanism privacy parameters used in Theorems 3.2, 4.2, and 4.4 do not satisfy the paper's own composition lemma (Lemma 2.2). The denominators are missing a factor of approximately √m, and the δ/(2k) allocation is omitted. This means all approximate-DP guarantees are unproven and generally false under the stated parameters.

**Arbiter's justification:**
> This is a systematic, global error affecting every approximate-DP theorem in the paper. The stated (ε,δ)-DP guarantees do not follow from the paper's own privacy lemma, and the parameters are materially wrong (not just slightly loose). Since the approximate-DP results are presented as central contributions, this invalidates the paper's main claims as written. Both reviewers agree on the severity after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F067

- Paper: *A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

**Candidate finding (rated retraction-worthy):**
> Lemma 3.2 (tree release primitive) has an incorrect sensitivity analysis. The paper claims the released vector of distances has ℓ1-sensitivity 1 because subtrees are disjoint, but changing one edge weight can affect multiple distances whose shortest paths traverse that edge, yielding sensitivity larger than 1. The noise calibration is therefore insufficient for the claimed privacy guarantee.

**Arbiter's justification:**
> This primitive is invoked repeatedly throughout Sections 3 and 4 as the building block for all main algorithms. If the privacy proof of the primitive is invalid, every downstream theorem inherits the flaw. Reviewer A identifies this precisely; Reviewer B's 'composition of compositions' concern is a related but differently framed version of the same core issue (the per-tree privacy/accuracy tradeoff is not as claimed). Because the paper's central contribution is the family of DP algorithms built on this primitive, this undermines the main conclusions.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F068

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> Proof of Theorem 1.1: The inference that H is dense in G from item (2) of Lemma 2.3 is incorrect. Item (2) states G \ (L+U) has empty interior, which means L+U is dense, but the proof conflates L+U with U + span{x_i} and does not correctly establish that H contains a dense subset.

**Arbiter's justification:**
> Density of H is essential for applying the extension lemma (Lemma 2.2). Reviewer A correctly notes that the logical chain from item (2) to density of H is broken. Without density, the automorphism cannot be extended to all of G, and the main theorem fails.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F069

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> Misapplication of the Shannon capacity formula (Eqs. 9-10) to argue that loss in data rate and loss in beamforming gain are equivalent in a fixed-bandwidth system. The low-SNR approximation R ≈ SNR/ln(2) applies only in the wideband/infinite-bandwidth regime, not a fixed 100 MHz channel.

**Arbiter's justification:**
> Both reviewers identified this error. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman, agreeing that this formula is essential to the paper's multiuser equivalence argument. In a fixed-bandwidth system, halving user rate does not halve required SNR in the linear way the paper claims. Since this argument underpins the conclusion that MA-TISK matches beamforming for multiuser scenarios, its invalidity removes support for a central claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F070

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Theorem 2.1's explicit formula λ_1^X(D) = (r/|D|) ∫_D ∫_{D^c} j(y−x) dy dx is the spatial average of the one-step escape rate, not the principal eigenvalue of the killed generator. The generator of the killed compound Poisson semigroup is a nonlocal integral operator with spatially varying killing rate r∫_{D^c} j(y−x) dy, whose principal eigenvalue is not generally equal to the spatial average of this rate. A counterexample structure exists: for domains with weakly connected components, the principal eigenvalue is governed by eigenfunction localization, not the global average.

**Arbiter's justification:**
> Reviewer A provides both the generator calculation and a counterexample argument showing the formula is likely false in general. The averaging over D produces a quantity that does not coincide with the principal eigenvalue of a nontrivial integral operator except in special (e.g., constant-kernel-on-D) cases. This is the paper's central theorem.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F071

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> Computational efficiency claims (30% processing time reduction) are reported without hardware specifications, software environment, image resolution, latency measurement protocol, or any experimental details.

**Arbiter's justification:**
> Runtime performance is entirely dependent on measurement conditions. Without these details, the efficiency claim cannot be interpreted or reproduced and is therefore unsupported as presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F072

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The topology proof of Lemma 3 (χ(M^+)=1) is not rigorous. The argument claims coordinate projections induce fibrations with contractible fibers, but no local triviality, continuity of fiber type, or explicit deformation retracts are provided. Fiber descriptions ('quarter of a ring belt,' 'quarter of a circle') are informal and the fiber type changes at boundaries, which is incompatible with a fibration structure.

**Arbiter's justification:**
> Both reviewers independently rate this retraction-worthy and neither downgrades it during steelman. Lemma 3 is the sole global topological input to the Morse equation; if χ(M^+)≠1, the uniqueness conclusion α₀=1 does not follow. The gaps are not minor omissions but fundamental: the claimed fibrations are not verified, and the informal geometric descriptions do not constitute a proof of contractibility. Reviewer B's steelman observation that fiber type changes at boundaries reinforces that this cannot be trivially repaired.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F073

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> Claim 7's proof contains unjustified greedy reconfiguration steps (e.g., 'greedily move all remaining tokens to J_m'). In token jumping, each move must maintain independence of the entire current token set. The manuscript treats this as trivial when it is not—independence of the destination set does not imply legality of the moves, which depends on adjacency to all currently-occupied vertices.

**Arbiter's justification:**
> Reviewer A rated RETRACTION-WORTHY; Reviewer B initially rated the broader Claim 7 as MAJOR-REVISION but upgraded after steelman. The issue is that the equivalence proof requires a valid sequence of legal token jumps, and the manuscript provides no such argument. This is the substance of the correctness proof, not a peripheral detail. However, there is a small chance the steps could be made rigorous with significant additional argument, so confidence is slightly lower.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F074

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> The quantum protocol requires orthogonality for confusable pairs (edges of G^(m)), but Lemma 4 and Definition 4 define orthogonal representations on the complement graph Ḡ^(m), where orthogonality is enforced on non-adjacent vertices. This categorical mismatch means Theorem 4's quantum rate formula optimizes the wrong graph parameter, and the claimed quantum advantage (R_quantum(g) < R_classical(g)) is unsupported.

**Arbiter's justification:**
> Both reviewers identify this as the central error and rate it RETRACTION-WORTHY. Reviewer A considered downgrading to MAJOR-REVISION in the steelman only if the problem were a globally consistent convention swap, but acknowledged this would still require every cited inequality and product identity to be re-verified under the swapped convention—something the manuscript does not do. Reviewer B's steelman reinforced the severity. The error is not a typo: it inverts which pairs must be orthogonal, changing the feasible set, the relevant ξ-quantity, and the asymptotic rate. Because the quantum advantage demonstration is the paper's primary contribution, this is RETRACTION-WORTHY under the provided standard.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F075

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Elimination half-lives vastly exceed the 128-hour observation window (plasma 3368 h, liver 420 h), and Ka values near zero (0.0002 h⁻¹ in plasma) imply absorption half-lives of thousands of hours.

**Arbiter's justification:**
> While terminal half-life overestimation from short sampling windows is a known limitation, the magnitude here (3368 h from 128 h sampling = 26× the observation period) goes beyond 'unstable estimate' to 'meaningless parameter.' A Ka of 0.0002 h⁻¹ implies absorption would take years for OTC in fish, which is biophysically absurd. Reviewer B rated RETRACTION-WORTHY; Reviewer A rated MAJOR-REVISION for the half-life issue alone but rated related contradictions as RETRACTION-WORTHY. On balance, these extreme values—combined with the NCA/compartmental mismatch and internal contradictions—are not independently remediable by restricting terminal-phase estimation because they reflect a fundamentally broken analytical pipeline.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F076

- Paper: *From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

**Candidate finding (rated retraction-worthy):**
> The local machinery around Claim 4.10 / Theorem 4.9 (1-queue layouts for bipods, global queue assembly) is internally corrupted: interleaved incompatible proof branches, malformed inequalities, references to undefined queue families, and notation switches mid-argument.

**Arbiter's justification:**
> Reviewer A identified this as a separate fatal defect from the incompleteness of Theorem 4.9. The local non-nesting lemmas are the engine of any queue-layout proof; if they are textually garbled to the point of being mathematically unreadable, the global bound cannot be assembled. Reviewer B's reflection acknowledged the corrupted text blocks verification. This independently prevents support of the 38-queue claim even if one attempted to reconstruct intent from the fragments.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F077

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript states that the increase in global temperature from 1880–2000 is 'statistically indistinguishable from 0°K,' contradicting all major observational temperature datasets.

**Arbiter's justification:**
> The ~0.8°C warming over this period is documented with clear statistical significance by NASA GISS, NOAA, HadCRUT, and Berkeley Earth. This claim is empirically false and directly supports the paper's conclusion that warming is not occurring. Both reviewers flag this.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F078

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Impossible analytical validation values: negative LOD/LOQ (e.g., LOD = -587.51 µg/kg, LOQ = -1780.34 µg/kg in kidney) and R² values outside the valid 0–1 range (e.g., muscle R² = 6.96, skin R² = 0.002). The authors' claim that negative LOD/LOQ values 'affirm method impartiality' is scientifically incorrect.

**Arbiter's justification:**
> Negative concentration limits are physically meaningless, and R² > 1 is mathematically impossible. These are not ambiguous analytical choices — they indicate that either the calibration/validation was fundamentally flawed or the values are gross reporting errors. Since all tissue concentration data depend on validated analytical methods, the entire quantitative dataset (PK concentrations, residue levels, withdrawal times) is rendered unreliable. Both reviewers flagged this independently with the highest severity.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F079

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The core subroutine BFS+ is never formally defined. All correctness and runtime analyses depend on its exact behavior, but the manuscript provides only informal prose references to a 'slightly modified BFS' without pseudocode, data-structure specifications, or algorithmic rules.

**Arbiter's justification:**
> An algorithm paper claiming a breakthrough must specify the algorithm. The entire detection mechanism is this undefined subroutine. Without it, there is no algorithm to verify, and the main theorem is an unsupported existence claim. Both reviewers independently rated this RETRACTION-WORTHY and defended the rating through reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F080

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> Lemma 2 establishes positive definiteness of the ambient Hessian D²W(r) in all six distance variables and concludes that constrained critical points are non-degenerate minima of Morse index 0 on M^+. However, for constrained Morse theory, non-degeneracy must be verified for the Hessian of U restricted to the tangent space of M^+, which is a different object. The manuscript does not compute the restricted/bordered Hessian, nor does it establish that M^+ is a smooth manifold at critical points (requiring regularity of the constraint map).

**Arbiter's justification:**
> The Morse index assignment (all critical points have index 0) is directly used in the counting formula. If the constrained Hessian has different signature, the count changes and uniqueness fails. Reviewer B rated this retraction-worthy; Reviewer A rated it major-revision. The argument is that while ambient positive definiteness is suggestive, the constrained Morse analysis is entirely absent, not merely incomplete. Given that the smooth-manifold hypothesis for M^+ is also unverified, the entire Morse-theoretic framework is unsubstantiated. However, because positive definiteness of the full Hessian often does imply positivity on tangent subspaces, there is some probability this could be repaired, placing this at the boundary. I classify it as retraction-worthy because the needed smooth-manifold and tangent-space arguments are absent, not merely incomplete.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F081

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Theorem 4.5 (linking heads of tensor products of simple modules to generic extensions, and claiming to prove Conjecture 5.1 of [LM21]) is not proved. The proof depends on the invalid Proposition 4.3 and unproved Theorem 3.2, and independently fails at its final step where the existence of the required exact sequence is dismissed with 'It is easy to see' without derivation.

**Arbiter's justification:**
> This is one of the paper's principal advertised applications. Both reviewers agree the proof is incomplete and depends on earlier broken results. Reviewer A rates it RETRACTION-WORTHY; Reviewer B initially rated it MAJOR-REVISION but effectively treats it as fatal in the second pass by noting the cascading dependency on invalid prior results. Since the paper explicitly claims to prove an open conjecture via this theorem, its failure means a headline claim of the paper is unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F082

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Dye identification in real textile wastewater is based solely on matching UV-Vis absorption peaks/humps, with no chromatographic confirmation, spike-recovery experiments, or matrix correction. In a complex effluent, multiple absorbing species can produce overlapping peaks that mimic target dyes.

**Arbiter's justification:**
> Reviewer A identifies this as retraction-worthy, and Reviewer B raises the same concern through the wastewater characterization finding. If the dyes are not actually present or are not the species being measured, the entire applied wastewater claim collapses. Combined with the lack of controls, this invalidates the paper's principal application claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F083

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> The proposed 'enhancements' to MediaPipe are never concretely described. The paper uses vague phrases ('refined algorithms,' 'advanced neural network architectures') but provides no architecture modifications, training procedures, hyperparameters, loss functions, or optimization details. The only concrete processing described is a rule-based angle threshold for curl counting.

**Arbiter's justification:**
> The paper's central novelty claim is that specific enhancements to MediaPipe produced measurable improvements. If the enhancements are undefined, there is no identifiable intervention to evaluate, attribute gains to, or replicate. The central scientific contribution is untestable. Reviewer A rated this RETRACTION-WORTHY and defended it vigorously; Reviewer B initially rated a related finding as MAJOR-REVISION but in reflection concurred that the absence of any described modification may indicate the claimed innovation does not exist.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F084

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Lemma 4.4, even if technically correct, proves only convergence of the law of S_n conditioned on {S_n∈D} to uniformity on D—not convergence under the path-survival conditioning {S_1∈D,...,S_n∈D} that the subsequent proof requires.

**Arbiter's justification:**
> This is logically independent of whether the CLT computation in Lemma 4.4 is correct. The lemma addresses the wrong conditional law. Path-survival conditioning biases the endpoint distribution toward the interior of D (quasi-stationary behavior), which generally differs from endpoint conditioning. No argument bridging these two conditioning regimes is provided. This gap is structural and cannot be fixed by minor revision of the existing proof strategy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F085

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The manuscript describes two incompatible methods—MSP-MVS (deformable-patch MVS with multi-granularity segmentation prior, anchor equidistribution, iterative local search) and TSAR-MVS (post-processing pipeline with confidence filtering, superpixel/RANSAC refinement, WMF propagation, textureless-aware segmentation)—under one paper. The evaluated algorithm cannot be uniquely identified, breaking the method-to-results correspondence required for any scientific claim.

**Arbiter's justification:**
> Both reviewers independently identified this as retraction-worthy and neither downgraded upon reflection. This is not a naming typo—the two described pipelines operate at different stages (full MVS vs. post-processing), have different inputs, different module architectures, and different contribution claims. If confirmed, no reader can determine what algorithm generated the benchmark numbers, making the central SOTA claims scientifically unsupported. This meets the retraction test: the paper's central conclusions cannot be supported by the data as presented because the method generating those data is undefined.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F086

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> No dataset is identified or described. There are no dataset names, subject counts, number of images/videos, train/test splits, annotation procedures, or acquisition protocols.

**Arbiter's justification:**
> Without a defined evaluation dataset and ground truth, the reported accuracy and efficiency improvements cannot be interpreted, reproduced, or verified. The empirical foundation of the paper does not exist.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F087

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The manuscript does not solve the stated problem of approximation from a fixed finite gate set. The theorem explicitly uses a gate set depending on ε (including {P(πℓ/2^m)} where m grows with 1/ε), and the discussion appeals to hardware-native arbitrary phase rotations P(α). This contradicts the introduction's framing as addressing the Nielsen-Chuang challenge for fixed-set approximation complexity.

**Arbiter's justification:**
> Both reviewers identified this issue. Reviewer A initially rated it RETRACTION-WORTHY; Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman exchange. Reviewer A acknowledged in steelman that under an honest reframing (e.g., ε-dependent instruction library) the mathematics might be partially salvageable, suggesting some uncertainty. However, as the paper is written, the central claim addresses a problem it does not actually solve. The mismatch between problem statement and solution is fundamental.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F088

- Paper: *The Art of Staying Ahead of Deadlines: Improved Algorithms for the Minimum Tardy Processing Time*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the runtime analysis omits the contribution of the processing times within the interval [d_j - p_j, d_{j - 1}], which leads to an incomplete and therefore incorrect calculation of the total processing time.

**Candidate finding (rated retraction-worthy):**
> The multi-machine extension (Pm||∑pjUj) is not justified. No recurrence for the m-dimensional DP state is given, the 'point-wise trimming' strategy is asserted without proof of correctness, the required multi-dimensional dynamic string data structure is not shown to exist, and the persistence property (Lemma 4.1) is not proved for the multi-machine case.

**Arbiter's justification:**
> Both reviewers flagged this independently. The m-machine result is a headline contribution but rests on unsupported assertions. Feasibility on m identical machines is not a coordinate-wise independent condition, so 'point-wise' adaptation requires substantial justification that is entirely absent. The multi-dimensional data structure needed is not established in the literature or in this manuscript.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F089

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> The reported energy density (61.05 Wh/kg) is arithmetically inconsistent with the manuscript's own stated formula and inputs. Using SE = Cs×ΔV²/7.2 with Cs = 1502 F/g and ΔV = 0.65 V yields ~88 Wh/kg, not 61.05 Wh/kg. No corrected voltage window or IR-drop adjustment is disclosed.

**Arbiter's justification:**
> A headline quantitative result fails a direct substitution check using the paper's own equation and stated parameters. The ~44% discrepancy is far too large for rounding. This means the promoted energy density value is either calculated with undisclosed inputs or is simply wrong. Either way, a central claim in the abstract is numerically unsupported. Reviewer A identified this; Reviewer B acknowledged it as a critical arithmetic error in reflection. This independently breaks a headline claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F090

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> Energy density and power density are derived from a three-electrode half-cell measurement but presented as supercapacitor device performance metrics (61.05 Wh/kg, 270.5 W/kg). No two-electrode device was constructed or tested.

**Arbiter's justification:**
> Half-cell electrode data systematically overstate device-level energy and power density. The manuscript foregrounds these values in the abstract and conclusion as evidence of practical supercapacitor performance. Since no full device was tested, these application-level claims are methodologically invalid regardless of whether the underlying electrode material is good. Reviewer A rated this retraction-worthy; Reviewer B recognized it as a separate fundamental error in reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F091

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The maximum principle argument in Proposition 3.1 is structurally invalid: I_A is an infimum-defined isoperimetric profile, not a classical smooth solution of a parabolic PDE, and the paper applies a standard comparison principle without establishing the required smoothness, regularity, or viscosity/barrier framework.

**Arbiter's justification:**
> Both reviewers independently identify this as the fatal core defect. Hamilton-style isoperimetric arguments require delicate viscosity or barrier arguments precisely because the profile is defined as an infimum and is generally nonsmooth. The manuscript treats I_A^2 as a classical PDE solution and invokes the maximum principle directly, which is a category error, not a missing lemma. Since Proposition 3.1 is the engine of the entire proof and no alternative argument exists in the paper, its failure collapses the main theorem.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F092

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The cost-benefit conclusion against Net Zero is asserted without any transparent economic model, discounting assumptions, damage functions, uncertainty analysis, or comparison with adaptation/mitigation benefits.

**Arbiter's justification:**
> The paper's policy recommendation is presented as a scientific conclusion, but no valid cost-benefit methodology supports it. Economic cost figures are drawn from advocacy reports and combined rhetorically rather than analytically.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F093

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> Lemma 3 (χ(M⁺)=1) is inadequately proven. The arguments invoke 'fibrations' from projections with contractible fibers but never establish local triviality or bundle structure. Contractible fibers over a contractible base do not in general yield a contractible total space. The analysis contains inconsistent variable/domain descriptions, treats the cosθ=0 case incompletely, and the passage from equal masses to arbitrary masses via 'continuous deformation invariance of χ' is asserted without constructing an explicit homeomorphism or showing that M⁺ varies continuously in a topology-preserving manner as masses change.

**Arbiter's justification:**
> Both reviewers flag this (A-finding 4, A-finding 5, B-findings 4-5). The Euler characteristic is the linchpin of the uniqueness argument: α₀ = χ(M⁺) = 1 forces exactly one minimum. If χ(M⁺)=1 is not established, the entire Morse counting argument collapses. The topological claims are hand-wavy and miss standard requirements for the tools invoked. Since this is not an auxiliary lemma but a load-bearing step, its failure is fatal to the main theorem.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F094

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript calculates that anthropogenic CO2 is only ~4.3% of atmospheric CO2 (~18 ppm) by dividing annual human emissions (32.7 Pg C/yr) by total gross carbon flux (~760 Pg C/yr). This is an invalid mass-balance calculation because natural gross fluxes are approximately balanced; the correct comparison is net anthropogenic emissions versus the net change in atmospheric concentration.

**Arbiter's justification:**
> Both reviewers independently identify this as a fundamental carbon-cycle accounting error. The observed rise in atmospheric CO2 from ~280 to ~420 ppm is quantitatively consistent with cumulative anthropogenic emissions (confirmed by isotopic and mass-balance evidence). Dividing emissions by gross throughput rather than comparing to the net atmospheric increase uses the wrong denominator and the wrong accounting identity. This error directly supports the manuscript's central claim that human CO2 is negligible, and its correction demolishes that claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F095

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> Claim 7's equivalence proof is incomplete: the induction-based argument does not rigorously verify that each intermediate token move preserves independence, that enough target vertices are available, and that tokens outside the currently discussed class do not create conflicts.

**Arbiter's justification:**
> Both reviewers flagged this. Reviewer A rated it retraction-worthy; Reviewer B called it a major revision issue but noted the proof is 'incomplete and unconvincing.' Since Claim 7 is the core equivalence statement required for kernelization, and the argument has multiple unverified steps, the main theorem is not established. The severity is at the retraction-worthy/major-revision boundary, but given that this is the proof's central mechanism, the higher rating is appropriate.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F096

- Paper: *How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

**Candidate finding (rated retraction-worthy):**
> The protocol purports to implement the partial transpose of a Gaussian channel via CV gate teleportation, but partial transpose is not a completely positive map. The paper never rigorously proves that the overall physically realized protocol (composition of beam splitters, squeezers, homodyne measurements, displacements, and entangled ancillae) yields a CPTP map on arbitrary input states. Without this proof, Theorem 5 and all downstream conclusions (noise polarization, entanglement distillation) are not established as statements about physical quantum operations.

**Arbiter's justification:**
> The entire paper's contribution hinges on physically realizing a channel transformation that corresponds to partial transposition. If this step is not proven to yield a valid quantum channel, the central theorem is unsupported. This is not a missing robustness check — it is an absent proof of the principal construction's physical validity. Both reviewers flagged this and both strengthened their assessment upon reflection. The slight residual uncertainty is because the composition of physical operations is inherently CPTP, so the real question is whether the effective channel matches the claimed form; but this matching is exactly what the paper fails to demonstrate rigorously.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F097

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Theorem 3.2 (main multiplication formula) proof is incomplete and unvalidated for the stated setting. The proof is transplanted from GLS07 (preprojective algebra / 2-CY setting) without verifying that the required hypotheses (constructibility, stratification, Euler characteristic arguments, Ext-symmetry) hold for the infinite-dimensional Jacobian algebra A of a semi-infinite quiver. Critical steps between equations (3.9) and (3.16) are not established.

**Arbiter's justification:**
> Both reviewers independently identify this as the paper's central result and both conclude its proof is not valid as written. This is not a matter of missing minor details—the entire argument framework depends on unverified assumptions about the algebraic and geometric setting. Without this theorem, the paper's main contributions collapse.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F098

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The Morse-theoretic argument is performed on M^+ (defined by I=I₀ and C=0 in the positive orthant), which is strictly larger than the space of planar realizable strictly convex quadrilateral configurations. The manuscript never proves that every critical point of U on M^+ corresponds to a realizable planar convex central configuration, nor that spurious algebraic critical points outside the geometric domain cannot occur. Uniqueness on M^+ does not imply uniqueness of geometric central configurations without such an equivalence.

**Arbiter's justification:**
> This is a theorem-domain mismatch at the heart of the paper. The stated theorem concerns planar convex central configurations, but the proof counts critical points on a larger algebraic set. Without proving the domains share the same critical-point structure, the central inference is invalid. Reviewer A identified this as retraction-worthy and defended it in reflection; Reviewer B raised related concerns about M^+ containing non-geometric points.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F099

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Proposition 4.3 (simplicity of L1⊗L2 iff Ext^1=0) contains a logically invalid or circular proof. The proof assumes that vanishing Ext implies the product of F-polynomials equals a single cluster monomial, which is what needs to be proved. The contradiction argument for the 'only if' direction unjustifiably assumes all summands Y in the multiplication formula must equal T.

**Arbiter's justification:**
> Both reviewers agree the proof is flawed. This proposition is the key bridge between the multiplication formula and the paper's advertised application to quantum affine algebra representations. A logically invalid proof of a central application-level result means the paper's conclusions about tensor product simplicity are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F100

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Analytical validation table reports impossible values: negative LOD and LOQ (e.g., kidney LOD = -587.51 µg/kg, LOQ = -1780.34 µg/kg) and R² values exceeding 1.0 (e.g., muscle R² = 6.96), while other matrices show near-zero R² (skin R² = 0.002) yet are still used for quantitation.

**Arbiter's justification:**
> LOD/LOQ are defined as positive multiples of SD/slope and cannot be negative under any valid calibration. R² is bounded [0,1] by definition. These are mathematical impossibilities that indicate fundamental errors in the calibration/validation procedure. Since all tissue concentration data and all derived PK parameters depend on the validity of the LC-MS/MS assay, these impossible validation metrics invalidate the entire quantitative foundation of the paper.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F101

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> Systematic mismatch between gravimetric and areal capacitance values. At 5 mg/cm² loading, 1502 F/g should correspond to ~7.51 F/cm², but the paper reports 4.39 F/cm²—a ~42% discrepancy. Similar mismatches exist for the other electrode materials.

**Arbiter's justification:**
> This is an independent arithmetic inconsistency in the same core metric, reinforcing that the normalization process is fundamentally flawed. Combined with the energy density error, it establishes a pattern of systematic calculation errors affecting the primary reported values. Both reviewers identified this, and Review B upgraded it to retraction-worthy in steelman. The discrepancy is too large (~42%) to be experimental error and too systematic to be a typo.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F102

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The claim that objects with superluminal recession velocity are unobservable ('we simply can't detect any light signal from the CO') is false in standard FLRW cosmology.

**Arbiter's justification:**
> Many observed galaxies had or have superluminal recession speeds depending on the definition used, yet are readily observable. This statement reveals a fundamental misunderstanding of the kinematic framework the paper relies on. Since the paper's entire mechanism depends on mapping recession velocity to SR aberration, this misconception propagates into all results.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F103

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> The reported specific capacitance of 1502 F/g at 1.0 A/g in a 0.65 V window in aqueous KOH is physically implausible. This corresponds to ~271 mAh/g equivalent capacity, exceeding known pseudocapacitive material limits in such a narrow window. Combined with a moderate BET surface area (61.43 m²/g), the implied areal capacitance (~24.4 F/m²) is far beyond established double-layer or pseudocapacitive limits.

**Arbiter's justification:**
> While plausibility arguments alone can be debatable, here the implausibility is extreme and is corroborated by multiple independent calculation errors (broken formulas, arithmetic inconsistency). The convergence of an implausible number with demonstrably flawed calculation methods strongly indicates the value is erroneous. Reviewer B rated this retraction-worthy; Reviewer A's formula-error findings provide the mechanistic explanation for why the number is wrong. Together this meets the threshold.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F104

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> Referenced Table 1 and Figures 1–3 containing experimental results are absent from the manuscript. No quantitative data, numerical comparisons, variance estimates, or statistical outputs are actually presented, yet the paper makes specific claims (20% IoU improvement, 30% speed reduction).

**Arbiter's justification:**
> The paper's central conclusions are empirical and comparative. The complete absence of results data means there is zero evidential support for the headline claims within the manuscript. This is not a formatting gap—it is an empty results section with unsupported assertions. Both reviewers rated this RETRACTION-WORTHY and defended it through reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F105

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> Sex-specific schizophrenia kinase perturbation claims are unsupported because there is one pooled sample per sex-by-diagnosis cell, making interaction or sex-stratified disease effects impossible to estimate.

**Arbiter's justification:**
> Establishing a sex-specific disease effect requires replication within each sex-by-diagnosis cell or a model with subject-level data. One pool per cell (female control, female SCZ, male control, male SCZ) cannot support such claims. These sex-specific findings are highlighted prominently in figures, results, and discussion, making them central rather than peripheral conclusions. This is a direct corollary of the pooling design flaw but targets a particularly emphasized and especially untenable claim category.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F106

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 3.2 contains a flawed contradiction/limiting argument translating the barrier estimate into exponential decay of κ(t). Reviewer A identifies that the inequality direction is reversed — the two lower bounds on I_A^2 do not imply the ordering needed for the contradiction. Reviewer B identifies that the constant C depends on A and C→+∞ as A→0, so e^{-BT-C}→0 and the exponential expressions cannot be treated as fixed in the limit, destroying the contradiction.

**Arbiter's justification:**
> This is the step that converts the isoperimetric estimate into the curvature decay claim, which is the paper's principal conclusion. Both reviewers find independent reasons why this step fails. Whether the issue is inequality direction (Review A) or singular dependence on A (Review B), the result is the same: the claimed estimate κ(t)−1 ≤ (κ(0)−1)e^{-2t} is not established.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F107

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> Claim 3 (interior vertices from different X-pairs are non-adjacent) relies on planar embedding arguments with 'cycles' that are not guaranteed to exist as cycles in the graph. The proof conflates geometric embedding intuition with combinatorial graph structure without a rigorous Jordan-curve-type argument.

**Arbiter's justification:**
> This claim is repeatedly invoked to guarantee that different X-pair classes are independent, which underpins the decomposition into a linear forest structure and the counting arguments. Both reviewers flag it as seriously flawed. Reviewer A upgraded to RETRACTION-WORTHY on reflection; Reviewer B rated it RETRACTION-WORTHY throughout. The claim is central enough that its failure cascades through multiple later arguments.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F108

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The central equivalence between temporal/frequency combining gain and transmit beamforming gain is not established under consistent power, rate, and bandwidth normalization. The paper treats T-fold matched-filter integration over time-frequency degrees of freedom as a no-loss replacement for N-antenna spatial beamforming gain, without specifying or enforcing equal total energy, equal average power, equal throughput, equal bandwidth, and equal latency. Under standard communication-theoretic normalization, temporal processing gain and spatial array gain are distinct quantities; the claimed equivalence collapses into a trivial resource tradeoff.

**Arbiter's justification:**
> This is the paper's headline claim. Both reviewers independently identified this as the most critical flaw. Reviewer A rated it RETRACTION-WORTHY from the start and defended it vigorously in reflection. Reviewer B's finding #10 evolved toward RETRACTION-WORTHY during reflection. If the normalization is corrected, the paper's central conclusion—'no loss in link budget gain compared to spatial beamforming'—is either false or becomes a trivially obvious time-bandwidth tradeoff, which is not the claimed contribution. This is not fixable by adding experiments; it requires abandoning or fundamentally reformulating the core thesis.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F109

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The manuscript uses an ε-dependent finite gate set while framing its contribution as addressing the fixed finite universal gate-set approximation problem (Nielsen–Chuang challenge / Solovay-Kitaev improvement). An ε-indexed family of finite sets is fundamentally different from a single fixed finite set.

**Arbiter's justification:**
> This is a problem-definition error, not a presentation issue. The paper explicitly states gates are 'chosen from a finite set depending on the value of ε.' Standard lower bounds and comparisons to Solovay-Kitaev do not apply when the generating set changes with target precision. Reviewer A identified this; Reviewer B acknowledged it as a missed finding they would rate RETRACTION-WORTHY. The paper does not solve the problem it claims to address.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F110

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> The manuscript's central claim that exosomes significantly reduce pro-inflammatory cytokines is directly contradicted by its own reported p-values: three of four cytokines (TNF-α, IFN-γ, IL-17) show non-significant differences (p=0.055, 0.327, 0.627) in the key exosome-treatment condition, yet the text claims 'all our results demonstrated a significant difference.'

**Arbiter's justification:**
> This is not overstatement or spin — it is a direct logical contradiction between the narrative conclusion and the reported statistical results. If 75% of the primary outcome comparisons are non-significant by the paper's own analysis, the central conclusion that exosomes suppress hyperinflammation is unsupported. This meets the retraction threshold: the paper's central conclusions cannot be supported by the data as presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F111

- Paper: *Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

**Candidate finding (rated retraction-worthy):**
> The XRD discussion contains extended text about 'Fe-Al-based mesoporous metal oxides,' 'BMO,' and 'Cu Kα peaks in BMO' that are entirely irrelevant to a fish-bone hydroxyapatite study, indicating text recycling or contamination from an unrelated manuscript.

**Arbiter's justification:**
> The presence of clearly unrelated scientific content in the results/discussion section indicates either plagiarism, text fabrication, or such severe carelessness that the integrity of the entire analytical interpretation is called into question. If confirmed as recycled text, readers cannot trust that the XRD interpretation actually corresponds to the samples studied. This undermines a core characterization pillar of the paper.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F112

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The numerical example showing temporal combining gain exceeding 12 dB (the 16-antenna beamforming gain) when T = 18.375 > N = 16, and claims of 15 dB gain for T = 46, N = 32, are strong indicators that the gain metric is not physically comparable to beamforming gain and likely double-counts processing gain from reduced symbol density.

**Arbiter's justification:**
> Both reviewers flag this. Exceeding the coherent array gain in a fair comparison would require consuming additional resources. The manuscript presents this as an advantage without identifying what resource was additionally consumed, which is a hallmark of a flawed normalization. This finding is tightly coupled to the first two and collectively they invalidate the paper's primary conclusion.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F113

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The proof that M^+ is contractible (Lemma 3), hence χ(M^+)=1, is invalid. The manuscript invokes 'fibration' language without establishing fibrations or local triviality, describes fibers incorrectly (e.g., quarter-circle arcs claimed contractible without justification, variable-plane inconsistencies), and draws contractibility conclusions that do not follow from the stated constructions. The topology of M^+ as a nonlinear algebraic set in the positive orthant is non-trivial and is not established by the given argument.

**Arbiter's justification:**
> The Morse counting relation Σ(-1)^q α_q = χ(M^+) = 1 is the sole mechanism yielding uniqueness. If χ(M^+) is not established, the main theorem has no proof. Both reviewers agree this is a fundamental failure after reflection. Reviewer A identified it as retraction-worthy from the start; Reviewer B upgraded it to retraction-worthy in reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F114

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> The proof of Lemma 2.3 contains an invalid maximality contradiction: the argument constructs W:=U∪V' and claims W∈𝒫 by asserting disjointness of translates x+W and y+W for distinct x,y∈L. However, only same-type disjointness ((x+U)∩(y+U)=∅ and (x+V')∩(y+V')=∅) is established. The mixed intersections (x+U)∩(y+V') and (x+V')∩(y+U) are never shown empty, so the disjointness of x+W and y+W does not follow. Without this, the contradiction to maximality fails and item (2) of the lemma (that the complement of L+U has empty interior) is unproved.

**Arbiter's justification:**
> This is a definitive logical non sequitur internal to the written proof, not a mere gap or missing citation. Lemma 2.3 is the sole mechanism for producing the dense subgroup in the main theorem's only nontrivial case. Both reviewers independently flagged this lemma as fatally flawed. Reviewer A's specific identification of the mixed-intersection failure is a clean, precise error that survives charitable reconstruction—even granting V' is non-empty and open, the proof still does not establish what it needs. The manuscript's central conclusion cannot be supported without this lemma.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F115

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The contradiction argument in Theorem 3.2 misuses the 'tightness' of the small-area asymptotic: having two lower bounds on I_A^2 that both approach the true value as A→0 does not produce the inequality in the direction needed for contradiction.

**Arbiter's justification:**
> Reviewer A identifies this as an independent logical error in the paper's main theorem: tightness of one lower bound does not imply it dominates another lower bound. Reviewer B corroborates by noting the inequality direction is wrong. Since Theorem 3.2 is the paper's central result and this step is the only bridge from the profile estimate to curvature decay, its failure is independently fatal even if Proposition 3.1 were somehow rescued.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F116

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The manuscript does not solve the stated problem of approximation from a fixed finite gate set. The gate set {H, P(πℓ/2^m)} depends on ε through m, and the set of allowed rotations P(πℓ/2^m) for ℓ < 2^m contains O(2^m) elements that grow with 1/ε. This fundamentally changes the problem and makes comparisons to the Solovay-Kitaev theorem and the Ω(log(1/ε)) lower bound meaningless.

**Arbiter's justification:**
> Both reviewers identify this independently. The central framing of the paper is as an advance on the finite-gate-set synthesis problem. An ε-dependent gate set of exponential size trivializes the problem entirely (one could simply include the target gate). This is not a matter of interpretation—the paper explicitly acknowledges varying the gate set with ε but dismisses the issue, which is the core theoretical challenge.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F117

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The maximum-principle comparison in Proposition 3.1 is not justified. I_A is defined as an infimum over separating curves enclosing area A, not as a smooth scalar field satisfying a parabolic PDE in a spatial variable. The evolution equation (2.5) involves a second-derivative term ∂_r² ln I_A² whose sign is not controlled, and no subsolution/supersolution structure is established that would permit comparison with the spatially constant ODE barrier f(t). This is a categorical misapplication of the maximum principle.

**Arbiter's justification:**
> Both reviewers flagged this as retraction-worthy. Reviewer B upgraded their confidence after the steelman exchange. Reviewer A's steelman reinforced the point by noting the conceptual mismatch between profile-level infima and pointwise PDE solutions. This proposition is the engine of the entire proof; its failure collapses the main theorem.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F118

- Paper: *Large Bricks and Join-irreducible torsionfree classes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> There is a logical gap in the proof of Proposition 3.9, meaning that a necessary step or justification is missing, so the conclusion does not properly follow from the premises given.

**Candidate finding (rated retraction-worthy):**
> Lemma 3.7 unjustifiably concludes that any nonzero map from a lim→f-simple module F to a simple object S in the HRS heart must be a monomorphism 'by simplicity of F.' The module F has only been shown to be lim→f-simple in the module category, not simple in the heart. No proof or reference bridges these two notions, and Proposition 3.5 (which connects torsionfree almost-torsion modules to simple objects in the heart) applies to a different class of modules. This step is essential for embedding F into a brick B, which is the core of the main theorem.

**Arbiter's justification:**
> Both reviewers identify this as a critical unsupported implication. Reviewer A calls it retraction-worthy; Reviewer B flags it as major-revision but acknowledges the step is needed for the final construction. The implication is not merely a gap in exposition—it conflates two distinct categorical notions (lim→f-simplicity in Mod-Λ vs. simplicity in the heart), and no known result bridges them automatically. Without this step, the main theorem's proof collapses.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F119

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> Theorem 1.4's constructive rotation step ('rotate E into region (9)') cannot produce swap-intolerant nonlocality because (a) CHSH is swap-invariant, and (b) the rotation changes the relationship between the β-vector and τ-vector, altering eigenvalues and positivity conditions in ways the proof does not account for.

**Arbiter's justification:**
> Even granting all auxiliary results, the final constructive step aims to produce an effect that is mathematically forbidden. Two independent problems (swap invariance from Reviewer A, uncontrolled eigenvalue changes from Reviewer B) each independently invalidate the construction. Both reviewers rate this retraction-worthy after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F120

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> The trapezoidal AUC formula is stated as (Cᵢ + Cᵢ₊₁)·Δt rather than the correct 0.5·(Cᵢ + Cᵢ₊₁)·Δt, which would double all AUC values if actually applied.

**Arbiter's justification:**
> AUC is the primary exposure metric and directly informs bioavailability estimates, tissue distribution comparisons, and withdrawal time calculations. If the stated formula was used, all AUC values are inflated by 2×, fundamentally changing PK interpretation. There is a small possibility this is only a typographical error in the equation while the calculation was done correctly, but given the other mathematical impossibilities in the paper, there is no basis to extend this benefit of the doubt.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F121

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Claim that 'no increase in floods, droughts, hurricanes, or extreme weather events' has been observed, contradicting IPCC AR6 documented increases in extreme precipitation intensity, heatwave frequency, and regional changes in drought and tropical cyclone intensity.

**Arbiter's justification:**
> Both reviewers flag this. The claim is presented as established fact using selective citations while ignoring comprehensive assessment reports. However, confidence is slightly lower because the extreme events literature is genuinely complex with regional heterogeneity, and some specific event categories (e.g., normalized hurricane damages) do have legitimate debate. The blanket 'no increase' claim nevertheless misrepresents the overall evidence.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F122

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Theorem 2.3 (a structural result about the Gabriel quiver) is essentially unproved. The manuscript promises a computation but does not carry it out, instead invoking BIRS09 from a different (2-CY) framework without verifying that its hypotheses apply to the present setting.

**Arbiter's justification:**
> Reviewer A identifies this as RETRACTION-WORTHY; Reviewer B does not separately flag it but the concern is implicitly covered by the cascading dependency analysis. The proof as written consists of an unverified citation transfer and an absent calculation for an advertised structural result. However, I note slightly lower confidence because it is conceivable that the BIRS09 result does apply with additional checking—the gap is more clearly one of missing verification than of demonstrated impossibility. Still, as a flagship theorem with no valid proof in the manuscript, it meets the retraction threshold.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F123

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> Energy density and power density are computed from three-electrode half-cell data and presented as supercapacitor device performance metrics. The specific energy formula used (SE = Cs×ΔV²/7.2) appears to omit the factor of ½, yielding ~61 Wh/kg instead of the correct ~44 Wh/kg (using Cs = 1502 F/g and ΔV = 0.65 V with the standard E = 0.5·Cs·ΔV²/3.6). This inflated headline result is the paper's central performance claim.

**Arbiter's justification:**
> Both reviewers flagged this. The combination of (a) using a three-electrode potential window to compute device-level energy/power density and (b) an incorrect formula that over-estimates SE by roughly 40% means the paper's primary quantitative conclusion—outstanding energy density for supercapacitor application—is fundamentally unsupported by the data as presented. Recalculation with the correct formula and appropriate device-level methodology would yield substantially different numbers, invalidating the comparison tables and the paper's positioning against the literature.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F124

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> Section VI contains invalid graph-complement identities: claims C₅^{∨m} = C̄₅^{⊠m} = C₅^{⊠m}, conflating complement of product with product itself.

**Arbiter's justification:**
> For self-complementary G, one has complement(G ∨ H) ≅ Ḡ ⊠ H̄ ≅ G ⊠ H (using self-complementarity), but this gives complement(G^{∨m}) ≅ G^{⊠m}, NOT G^{∨m} = G^{⊠m}. The paper equates a graph with its complement, which for nontrivial graphs is false. The claimed exact value R_quantum(g) = ½ log₂ 5 for the C₅ example depends on these identities. Since this is the paper's central showcase of quantum advantage, the quantitative separation is unestablished.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F125

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The derivation of inequality (15) contains an indexing/aggregation error where the right-hand side depends on a single j while the left-hand side sums over all j. The subsequent averaging to define S_{x'}(x) does not resolve this mismatch.

**Arbiter's justification:**
> Review A identifies this specifically; Review B covers it implicitly under general proof incompleteness. This is inside the core derivation chain. However, there is some possibility this is a notational/expository error that could be clarified (e.g., the inequality might hold for each j separately and then be summed). Given some residual uncertainty about whether this is a true logical error versus a presentation error, confidence is slightly lower, but it is still classified as retraction-worthy because as written the derivation does not work.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F126

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> The claim that (Z, ⊙_{l,k}) is an abelian group when l | k(k-1) is false. The operation ⊙_{l,k} corresponds to multiplication on lZ+k under the isomorphism x ↦ lx+k, and invertibility fails in Z in general (e.g., l=1, k=1 gives x ⊙ y = xy+x+y, where x=1 has no inverse). This is a foundational algebraic error on which downstream Stone–Čech compactification and ideal arguments depend.

**Arbiter's justification:**
> The entire framework of transferring ideal structure and idempotent arguments through (βZ, ⊙_{l,k}) depends on correct identification of the algebraic object. If (Z, ⊙_{l,k}) is not a group, the semigroup structure of its Stone–Čech extension is different from what is assumed, and minimal ideals, idempotents, and central sets behave differently. This affects Theorems 4.8, 4.10, 4.11, and Corollary 4.12. However, there is some possibility the authors intend a restricted domain or the error is partially recoverable for semigroup (not group) arguments, hence not absolute certainty.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F127

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The manuscript presents two fundamentally different and incompatible methods (MSP-MVS and TSAR-MVS) as a single contribution. MSP-MVS uses Semantic-SAM for multi-granularity segmentation prior, anchor equidistribution, and iterative local search, while TSAR-MVS uses Roberts edge detection, Hough line detection, confidence-based outlier filtering, superpixel RANSAC refinement, and textureless-aware segmentation. The title, abstract, and conclusion refer to MSP-MVS, but large central sections describe TSAR-MVS. No explanation of the relationship between the two methods is provided.

**Arbiter's justification:**
> Both reviewers independently identified this as the central fatal flaw. The experimental results cannot be attributed to a single, well-defined method. The reader cannot determine which algorithm was actually implemented and evaluated. This is not an editorial oversight but a structural inconsistency that breaks the fundamental scientific contract: the method must be uniquely defined for results to be meaningful. All benchmark claims, state-of-the-art assertions, and generalization conclusions are rendered unsupported because the evaluated system is undefined.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F128

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Conflation of CO₂ molecular residence time (~3-5 years) with the perturbation lifetime of anthropogenic CO₂ (centuries). The manuscript uses rapid molecular exchange to argue that anthropogenic CO₂ cannot accumulate, ignoring ocean buffering chemistry and multi-reservoir dynamics.

**Arbiter's justification:**
> Both reviewers flag this as a well-known, basic carbon-cycle error. The distinction between individual molecular turnover and net perturbation removal is foundational. This error directly supports the paper's central claim that human CO₂ emissions are inconsequential, and its correction would eliminate that conclusion. Isotopic evidence (δ¹³C, ¹⁴C) independently confirms the anthropogenic origin of the CO₂ increase, which the manuscript ignores.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F129

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The ablation study components (w/o. SAM, w/o. Her, w/o. Agr., w/o. CRF., w/o. Equ., etc.) do not map cleanly onto either method description, making the causal evidence for the paper's claimed contributions uninterpretable.

**Arbiter's justification:**
> Both reviewers identified this. The ablations are supposed to establish which components drive performance, but if the evaluated system includes modules from both MSP-MVS and TSAR-MVS pipelines (or only one, but it's unclear which), the ablation evidence is logically disconnected from the stated contributions. Review A upgraded this to borderline RETRACTION-WORTHY after steelmanning. Combined with the identity-confusion finding, this collapses the paper's mechanistic claims.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F130

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Corollaries 4.12 and 4.14 state equations involving the operation ⊕_{l,k}, which is never defined anywhere in the manuscript. The proof of Corollary 4.12 concludes with ⊕_{l,k} rather than ⊙_{l,k}. Since the paper's contribution is precisely new partition-regular equations under a specifically defined operation, using an undefined operation in the final stated results renders them mathematically meaningless.

**Arbiter's justification:**
> These are the paper's highlighted end-products (Corollary 4.12 is the abstract's main claim answering Di Nasso's question). The conclusions are literally stated using an undefined mathematical object. Combined with the upstream proof failures, this cannot be dismissed as a harmless typo.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F131

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> The Horodecki criterion is derived and proven only for valid quantum states (positive semidefinite, trace 1). The manuscript applies this criterion to operators with negative eigenvalues without providing any justification that the criterion retains meaning for non-physical operators. The concept of 'nonlocality' (violation of local hidden variable models via Bell-CHSH inequality) is undefined for non-PSD matrices because measurement probabilities can become negative.

**Arbiter's justification:**
> Both reviewers flag this issue. Even setting aside the swap-invariance problem, the paper's entire framework—extending the Horodecki nonlocality criterion to non-physical operators and interpreting M>1 as 'nonlocality'—lacks any mathematical or physical foundation. The Horodecki theorem's proof relies on properties specific to quantum states. Applying its formula to non-states and drawing conclusions about nonlocality is a category error. Combined with the swap-invariance issue, this further confirms the paper's conclusions are fundamentally unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F132

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Theorem 3.3: The proof claims cl(K(βℤ,+)) is a left ideal in (βℤ*,⊙_t), but the key step — that the affine image t(t+1)−tn+(n−t)B is additively piecewise syndetic whenever B is — is unjustified and concretely fails when n=t, where the image collapses to a singleton. This theorem produces the ultrafilter intersection that drives all main partition-regularity results.

**Arbiter's justification:**
> Both reviewers identify this as the critical bottleneck. Reviewer A initially rated it RETRACTION-WORTHY and maintained this through steelman. Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman, explicitly acknowledging the n=t counterexample. The degenerate case is concrete and undeniable, and no alternative argument is provided. Since Theorems 4.10, 4.11, and Corollary 4.12 all require the ultrafilter intersection that this theorem is supposed to produce, the central conclusions are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F133

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> All downstream results—BMM in O(n^{25/9} log n) (Theorem 3), k-clique in O(n^{7k/9}) (Theorem 4), Max-Cut (Theorem 5), and numerous corollaries—depend entirely on the correctness of the triangle detection algorithm (Theorem 2) and therefore collapse if Theorem 2 is invalid.

**Arbiter's justification:**
> Both reviewers agree that these are pure corollaries of Theorem 2 via standard reductions. None is independently established. Since the base result is broken, the derived claims are unsupported. The paper's headline claims about invalidating the combinatorial k-clique conjecture and related conjectures are therefore unjustified.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F134

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Misrepresentation of greenhouse physics: the manuscript states the IPCC explanation 'makes no sense scientifically' and is 'immediately falsified,' but provides no correct radiative-transfer derivation and ignores radiative-convective equilibrium, emission-level arguments, spectroscopy evidence, and the well-verified spectral fingerprint of greenhouse forcing.

**Arbiter's justification:**
> Both reviewers identify this. The paper's central thesis is that greenhouse-gas warming lacks scientific basis. A wholesale mischaracterization of the underlying physics — attacking straw mechanisms rather than the actual theory — invalidates this central conclusion.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F135

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript conflates atmospheric CO2 residence time (the average time an individual molecule stays in the atmosphere) with the perturbation adjustment time (the timescale for an excess concentration to decay). It uses seasonal exchange and short residence times to argue that anthropogenic CO2 cannot persist long enough to matter.

**Arbiter's justification:**
> This is a well-documented category error in carbon-cycle science. A short molecular residence time does not imply rapid removal of a concentration perturbation when gross fluxes are approximately balanced. The manuscript uses this conflation to claim human CO2 contributions are transient and inconsequential—a claim that directly supports its conclusion that anthropogenic climate change is negligible. Reviewer A rates this RETRACTION-WORTHY and defends it; Reviewer B acknowledges and upgrades to RETRACTION-WORTHY in reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F136

- Paper: *How to surpass no-go limits in Gaussian quantum error correction and entangled Gaussian state distillation?*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the statements or proofs of Lemma 3 and Lemma 4 contain inaccuracies, likely due to incorrect assumptions, logical gaps, or invalid mathematical steps, which compromise the validity of their conclusions.

**Candidate finding (rated retraction-worthy):**
> The protocol requires ideal infinitely squeezed EPR states (infinite energy, non-normalizable), yet the paper frames its construction as relying on 'local Gaussian resources' and draws practical conclusions about Gaussian QEC and entanglement distillation. The finite-squeezing analysis (Appendix G) provides only state-level fidelity bounds, not channel-level error analysis (e.g., diamond norm, induced noise parameters), and does not demonstrate that noise polarization or distillation survives with realistic squeezing levels.

**Arbiter's justification:**
> The key lemmas (2, 3) and the resulting noise-polarization theorem hold exactly only in the unphysical infinite-squeezing limit. For any finite squeezing, the protocol introduces additional noise that is never quantified at the channel level. Since the paper's headline claim is about circumventing Gaussian QEC no-go results with physical resources, and this circumvention is only demonstrated in an unphysical limit, the central practical conclusions are unsupported. Both reviewers agree this is at minimum a devastating flaw. The confidence is somewhat lower because a sufficiently careful finite-squeezing analysis might rescue a weaker version of the result, but such analysis is entirely absent.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F137

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> Proposition 1 asserts G ⊠ H = G̅ ∨ H̅ (or equivalently that the strong product equals the OR product). This is false under the manuscript's own definitions. In the OR product, adjacency in one coordinate suffices regardless of the other; in the strong product, the non-adjacent coordinate must satisfy equality or adjacency. These are distinct graph products with different edge sets in general.

**Arbiter's justification:**
> This is not a typo but a fundamental graph-theoretic misidentification. The paper's framework distinguishes between G^(m), G^{⊠m}, and G^{∨m} and uses containment relations among them to derive bounds and equalities. If the paper simultaneously claims two of these benchmark products are identical when they are not, the entire product-based proof architecture becomes internally inconsistent. All subsequent inclusion-based arguments, parameter bounds, and rate calculations that depend on distinguishing these products are compromised.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F138

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The construction of x' is not rigorously specified to be independent of x, yet the proof framework requires a fixed x'. The manuscript's own Remark reveals that the construction depends on the factorization of x and x−a_j, making x' depend on x. Without a valid x-independent construction ensuring the required integrality and valuation properties, the deduction of the main theorems from Theorem 2.1 collapses.

**Arbiter's justification:**
> Both reviewers flag this. If x' depends on x, inequality (14) is not the fixed inequality it purports to be, and the entire argument structure is invalidated. Review A provides the more detailed analysis showing the dependency, while Review B notes the missing link between the algebraic construction and the analytic estimate. Neither reviewer sees a way to repair this within the manuscript's framework.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F139

- Paper: *The Art of Staying Ahead of Deadlines: Improved Algorithms for the Minimum Tardy Processing Time*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the runtime analysis omits the contribution of the processing times within the interval [d_j - p_j, d_{j - 1}], which leads to an incomplete and therefore incorrect calculation of the total processing time.

**Candidate finding (rated retraction-worthy):**
> The dynamic-string representation has internal inconsistencies regarding fixed string length. After splitting at position d_j - p_j, the resulting substring has length d_j - p_j + 1, not u = d_max + 1. Subsequent concat and split operations assume a common universe of size d_max + 1 but the actual string lengths do not match, making key algorithmic steps ill-defined.

**Arbiter's justification:**
> This affects the central algorithmic construction. Without a valid and consistent representation of the indicator strings under split/shift/merge, the core single-machine algorithm is not established. Both reviewers noted this: Reviewer A identified the specific length mismatch, and Reviewer B noted the operations are underspecified to the point of being unverifiable. The issue is fundamental to the paper's main contribution, though a careful rewrite with explicit padding/alignment conventions could potentially repair it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F140

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The derivation of the telescope acceptance-cone transformation (Eqs. 9–13) using SR aberration between distant source and observer frames is not a valid cosmological calculation of collected flux. Photon bundle transport in curved spacetime is governed by null geodesic deviation and optical scalars, not by a global SR solid-angle transformation.

**Arbiter's justification:**
> This is the specific mathematical step where the extra (1+z) enters. If the solid-angle transformation is invalid (and both reviewers argue it is), then Eqs. 13–16, the revised luminosity distance, and all cosmological consequences are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F141

- Paper: *From Tripods to Bipods: Reducing the Queue Number of Planar Graphs Costs Just One Leg*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 4.2 is incorrect, so the proof relying on it is invalid and requires new technical details to correct the decomposition argument.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 4.9 (the key 38-queue bound) is incomplete, containing explicit draft markers, duplicated/reordered proof fragments, undefined queue families, and no finished queue assignment or non-nesting verification. The manuscript's headline numerical claim is therefore unsupported.

**Arbiter's justification:**
> Both reviewers agree the proof is unfinished. Reviewer A identified draft markers, corrupted text, and undefined objects; Reviewer B acknowledged in reflection that the 'DRAFT' marker makes the 38-queue claim unverifiable. A queue-number proof requires an exact partition of edges into queues and a complete non-nesting argument for each queue class. Neither is present. This is not a gap in an otherwise complete argument—it is an absent proof of the central claim. Under the key test, confirmation of this finding means the paper's headline result requires complete re-proving, which meets the RETRACTION-WORTHY standard.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F142

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The main gate-count complexity claim is internally inconsistent and mathematically impossible. The paper states a gate count of O(ε log(1/ε) log log(1/ε) ···) which decreases as ε→0, and the recursion structure (angle-doubling with constant gates per level) yields at most O(m) = O(log(1/ε)) gates, not the iterated-log product claimed. The choice of m and the precision allocation are mutually contradictory.

**Arbiter's justification:**
> The paper's sole headline contribution is an asymptotic scaling theorem. Both reviewers independently identify that the scaling formula is impossible (gate count decreasing with accuracy demand) and that the recursion structure cannot produce the claimed complexity. The derivation contains contradictory precision budgets (δ ≤ ε/⌈log₂(1/ε)⌉ vs. later claiming error ε·log(1/ε)·loglog(1/ε)···) and an asymptotically nonsensical choice of m. These are not isolated typos but pervasive failures in the proof of the central result. Without a valid derivation, the main theorem is unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F143

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Invalid inference from annual anthropogenic flux being a small fraction of gross natural fluxes to the claim that human contribution to atmospheric CO₂ is negligible. The relevant quantity is net imbalance, not gross source fraction.

**Arbiter's justification:**
> Both reviewers flag this. Natural fluxes are approximately balanced; the anthropogenic addition is a net perturbation to a near-equilibrium system. This is a basic stock-flow accounting error that directly underlies the paper's claim that human CO₂ is too small to matter.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F144

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Section 4.8's generalization to ⊙_{l,k} silently changes the hypothesis from l | k(k−1) to l | (k−1) without justification. The generalized partition-regularity theorems (4.10–4.14) are stated under the different condition, and there is no coherent reconciliation.

**Arbiter's justification:**
> Combined with the false group claim above, this means the generalized framework has no stable, coherent set of hypotheses. The later theorems cannot be evaluated because it is unclear under what conditions they are even intended to hold.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F145

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The final asymptotic complexity statement is internally inconsistent. The conclusion states O(ε log(1/ε) log log(1/ε) ···) gates, which tends to 0 as ε→0 and is nonsensical for a gate count. Earlier sections claim O(log(1/ε) log log(1/ε) ···). The formula for m in the conclusion also appears dimensionally incorrect.

**Arbiter's justification:**
> Both reviewers note this inconsistency. While one instance could be a typo, the coexistence of multiple inconsistent formulas for the same quantity (m, gate count, angle precision) across different sections suggests the derivation itself is not controlled. The paper's main quantitative claim—the asymptotic gate count—cannot be determined from the manuscript.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F146

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The ablation studies describe components (e.g., 'edge correction (w/o. CRF)', 'aggregation (w/o. Agr.)', 'sector averaging', 'anchor clustering') that are not defined in the main methods section and do not clearly correspond to either the MSP-MVS or TSAR-MVS pipeline descriptions. The ablations cannot be mapped to a specific, coherent method.

**Arbiter's justification:**
> Ablation studies are the primary evidence for the contribution of individual components. When the ablated components cannot be matched to the described method—and the method itself is ambiguous between two different systems—the ablation evidence is meaningless. This compounds the core inconsistency and independently undermines the paper's claims about which components drive performance. Both reviewers flagged this, though Reviewer A classified it as retraction-worthy and Reviewer B as major-revision. Given the direct coupling to the identity confusion, retraction-worthy is appropriate.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F147

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> Equation (4) identifies cosmological redshift with the pure SR Doppler formula and Eq. (5) uses it to define a global recession velocity for all redshifts, which is then used to parameterize aberration. This identification is not generally valid in FLRW cosmology and is the direct input to the flawed aberration derivation.

**Arbiter's justification:**
> While one can formally decompose cosmological redshift into chains of infinitesimal Doppler shifts, one cannot extract a single global SR velocity and then apply finite-boost aberration formulas as if source and observer shared a Minkowski chart. This is not a matter of convention but a misapplication of SR in curved spacetime. The entire quantitative framework collapses without this step.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F148

- Paper: *Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

**Candidate finding (rated retraction-worthy):**
> The definition of f̃_{j_i}(x) in equation (2.10) depends on U_{k,γ}, which is constructed from period integrals of φ_C(U_k). The claimed 'explicit algebraic description' of complex conjugation therefore depends on the very transcendental periods it purports to describe algebraically, creating a vicious circle.

**Arbiter's justification:**
> The paper's central contribution is an explicit algebraic formula for complex conjugation on de Rham cohomology. If that formula requires knowing the periods first, it is not algebraic in any meaningful sense—it reduces to a formal tautology. Reviewer B identified this as the core structural flaw; Reviewer A acknowledged it as a new error in reflection. This is independently fatal: even if the equality-vs-conjugation issue were resolved, the formula would still fail to deliver what is promised.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F149

- Paper: *Every Polish group has a non-trivial topological group automorphism*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that extending a non-trivial automorphism of L by fixing elements of a maximal independent subset Y of U can inadvertently redefine the automorphism on elements of L that are generated by Y, making the extension invalid.

**Candidate finding (rated retraction-worthy):**
> Lemma 2.3: The Zorn's lemma argument is invalid. The union U_I = ⋃_α U_α of a chain of identity neighborhoods is not shown to be an identity neighborhood (i.e., an element of the poset). Neighborhoods of the identity in a topological group must satisfy specific properties that arbitrary unions need not preserve. Without verifying the poset is inductive, the maximal element U is not obtained.

**Arbiter's justification:**
> Reviewer A identifies a concrete mathematical error: the upper bound construction fails because the union of identity neighborhoods need not be an identity neighborhood. This is not a gap that can be trivially filled—it is a fundamental flaw in the Zorn's lemma application. Lemma 2.3 is a critical building block for the main theorem. Reviewer B also flags problems with Lemma 2.3 but rates it MAJOR-REVISION; however, Reviewer A's more detailed analysis is persuasive that the error is structural rather than merely a matter of missing justification.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F150

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Conflicting Tmax statements for the same tissue: gill peak concentration is reported at 3 h, 6 h, and 8 h in different passages of the manuscript.

**Arbiter's justification:**
> Tmax is a basic descriptive statistic read directly from concentration-time data. Three different values for the same tissue in the same experiment indicate profound inconsistency in the core data reporting. This, combined with the contradictory half-lives for gill, indicates that the PK results section is unreliable at the most fundamental descriptive level.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F151

- Paper: *Large Bricks and Join-irreducible torsionfree classes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> There is a logical gap in the proof of Proposition 3.9, meaning that a necessary step or justification is missing, so the conclusion does not properly follow from the premises given.

**Candidate finding (rated retraction-worthy):**
> Lemma 3.7 conflates module-theoretic simplicity (every proper quotient is torsion) with simplicity in the HRS heart. The proof claims a nonzero map F → S must be a monomorphism 'by simplicity of F,' but F is lim→f-simple as a module, not simple in the heart. The deduction that F embeds into the torsionfree almost-torsion module B is the sole bridge from the direct limit construction to a single cogenerating brick, and it fails.

**Arbiter's justification:**
> Reviewer A initially rated RETRACTION-WORTHY; Reviewer B initially rated MAJOR-REVISION but upgraded to RETRACTION-WORTHY during steelman after recognizing the conceptual depth of the error. The conflation of two distinct notions of simplicity is structural, not a typo or missing citation. Without a valid embedding F ↪ B, the entire proof pipeline from the direct limit object to a single cogenerating brick collapses.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F152

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> Claim 7's induction proof does not verify that each proposed token jump preserves independence globally. The assumption 'no token appears on the closed neighborhood of z''_{i-1}' is stated without justification, effectively assuming what needs to be proved.

**Arbiter's justification:**
> Claim 7 is the core equivalence proof for the kernel. Token jumping requires every intermediate configuration to be independent. The proof does not check this, making the reduction's correctness unestablished. Both reviewers identify this; Reviewer A calls it retraction-worthy, Reviewer B calls the equivalence proof retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F153

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> The degradation experiments lack all essential controls: no dye + sunlight without catalyst (photolysis control), no dye + catalyst in dark (adsorption control), no tea-extract-only control, and no nanoparticle optical blank subtraction.

**Arbiter's justification:**
> Both reviewers independently identified this and both maintained or strengthened it on reflection. The paper claims photocatalytic degradation by SBT-AgNPs, but the design cannot distinguish photocatalysis from direct photolysis, adsorption, scattering artifacts, or extract effects. The causal claim is untestable from the presented experiments. New experiments, not editorial corrections, would be needed.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F154

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> The application of Theorem 4.9 in Theorems 4.10 and Corollary 4.12 conflates ultrafilter membership across different semigroup operations. Theorem 4.9 requires an ultrafilter to satisfy two equations in a compatible sense, but the two equations involve different operations (additive vs. ⊙_{l,k}). The paper assumes a single set A ∈ p simultaneously contains additive structure (arithmetic progressions) and ⊙_{l,k}-structure (IP sets) without combinatorial intersection arguments.

**Arbiter's justification:**
> This directly undermines the paper's claimed main result and the affirmative answer to Di Nasso's question. Reviewer B identifies this as the critical methodological flaw. However, there is some possibility that the intended argument uses the dual membership of p in both structures more carefully than written, so confidence is slightly lower.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F155

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> Proposition 3.1's geometric argument that semi-trivial perp states cannot be simultaneously positive-semidefinite and nonlocal is incorrect. The inequality |E| > 1 does not force the smallest eigenvalue negative because the radii r_+ and r_- depend on adjustable parameters τ_p. Appropriate choices of τ_p can yield |E| > 1 with nonnegative eigenvalues.

**Arbiter's justification:**
> This proposition is a key logical pillar: it motivates the necessity of leaving the PSD set and aligns the positivity boundary with the nonlocality boundary. If it is false, the entire constructive strategy collapses independently of the swap-invariance issue. Reviewer B identified this clearly; Reviewer A flagged the unverified optimization. Both agree it is fatal after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F156

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The asymptotic gate count is internally self-contradictory. The paper claims O(log(1/ε) log log(1/ε) log log log(1/ε)···) in one place but O(ε log(1/ε) log log(1/ε)···) elsewhere; the latter decreases with smaller ε, which is impossible for a compilation cost. The definition m = ceil(ε / [log(1/ε) log log(1/ε)···]) has the wrong scaling direction (m→0 as ε→0 instead of growing). The iterated-log product is mathematically ill-defined with no specified termination. The precision budget δ ≤ ε/⌈log₂(1/ε)⌉ is inconsistent with the claimed product-of-logs scaling.

**Arbiter's justification:**
> The paper's principal contribution is a quantitative upper bound on gate count. Both reviewers independently identified that this bound is self-contradictory, and the steelman exchange strengthened rather than weakened this finding. An internally inconsistent complexity formula means the main theorem as stated is not a valid mathematical claim. Neither reviewer downgraded this finding.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F157

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> No systematic review methodology: no search strategy, databases, inclusion/exclusion criteria, quality assessment, or synthesis protocol. The paper claims to be an evidence-based review but provides no reproducible method.

**Arbiter's justification:**
> Both reviewers identify this as fatal for a review article. The paper's conclusions depend entirely on which literature is surveyed and how it is evaluated. Without a transparent methodology, the review is non-reproducible and its conclusions are unsupported by any verifiable process. This is not a minor reporting gap — for a review article, the method IS the study design.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F158

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> Lemma 4/Theorem 4: The converse direction — from an arbitrary zero-error quantum protocol with mixed states to an orthogonal representation of the complement graph — is invalid. The proof selects an arbitrary eigenvector from each mixed state and claims the resulting vectors form an orthogonal representation. This fails because: (a) zero-error function computation only requires distinguishability conditioned on Bob's side information y and differing outputs, not global pairwise orthogonality of code states; (b) orthogonality of supports for adjacent pairs does not imply that arbitrary eigenvector selections yield orthogonal vectors; (c) no equivalence between the operational zero-error criterion and orthogonal rank is established for the mixed-state model. This invalidates the claimed formula R_quantum = inf_m (1/m) log ξ(G^(m)).

**Arbiter's justification:**
> This lemma is the indispensable bridge between operational quantum protocols and the graph parameter (orthogonal rank) that powers the paper's main quantum/classical separation. Without a valid converse, the exact quantum rate formula is unsupported, and all downstream separation claims collapse. The error is structural and not a matter of missing detail that could be easily patched.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F159

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> The final equivalence argument (Claim 7) invokes 'Claim 4' to conclude reconfigurability, but Claim 4 only provides a size bound, not a reconfiguration guarantee. This is a direct logical misapplication at the critical last step of the proof.

**Arbiter's justification:**
> Both reviewers identified this issue. Reviewer A flagged it as retraction-worthy; Reviewer B noted the incorrect reference and called the equivalence argument insufficient. As written, the final step of the main theorem relies on an inference that does not follow from the cited claim. This is not a typo issue—if the intended claim (e.g., Claim 5) were substituted, its own proof is only a sketch, so the gap remains. The central conclusion is unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F160

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> No reproducible review methodology: no search strategy, databases, inclusion/exclusion criteria, quality assessment, or synthesis protocol is provided for what is presented as an evidence-based literature review.

**Arbiter's justification:**
> The manuscript's entire contribution depends on its review-based inference. Without a valid, reproducible methodology, the central conclusions cannot be said to arise from a scientific process. Both reviewers identify this as a foundational failure.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F161

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> Schizophrenia kinome analysis is based on pooled postmortem samples (one pool per sex-by-diagnosis cell) with technical triplicates treated as the basis for biological inference about disease and sex effects.

**Arbiter's justification:**
> Pooling collapses all subject-level biological variability into a single composite per group. Technical triplicates measure assay reproducibility on the same pooled material, not between-subject variation. There is effectively n=1 biologically per group. No valid statistical inference about disease effects or sex differences is possible. This is not low power—it is zero valid inferential degrees of freedom for the biological question. The paper's central disease-related conclusions (disease separation, global phosphorylation reduction, upstream kinase changes, sex-specific enrichment) cannot be supported by these data. Both reviewers independently identified this as retraction-worthy and defended it through reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F162

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Misapplication of Theorem 4.9 (cited as [8, Lemma 2.1]) in Theorem 4.10. The lemma allows identifying one free variable (x_1 = y_1) across two ultrafilter-realized equations, but the proof uses it to equate results/configurations across different equation forms (e.g., deriving (a+b)/2 = c ⊙ d). This misinterpretation of the logical statement invalidates the proof of Theorem 4.10.

**Arbiter's justification:**
> Theorem 4.10 is a flagship new partition-regular equation, and Corollary 4.12 depends on it. The misapplication is a fundamental logical error, not a gap that can be filled. However, confidence is slightly lower because the precise scope of what the lemma allows may depend on the exact formulation in the cited source.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F163

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The core construction for implementing logical phase gates P(α)_L transversally via solving Hv = w over ℝ (Eq. 4) is mathematically unjustified and likely invalid. The claim that full row rank over F₂ implies full row rank over ℝ is false, and even when a real solution exists, no proof is given that the resulting tensor product of physical phase gates preserves the code space and induces the correct logical action.

**Arbiter's justification:**
> Both reviewers identify this as the indispensable primitive enabling the entire recursive scheme. Reviewer B provides a concrete counterexample class (even-weight row dependencies). Reviewer A emphasizes the missing proof of logical action on all codewords/cosets and compatibility with stabilizer structure. If this construction fails, the recursion has no valid starting point and the entire method collapses. The Steane code example is stated without derivation and does not constitute a general proof.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F164

- Paper: *HDRTransDC: High Dynamic Range Image Reconstruction with Transformer Deformation Convolution*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is related to potentially incorrect metric calculations in Sections 4.2 and 4.3, meaning the statistical results reported in these sections may be inaccurate or misleading and require further validation.

**Candidate finding (rated retraction-worthy):**
> The primary quantitative comparison table omits the most directly relevant state-of-the-art baseline (Liu et al. 2022, 'Context-Aware Transformer'), while the text explicitly claims superiority over it by specific margins (0.34 dB, 0.33 dB, 0.07). The baseline's actual numbers are nowhere in the manuscript, making the central 'state-of-the-art' claim unverifiable.

**Arbiter's justification:**
> The paper's primary contribution claim is achieving state-of-the-art performance. If the most relevant competitor's results are absent from the comparison table while the paper claims to beat it, this is not merely incomplete reporting—it means the paper's central conclusion cannot be supported by the data as presented. Readers cannot verify the claimed margins, cannot assess whether the comparison was conducted fairly, and cannot determine if Liu et al.'s method was evaluated under the same protocol. This crosses from 'could be improved' to 'fundamentally broken' as an evidentiary basis for the main claim.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F165

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The manuscript conflates two distinct methods (MSP-MVS and TSAR-MVS) with different pipelines, different contributions, and different algorithmic components, making it impossible to determine what method was actually implemented, evaluated, and reported on.

**Arbiter's justification:**
> Both reviewers identified this independently. Review A upgraded to RETRACTION-WORTHY after steelmanning. The title/abstract/conclusion describe MSP-MVS (segmentation prior, anchor equidistribution, ILS), while a substantial central section describes TSAR-MVS (confidence filtering, superpixel-RANSAC, Roberts+Hough segmentation). This is not a local typo or naming inconsistency — it represents an identity failure of the object under study. The central conclusions ('our method achieves SOTA') cannot be supported because the manuscript does not establish which method produced the data. This meets the RETRACTION-WORTHY definition: the paper's central conclusions cannot be supported by the data as presented.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F166

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> Critical lack of vehicle/process control and confounded treatment-time contrast. The experimental design compares cytokine levels before and after exosome addition, but no matched vehicle control (PBS, buffer, or carrier alone) was added to parallel cultures at the same time point. The 'before' measurement is at 24h post-virus and the 'after' is at 96h total, meaning natural cytokine decay, degradation, cell exhaustion, dilution from medium addition, or any non-exosome component could explain the observed reductions.

**Arbiter's justification:**
> Both reviewers identified this as a fundamental design flaw. Reviewer A upgraded this toward RETRACTION-WORTHY after steelmanning B. Reviewer B defended it as RETRACTION-WORTHY throughout. Without a vehicle control, the primary causal claim that exosomes reduce cytokines is not identifiable from the data—this is not a matter of interpretation or overclaiming but a structural inability of the design to support its central conclusion. The rubric states RETRACTION-WORTHY applies when 'the paper's central conclusions CANNOT be supported by the data as presented,' which fits here.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F167

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Sampling/replication structure is unclear and likely pseudoreplicated. Three fish per tank were pooled into one tissue sample; tanks may have been in triplicate, but statistical analyses report means ± SD without clarifying the unit of analysis. For PK, each time point may have only n=1 pooled value, making inferential statistics on PK parameters impossible.

**Arbiter's justification:**
> If pooled samples were treated as independent fish-level replicates, all variance estimates and p-values are invalid. For the PK study, n=1 pooled samples per time point mean no inter-individual variability can be estimated, which is essential for reliable PK parameter estimation. While pooled designs exist in destructive sampling studies, the manuscript's statistical claims go well beyond what such a design supports. The severity is high because it affects both the PK and biosafety inferential conclusions, though some uncertainty remains about the exact replication structure.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F168

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> The trapezoidal AUC formula is stated as AUC = Σ(Ci + Ci+1)·Δt instead of the correct 0.5·(Ci + Ci+1)·Δt.

**Arbiter's justification:**
> AUC is the central metric of drug exposure in the PK study. If this formula was actually used as written, all AUC values would be doubled, invalidating exposure estimates, tissue comparisons, and any downstream parameter dependent on AUC. It is possible this is only a typographical error in the methods text while correct computation was performed, but the paper as presented asks readers to accept an explicitly wrong formula for its primary endpoint. Reviewer A identified this; Reviewer B acknowledged missing it and upgraded to RETRACTION-WORTHY on reflection. The slight uncertainty is whether it was actually applied or is merely a writing error, but as presented it is fundamentally broken.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F169

- Paper: *The Art of Staying Ahead of Deadlines: Improved Algorithms for the Minimum Tardy Processing Time*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the runtime analysis omits the contribution of the processing times within the interval [d_j - p_j, d_{j - 1}], which leads to an incomplete and therefore incorrect calculation of the total processing time.

**Candidate finding (rated retraction-worthy):**
> The bitwise OR (merge) operation required to compute S_j = L_{j-1} shifted ∪ R_{j-1} is not implementable with the listed dynamic string data structure operations (split, concatenate, make_string). The manuscript defers to Fischer and Wennmann without explaining how OR is performed in the new setting where strings have length d_max+1 rather than P. Split and concatenation alone cannot implement bitwise OR on indicator strings. Without this operation, the algorithm cannot compute its central recurrence.

**Arbiter's justification:**
> The OR merge is the step that combines the shifted left part with the right part to produce S_j. If this operation cannot be performed within the data structure, the algorithm is fundamentally incomplete. The manuscript's only justification is a reference to prior work that operated in a different setting (strings of length P, not d_max). This is not a missing detail—it is a missing core algorithm. However, there is some possibility that the referenced Fischer-Wennmann machinery does contain a transferable OR implementation that works in this context and the authors simply failed to explain the adaptation. This slight uncertainty prevents full confidence, but the burden of proof is on the manuscript, and it fails to meet it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F170

- Paper: *Shafarevich-Tate groups of holomorphic Lagrangian fibrations II*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> There is likely a mistake in the formulation or derivation of equations related to Kähler twists, such as an incorrect application of properties of Kähler manifolds or errors in twisting procedures within the proof.

**Candidate finding (rated retraction-worthy):**
> Theorem D uses an incorrect criterion for Fujiki class C. The proof assumes that if X^φ is of Fujiki class C, there exists a rational map f: X^φ → Y to a Kähler manifold Y with a pullback Kähler class h on X^φ. In reality, Fujiki class C means bimeromorphic to a compact Kähler manifold via a modification μ: Z → X^φ from a Kähler Z, not a rational map from X^φ to a Kähler target. This is a category error that destroys the contradiction strategy.

**Arbiter's justification:**
> Both reviewers independently identified this as retraction-worthy. The error is not a gap but a fundamental misunderstanding of the geometric criterion being applied. The entire proof mechanism for Theorem D collapses. No local repair is possible—a completely new argument would be needed.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F171

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The angular-diameter distance derivation (Eq. 29: d_A = (1+z)r_O) is not independently derived from geodesic deviation or ray bundle geometry but is back-solved to preserve the Etherington relation after the luminosity distance has been modified by the spurious aberration factor.

**Arbiter's justification:**
> In standard cosmology, d_A is determined by the transverse physical size at emission divided by observed angle and is derived from the geodesic deviation equation. The paper's d_A is not obtained this way; it is adjusted to force d_L = (1+z)^2 d_A after d_L has been altered. This circular reasoning means one of the paper's two principal observables is not grounded in physics. Both reviewers identify this circularity, and Reviewer B upgraded it to RETRACTION-WORTHY after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F172

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Missing essential controls make it impossible to attribute observed absorbance decreases to photocatalysis. No dark control (to quantify adsorption), no light-only control (to quantify photolysis), no spent tea extract-only control, and no proper baseline were included. The entire mechanistic attribution of 'photocatalytic degradation' is unsupported.

**Arbiter's justification:**
> Both reviewers identify this as a fundamental flaw. Without these controls, the observed absorbance decrease could be entirely due to adsorption, photolysis, sedimentation, or spectral interference from nanoparticles. The paper's central conclusion—that SBT-AgNPs photocatalytically degrade dyes—cannot be sustained from the presented data. This is not a matter of improving the study; the core inference is broken.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F173

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> Specific capacitance equations are internally inconsistent and at least one is dimensionally incorrect. Eq. (3) for CV-derived gravimetric capacitance has incorrect variable arrangement; Eq. (4) is labeled as specific capacitance but computes areal capacitance. The text conflates these throughout, making the derivation of the headline 1502 F/g value unverifiable and likely incorrect.

**Arbiter's justification:**
> The paper's central claim is a specific capacitance value. If the equations used to derive that value are dimensionally wrong or confuse gravimetric and areal normalization, then the flagship number is not a valid measurement of the claimed quantity. This is not a presentation issue—it means the primary result cannot be supported as presented. Both reviewers flagged formula problems; Reviewer A rated this retraction-worthy and Reviewer B rated it major-revision but acknowledged the formulas could invalidate reported numbers. On balance, the direct link between broken equations and the headline metric meets the retraction-worthy threshold.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F174

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> Internally contradictory statistical reporting that prevents verification of primary analyses. Table 4 is labeled as 'paired t-test' but reports medians, IQRs, Z-statistics, and r-values characteristic of Wilcoxon signed-rank tests. Table 5 (Wilcoxon) uses the same data structure. Cohen's d is referenced in table headers but not reported. These contradictions mean readers cannot determine what statistical test was actually performed on the primary endpoints.

**Arbiter's justification:**
> Both reviewers flagged this. Reviewer A upgraded it toward RETRACTION-WORTHY after steelman exchange, acknowledging that contradictory test labels and output formats could mean the primary analyses are unverifiable. Reviewer B rated it RETRACTION-WORTHY from the start. If the wrong test was applied or the wrong outputs were reported, all significance claims could be invalid. This is not a minor formatting issue—it strikes at the inferential backbone of the paper.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F175

- Paper: *Large Bricks and Join-irreducible torsionfree classes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> There is a logical gap in the proof of Proposition 3.9, meaning that a necessary step or justification is missing, so the conclusion does not properly follow from the premises given.

**Candidate finding (rated retraction-worthy):**
> The construction of a directed system from a spanning tree of the Hasse quiver in Proposition 3.9 is mathematically invalid. A spanning tree does not define a directed/filtered index category, and the paper's explicit claim that 'we don't have any compatibility condition to check on the maps as the underlying graph is a tree' is false. A direct limit requires a directed indexing category with coherent transition maps for all composable pairs. Without a properly defined directed system, the central object F (whose existence drives the entire main proof) is not well-defined.

**Arbiter's justification:**
> Both reviewers flag this as the most critical error. Reviewer A calls it MAJOR-REVISION on the grounds that the result might be salvageable by a different construction, but Reviewer B correctly argues that this is not a mere gap in exposition — it is an error in the definition of a fundamental categorical construction. The paper explicitly asserts that no compatibility check is needed, which is mathematically wrong. The direct limit F is the sole vehicle for the main theorem's proof, and without it the entire argument collapses. While a different proof strategy might exist, the proof as presented is fundamentally broken at this step. Under the key test: if confirmed, this finding alone means the paper's central conclusion is not supported by the argument as given, which is retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F176

- Paper: *MSP-MVS: Multi-granularity Segmentation Prior Guided Multi-View Stereo*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The problem is that there is a significant flaw in how the experiment was designed in the Multi-granularity section, which affects the reliability of the resulting data analysis and the validity of the study’s conclusions.

**Candidate finding (rated retraction-worthy):**
> The manuscript explicitly proposes TSAR-MVS ('Therefore, we propose TSAR-MVS') while simultaneously citing 'TSAR-MVS (Yuan et al. 2024b)' as prior work in the related work section, creating a direct contradiction about whether the core contribution is novel or previously published.

**Arbiter's justification:**
> Reviewer A rated this retraction-worthy and defended it strongly in reflection; Reviewer B identified it as a new error in reflection that strengthened the retraction case. If confirmed, this collapses the novelty claim—a methods paper's central contribution is that a new method is being proposed. However, there is some residual possibility this reflects careless editing of a revision/extension of the authors' own prior work rather than deliberate misrepresentation. Even so, the manuscript as submitted cannot support its novelty claims. The severity remains retraction-worthy because the paper in its current form misrepresents originality at the most fundamental level.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F177

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Biosafety data show identical baseline (Day 0) values across all five groups (Control, 1×, 3×, 5×, 10×) for ALP (5 U/L), AST (100 U/L), ALT (20 U/L), and Creatinine (0.2 mg/L), with significance annotations placed on these identical values.

**Arbiter's justification:**
> Identical values to 1–3 significant digits across five independent biological groups is biologically implausible. Real biological variation in fish enzyme and metabolite measurements precludes exact agreement across groups. Significance markers on identical values are nonsensical. This pattern strongly suggests either data fabrication, template copying, or extreme rounding that renders the presented data non-representative of actual measurements. Reviewer B rated RETRACTION-WORTHY; Reviewer A initially rated MAJOR-REVISION but upgraded on reflection after considering the combined evidence of identical values plus significance annotations. The slight uncertainty reflects the possibility that extreme rounding or figure-generation artifacts could partially explain the pattern, though this would still mean the data as presented do not support the biosafety conclusions.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F178

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> The sole validation experiment (EPHA6/GAB1 co-incubation mass spectrometry) is a single unreplicated experiment lacking FDR control and phosphosite confidence metrics, and the reported EPHA6 autophosphorylation sites (pY259, pY484) appear impossible given the stated recombinant construct spanning residues 683-1130.

**Arbiter's justification:**
> The paper claims 195 novel kinase-substrate interactions but validates only one pair, and that single validation has no replication, no statistical framework, and a site-numbering problem that suggests either the construct, the numbering, or the MS annotation is wrong. Reviewer A identified the site inconsistency; Reviewer B acknowledged missing it and agreed it was devastating. In steelman, B upgraded the overall validation problem to RETRACTION-WORTHY when combined with the site inconsistency. Without even one credible validation, the entire substrate discovery pipeline lacks ground truth. Confidence is slightly lower than for the pooled-sample finding because the site-numbering issue could conceivably reflect a reporting/isoform numbering error rather than a data error, but even so the validation remains critically inadequate.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F179

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The k-clique reduction (Theorem 4) has two independent fatal flaws: (1) the cost of constructing the auxiliary graph (enumerating all ℓ-cliques and checking all pairs for 2ℓ-clique formation) is omitted and can dominate the claimed runtime; (2) the auxiliary graph construction does not enforce disjointness or partition conditions on the three ℓ-cliques forming a triangle, so a triangle in the auxiliary graph may not correspond to a valid 3ℓ-clique in the original graph.

**Arbiter's justification:**
> Both reviewers flag the k-clique reduction as severely flawed. Review A identifies the construction cost omission; Review B identifies the missing disjointness condition. After steelman exchange, both agree this is retraction-worthy on multiple grounds. The standard Nešetřil-Poljak reduction requires careful partitioning that the manuscript omits, making the reduction potentially semantically incorrect, not just incomplete in runtime accounting.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F180

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The fault-tolerance claim assumes availability of arbitrary physical phase rotations P(α) on each qubit to realize logical P(α)_L transversally, thereby presupposing the very continuous rotations the paper claims to synthesize fault-tolerantly from a finite discrete set.

**Arbiter's justification:**
> This collapses the distinction between physical analog control and fault-tolerant logical gate synthesis, which is the entire point of the FT synthesis problem. Reviewer A identified this as a category error that voids the claimed novelty. Reviewer B acknowledged this as a missed finding they would rate RETRACTION-WORTHY. If arbitrary-angle physical rotations are assumed at the encoded level, the claimed approximation breakthrough is vacated.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F181

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> Theorem 1.5/6.3 has an internal contradiction: the Galois group of the trivializing extension is described as an open subgroup of GL₂(Z_ℓ) but then stated to be pro-p, while working over Z_ℓ with ℓ-adic μ-invariants. An open subgroup of GL₂(Z_ℓ) is pro-ℓ (up to finite index), not pro-p for p ≠ ℓ.

**Arbiter's justification:**
> The entire noncommutative Iwasawa-theoretic framework of Part II depends on the correct identification of the ambient prime and group structure. If G is pro-ℓ rather than pro-p, then Λ(G) is the wrong Iwasawa algebra, the μ-invariant is defined over the wrong prime, and all cohomological/Nakayama arguments are in the wrong category. However, there is a small possibility this is a systematic notational confusion (consistently swapping p and ℓ) that could be mechanically corrected without changing the mathematical content, which introduces slight uncertainty. Nevertheless, as printed, the theorem specifies mutually incompatible hypotheses and the main result of Part II is incoherent.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F182

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Theorem 3.2 (main multiplication formula): The proof imports results from [GLS07] that were established in the preprojective/2-Calabi-Yau setting without verifying the required hypotheses hold for the Jacobian algebra A. Key objects and maps (decomposition Y, map q, notation E(M1,M2)_Y) are undefined or insufficiently justified. The critical equation (3.16) is asserted rather than derived. The entire proof is logically incomplete.

**Arbiter's justification:**
> This is the paper's central technical contribution. Both reviewers independently identified that the proof is incomplete, relies on unjustified transfers from a different algebraic setting, and contains undefined objects. Without a valid proof of this theorem, all downstream results (Propositions 4.3, Theorem 4.5, etc.) are unsupported. The issue is not merely a gap that can be filled with a sentence—it requires verifying that an entire framework applies in a new context.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F183

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The probability-of-success argument only establishes that a random sample lands in A = N+(T) with sufficient probability. It does not establish that this event implies algorithmic detection of a triangle, because the implication depends on the unproved correctness of BFS+. The advertised error bound (e.g., ≤ 10^{-30}) is therefore unsupported.

**Arbiter's justification:**
> The paper amplifies the probability of the wrong event. The sampling calculation may be correct, but it is irrelevant unless landing in N+(T) deterministically triggers detection—an implication that is not proved. The formal guarantee of the theorem is thus unsubstantiated. Both reviewers identified this; Reviewer A rated it RETRACTION-WORTHY and defended it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F184

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> Human schizophrenia vs. control kinome analysis is based on pooled samples (one pool per sex-by-diagnosis group) with only technical triplicates, constituting pseudoreplication that eliminates valid statistical inference about disease effects, sex-specific effects, and all downstream analyses derived from these comparisons.

**Arbiter's justification:**
> Both reviewers independently rated this RETRACTION-WORTHY. Both steelman exchanges confirmed the severity without downgrade. Pooling removes all biological variance estimation; technical triplicates of a single pooled sample cannot support inferential claims about population-level disease or sex differences. All reported differential phosphorylation, upstream kinase predictions, peptide set enrichment linking dark kinases to schizophrenia, and sex-specific schizophrenia claims are fundamentally unsupported. This infects the paper's central disease-association narrative.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F185

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The constants B and C in Proposition 3.1 depend on A, with B diverging as A→0, yet the proof fixes A for the ODE comparison and then sends A→0 in the contradiction argument. This makes the limiting manipulation invalid.

**Arbiter's justification:**
> Both reviewers flag this. Reviewer A initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY upon reflection, noting that the A-dependence independently destroys the final contradiction step. Reviewer B initially rated the B-divergence as the primary mechanism breaking the contradiction. Since the proof's terminal step requires a limit that is mathematically impossible as written (B→∞ makes e^{-BT}→0, not the intended comparison), and no alternative argument is supplied, this defect independently invalidates Theorem 3.2.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F186

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Confusion of correlation with causation in planetary comparison: cross-planet associations between surface pressure and temperature are treated as proof that pressure causes temperature independently of radiative properties.

**Arbiter's justification:**
> Both reviewers identify this (A explicitly, B as part of the ideal gas law finding). Pressure and temperature co-vary because massive greenhouse atmospheres are both dense and opaque to IR. The manuscript's headline physical argument depends on a causal interpretation that the data do not support.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F187

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Theorem 4.3's proof contains algebraically incorrect manipulations. From A ∈ p ⊙_t q one gets {n : n^{-1}A ∈ q} ∈ p, not '⊆ p'. The transport step with F'={1/(n−t)f : f∈F} and claims about a + (1/n)P(d) ∈ n^{-1}A mixes additive polynomial patterns, scalar division, and the nonstandard semigroup law incorrectly. This theorem is a main technical engine for polynomial/symmetric partition results.

**Arbiter's justification:**
> The proof mechanism is not merely incomplete but algebraically wrong in type and substance. Since Theorem 4.3 feeds later polynomial pattern claims (the paper's advertised new results), the derived conclusions are unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F188

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The derivation of the central inequality (14) in Theorem 2.1 relies on a local-to-global estimate that conflates valuations across places, mishandles normalizations between the base field κ and extension field K (suppressing [K_w:κ_v] factors), and uses undefined or inconsistent notation (N_{x'}(x), S_{j,x'}(x), 2m⌈x'Q(x),∞⌉). The theorem statement and proof are not mathematically well-posed.

**Arbiter's justification:**
> Both reviewers flag this as the foundation of all subsequent results. If the central inequality is not coherently stated or proved, the entire proof chain collapses. The notation issues are not cosmetic—they prevent verification of the mathematical content.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F189

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Lemma 4.5 is not proved: the proof consists of an unsupported assertion and an editorial placeholder '[AUTHOR_1]'. This lemma is the key technical input to Theorem 2.1, establishing the limiting constant α that determines the explicit eigenvalue formula.

**Arbiter's justification:**
> Both reviewers independently identify this as RETRACTION-WORTHY. Neither downgraded during steelman. The manuscript literally does not contain a proof of the lemma on which the central theorem depends. Without Lemma 4.5, Theorem 2.1's explicit formula is unsubstantiated, and all downstream results (Corollary 2.2, Theorem 2.3) collapse.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F190

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 1.4 invokes Dirichlet's unit theorem to claim that for an arbitrary algebraic integer y, there exists a field-dependent constant c(κ) such that |y|_v ≤ c(κ)|y|_w for any two Archimedean places v, w, and hence m(y,0)=O(1). This is not a consequence of Dirichlet's unit theorem and is false in general: algebraic integers can have wildly unbalanced Archimedean absolute values. This step is the sole mechanism used to eliminate the term 2m(x'Q(x),∞) from Theorem 2.1 and obtain the main inequality of Theorem 1.4.

**Arbiter's justification:**
> Both reviewers independently identify this as a fatal error. The invoked principle is mathematically incorrect for arbitrary algebraic integers. Without this step, Theorem 1.4's proof collapses entirely. No minor revision can repair a proof that rests on a false mathematical claim at its decisive step.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F191

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Analytical method validation reports mathematically impossible values: negative LOD/LOQ (e.g., kidney LOD = −587.51 µg/kg, LOQ = −1780.34 µg/kg) and R² values outside [0,1] (muscle R² = 6.96, skin R² = 0.002).

**Arbiter's justification:**
> LOD/LOQ computed as 3.3σ/slope and 10σ/slope cannot be negative under standard calibration, and R² is bounded [0,1] by definition. These are not debatable analytical choices—they are mathematical impossibilities indicating either catastrophic calculation errors or fundamental misunderstanding of validation statistics. Because the analytical assay underpins every concentration measurement in both the PK and residue-depletion studies, invalid validation severs the evidentiary chain from sample to PK conclusion. Both reviewers rated this RETRACTION-WORTHY; neither downgraded after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F192

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The paper confuses frame-dependent aberration of ray direction with a new independent physical photon-loss mechanism, treating the angular redistribution under frame change as an additional dimming beyond what is already encoded by angular-diameter distance and reciprocity.

**Arbiter's justification:**
> Changing frames changes the angular description of a ray bundle but does not create additional photon loss. Once beam area, solid angle, and redshift are treated covariantly, there is no extra cosmological dimming term. Etherington reciprocity and Liouville's theorem already connect these quantities consistently. The paper's interpretation of its Eqs. 11-13 as a new photon-loss factor is a conceptual error that directly generates the incorrect central result.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F193

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Proposition 4.3's proof is logically invalid. The contradiction argument claiming F_T = 2F_T does not follow from Theorem 3.2 (even if that theorem were valid). The right-hand side of the multiplication formula is a sum over multiple Y with different Euler-characteristic coefficients, and there is no mechanism shown to collapse it to a single term with coefficient 2. Additionally, the proposition uses Ext over 𝒜 (a cluster algebra) rather than Ext over A (the Jacobian algebra), making the statement formally ill-posed.

**Arbiter's justification:**
> This proposition is the essential bridge from the multiplication formula to all representation-theoretic conclusions about tensor product simplicity and heads. Both reviewers identify the contradiction argument as a non sequitur. Reviewer A additionally identifies the category error (Ext over 𝒜 vs A). Reviewer B's second pass upgrades severity even further. Since this proposition is indispensable for Theorems 4.5 and 2.3, its failure propagates to all main applications. The logical error is elementary and cannot be repaired by minor revision—it requires a completely new argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F194

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Theorems 4.10 and 4.11 invoke the existence of ultrafilters p ∈ cl(K(βZ,+)) ∩ E(K(βZ, ⊙_{l,k})) from earlier theorems that do not establish this existence. Theorem 4.10 cites Theorem 4.8, which does not prove such an intersection is nonempty. Theorem 4.11 cites Theorem 3.3, which concerns only ⊙_t (not general ⊙_{l,k}) and does not explicitly produce idempotents in the intersection. The main partition-regularity conclusions therefore rest on unestablished objects.

**Arbiter's justification:**
> These are the paper's central results. The entire method depends on finding ultrafilters that simultaneously belong to the closure of the minimal ideal under addition and are idempotent in the ⊙_{l,k} semigroup. Without establishing their existence, the combinatorial conclusions (new partition-regular equations) are unsupported. Both reviewers identify this gap from different angles.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F195

- Paper: *The Art of Staying Ahead of Deadlines: Improved Algorithms for the Minimum Tardy Processing Time*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the runtime analysis omits the contribution of the processing times within the interval [d_j - p_j, d_{j - 1}], which leads to an incomplete and therefore incorrect calculation of the total processing time.

**Candidate finding (rated retraction-worthy):**
> The multi-machine extension (Section 4) claims Õ(n + d_max^m) time for constant m but provides no multidimensional data structure construction, no operation definitions, no complexity proofs. The result is asserted by analogy with the 1D case in a single paragraph.

**Arbiter's justification:**
> Both reviewers independently classified this as retraction-worthy. Neither downgraded during steelman. The paper claims a distinct theorem without supplying the central algorithmic object needed to state or analyze it. No cited multidimensional dynamic string structure exists with the required properties. This is not an exposition gap — it is a completely unsupported claim that constitutes a headline contribution of the paper.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F196

- Paper: *On the Existence of an Extremal Function for the Delsarte Extremal Problem*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the uniform convergence on compact subsets cannot be concluded without first establishing that the limit function f is continuous and satisfies f(0)=1, which has not been shown at this point in the proof.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 8 asserts that the admissible class G_G(Ω) is contained in a closed, bounded subset of L²(G) and hence is weakly sequentially compact. No argument is given that admissible functions belong to L²(G) or have uniformly bounded L²-norms. The pointwise bound |f| ≤ 1 and finite measure of Ω only control the positive part; the negative part may live on a set of infinite measure, so ∫|f|² can be infinite. Without L²-boundedness, the weak compactness extraction that produces the candidate extremizer is invalid, and the entire existence proof collapses. Theorem 9 depends on Theorem 8, so the main result is unsupported.

**Arbiter's justification:**
> Both reviewers flagged this independently with high confidence. The gap is not a matter of missing details—it concerns a claim that appears to be false under the paper's hypotheses. If the functions are not in L²(G), weak compactness in L² cannot be invoked, and no alternative compactness framework is provided. The entire existence proof rests on this step.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F197

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> The manuscript asserts G[J_s ∪ J_t ∪ J_m] is a linear forest without proof. J_s and J_t individually inducing linear forests and J_m being independent does not imply their union induces a linear forest—cross-edges can create cycles or high-degree vertices.

**Arbiter's justification:**
> This is a necessary structural premise for the final reconfiguration step. Without it, the entire YES-preservation direction of the kernel equivalence collapses. Both reviewers flag this; neither finds any argument in the text that could establish it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F198

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> The study draws therapeutic efficacy and safety conclusions about exosome treatment for COVID-19 patients from an in vitro PBMC stimulation assay with n=5 patients and n=5 controls — a fundamental mismatch between evidence and claims.

**Arbiter's justification:**
> The manuscript's stated conclusions concern clinical treatment efficacy and safety, but the study design is a small ex vivo laboratory experiment with no patient administration, clinical endpoints, pharmacology, or adverse-event data. Reviewer A upgraded this to retraction-worthy on reflection when the headline conclusion is taken as the paper's core contribution, and the data fundamentally cannot support it. The overclaim is not stylistic — it is a category error between study design and stated conclusions that cannot be fixed by reanalysis alone.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F199

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The paper double-counts propagation effects already incorporated in standard FLRW distance theory by adding an extra aberration factor of (1+z)^{-2} to the observed flux, yielding modified d_L and d_A relations (Eqs. 16, 24, 29).

**Arbiter's justification:**
> Standard cosmological radiative transfer, derived from null geodesic congruences, phase-space invariants (I_ν/ν^3), and photon number conservation, already yields the correct (1+z)^4 surface brightness dimming and the standard luminosity distance d_L = (1+z)R_0 r_1. The claimed additional (1+z)^{-2} factor from aberration is not missing; inserting it violates Liouville's theorem and photon number conservation. The paper's headline equations are products of this double count, and all downstream cosmological implications inherit the error.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F200

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Misuse of the Ideal Gas Law as a causal explanation for planetary surface temperatures, used to dismiss the greenhouse effect. PV=nRT is an equation of state, not an energy balance theory; it cannot determine equilibrium temperature without radiative boundary conditions.

**Arbiter's justification:**
> Both reviewers identify this as a fundamental physical error. The ideal gas law relates state variables but does not independently explain why a planet has a particular temperature. This error underpins one of the paper's central physical arguments against the greenhouse effect. It is not a matter of interpretation — it is a category error in physics.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F201

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Pharmacokinetic parameters are internally contradictory and violate basic PK identities: e.g., gill kel = 0.01 h⁻¹ implies t1/2 ≈ 69.3 h but reported half-lives are 0.94 h, 19.39 h, and 198.48 h; liver t1/2 is reported as both 238.68 h and 420.28 h; plasma Tmax is 24 h in the abstract but 3 h in text; gill Cmax timing is reported as 3 h, 6 h, and 8 h in different sections.

**Arbiter's justification:**
> These are not ambiguities or matters of interpretation—they are direct numerical contradictions within the same manuscript for primary PK descriptors (half-lives, Tmax, Cmax timing). When the reported rate constant and corresponding half-life violate t1/2 = ln(2)/k, the results table is arithmetically self-contradictory. A reader cannot determine which values, if any, are correct. Since tissue-specific PK characterization is the paper's central contribution, irreconcilable contradictions in these parameters make the core conclusions unsupportable. Both reviewers rated these contradictions RETRACTION-WORTHY; both defended this after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F202

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Theorem 4.11 invokes Theorem 3.3 to obtain an ultrafilter in cl(K(βZ,+)) ∩ E(K(βZ, ⊙_{l,k})), but Theorem 3.3 concerns only ⊙_t (the special case), not the generalized operation ⊙_{l,k}. No analogue for the generalized operation is proved anywhere.

**Arbiter's justification:**
> This is a direct logical gap: the main generalized theorem starts from a premise not established in the paper. Corollary 4.12 (the headline answer to Di Nasso's question) and Corollary 4.14 depend on this theorem, so the central generalized conclusions collapse.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F203

- Paper: *Facile synthesis of SnSe‚ÄìMnTe nanocomposite as a promising electrode for supercapacitor applications*
- Field: Materials Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the EDX spectrum in Figure 2d was incorrectly labeled, showing inconsistencies such as a flat background and missing expected iron peaks, which led to incorrect assignment of elements to peaks.

**Candidate finding (rated retraction-worthy):**
> Internal inconsistency between reported energy density (61.05 Wh/kg) and the value derivable from stated capacitance (1502 F/g) and voltage window (0.65 V). Both the standard formula and the paper's own formula yield ~88.2 Wh/kg—a ~31% discrepancy that cannot be explained by rounding.

**Arbiter's justification:**
> Energy density is the headline metric in the abstract and conclusions. The discrepancy is mathematically undeniable from the paper's own numbers and cannot be attributed to a typo or rounding. It demonstrates either that the capacitance value used for the energy calculation differs from the reported 1502 F/g, or that an incorrect formula was applied. Either way, the central performance claim as published is arithmetically unsupported. This was identified by Review A, strongly endorsed by Review B in steelman, and neither reviewer could explain it away.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F204

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> The proposed methodological contribution is never described. The paper claims 'novel modifications,' 'refined algorithms,' and 'advanced neural network architectures' integrated into MediaPipe but provides no algorithmic details, architectural changes, code modifications, or technical description of what was actually done.

**Arbiter's justification:**
> A paper claiming methodological innovation must describe the method. Without any concrete description of the purported enhancements, there is nothing to evaluate, reproduce, or connect causally to the claimed performance gains. The scientific contribution is unverifiable.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F205

- Paper: *Quantum advantage in zero-error function computation with side information*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Claim 3 is likely due to an incorrect equation or flaw in the logical steps of the proof, which may result from the misuse of mathematical principles, incorrect assumptions, or an invalid derivation that undermines the claim's validity.

**Candidate finding (rated retraction-worthy):**
> Proposition 1 claims G ⊠ H = G ∨ H (strong product equals OR/disjunctive product) for simple graphs, which is false in general.

**Arbiter's justification:**
> The strong product and OR (disjunctive) product are well-known to be distinct graph products (see Imrich & Klavžar, 'Product Graphs'). In the strong product, vertices differing in both coordinates are adjacent only if BOTH coordinate pairs are adjacent; in the OR product, adjacency holds if AT LEAST ONE coordinate pair is adjacent. These edge sets differ for most nontrivial graphs. This proposition is foundational: Theorem 3's sandwiching argument, the Lovász theta multiplicativity claims, and the quantum-classical separation all depend on it. Both reviewers independently identified this error. The proof is relegated to a missing appendix, making it unverifiable, but the claim itself is contradicted by standard graph theory. If this equality is used substantively in proofs (not just as a notational convention for a nonstandard definition), the paper's central conclusions collapse.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F206

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The revised angular diameter distance definition (Eq. 29, d_A = r_O(1+z)) scales oppositely to the standard FLRW result (d_A = a_0 r / (1+z)), and appears reverse-engineered to restore Etherington reciprocity after the aberration factor was introduced.

**Arbiter's justification:**
> The standard Etherington relation d_L = (1+z)^2 d_A is a theorem under broad, well-satisfied conditions. The manuscript first violates it by adding an extra (1+z) to d_L, then redefines d_A ad hoc to restore it. This is not a self-consistent derivation but a post-hoc patch, and the resulting d_A(z) relation is physically wrong.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F207

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Degradation/removal in wastewater is inferred from raw absorbance decreases at selected wavelengths without controls for nanoparticle scattering, adsorption onto particles, agglomeration/settling, matrix background changes, or dilution effects. No dark control, no catalyst-free light control, no extract-only control.

**Arbiter's justification:**
> The paper claims photocatalytic degradation as its main outcome, but the experimental design cannot distinguish photocatalysis from adsorption, flocculation, settling, or photolysis. The comparison is AgNPs+room light vs. AgNPs+sunlight (i.e., light vs. more light), with no dark control. Both reviewers flagged this. Review A initially rated it RETRACTION-WORTHY, then softened slightly during steelman; Review B rated the missing controls as MAJOR-REVISION but upgraded the overall mechanistic claim to unsupported during steelman. The combination of no mechanistic controls plus absorbance-only measurement in a complex matrix means the central photocatalytic degradation conclusion cannot be supported by the presented data.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F208

- Paper: *The impact understanding of exosome therapy in COVID-19 and preparations for the future approaches in dealing with infectious diseases and inflammation*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the figure shows a micrograph from a TESCAN MIRA 3 device, whereas the text in the Materials and Methods section incorrectly describes the instrument used as a Hitachi S-4160 and Zeiss EM10C, resulting in a discrepancy between the described methods and the actual data presented.

**Candidate finding (rated retraction-worthy):**
> Fundamental mismatch between study design and claimed conclusions: The paper claims to assess the efficacy and safety of exosome therapy in COVID-19 patients, but only performs an in vitro PBMC stimulation experiment on 5 patients and 5 controls. No patients received exosomes. The title, abstract, and conclusions misleadingly imply a clinical intervention.

**Arbiter's justification:**
> Both reviewers independently identify this as the core fatal flaw. The paper's central conclusions about therapeutic safety and efficacy in COVID-19 patients are not supported by in vitro data. The data at most support a limited observation about exosome-mediated cytokine modulation in cultured PBMCs. The disconnect between the experimental design and the headline claims is not a matter of reframing—it fundamentally invalidates the paper's stated conclusions. A complete rewrite reframing the study as a preliminary in vitro observation would constitute a different paper.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F209

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Failure to engage with mainstream attribution, carbon-budget, and assessment literature while making sweeping claims that overturn those fields. The paper does not address the strongest contrary evidence (satellite spectral measurements, vertical warming patterns, isotopic constraints, paleoclimate sensitivity estimates).

**Arbiter's justification:**
> Both reviewers identify this. A review claiming to overturn established science must rigorously engage the strongest opposing evidence. The manuscript simply declares mainstream findings 'non-existent' or 'invalid' without substantive rebuttal. This is not a minor omission — it means the paper's extraordinary claims lack the extraordinary evidence required.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F210

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript confuses radiative transfer with thermal conductivity, implying the greenhouse effect should manifest as a bulk thermal conductivity anomaly in laboratory gases.

**Arbiter's justification:**
> The greenhouse effect is fundamentally a radiative-transfer phenomenon operating on planetary scales with an atmospheric column. Expecting it to appear as a conductive property of gas samples reflects a category error in physics that undermines a substantial section of the paper's argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F211

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> The paper claims standard cosmology omitted relativistic aberration from its distance-redshift framework, but this is factually false. Standard FLRW distance theory fully incorporates all relevant geometric and kinematic effects.

**Arbiter's justification:**
> The paper's entire novelty rests on correcting a purported omission in the standard framework. If that omission does not exist—and it does not, as the standard derivation accounts for beam geometry, redshift, time dilation, and solid-angle evolution covariantly—then the paper's central contribution is void. This is not merely a misrepresentation of the literature; it is the false premise upon which the entire manuscript is constructed. Both reviewers converged on RETRACTION-WORTHY for this finding after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F212

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> Technical replicates of pooled material are used to compute fold changes, clustering, and upstream kinase predictions, creating pseudoreplication throughout the disease-analysis pipeline.

**Arbiter's justification:**
> Using technical replicates as if they were independent biological observations grossly underestimates uncertainty. Apparent clustering and separation of groups may reflect high assay precision on the same pooled lysate rather than reproducible disease biology across individuals. All downstream analyses (differential peptides, kinase inference, pathway enrichment, connectivity) inherit this invalid variance structure. Both reviewers recognized this mechanism; Reviewer A articulated it as a distinct finding from the pooling design itself.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F213

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> All downstream theorems (BMM via Theorem 3, k-clique via Theorem 4, Max-Cut via Theorem 5, and numerous other applications) are explicitly derived from Theorem 2 and are presented as established results, but they collapse if Theorem 2 is unsupported.

**Arbiter's justification:**
> These are not independent results; they are corollaries of the broken core theorem. The manuscript presents them as proved consequences, including claims to invalidate major open conjectures. Since the foundation is unsupported, none of these conclusions can stand as presented. Reviewer A rated this RETRACTION-WORTHY; Reviewer B's analysis supports it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F214

- Paper: *The effect of Relativistic Aberration on Cosmological Distances*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the computations incorrectly assume galaxies are in a different reference frame than the observer, leading to fundamentally flawed equations and invalid results throughout the paper.

**Candidate finding (rated retraction-worthy):**
> Double-counting of redshift/flux effects: the paper adds an extra (1+z)^{-2} 'aberration correction' to the solid angle on top of the standard FLRW flux formula, which already includes two factors of (1+z)^{-1} (energy loss and arrival-rate dilation), yielding d_L ∝ (1+z)^2 r instead of the standard d_L ∝ (1+z) r.

**Arbiter's justification:**
> The standard derivation from first principles (Boltzmann equation, Liouville's theorem, or direct FLRW geodesic computation) yields the correct (1+z)^{-4} surface brightness dimming without any missing beaming term for isotropic emission in the source rest frame. The additional (1+z)^{-2} factor is exactly the paper's novel quantitative result; if it is double-counting, the main conclusion is directly invalidated. Both reviewers identified this independently and both rated it retraction-worthy. Neither downgraded it during steelman.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F215

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> The final YES-preservation argument cites Claim 4 for a reconfiguration conclusion, but Claim 4 is a size bound and provides no reconfiguration guarantee. The proof literally states 'by Claim 4 the answer is YES' when Claim 4 does not establish any such implication. This is a direct logical disconnect at the theorem's conclusion.

**Arbiter's justification:**
> This is not a typo or minor citation error—it is invocation of a nonexistent implication at the exact point where the kernel's correctness is concluded. No valid replacement argument is provided. Both reviewers agree after steelman that this is fatal.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F216

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The proof works on the enlarged set M⁺ (defined by I=I₀, C=0, r_ij>0) rather than the actual configuration space of realizable strictly convex quadrilaterals. M⁺ contains non-realizable distance vectors (violating triangle inequalities, F₄<0, 3-body-collinear configurations). Uniqueness of critical points on M⁺ does not imply uniqueness on the physical configuration set unless all critical points on M⁺ are shown to be realizable, which is never established. Additionally, 3-body-collinear configurations in M⁺ are dismissed as non-central-configurations but are never excluded as critical points of U|_{M⁺}, invalidating the Morse-theoretic count.

**Arbiter's justification:**
> This is the fundamental logical gap identified by Reviewer A (findings 1, 6, 10). The main theorem's conclusion is drawn from a critical-point count on a domain that is strictly larger than the relevant configuration space. Without proving that every critical point on M⁺ corresponds to a realizable convex quadrilateral, the uniqueness claim for actual central configurations is unsupported. This is not a matter of missing detail — it is a structural flaw in the proof architecture.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F217

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> The reported AUC trapezoidal formula omits the required 1/2 factor: manuscript gives Σ(Ci + Ci+1)×(Δt) instead of the correct Σ((Ci + Ci+1)/2)×(Δt), which would double all AUC values.

**Arbiter's justification:**
> AUC is a central pharmacokinetic exposure metric used for tissue distribution comparisons and regulatory interpretations. If the stated formula was actually used, all AUC values are doubled and exposure estimates are systematically wrong. If the formula is merely misreported, it reflects a level of carelessness that compounds the other errors. Given the other mathematical inconsistencies, it is plausible the formula error is real.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F218

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> Lemma 4's Morse-theoretic argument requires M⁺ to be a compact smooth manifold (or a manifold with boundary where boundary behavior is carefully handled). M⁺ has positivity constraints (r_ij > 0) creating boundary/corner structure. No proof is given that U|_{M⁺} is a proper Morse function, that boundary critical points are excluded, or that standard Morse equalities apply to this domain.

**Arbiter's justification:**
> Reviewer A's finding 2, partially echoed by Reviewer B's finding 6 on boundary behavior. The Morse equality ∑(-1)^q α_q = χ requires specific conditions on the domain and the function. The manuscript applies it without verification. Combined with the issues above, this represents another independent failure of the proof's central mechanism. Downgrading to MAJOR-REVISION might be warranted if the other issues were absent, but in context, this compounds the fundamental breakdown.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F219

- Paper: *Illuminating the dark kinome: utilizing multiplex peptide activity arrays to functionally annotate understudied kinases*
- Field: Biology
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the recombinant protein fragments used for at least three kinases do not include their respective kinase domains, meaning the reagents do not have intrinsic kinase activity and the experimental results do not reflect actual kinase function for those proteins.

**Candidate finding (rated retraction-worthy):**
> Schizophrenia/control and sex-specific comparisons are based on single pooled samples per group with only technical triplicates, providing no biological replication for population-level inference.

**Arbiter's justification:**
> Both reviewers independently identify this as the most critical flaw. A single pooled lysate per condition (male control, male SCZ, female control, female SCZ) with technical triplicates cannot estimate between-subject variance. All statistical comparisons, heatmaps, upstream kinase analyses, and sex-specific claims derived from these pooled samples are pseudoreplicated. The disease-association conclusions—a central pillar of the paper—are fundamentally unsupported by the experimental design. This is not a matter of being underpowered; the design structurally cannot answer the questions posed.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F220

- Paper: *Efficient Fault-Tolerant Single Qubit Gate Approximation And Universal Quantum Computation Without Using The Solovay-Kitaev Theorem*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Equation 6, derived using real arithmetic, is incorrectly applied to a context that uses modulo 2 arithmetic, making the result incompatible with the actual operations on the state ket.

**Candidate finding (rated retraction-worthy):**
> The fault-tolerance claim is not established under standard FT assumptions. The recursive scheme requires implementing P(α v_j) transversally on physical qubits for arbitrary non-Clifford angles. These are not available as fault-tolerant operations from a fixed protected gate set in the standard model. The paper's appeal to hardware-native arbitrary rotations undermines the FT compilation framework rather than establishing it. No error propagation, threshold, or concatenation analysis is provided.

**Arbiter's justification:**
> Reviewer A rated this RETRACTION-WORTHY throughout. Reviewer B initially rated it MAJOR-REVISION but upgraded to RETRACTION-WORTHY after steelman, finding Reviewer A's argument about physical rotation availability compelling. However, there is some residual uncertainty: if the work were repositioned as an architecture-specific proposal rather than a standard FT compilation theorem, the underlying idea might survive in weakened form. Given the paper's current claims, the severity is retraction-level.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F221

- Paper: *Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

**Candidate finding (rated retraction-worthy):**
> No statistical analysis reported for cell viability data (no replicates, no variance, no p-values, no statistical test identified), yet the manuscript makes explicit claims of 'no significant adverse effects' and 'significantly higher viability.'

**Arbiter's justification:**
> The biomedical conclusion depends on statistical inference, but no inferential substrate exists in the paper. A single percentage (92%) with no n, no error, and no test cannot support claims of significance. This is not a reporting gap—it is the absence of the evidence required for the stated conclusion. Both reviewers independently rated this retraction-worthy and defended it through reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F222

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> Equation (2.5) uses second derivatives with respect to a spatial/normal variable r, but I_A is defined as a function of enclosed area A, not of r. The PDE is not well-posed for the stated unknown because the independent-variable structure is undefined.

**Arbiter's justification:**
> Reviewer A identifies this as a separate structural flaw from the maximum principle issue: the manuscript never defines how I_A depends on r, never establishes a parametrization through minimizers, and never justifies differentiability in the requisite variables. Reviewer B, upon reflection, acknowledges this as an additional structural flaw reinforcing the retraction-level assessment. A PDE with undefined independent variables is not a correctable notational issue—it means the core evolution formula is not mathematically meaningful as written.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F223

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Elimination rate constant and half-life values are internally inconsistent with the stated equations. For example, Ke = 0.01 h⁻¹ should yield t½ = ln(2)/0.01 = 69.3 h, not the 0.94 h reported.

**Arbiter's justification:**
> This is a direct mathematical inconsistency between reported parameters and the equations used to derive them. It indicates either the equations were not actually applied or the parameters were incorrectly calculated/transcribed. Combined with the other contradictory half-life values, this confirms that the PK parameter estimates are unreliable.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F224

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript argues that because CO2 radiative forcing is logarithmic, additional CO2 must produce negligible warming, and presents ~0.64–0.81°C for a doubling from 400 to 800 ppm as a definitive or upper-bound estimate. This is derived using a fixed low climate sensitivity parameter (lambda) while omitting all feedback processes.

**Arbiter's justification:**
> Logarithmic forcing does not imply negligible temperature response; the temperature outcome depends critically on feedbacks (water vapor, albedo, lapse rate, clouds) which the manuscript ignores entirely. Presenting a no-feedback estimate as an upper bound forecloses the actual uncertainty space and converts an unjustified assumption into a false impossibility claim. Both reviewers rate this or closely related findings as RETRACTION-WORTHY and defend through reflection. The manuscript's central quantitative policy argument (that warming from further CO2 is too small to justify mitigation) depends directly on this invalid inference.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F225

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Lemma 4.4's proof contains a mathematical error in the CLT-based density argument: it evaluates the density j_n of the standardized sum S_n/(σ√n) at points v/(σ√n) that shrink to zero and claims convergence to γ(0), but this confuses the density of the standardized sum with its value at a vanishing argument. The scaling is mishandled.

**Arbiter's justification:**
> This is a separate mathematical error from the conditioning issue. If the density convergence argument is invalid, Lemma 4.4 is unproven, breaking the proof chain at an even earlier stage. However, there is some possibility that a corrected local CLT argument could salvage Lemma 4.4 itself (though not the downstream conditioning error in Lemma 4.5). Given that even a correct Lemma 4.4 is insufficient for the main theorem due to the conditioning error, the combined effect is definitively retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F226

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Quantification of dye removal in wastewater using raw absorbance changes at selected wavelengths without matrix-matched calibration, baseline correction, deconvolution, or accounting for nanoparticle scattering/adsorption. Absorbance decrease ≠ photocatalytic degradation.

**Arbiter's justification:**
> Both reviewers note that the quantitative removal percentages are derived without validated calibration in the wastewater matrix. The presence of nanoparticles in the measured solution introduces scattering artifacts. Without separating these confounds, the reported degradation percentages are meaningless, directly undermining the paper's quantitative conclusions.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F227

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Fundamental misapplication of non-compartmental analysis (NCA). The manuscript claims NCA but reports absorption rate constants (Ka), absorption half-lives (t½a), distribution phases, and biphasic compartmental interpretations. Standard NCA from oral data cannot directly estimate Ka without IV reference data or deconvolution. The reported t½a and t½b parameters imply a two-compartment model that was never formally fitted or justified.

**Arbiter's justification:**
> The entire PK parameter set is derived from a methodology that is incorrectly described and apparently incorrectly applied. Parameters like Ka from NCA of oral-only data are not valid without additional modeling assumptions that are neither stated nor justified. This means the absorption, distribution, and elimination characterization — the core of the paper — is built on an invalid analytical framework. Both reviewers flagged this.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F228

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The central claim of equivalent or superior link-budget gain compared to transmit beamforming rests on comparing coherent spatial beamforming gain against a 'temporal combining gain' without proper normalization of total transmitted energy, occupied bandwidth, symbol rate, and noise bandwidth. The two mechanisms are fundamentally different, and the manuscript does not prove their equivalence under identical resource constraints.

**Arbiter's justification:**
> Both reviewers identify this as the paper's most critical flaw. Beamforming gain arises from coherent spatial superposition at a point in space; the proposed temporal combining gain arises from spreading symbols over more time-frequency dimensions. Without a rigorous proof that these yield the same SNR for the same total radiated power, bandwidth, and data rate, the paper's headline conclusion is unsupported. The numerical examples where T > N and the temporal gain exceeds beamforming gain strongly suggest the comparison is not resource-normalized, making the central conclusion fundamentally broken rather than merely incomplete.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F229

- Paper: *On the uniqueness of the strictly convex quadrilateral central configuration with a fixed angle*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Lemma 1 contains incorrect equations or logical steps, undermining the validity of the proof and making the results that rely on it, including Proposition 2 and the main theorem, unreliable.

**Candidate finding (rated retraction-worthy):**
> The manuscript does not prove that critical points of U on the enlarged set M^+ lie within the geometrically realizable planar convex quadrilateral set C. The final step 'Since C ⊂ M^+, U has at most one critical point on C' is logically valid for an upper bound, but the paper does not establish that the unique critical point on M^+ (if it exists) belongs to C, nor does it properly invoke an external existence result to close the argument.

**Arbiter's justification:**
> Reviewer A rated this retraction-worthy; during steelman, A considered downgrading to major-revision if the paper is read as proving only an upper bound combined with external existence results. However, Reviewer B fully endorsed A's original severity. The issue is that uniqueness on a superset does imply at most one on a subset, which partially works, but the paper's own theorem statement claims existence-and-uniqueness for given angle θ, and the existence part is not established within the paper's framework. Since the theorem as stated is not supported without this step, and the manuscript does not clearly separate 'at most one' from 'exactly one,' this remains retraction-worthy, though with slightly lower confidence.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F230

- Paper: *A Simple, Nearly-Optimal Algorithm for Differentially Private All-Pairs Shortest Distances*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is the incorrect assumption in Sections 3 and 4 that the topology of the shortest path trees is public, which may not be true; additionally, in Section 3, Lemma 2.4 is applied inappropriately under this false assumption.

**Candidate finding (rated retraction-worthy):**
> Advanced composition is misapplied in the approximate-(ε,δ)-DP results. The manuscript uses per-mechanism privacy budget scaling as 1/k (or 1/s) rather than 1/√k (or 1/√s), inconsistent with the paper's own stated Lemma 2.2. This affects the error bounds in Theorems 3.2, 4.2, and related results.

**Arbiter's justification:**
> This is not a constant-factor issue; it changes the asymptotic dependence on s (and hence n) in the final error rate. The headline Õ(n^{1/4}/ε) bound for approximate DP is derived from a balancing argument that relies on this incorrect scaling. If corrected, the optimal parameter choice and resulting rate change materially. Both reviewers flag this: Reviewer A pinpoints the specific algebraic discrepancy (1/s vs 1/√s), and Reviewer B identifies the balancing argument as fundamentally flawed for related reasons.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F231

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> Extreme selection bias: the review omits the principal lines of evidence bearing on its thesis—observed energy imbalance, attribution studies, paleoclimate constraints, fingerprinting, ocean heat content, and multiple independent temperature datasets.

**Arbiter's justification:**
> A review that selectively samples only contrarian material while claiming to adjudicate an entire field cannot support its conclusions. The omission of the strongest contrary evidence is a fatal synthesis failure, not merely an oversight.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F232

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The BFS+ subroutine—the core detection mechanism of the algorithm—is never defined. The manuscript repeatedly references steps and behaviors of BFS+ (e.g., 'See Step 12') but provides no pseudocode or formal specification. Without this, neither correctness nor runtime can be verified.

**Arbiter's justification:**
> Both reviewers independently identify this as the most critical flaw. The entire paper rests on this subroutine. An algorithm paper whose central algorithm is absent is fundamentally unverifiable. This is not a minor omission—it is the mechanism that supposedly achieves the breakthrough result.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F233

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 1.4 asserts that y = 1/(x'Q(x)) is an algebraic integer when x is an algebraic integer, but never supplies the required valuation argument. The ideals a_0 and a_∞ used in the construction of x' are undefined, and the divisor bookkeeping needed to verify ord_v(x') ≤ Σ_j ord_v(x−a_j) at all finite places is absent. The same unsupported integrality claim is reused in the proof of Theorem 1.5.

**Arbiter's justification:**
> Both reviewers agree this is a critical unsupported claim. The integrality of y is a prerequisite for the subsequent Archimedean argument. Without it, the passage from Theorem 2.1 to Theorem 1.4 does not function, and Theorem 1.5 (and hence the abc corollary) also fails. The manuscript provides no basis to believe the claim is even true as stated.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F234

- Paper: *A Strongly Subcubic Combinatorial Algorithm for Triangle Detection with Applications*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The analysis in Case 2.1 is faulty because it incorrectly assumes that the triangle detection algorithm will always succeed under certain conditions, but there exist cases where the algorithm fails, making the proof invalid.

**Candidate finding (rated retraction-worthy):**
> The claimed O(m) time per BFS+ trial is unjustified. Detecting triangles during BFS as described requires checking non-tree edges among vertices at the same or adjacent levels, which standard BFS does not perform without additional adjacency queries whose cost is not analyzed.

**Arbiter's justification:**
> The headline O(n^{7/3}) bound is the product of the number of trials and the per-trial cost. If the per-trial cost exceeds O(m) due to the unanalyzed detection checks, the main runtime claim fails. This is not an accounting refinement but a structural incompatibility between what the correctness argument needs and what O(m) BFS provides. Reviewer A rated this RETRACTION-WORTHY; Reviewer B's parallel findings support this.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F235

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript claims Venus's high surface temperature is explained 'simply because the atmospheric pressure is so great,' presenting this as flagship evidence that greenhouse physics is unnecessary. Pressure alone cannot create or sustain high temperatures without an energy source and radiative constraints.

**Arbiter's justification:**
> This is used as a principal empirical demonstration supporting the rejection of greenhouse warming. Pressure profiles redistribute temperature vertically via the adiabatic lapse rate but do not independently set the total energy content of a planetary atmosphere. The example is physically non-responsive to the energy-balance question it purports to settle. Reviewer A flags this as a separate RETRACTION-WORTHY finding; Reviewer B subsumes it under the ideal gas law error. Both agree the underlying physics is wrong and central to the paper's argument.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F236

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Reported dye standard concentrations are physically impossible or internally inconsistent: malachite green at 100–500 mg in 10 mL (10,000–50,000 mg/L) far exceeds aqueous solubility (~4,000 mg/L); methylene blue listed masses do not match stated working concentrations; textile wastewater described as both '1 µl/ml' and '0.001 mg/ml'.

**Arbiter's justification:**
> Reviewer B identified this as the primary quantitative defect, and Reviewer A upgraded it upon reflection. If the starting dye concentrations are undefined or physically impossible, every calculated degradation percentage is meaningless. This is not a unit-labeling problem that could be resolved by a corrigendum; the actual experimental conditions are unknowable from the manuscript, invalidating all quantitative removal claims.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F237

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> The final equivalence argument misapplies Claim 4 (a size-bound claim) where it needs a reconfigurability result. Even substituting Claim 5 does not work because its premises (that J_s and J_t are independent sets in a linear forest) are not established—the text itself admits J_s and J_t are 'not necessarily independent.'

**Arbiter's justification:**
> The proof's terminal inferential step invokes a claim that does not entail the needed conclusion, and no available substitute has its hypotheses satisfied. This leaves the main theorem without a logically valid final step. Both reviewers identify this independently.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F238

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The proof that m(x'Q(x),∞) = O(1) for algebraic integers (Theorem 1.4) and simple numbers (Theorem 1.5) is mathematically incoherent. The argument conflates m(y,0), h(y), N(y,0), and m(y,∞) in an invalid identity chain, and the appeal to Dirichlet's unit theorem to bound Archimedean absolute values of an arbitrary algebraic integer y is unjustified. Without this bound, the main error term in inequality (14)/(19) is uncontrolled and Theorems 1.4 and 1.5 are unproved.

**Arbiter's justification:**
> Both reviewers independently identified this as the single most critical failure. This step is the lynchpin of the entire proof chain — if it fails, the paper's central claimed inequalities (11) and (12) have no valid derivation. The reasoning presented is not a gap that could be filled; it is logically incoherent as written.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F239

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> The transition from inequality (15) to (16) and the subsequent derivation of (17)–(18) are algebraically unjustified. The dependence on the index j is not handled consistently, sign conventions are confused between proximity and valence functions, and the place-by-place estimate (17) mixes |·|_v and |·|_{v+} with dimensionally inconsistent constants c_v. The conclusion S_{x'}(x) ≤ 2m(x'Q(x),∞) + O(1) therefore lacks a valid foundation.

**Arbiter's justification:**
> This is the mechanism by which a sum of proximity terms is replaced by a single proximity term—the key technical trick. Both reviewers identify independent errors here. Without this step, inequality (19) and hence Theorem 2.1 do not follow.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F240

- Paper: *Unveiling the biological effects of radio-frequency and extremely-low frequency electromagnetic fields on the central nervous system performance*
- Field: Medicine
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the manuscript incorrectly refers to "C57BL/6 rats," but C57BL/6 is a strain of mice, not rats; thus, there is a misidentification of the animal model used.

**Candidate finding (rated retraction-worthy):**
> Complete absence of review methodology. The Methods section is a single sentence fragment containing a template placeholder ('[JOURNAL]'). No search strategy, databases, date ranges, keywords, inclusion/exclusion criteria, study selection process, data extraction procedure, or synthesis method is described.

**Arbiter's justification:**
> For a review article, the methodology for identifying, selecting, and synthesizing evidence IS the scientific method. Its total absence means the central conclusions — which purport to summarize a field — are built on an opaque, unreproducible, and potentially biased author-selected literature set. This is not a gap that can be patched; the entire review would need to be reconstructed from scratch. The paper's core scientific product (a synthesized evidence summary) cannot be supported by the paper as presented. Both reviewers rated or upgraded this to RETRACTION-WORTHY after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F241

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> Equations (3)–(4) and the claim that a unitary spreading matrix F_b yields a T-fold received-power/SINR improvement are either incorrect or severely under-specified. Matched filtering against orthogonal spreading codes recovers signal components but does not create extra received energy without a corresponding increase in transmitted energy or decrease in data rate.

**Arbiter's justification:**
> This is the theoretical foundation of the proposed scheme. Reviewer A identifies this as a core error; Reviewer B implicitly flags it by noting the absence of a fundamental limit derivation for temporal combining gain. If the T-fold gain is illusory (i.e., it merely reflects spreading gain that is offset by reduced symbol density), then the entire theoretical framework collapses. There is sufficient concern from both reviews to classify this as retraction-worthy, though some residual uncertainty remains about whether a correct reformulation could rescue partial claims.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F242

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> Elimination half-life values are internally contradictory and biologically implausible. Gill tissue is reported with three mutually exclusive t½ values (0.94 h, 19.39 h, 198.48 h) in different parts of the manuscript. Plasma t½ is reported as 3368.24 h (~140 days), which is biologically implausible and contradicts observed concentration decline within the 128 h observation window.

**Arbiter's justification:**
> Half-life is a core pharmacokinetic parameter. Three different values for the same tissue in the same study indicate either calculation errors, transcription errors, or data fabrication. A plasma t½ of 140 days estimated from a 128 h sampling window is statistically unjustifiable and biologically nonsensical at 20°C. These contradictions mean the manuscript's central PK conclusions (elimination kinetics, tissue retention, withdrawal recommendations) cannot be trusted.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F243

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> Lemma 4.4's proof contains a scaling error and an incomplete local limit theorem argument. The CLT-based rescaling by 1/√n shrinks D to a point, so the approximation j_n(v/σ√n) ≈ γ(0) only shows the density near 0 dominates, not that the conditional distribution on D becomes uniform. The missing (σ√n)^{-d} normalization factor is dropped without justification. Uniformity in x is claimed but not established.

**Arbiter's justification:**
> Both reviewers flag this lemma. Reviewer A identifies a fatal scaling error (missing normalization factor); Reviewer B identifies the conceptual flaw that the CLT-based argument does not apply in the large deviations regime relevant to {S_n ∈ D} for fixed bounded D. This lemma feeds directly into Lemma 4.5 and hence Theorem 2.1. While a proper local limit theorem might salvage the statement, the proof as written is fundamentally flawed.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F244

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> The proof of Theorem 3.2 (the central multiplication formula) imports GLS07-style geometric arguments (Euler characteristics of constructible strata, fiber descriptions, Grassmannian decompositions) into the setting of modules over an infinite-dimensional Jacobian algebra A without establishing that the required geometric prerequisites (algebraicity, finite type, constructibility, affine fiber properties) hold in this new context.

**Arbiter's justification:**
> This is the paper's core theorem. The entire proof strategy depends on geometric properties that are highly setting-sensitive and known to hold in 2-CY/Frobenius/finite-type contexts but are not verified here. Both reviewers independently identify this as fatal. Reviewer A emphasizes the categorical transfer failure; Reviewer B emphasizes undefined objects and non sequiturs. Together they establish that the proof is not a sketch with gaps but rather a wholesale unverified import of methodology. Under the prompt's key test, if confirmed, this requires retraction because the paper's primary contribution is unsupported.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F245

- Paper: *The Scientific Case Against Net Zero: Falsifying the Greenhouse Gas Hypothesis*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The author used the base-10 logarithm (log10) instead of the natural logarithm (ln, neperian logarithm) in the IPCC radiative forcing equation, resulting in incorrect temperature change calculations.

**Candidate finding (rated retraction-worthy):**
> The manuscript claims 'the increase in temperature from 1880 through 2000 is statistically indistinguishable from 0 K' and that 'recent global average surface temperatures remain relatively stable,' without presenting a transparent or reproducible statistical analysis.

**Arbiter's justification:**
> Multiple independent observational datasets (HadCRUT, GISTEMP, Berkeley Earth, ERA5, satellite records) show approximately 1.0–1.2°C warming over this period, with statistical significance far exceeding conventional thresholds. The manuscript's claim is incompatible with the observational record as ordinarily understood and is presented without any valid supporting analysis. Both reviewers rate this RETRACTION-WORTHY. This is a central empirical premise of the paper; if observed warming is not effectively zero, the paper's argument that there is no warming to explain collapses.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F246

- Paper: *Multi-Antenna Towards Inband Shift Keying*
- Field: Computer Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that the paper underestimates the beamforming gain for transmit beamforming with N antennas, stating it as N when the correct value is N^2.

**Candidate finding (rated retraction-worthy):**
> The central claim that transmit beamforming can be replaced by temporal repetition coding 'without reducing the data rate or the link budget' is unsupported by any valid comparative analysis under matched resource constraints (same bandwidth, time, energy, latency, channel model).

**Arbiter's justification:**
> Spatial beamforming gain arises from coherent combining across antennas at fixed time/frequency resources and provides directional array gain. Temporal repetition consumes additional time resources, changes latency, and does not produce directional gain. The paper asserts equivalence by invoking a scalar AWGN capacity formula, but this does not establish operational equivalence in multi-antenna mmWave/THz systems. No end-to-end link budget, channel simulation, or fair comparison is provided. Since this is the paper's title-level and conclusion-level claim, and the reasoning is logically flawed (not just empirically incomplete), the central conclusion cannot be supported by the presented data. Reviewer A rated this RETRACTION-WORTHY and defended it vigorously; Reviewer B acknowledged the conflation as a logical error (MAJOR-REVISION) but argued the modulation might survive independently. However, the paper's framing, motivation, and conclusions all rest on this replacement claim, making it the paper's core thesis rather than a peripheral point.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F247

- Paper: *Photocatalytic removal of textile wastewater-originated methylene blue and malachite green dyes using spent black tea extract-coated silver nanoparticles*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error in Fig. 4 is that the UV-Vis spectrum for the "chemically synthesized Ag nanoparticles" displays an artifact—a sharp, anomalous peak at ~260 nm—due to unfiltered junk data not being removed before plotting, and the horizontal axis label is also misspelled.

**Candidate finding (rated retraction-worthy):**
> Impossible or internally inconsistent dye concentrations reported in the methods. Malachite green is described at 100 mg/ml (100,000 ppm), which far exceeds solubility and would saturate any UV-Vis measurement. Methylene blue concentrations are reported inconsistently as masses and concentrations. These errors make the degradation calculations physically implausible or unreproducible.

**Arbiter's justification:**
> Reviewer B identifies this as retraction-worthy. If the concentrations are as stated, the UV-Vis data are physically impossible; if they are reporting errors, all derived degradation percentages are based on incorrect inputs and are meaningless. Either way, the quantitative core of the paper is invalidated. Reviewer A corroborates this through findings about unit inconsistencies and missing calibration.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F248

- Paper: *A Simple Ricci Flow Proof of the Uniformization Theorem*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly assumes that the value of A at t=0 and t=T are identical, but without a justification or condition ensuring this, the main inequality in the argument does not necessarily hold.

**Candidate finding (rated retraction-worthy):**
> The maximum principle comparison in Proposition 3.1 is applied without a valid PDE framework. The isoperimetric ratio I_A is defined as an infimum over curves, and no regularity, classical solvability, or viscosity formulation is established for the evolution equation (2.5). The spatial variable (normal direction r vs. enclosed area A) is left unexplained. Without these, the comparison of the PDE solution with the logistic ODE subsolution is unjustified.

**Arbiter's justification:**
> This is the main engine of the proof. Both reviewers flag this independently: Reviewer A notes the absence of a fixed spatial domain, boundary conditions, and regularity for the infimum-defined profile; Reviewer B notes the lack of verification that the diffusion and reaction terms permit the claimed ODE comparison. If this comparison fails, the lower bound on I_A^2 is unproven and the entire argument collapses.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F249

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> Corollary 4.12 (and 4.14): The stated equation uses ⊙_{l,k} but the proof concludes with ⊕_{l,k}, which is undefined in the manuscript. The flagship partition-regularity claim — the paper's main advertised result — is not actually proved as written.

**Arbiter's justification:**
> Reviewer A flagged this as RETRACTION-WORTHY and defended it through steelman (downgrading to MAJOR-REVISION in the spirit of charity, but noting it is 'certainly a serious presentation/theorem-statement defect'). Reviewer B identified the Corollary 4.12 operation mismatch as 'the single clearest fatal error.' The mismatch between the stated theorem and what the proof attempts to show means the paper's headline claim is literally unproved. While this could conceivably be a consistent notation error, ⊕_{l,k} is never defined, so the reader cannot determine what was intended.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F250

- Paper: *A Relationship Between Nonphysical Quasi-probabilities and Nonlocality Objectivity*
- Field: Physics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the calculation incorrectly claims different eigenvalues for β^{T}β in the right-identity case, when in fact the eigenvalues remain unchanged for both the left- and right-identity cases, invalidating the argument's main result.

**Candidate finding (rated retraction-worthy):**
> CHSH nonlocality (Horodecki quantity M) is invariant under qubit swap. Swapping subsystems sends the correlation matrix T to T^T, and the Horodecki quantity depends on eigenvalues of T^T T (equivalently T T^T), which have identical spectra. Therefore 'swap-intolerant nonlocality'—where a state is CHSH-nonlocal but becomes local after swap—cannot exist for any Hermitian trace-1 operator, regardless of positive semidefiniteness.

**Arbiter's justification:**
> This is a clean linear-algebraic invariance that directly contradicts the paper's central definition and theorem. It is not a matter of interpretation or proof technique—the claimed phenomenon is mathematically impossible. Both reviewers agree after reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F251

- Paper: *On the principal eigenvalue for compound Poisson processes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The main flaw is that the proof does not account for a key exception or missing condition, which leads to Theorem 2.1 being stated too generally and thus not holding in all claimed cases.

**Candidate finding (rated retraction-worthy):**
> The lower bound derivation in the proof of Theorem 2.1 requires uniform convergence (in x and eventually in n) of the conditional probability from Lemma 4.5 to iterate into an exponential bound, but only pointwise convergence is claimed (and not even proved).

**Arbiter's justification:**
> Reviewer B identifies this initially as MAJOR-REVISION but upgrades to RETRACTION-WORTHY during steelman, since without uniform control the exponential asymptotics cannot be extracted. Reviewer A agrees in steelman. Since the theorem is central, the compounding of this gap with the unproven Lemma 4.5 makes it fatal.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F252

- Paper: *Characteristic ideal of the fine Selmer group and results on $Œº$-invariance under isogeny in the function field case*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error in the proof of Theorem 5.1 involves a flaw or gap in the logical reasoning or calculations that invalidates the original proof, and a corrected version has been provided in arXiv:2407.21431.

**Candidate finding (rated retraction-worthy):**
> The derivation of equation (11) in the proof of Theorem 5.1 relies on unjustified multiplicativity of Euler characteristics from the flat cohomology long exact sequence. The claimed ratio of Euler characteristics does not follow from the provided setup without additional finiteness/vanishing hypotheses that are not established.

**Arbiter's justification:**
> This is a third independent failure point in the proof of Theorem 5.1, identified primarily by Reviewer B and acknowledged by Reviewer A in reflection. The algebraic manipulation assumes properties of Euler characteristics that are not generally valid for arbitrary Λ-modules. Combined with the hypothesis mismatch and the local Galois group error, this makes the proof of Theorem 5.1 triply broken. Any one of these errors alone would be sufficient; together they are decisive.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F253

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Theorem 4.5 proof is logically broken: it appears to prove Lemma 4.4 rather than Theorem 4.5, with abrupt switches to determinantal modules and i-boxes. Key steps (existence of exact sequences, rigidity implying T = M1*M2 or M2*M1) are asserted without justification.

**Arbiter's justification:**
> Reviewer A provides detailed evidence that the proof text does not match the theorem statement and that the argument is spliced from different contexts. This is one of the paper's main advertised applications. While conceivably a drafting error, the mismatch is too severe to be a simple fix—there is no discernible proof of the stated theorem in the manuscript.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F254

- Paper: *A form of refined Roth's theorem and its application to the $abc$-conjecture*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> Theorem 1.6 contains an error because one or more of the equations or logical steps used in the proof are incorrect, possibly due to an invalid assumption or a misapplied result that invalidates the theorem's conclusion.

**Candidate finding (rated retraction-worthy):**
> Equation (19) in the proof of Theorem 2.1 replaces full counting functions N(x, a_j) with truncated counting functions N̄(x, a_j) without justification. Since N̄ ≤ N, this is a one-directional inequality being used in the wrong direction—it strengthens the bound and cannot be done without a separate multiplicity estimate that is not provided.

**Arbiter's justification:**
> Reviewer A identifies this as a direct logical error; Reviewer B acknowledges it as a missed fatal error in reflection. Theorem 2.1 is the engine for all subsequent results; if its statement involves truncated counts but the proof only establishes the inequality for full counts, the theorem is not proved as stated.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F255

- Paper: *Extraction and characterization of biocompatible hydroxyapatite (Hap) from red big eye fish bone: Potential for biomedical applications and reducing biowastes*
- Field: Environmental Science
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> Figures 1 and 2 are supposed to display FT-IR and XRD spectra, but instead show SEM images, indicating the figure images and their legends are mismatched and do not represent the described data.

**Candidate finding (rated retraction-worthy):**
> Text fragments from an unrelated materials science study (Fe-Al-based mesoporous metal oxides 'BMO', Cu Kα peaks, HRTEM discussion) appear to have been inserted into the manuscript's characterization narrative.

**Arbiter's justification:**
> If confirmed, this means parts of the analytical interpretation were copied from another manuscript rather than derived from the authors' own data. This is a core integrity failure that undermines confidence in whether the presented characterization accurately describes the authors' actual experiments. Both reviewers escalated this to retraction-worthy during reflection.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F256

- Paper: *Token Jumping in Planar Graphs has Linear Sized Kernels*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The proof incorrectly claims a linear kernel size in k, but the correct approach only yields a quadratic kernel, as shown in later work; the original proof thus overstates the achievable bound.

**Candidate finding (rated retraction-worthy):**
> The proof applies the linear-forest reconfiguration argument to G[J_s ∪ J_t ∪ J_m] without rigorously establishing that this induced subgraph is a linear forest. J_s and J_t are stated to be 'not necessarily independent,' and edges involving boundary vertices are not controlled.

**Arbiter's justification:**
> Reviewer A identified this as retraction-worthy. The entire equivalence argument depends on the linear-forest structure of this subgraph to apply the reconfiguration result. Without verification that the subgraph has maximum degree ≤2 and no cycles, the proof collapses. Reviewer B's concerns about J_s/J_t construction reinforce this: if these sets are not well-characterized, the structural claim about their union is unverifiable.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F257

- Paper: *The interplay between additive and symmetric large sets and their combinatorial applications*
- Field: Mathematics
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The definition or expression of the operation \( p \odot_t q \) is incorrect, which undermines the validity of the subsequent results that rely on this operation.

**Candidate finding (rated retraction-worthy):**
> The claim '(Z, ⊙_{l,k}) is an abelian group when l | k(k−1)' is false in general. The map x ↦ lx+k transports ⊙_{l,k} into ordinary integer multiplication, but Z under multiplication is not a group (only ±1 are units). A concrete counterexample with l=1, k=1 shows the identity is 0 but element 1 has no inverse. Later sections explicitly rely on group/ideal behavior of this structure.

**Arbiter's justification:**
> This is a foundational structural claim on which the generalized machinery (Theorems 4.8–4.14) is built. It is demonstrably false by elementary counterexample. The paper's generalized partition-regularity results cannot stand on a non-existent group structure.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F258

- Paper: *Large Bricks and Join-irreducible torsionfree classes*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> There is a logical gap in the proof of Proposition 3.9, meaning that a necessary step or justification is missing, so the conclusion does not properly follow from the premises given.

**Candidate finding (rated retraction-worthy):**
> Lemma 3.6 argues that to show every proper quotient of F is torsion, it suffices to check maps from simple modules S into F and examine their cokernels. This tests the wrong direction: maximal proper quotients correspond to surjections F ↠ S onto simples, not injections S ↪ F. The proof as written does not establish that the direct limit F is lim→f-simple.

**Arbiter's justification:**
> Reviewer A identifies this as retraction-worthy with clear mathematical reasoning. Reviewer B raises concerns about the same lemma from a different angle (factoring maps through direct limits). The directional error is concrete: testing injectivity of maps from simples into F is not equivalent to testing that all proper quotients are torsion. Since Lemma 3.6 is the mechanism producing lim→f-simple objects, its failure breaks the chain to Proposition 3.9. However, there is some possibility the argument could be repaired by reversing the direction, so confidence is slightly lower.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F259

- Paper: *Assessing the effect of therapeutic level of oxytetracycline dihydrate on pharmacokinetics and biosafety in Oncorhynchus mykiss (Walbaum, 1792)*
- Field: Multidisciplinary
- SPOT severity tier: `errata`

**SPOT-annotated error in this paper (context only):**
> The error is that negative values are reported for pharmacokinetic parameters such as AUC, elimination rates, and LOQ in Table 1, which are nonsensical since these parameters should always be positive based on their definitions in pharmacokinetics and analytical chemistry.

**Candidate finding (rated retraction-worthy):**
> The paper claims non-compartmental analysis (NCA) but reports absorption rate constants (Ka), absorption half-lives (t1/2a), distribution half-lives, and interprets biphasic kinetics—parameters that require compartmental modeling assumptions.

**Arbiter's justification:**
> Standard NCA does not estimate Ka, absorption half-life, or separate distribution/elimination phases from oral data. If NCA was truly performed, these parameters are fabricated or meaningless. If compartmental modeling was performed, the methods are misreported and the analysis is irreproducible. Either way, the central PK parameters that form the paper's main conclusions are not supported by the stated analytical method. Reviewer A rated RETRACTION-WORTHY throughout; Reviewer B initially rated MAJOR-REVISION but explicitly upgraded to RETRACTION-WORTHY on reflection, noting that invalid parameters invalidate conclusions rather than merely needing clarification.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F260

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Internal to the proof of Theorem 3.2, multiple essential steps are undefined, unjustified, or logically disconnected: the set C in (3.12), the projection/fiber arguments, the notation ⊥d', equation (3.13) cited without hypothesis verification, the decomposition over an unspecified index set Y, and the conclusion that certain fibers are affine spaces—all asserted rather than derived.

**Arbiter's justification:**
> Even setting aside the ambient-setting transfer problem, the proof does not go through on its own terms. The steps needed to derive equation (3.16) from the preceding manipulations are missing. This is an independent fatal flaw in the same theorem. Both reviewers identify these gaps; Reviewer A separates them as a distinct finding while Reviewer B folds them into the same finding. Either way, the proof has no valid derivation chain.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F261

- Paper: *Algebraic description of complex conjugation on cohomology of a smooth projective hypersurface*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The statement and proof of Theorem 2.3 is not correct. What was described in the paper is an order 2 operation which swaps the Hodge components, which gives the complex conjugation only when the Hodge component has dimensions 1. But our description does not give the complex conjugation in the general case where the Hodge component has a bigger dimension

**Candidate finding (rated retraction-worthy):**
> The elliptic curve example defines a coefficient μ as (∫_{γ_1}ω · ∫_{γ_2}ω − ∫_{γ_2}ω · ∫_{γ_1}ω)/(24πi), which is identically zero because multiplication of complex numbers is commutative.

**Arbiter's justification:**
> An illustrative example that reduces to zero by tautology is a concrete demonstration that the formula does not work as claimed, at least in the simplest case. This is not merely a typo—it suggests either the formula is wrong or the specialization procedure is flawed. Both reviewers converge on this being retraction-worthy after reflection. Confidence is 0.78 because there is some chance the formula involves quantities (e.g., matrix entries, different differential forms) that are not commutative in a way obscured by the notation or OCR.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F262

- Paper: *Efficient Human Pose Estimation: Leveraging Advanced Techniques with MediaPipe*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the angle was calculated incorrectly in Section 3.3, leading to potential inaccuracies in the reported statistical results that rely on this value.

**Candidate finding (rated retraction-worthy):**
> No experimental dataset is described: no dataset name, number of subjects, number of frames, annotation protocol, ground-truth source, train/test split, resolution, frame rate, or ethical approval for human subjects.

**Arbiter's justification:**
> Pose-estimation accuracy metrics (MSE, IoU) are defined relative to ground-truth annotations. Without any specification of the dataset or reference standard, the reported metrics are not merely irreproducible—they are uninterpretable. The central accuracy claims have no scientific meaning. Both reviewers rated this RETRACTION-WORTHY and strongly defended it.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F263

- Paper: *Multiplication formula for Hernandez and Leclerc's quivers with potentials*
- Field: Mathematics
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that Jacobian algebras do not generally have the Ext-symmetry required for the GLS multiplication formula, and generalized preprojective algebras are not always Jacobian because the nilpotency relations for loops are not derived from the potential.

**Candidate finding (rated retraction-worthy):**
> Proposition 4.3 contains a logically invalid contradiction argument: from the multiplication formula it concludes F_T = 2F_T, but this requires linear independence of F-polynomials that is never established. The deduction that equality of F-polynomials/g-vectors implies existence of short exact sequences is also unjustified. Additionally, Ext is computed over the wrong category (script A = cluster algebra, not the module category of A).

**Arbiter's justification:**
> Both reviewers flag this as a broken argument. The contradiction step is a non-sequitur without proving linear independence of F-polynomials, and the category mismatch (Ext over the cluster algebra vs. the Jacobian algebra) is not merely cosmetic. This proposition is the key link between tensor product simplicity and homological algebra, so its failure undermines a main advertised application.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

### F264

- Paper: *A New Radio to Overcome Critical Link Budgets*
- Field: Computer Science
- SPOT severity tier: `retract`

**SPOT-annotated error in this paper (context only):**
> The error is that the beamforming gain for N antennas is incorrectly calculated as N, when it should actually be N^2, since coherent beamforming results in the received power increasing by the square of the number of antennas.

**Candidate finding (rated retraction-worthy):**
> The numerical examples compare MA-TISK with T > N (e.g., T = 18.375 versus N = 16) against N-antenna beamforming and report combining gains meeting or exceeding beamforming gain. This comparison is unfair because MA-TISK uses more time-frequency resources per symbol than the beamforming baseline. The benchmark could trivially be matched by allowing beamforming to also use longer integration windows or more subcarriers.

**Arbiter's justification:**
> This is the empirical instantiation of the normalization error above. The paper's primary numerical evidence (gains of 12.2–12.6 dB versus 12.0 dB for 16-antenna beamforming) is invalid because the two schemes are not compared under equal resource usage. Both reviewers flagged this. Reviewer A rated it RETRACTION-WORTHY from the start. Reviewer B initially rated the unfair comparison as MAJOR-REVISION but moved toward RETRACTION-WORTHY in reflection, recognizing it is not a 'fixable' issue but a logical invalidation of the reported results. Because this is the paper's main quantitative evidence for its headline claim, it is retraction-worthy.

Verdict (record in `audit_blinded.csv`): [ ] VALID  [ ] RELATED  [ ] FALSE

---

