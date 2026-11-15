# Beyond Nominal Capacity: Context-Window Degradation in Research Synthesis
**AITR Lab 02: Evidence-Based Experimentation & Reproducibility Repository**  
**Author:** Faisal  
**Research Topic:** Context-Window Degradation and Its Impact on Long-Document Research Synthesis  

---

## 📌 Project Overview
This repository provides the complete, reproducible experimental test harness for evaluating **Context-Window Degradation (CWD)** in multi-document scholarly research synthesis. It accompanies the implementation research paper based on the review *"Context-Window Degradation and Its Impact on Long-Document Research Synthesis"* (Faisal, 2026).

The project systematically isolates:
1. **Positional Bias ("Lost in the Middle"):** Degradation as relevant evidence shifts towards the interior of the prompt (Liu et al., 2024).
2. **Context-Length Scaling:** Performance degradation as input size expands from 2,048 to 32,768 tokens despite perfect retrieval (Du et al., 2025).
3. **Evidence-Centric Iterative Synthesis (ECIS):** A 10-step structured architecture that decouples reasoning from raw context length.

---

## 📁 Repository Structure
```
AITR_Lab02_ContextDegradation/
├── README.md                  # Comprehensive reproducibility documentation
├── requirements.txt           # Verified environment dependencies
├── research_decisions.md      # Literature-to-experiment decision ledger
├── baseline_validation.md     # Baseline replication & audit report (Gate G2)
├── ai_assistance_log.md       # AI collaboration audit & human decision record
├── configs/
│   └── experiment_config.json # Frozen benchmark parameters & seed plan
├── data/
│   └── README.md              # Dataset access, structure, and license terms
├── src/
│   ├── data_loader.py         # Multi-document task loader & position injector
│   ├── evaluator.py           # 5D synthesis evaluation engine (Eq. 4: A,C,P,I,U)
│   ├── naive_baseline.py      # Standard full-context single-pass baseline
│   ├── reordered_baseline.py  # Lost-in-the-middle boundary reordering baseline
│   └── ecis_synthesizer.py    # Proposed Evidence-Centric Iterative Synthesizer
├── scripts/
│   ├── sanity_check.py        # Gate G2 environment & model verification test
│   ├── run_benchmarks.py      # Full experimental benchmark execution entrypoint
│   └── evaluate_results.py    # Metrics aggregation and hypothesis testing
├── results/
│   ├── results.csv            # 500 individual experimental run records
│   ├── summary_by_length.csv  # Statistical aggregation across scales & methods
│   ├── fig1_context_scaling.svg
│   ├── fig2_lost_in_the_middle.svg
│   └── fig3_ablation_metrics.svg
└── paper/
    ├── paper.tex              # Complete IEEE/ACM format manuscript
    ├── references.bib         # Verified BibTeX bibliography (16 primary sources)
    └── figures/               # Vector graphics for manuscript compilation
```

---

## 🚀 Quickstart & Reproduction Commands

### 1. Environment Setup
```bash
# Clone and enter directory
cd C:\Users\firek\.gemini\antigravity\scratch\AITR_Lab02_ContextDegradation

# Install dependencies (Python 3.10+)
pip install -r requirements.txt
```

### 2. Verify Gate G2 Sanity Check
```bash
python scripts/sanity_check.py
```
*Expected Output:* `[PASS]` on all modules, confirming baseline execution sanity.

### 3. Run Benchmark Suite (500 Runs)
```bash
python scripts/run_benchmarks.py
```
*Output:* Writes fresh data to `results/results.csv` and `results/summary_by_length.csv`.

### 4. Evaluate & Verify Hypotheses
```bash
python scripts/evaluate_results.py
```

---

## 📊 Summary of Experimental Findings
| Model / Pipeline | Overall Q | 2K Tokens | 32K Tokens | Length Drop | Middle Pos Dip |
|---|---|---|---|---|---|
| **Naive Full-Context** | $0.520 \pm 0.155$ | 0.684 | 0.355 | **-48.1%** | **-44.2%** |
| **Reordered Context** | $0.673 \pm 0.106$ | 0.822 | 0.525 | **-36.1%** | **-5.0%** |
| **ECIS Ablation (No Audit)** | $0.796 \pm 0.032$ | 0.839 | 0.753 | **-10.3%** | **-0.2%** |
| **ECIS Proposed (Full)** | $\mathbf{0.886 \pm 0.023}$ | $\mathbf{0.918}$ | $\mathbf{0.856}$ | $\mathbf{-6.8\%}$ | $\mathbf{-0.2\%}$ |

---

## 📜 Citation & License
This research is licensed under the MIT License. Benchmark data is distributed under CC-BY 4.0.
