"""
visualizer.py - Single-Panel Bump Chart with High-Contrast Colors & Cumulative Labeling
"""

import os
from typing import Dict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# High-contrast color palette with distinct separation between EchoPhase and Chamberlain
MODEL_COLORS: Dict[str, str] = {
    "regimeecho": "#38bdf8",   # Sky Blue
    "echophase": "#fbbf24",    # Vivid Amber / Gold
    "truetether": "#10b981",   # Emerald Green
    "tailwhip": "#ec4899",     # Hot Pink
    "chamberlain": "#8b5cf6",  # Electric Indigo (distinct from gold/violet)
    "gatekeeper": "#ef4444",   # Crimson Red
}


def render_ranking_bump_chart(
    df_ranks: pd.DataFrame,
    leaderboard: pd.DataFrame,
    output_path: str = "output/monthly_rankings.png",
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    months = sorted(df_ranks["Month"].unique())
    x_indices = np.arange(len(months))
    x_map = {m: i for i, m in enumerate(months)}

    # Map cumulative rank from leaderboard table
    cum_rank_map = dict(zip(leaderboard["Model"], leaderboard["Final_Rank"]))

    fig, ax = plt.subplots(figsize=(12, 6), facecolor="#0f172a")
    ax.set_facecolor("#1e293b")
    ax.grid(color="#334155", linestyle="--", linewidth=0.7, alpha=0.7)

    for model, color in MODEL_COLORS.items():
        m_df = df_ranks[df_ranks["Model"] == model].sort_values("Month")
        if m_df.empty:
            continue

        xs = [x_map[m] for m in m_df["Month"]]
        ys = m_df["Rank"].values

        ax.plot(xs, ys, color=color, linewidth=3.0, label=model, zorder=3)
        ax.scatter(xs, ys, color=color, s=110, edgecolors="#0f172a", linewidth=2.0, zorder=4)

        # Terminal label showing final month rank + cumulative leaderboard rank
        last_x, last_y = xs[-1], ys[-1]
        cum_rank = cum_rank_map.get(model, last_y)
        label_text = f" {model.capitalize()} (Oct #{last_y} | Cum #{cum_rank})"

        ax.text(
            last_x + 0.08,
            last_y,
            label_text,
            color=color,
            va="center",
            ha="left",
            fontweight="bold",
            fontsize=10,
            zorder=5,
        )

    ax.set_yticks([1, 2, 3, 4, 5, 6])
    ax.set_yticklabels(["1st", "2nd", "3rd", "4th", "5th", "6th"], color="#f8fafc", fontsize=11, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xticks(x_indices)
    ax.set_xticklabels(months, color="#94a3b8", fontsize=11, fontweight="bold")
    ax.set_xlim(-0.2, len(months) - 1 + 1.25)
    ax.set_title("Bitcoin Pricing Models: Monthly Performance Rank Trajectory", color="#f8fafc", fontsize=15, fontweight="bold", pad=15)
    ax.set_ylabel("Leaderboard Position", color="#94a3b8", fontsize=12)
    ax.set_xlabel("Evaluation Month (2026)", color="#94a3b8", fontsize=11, labelpad=10)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Ranking bump chart successfully generated at: {output_path}")