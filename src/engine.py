"""
engine.py - Tabulation, Monthly Ranking Matrix, and Cumulative Composite Scorer
"""

import os
from typing import Dict, List, Tuple
import pandas as pd
from src.metrics import (
    compute_dual_crps,
    compute_coverage_penalty,
    compute_smad,
    compute_composite_score,
)

MODELS = [
    "truetether",
    "regimeecho",
    "tailwhip",
    "chamberlain",
    "gatekeeper",
    "echophase",
]


def load_actuals(actuals_path: str = "data/actuals.csv", include_in_progress: bool = False) -> pd.DataFrame:
    """
    Loads actuals and filters for evaluated months.
    Defaults to evaluating only CLOSED months.
    """
    if not os.path.exists(actuals_path):
        raise FileNotFoundError(f"Missing actuals file: {actuals_path}")

    df = pd.read_csv(actuals_path)
    df["Month"] = df["Month"].astype(str)
    
    if not include_in_progress and "Status" in df.columns:
        df = df[df["Status"].str.upper() == "CLOSED"].copy()

    return df.sort_values("Month").reset_index(drop=True)


def load_macro_friction(friction_path: str = "data/macro_friction.csv") -> pd.DataFrame:
    """
    Loads the qualitative macro friction ledger.
    """
    if not os.path.exists(friction_path):
        return pd.DataFrame(columns=["Month", "Regime", "Macro_Headwind_Tailwind", "Geopolitical_Shock"])
    
    df = pd.read_csv(friction_path)
    df["Month"] = df["Month"].astype(str)
    return df


def load_model_forecasts(models_dir: str = "models/") -> Dict[str, pd.DataFrame]:
    """
    Loads all model forecast CSVs from the models/ directory.
    """
    forecasts = {}
    for model in MODELS:
        file_path = os.path.join(models_dir, f"{model}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Missing forecast CSV for model '{model}' at: {file_path}")
        
        df = pd.read_csv(file_path)
        df["Month"] = df["Month"].astype(str)
        forecasts[model] = df

    return forecasts


def score_models_across_months(
    actuals_df: pd.DataFrame,
    forecasts: Dict[str, pd.DataFrame],
    base_anchor_s0: float = 69000.0,
) -> pd.DataFrame:
    """
    Scores each model for every month available in actuals_df.
    Computes CRPS, ECP, SMAD, and Composite Score.
    """
    records = []

    for _, actual_row in actuals_df.iterrows():
        month = actual_row["Month"]
        act_low = float(actual_row["Actual_Low"])
        act_high = float(actual_row["Actual_High"])

        for model_name, forecast_df in forecasts.items():
            match = forecast_df[forecast_df["Month"] == month]
            if match.empty:
                continue

            f_row = match.iloc[0].to_dict()

            crps_low, crps_high, crps_total = compute_dual_crps(act_low, act_high, f_row)
            ecp, breaches = compute_coverage_penalty(act_low, act_high, f_row)
            smad = compute_smad(act_low, act_high, f_row, base_anchor_s0=base_anchor_s0)
            composite = compute_composite_score(crps_total, smad, ecp)

            records.append({
                "Month": month,
                "Model": model_name,
                "CRPS_Low": crps_low,
                "CRPS_High": crps_high,
                "CRPS_Total": crps_total,
                "SMAD": smad,
                "ECP": ecp,
                "Composite_Score": composite,
                "Tail_Breach": breaches["tail_low"] or breaches["tail_high"],
                "Core_Breach": breaches["core_low"] or breaches["core_high"],
                "Actual_Low": act_low,
                "Actual_High": act_high,
                "Low_p50": float(f_row["Low_p50"]),
                "High_p50": float(f_row["High_p50"]),
            })

    df_scores = pd.DataFrame(records)
    return df_scores


def compute_monthly_ranks(df_scores: pd.DataFrame) -> pd.DataFrame:
    """
    Ranks models per month (1 = Best / Lowest Composite Score).
    Resolves ties deterministically by alphabetizing.
    """
    df_ranks = df_scores.copy()
    df_ranks["Rank"] = (
        df_ranks.groupby("Month")["Composite_Score"]
        .rank(method="min", ascending=True)
        .astype(int)
    )
    return df_ranks


def compute_cumulative_leaderboard(df_scores: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates composite metrics across all closed evaluated months.
    """
    grouped = df_scores.groupby("Model").agg(
        Mean_Composite=("Composite_Score", "mean"),
        Mean_CRPS=("CRPS_Total", "mean"),
        Mean_SMAD=("SMAD", "mean"),
        Total_ECP=("ECP", "sum"),
        Months_Evaluated=("Month", "count"),
    ).reset_index()

    grouped["Final_Rank"] = grouped["Mean_Composite"].rank(method="min", ascending=True).astype(int)
    return grouped.sort_values("Final_Rank").reset_index(drop=True)
    