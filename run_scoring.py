#!/usr/bin/env python3
"""
run_scoring.py - Main Entrypoint for btc-sim-scoring Pipeline
"""

import sys
from src.engine import (
    load_actuals,
    load_macro_friction,
    load_model_forecasts,
    score_models_across_months,
    compute_monthly_ranks,
    compute_cumulative_leaderboard,
)
from src.visualizer import render_ranking_bump_chart
from src.report import generate_markdown_report


def main():
    print("==================================================")
    print(" Running btc-sim-scoring Evaluation Suite")
    print("==================================================")

    # 1. Load data assets
    actuals = load_actuals("data/actuals.csv", include_in_progress=False)
    macro_friction = load_macro_friction("data/macro_friction.csv")
    forecasts = load_model_forecasts("models/")

    # 2. Compute metrics and rankings
    scores = score_models_across_months(actuals, forecasts)
    ranks = compute_monthly_ranks(scores)
    leaderboard = compute_cumulative_leaderboard(scores)

    # 3. Render visual bump chart
    render_ranking_bump_chart(ranks, macro_friction, "output/monthly_rankings.png")

    # 4. Generate markdown audit deliverable
    generate_markdown_report(scores, ranks, macro_friction, leaderboard, "output/performance_audit.md")

    print("Scoring run completed successfully.")


if __name__ == "__main__":
    main()