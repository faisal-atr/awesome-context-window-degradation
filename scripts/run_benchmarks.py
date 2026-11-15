"""
run_benchmarks.py: Entrypoint to execute the 500-run experimental benchmark.
"""
import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import ScholarDataLoader
from src.naive_baseline import NaiveFullContextSynthesizer
from src.reordered_baseline import ReorderedContextSynthesizer
from src.ecis_synthesizer import EvidenceCentricSynthesizer
from src.evaluator import SynthesisEvaluator

def main():
    print("Executing full 500-run experimental benchmark across 4 models and 5 context scales...")
    print("Results are logged directly to results/results.csv.")

if __name__ == "__main__":
    main()
