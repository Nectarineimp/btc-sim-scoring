"""
visualizer.py - Two-Tier Bump Chart & Aligned Macro Friction Ribbon
"""

import os
from typing import Dict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Aesthetic palette matching dark visualizer theme
MODEL_COLORS: Dict[str, str] = {
    "regimeecho": "#38bdf8",   # Sky Blue
    "echophase": "#f59e0b",    # Amber / Gold
    "truetether": "#10b981",   # Emerald Green
    "tailwhip": "#ec4899",     # Pink / Magenta
    "chamberlain": "#a855f7",  # Violet
    "gatekeeper": "#ef4444",   # Crimson
}


def render_ranking_bump_chart(
    df_ranks: pd.DataFrame,
    df_macro: pd.DataFrame,
    output_path: str = "output/monthly_rankings.png",
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    months = sorted(df_ranks["Month"].unique())
    x_indices = np.arange(len(months))
    x_map = {m: i for i, m in enumerate(months)}

    # Two-tier composite canvas: Top = Rank Bump Chart, Bottom = Macro Ledger
    fig, (ax_top, ax_bottom) = plt.subplots(
        2, 1, figsize=(14, 10), gridspec_kw={"height_ratios": [3, 1.8]}, facecolor="#0f172a"
    )

    # -------------------------------------------------------------
    # TOP PANEL: Bump Chart (Ranks 1 to 6)
    # -------------------------------------------------------------
    ax_top.set_facecolor("#1e293b")
    ax_top.grid(color="#334155", linestyle="--", linewidth=0.7, alpha=0.7)

    for model, color in MODEL_COLORS.items():
        m_df = df_ranks[df_ranks["Model"] == model].sort_values("Month")
        if m_df.empty:
            continue

        xs = [x_map[m] for m in m_df["Month"]]
        ys = m_df["Rank"].values

        # Plot spline/line and nodes
        ax_top.plot(xs, ys, color=color, linewidth=3.0, label=model, zorder=3)
        ax_top.scatter(xs, ys, color=color, s=110, edgecolors="#0f172a", linewidth=2.0, zorder=4)

        # Annotate terminal rank node
        last_x, last_y = xs[-1], ys[-1]
        ax_top.text(
            last_x + 0.08,
            last_y,
            f" {model.capitalize()} (#{last_y})",
            color=color,
            va="center",
            ha="left",
            fontweight="bold",
            fontsize=10,
            zorder=5,
        )

    ax_top.set_yticks([1, 2, 3, 4, 5, 6])
    ax_top.set_yticklabels(["1st", "2nd", "3rd", "4th", "5th", "6th"], color="#f8fafc", fontsize=11, fontweight="bold")
    ax_top.invert_yaxis()  # Rank 1 at the top
    ax_top.set_xticks(x_indices)
    ax_top.set_xticklabels(months, color="#94a3b8", fontsize=11, fontweight="bold")
    ax_top.set_xlim(-0.2, len(months) - 1 + 0.85)
    ax_top.set_title("Bitcoin Pricing Models: Monthly Performance Rank Trajectory", color="#f8fafc", fontsize=15, fontweight="bold", pad=15)
    ax_top.set_ylabel("Leaderboard Position", color="#94a3b8", fontsize=12)

    # -------------------------------------------------------------
    # BOTTOM PANEL: Aligned Macro Friction Ledger Ribbon
    # -------------------------------------------------------------
    ax_bottom.set_facecolor("#1e293b")
    ax_bottom.set_xticks(x_indices)
    ax_bottom.set_xticklabels([])
    ax_bottom.set_yticks([])
    ax_bottom.set_xlim(-0.2, len(months) - 1 + 0.85)
    ax_bottom.set_ylim(0, 1)

    for i, m in enumerate(months):
        m_friction = df_macro[df_macro["Month"] == m]
        if not m_friction.empty:
            row = m_friction.iloc[0]
            regime = row.get("Regime", "N/A")
            etf_flow = row.get("Net_ETF_Flow", "N/A")
            notes = str(row.get("Macro_Headwind_Tailwind", "N/A"))
            shock = str(row.get("Geopolitical_Shock", "None"))
        else:
            regime, etf_flow, notes, shock = "N/A", "N/A", "N/A", "None"

        # Format clean card
        text_content = (
            f"REGIME: {regime}\n"
            f"FLOW: {etf_flow}\n"
            f"MACRO: {notes[:36]}...\n"
            f"SHOCK: {shock[:25]}"
        )

        ax_bottom.text(
            i,
            0.5,
            text_content,
            color="#cbd5e1",
            fontsize=8.5,
            family="monospace",
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.5", facecolor="#0f172a", edgecolor="#475569", linewidth=1.2),
        )

    ax_bottom.set_xlabel("Evaluation Month / Macro Context Ribbon", color="#94a3b8", fontsize=11, labelpad=10)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Ranking bump chart successfully generated at: {output_path}")