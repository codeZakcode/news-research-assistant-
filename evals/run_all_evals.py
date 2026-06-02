"""
Member C — Master eval runner
Runs all 4 layers and prints a combined scorecard
"""

from eval_retrieval import run_retrieval_evals
from eval_answer_quality import run_answer_quality_evals
from eval_agent_behaviour import run_agent_behaviour_evals


def run_all_evals():
    print("\n" + "="*55)
    print("  NEWS RESEARCH ASSISTANT — FULL EVAL SCORECARD")
    print("="*55)

    retrieval = run_retrieval_evals(k=5)
    answer_quality = run_answer_quality_evals()
    agent_behaviour = run_agent_behaviour_evals()

    print("\n" + "="*55)
    print("  SUMMARY")
    print("="*55)
    all_results = {**retrieval, **answer_quality, **agent_behaviour}
    for metric, score in all_results.items():
        print(f"  {metric:<30} {score}")
    print("="*55)


if __name__ == "__main__":
    run_all_evals()
