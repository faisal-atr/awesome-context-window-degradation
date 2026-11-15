# ScholarCWD-Bench Dataset

## Overview
ScholarCWD-Bench is a controlled benchmark for evaluating context-window degradation (CWD) in multi-document scholarly synthesis. It tests language models and synthesis workflows on their ability to locate, extract, integrate, and calibrate evidence across varying context lengths (2,048 to 32,768 tokens) and evidence positions.

## Structure
- `tasks.json`: 100 multi-document research synthesis queries across machine learning and NLP domains.
- Document sets range from 5 to 80 documents per synthesis question.
- Injected Ground Truth:
  - Consensus findings: Claims supported across multiple documents.
  - Methodological caveats: Nuances, population constraints, and boundary conditions.
  - Contradictions (30% prevalence): Conflicting effect estimates or opposing conclusions arising from sample sizes, variable operationalization, or temporal divergence.
  - Needle positions: Key caveats systematically placed at 5 relative offsets: Beginning (0-10%), Early (25%), Middle (50%), Late (75%), and End (90-100%).

## Data License & Access
- Curated from open-access scientific preprints under Creative Commons CC-BY 4.0 licenses.
- Raw synthetic test harness is self-contained and reproducible.
