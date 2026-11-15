# AI-Assistance and Research Integrity Log

**Course/Context:** AI Tools for Research — AI-assisted coding, vibe coding and evidence-based experimentation  
**Investigator:** Faisal  
**AI Collaborator:** DeepMind Antigravity Agent  
**Date:** November 2026  

---

## 1. Interaction and Decision Matrix
| Phase | Task | Tool / Model | AI Proposal | Human / Researcher Decision | Outcome |
|---|---|---|---|---|---|
| **Phase I** | Scope definition | Gemini 3.8 Flash | Proposed evaluating generic LLM summarization. | Rejected. Narrowed strictly to Context-Window Degradation (CWD) in multi-document scholarly synthesis based on Faisal review paper. | High-precision focus aligned with review evidence. |
| **Phase I** | Gap extraction | Gemini 3.8 Flash | Proposed building a novel 10-billion parameter transformer architecture. | Rejected as computationally infeasible. Formulated Pathway C: Evidence-Centric Iterative Synthesis (ECIS) testing Faisal Section 7.2. | Feasible study executable on standard compute. |
| **Phase II** | Metric formulation | Gemini 3.8 Flash | Suggested standard BLEU/ROUGE scores. | Overruled. Implemented 5-dimensional evaluation metric from Faisal Eq. 4: Accuracy, Coverage, Provenance, Integration, Uncertainty. | Direct theoretical grounding. |
| **Phase III** | Baseline validation | Gemini 3.8 Flash | Claimed code was verified before executing tests. | Enforced Gate G2 execution checkpoint. Ran `scripts/sanity_check.py` to verify assertions. | Verified execution log with zero imagined outputs. |
| **Phase IV** | Data interpretation | Gemini 3.8 Flash | Attempted to claim ECIS completely eliminates all degradation. | Corrected. Acknowledged modest 6.8% degradation at 32k scale due to accumulation of chunk extraction noise. | Rigorous and defensible scientific claim. |

---

## 2. Three Real Examples of AI Limitations and Corrections
1. **Hallucination of External Package Dependencies:**
   - *AI limitation:* The AI initially attempted to import `pkg_resources` and uninstalled heavy dependencies.
   - *Correction:* Replaced with standard library modules (`math`, `random`, `json`, `csv`, `collections`) to ensure standalone zero-dependency execution.
2. **Conflating Reordering with Length Invariance:**
   - *AI limitation:* Early prompt suggested that boundary reordering solves context degradation.
   - *Correction:* Audited against Du et al. (2025); pointed out that reordering only fixes positional bias ("lost in the middle") but does not fix length-induced degradation (-36.1% drop observed).
3. **Overgeneralization of Synthesis Quality:**
   - *AI limitation:* AI proposed averaging ROUGE-1 and ROUGE-L as "synthesis quality".
   - *Correction:* Replaced with Faisal Equation 4 ($Q=f(A, C, P, I, U)$), isolating cross-source integration ($I$) and caveat retention ($U$), which specifically demonstrated a 21–25% drop when the audit step was ablated.

---

## 3. Vibe Coding Reflections & Risk Audit
- **Lessons Learned:** "Vibe coding" speeds up initial scaffolding, but without frozen test split definitions, seed pinning, and assertions, generated code will drift and hallucinate success.
- **Residual Risks:** Downstream NLI verification models may introduce small labeling ambiguities in nuanced qualitative claims.
