| Priority                     | Dataset / Benchmark | What it measures                                     | Why it fits your paper                                                     |
| ---------------------------- | ------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------- |
| **1 — Essential**            | **LongBench**       | Long-context QA, summarization, multi-document tasks | Best overall benchmark for demonstrating degradation as context grows      |
| **2 — Essential**            | **LooGLE**          | Long dependencies, QA, long-document summarization   | Directly targets failures in long-context understanding                    |
| **3 — Essential**            | **QASPER**          | QA over scientific papers + evidence selection       | **Excellent for research synthesis** because it uses real scholarly papers |
| **4 — Essential**            | **RULER**           | Controlled performance vs. context length            | Best for experimentally measuring **context-window degradation**           |
| **5 — Strongly recommended** | **GovReport**       | Long-document summarization                          | Useful for testing compression/summarization degradation                   |
| **6 — Recommended**          | **MultiDoc2Dial**   | Multi-document evidence-grounded reasoning           | Useful for distributed evidence across documents                           |
| **7 — Optional**             | **HotpotQA**        | Multi-hop reasoning                                  | Useful for testing evidence integration                                    |
| **8 — Optional**             | **NarrativeQA**     | Long-document comprehension                          | Useful as an additional long-document baseline                             |

