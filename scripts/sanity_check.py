"""
sanity_check.py: Gate G2 Verification Script.
Checks environment compatibility, data loader integrity, and baseline execution sanity.
"""
import sys
import os

def run_sanity_check():
    print("=" * 60)
    print("GATE G2: BASELINE AND ENVIRONMENT SANITY CHECK")
    print(f"Python Runtime: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Check imports
    try:
        from src.data_loader import ScholarDataLoader
        from src.naive_baseline import NaiveFullContextSynthesizer
        from src.reordered_baseline import ReorderedContextSynthesizer
        from src.ecis_synthesizer import EvidenceCentricSynthesizer
        from src.evaluator import SynthesisEvaluator
        print("[PASS] Successfully imported all src modules.")
    except Exception as e:
        print(f"[FAIL] Module import failed: {e}")
        return False

    # Check data generation
    try:
        config_path = os.path.join("configs", "experiment_config.json")
        loader = ScholarDataLoader(config_path)
        sample_task = loader.load_task(task_id=1, context_length=4096, position_ratio=0.5, seed=42)
        assert sample_task["target_context_tokens"] == 4096
        assert len(sample_task["ground_truth_evidence"]) == 4
        print(f"[PASS] ScholarDataLoader successfully generated task: {sample_task['research_question'][:45]}...")
    except Exception as e:
        print(f"[FAIL] Data loader verification failed: {e}")
        return False

    # Check baseline execution
    try:
        naive = NaiveFullContextSynthesizer()
        res_naive = naive.synthesize(sample_task)
        reordered = ReorderedContextSynthesizer()
        res_reorder = reordered.synthesize(sample_task)
        ecis = EvidenceCentricSynthesizer(enable_audit=True)
        res_ecis = ecis.synthesize(sample_task)
        
        q_naive = SynthesisEvaluator.evaluate_claims(sample_task["ground_truth_evidence"], res_naive)["Q"]
        q_reorder = SynthesisEvaluator.evaluate_claims(sample_task["ground_truth_evidence"], res_reorder)["Q"]
        q_ecis = SynthesisEvaluator.evaluate_claims(sample_task["ground_truth_evidence"], res_ecis)["Q"]
        
        print(f"[PASS] Model execution sanity verified.")
        print(f"       Naive Q (middle pos @ 4K):     {q_naive:.3f}")
        print(f"       Reordered Q (middle pos @ 4K): {q_reorder:.3f}")
        print(f"       ECIS Q (middle pos @ 4K):      {q_ecis:.3f}")
        assert q_ecis > q_naive, "ECIS must outperform Naive in middle position"
    except Exception as e:
        print(f"[FAIL] Model execution test failed: {e}")
        return False

    print("=" * 60)
    print("ALL GATE G2 SANITY CHECKS PASSED SUCCESSFULLY!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = run_sanity_check()
    sys.exit(0 if success else 1)
