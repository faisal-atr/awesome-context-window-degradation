# Research Decisions Log: Context-Window Degradation (CWD) Study

**Project Title:** Beyond Nominal Capacity: Evaluating and Mitigating Context-Window Degradation in Multi-Document Scholarly Research Synthesis  
**Investigator:** Faisal (Student Researcher)  
**Mentor & Assistant:** AI Research System / Technical Pair Programmer  
**Date:** November 2026  
**Status:** Frozen Experimental Protocol & Completed Evaluation  

---

## 1. Literature Evidence Ledger
Every claim is rigorously categorized under the three-tier evidence standard:
- `[VERIFIED]`: Directly confirmed from original literature and actual experimental runs.
- `[INFERRED]`: Plausible mechanistic deduction requiring empirical isolation.
- `[UNKNOWN]`: Unresolved empirical question requiring targeted benchmark exploration.

| ID | Finding / Statement | Status | Evidence Source | Technical Implication |
|---|---|---|---|---|
| L1 | Models display marked U-shaped positional degradation in long contexts ("lost in the middle"), suffering >20% accuracy drop in the middle. | `[VERIFIED]` | Liu et al. (2024), *TACL* [10]; Review p. 2, 4 | Context boundary reordering is an essential baseline. |
| L2 | Context length alone causes 13.9% to 85% performance degradation even when retrieval is flawless and irrelevant noise is masked. | `[VERIFIED]` | Du et al. (2025), *EMNLP* [4]; Review p. 2, 5 | Retrieval by itself cannot solve context degradation; reasoning scale fails. |
| L3 | Question-aware prompt compression and reordering can boost latency and performance in long-context QA. | `[VERIFIED]` | Jiang et al. (2024), *ACL* [7]; Review p. 5, 9 | Prompt compression optimizes $|C'| \ll |C|$ but risks losing critical caveats. |
| L4 | Effective context utilization diverges dramatically from nominal context window capacity (e.g., 128k/1M tokens). | `[VERIFIED]` | Bai et al. (2024), *LongBench* [1]; Li et al. (2024), *LooGLE* [9] | Evaluations must report continuous degradation curves, not single token caps. |
| L5 | Multi-document research synthesis requires cross-source contradiction detection and caveat preservation, which collapse under naive single-pass concatenation. | `[INFERRED]` | Faisal (2026) Review Sections 4.2–4.5 & Eq. 1–2 | Single-pass concatenation homogenizes conflicting effect sizes into false consensus. |
| L6 | An iterative 10-step evidence-centric synthesis pipeline (ECIS) can decouple reasoning from context length $L$. | `[INFERRED]` | Faisal (2026) Review Section 7.2 | Proposed contribution: lift documents into structured tuples $(C, E, V, S)$. |
| L7 | Exact mathematical form of evidence weighting $w(p_i, L, C)$ and composite quality $Q=f(A,C,P,I,U)$. | `[UNKNOWN]` | Faisal (2026) Review Eq. 2 & 4 | Must be operationalized and tested empirically in this study. |

---

## 2. Candidate Research Gaps & Ranking
From Faisal's review paper, five computationally testable research gaps were extracted:

1. **Gap 1: Disentangling Length-Induced Degradation from Positional Attenuation.**
   - *Review Passage:* Section 3.3 (Du et al.) vs. Section 3.2 (Liu et al.).
   - *Question:* Does reordering evidence to context boundaries rescue multi-document synthesis as context expands from 2K to 32K tokens?
   - *Feasibility:* High. Testable via controlled context scaling and boundary placement.

2. **Gap 2: Collapse of Methodological Caveats and Contradiction Detection in Single-Pass Synthesis.**
   - *Review Passage:* Section 4.3 & 4.5.
   - *Question:* How does increasing context length affect an LLM's ability to retain negative results and detect conflicting effect sizes?
   - *Feasibility:* Very High. Measure retention rate of injected caveats.

3. **Gap 3: Compression Lossiness vs. Downstream Synthesis Reasoning.**
   - *Review Passage:* Section 5.3 & Eq. 3 ($|C'| \ll |C|$).
   - *Question:* Does aggressive prompt compression discard the qualifiers needed for scientific synthesis?
   - *Feasibility:* Moderate. Requires measuring semantic qualifier retention.

4. **Gap 4: Dynamic Context Allocation based on Claim Significance.**
   - *Review Passage:* Section 7.5.
   - *Question:* Can an adaptive token budget allocator improve synthesis efficiency over fixed chunking?
   - *Feasibility:* Lower within current compute budget.

5. **Gap 5: Claim-Level Provenance Tracking in Cross-Document Synthesis.**
   - *Review Passage:* Section 4.4 & 7.3.
   - *Question:* Does structured evidence extraction guarantee citation fidelity compared to free-form generation?
   - *Feasibility:* High. Measurable via citation attribution precision.

### Top-3 Gap Ranking:
- **Rank 1 (Chosen): Gap 1 & 2 Combined.** Investigate whether boundary reordering prevents length-induced degradation in multi-document synthesis, and evaluate whether Evidence-Centric Iterative Synthesis (ECIS) recovers lost-in-the-middle caveats and contradictions.
- **Rank 2: Gap 5.** Claim-level provenance audit.
- **Rank 3: Gap 3.** Lossiness in prompt compression.

---

## 3. Study Pathway Decision
- **Selected Pathway:** **Pathway C (Targeted Modification / Extension)** combined with **Pathway B (Controlled Comparative Study)**.
- **Baseline:** Naive Full-Context Concatenation (representing standard RAG/single-pass ingestion).
- **Comparator:** Boundary Document Reordering (Jiang et al., 2024 / Liu et al., 2024).
- **Proposed Method:** Evidence-Centric Iterative Synthesis (ECIS), implementing the 10-stage architecture from Faisal (2026) Section 7.2.
- **Ablation:** ECIS without Contradiction and Provenance Audit.
- **Resource Constraints:** Executable on commodity GPU/CPU, evaluated over 500 controlled runs across 5 context sizes (2K, 4K, 8K, 16K, 32K) and 5 positional strata.
