"""
metrics.py - Probabilistic and Empirical Scoring Engine for btc-sim-scoring

Implements:
1. Discrete Quantile Continuous Ranked Probability Score (CRPS) approximation
2. Empirical Coverage Penalty (ECP) across 1-sigma core and 2-sigma tails
3. Scaled Median Absolute Deviation (SMAD)
4. Composite Performance Index (CPI) combining all loss components
"""

from typing import Dict, Tuple
import numpy as np


QUANTILE_LEVELS = [0.05, 0.16, 0.50, 0.84, 0.95]


def quantile_loss(y: float, q_val: float, tau: float) -> float:
    """
    Computes the standard asymmetric pinball/quantile loss for a single quantile level tau.
    QS_tau(y, q) = 2 * (1_{y < q} - tau) * (q - y)
    """
    indicator = 1.0 if y < q_val else 0.0
    return 2.0 * (indicator - tau) * (q_val - y)


def compute_distribution_crps(realized_val: float, quantiles: Dict[str, float], prefix: str) -> float:
    """
    Approximates CRPS across the 5 standard quantile levels: p05, p16, p50, p84, p95.
    Expects dictionary keys matching e.g. f"{prefix}_p05", f"{prefix}_p16", etc.
    """
    losses = []
    for tau in QUANTILE_LEVELS:
        key = f"{prefix}_p{int(tau * 100):02d}"
        if key not in quantiles:
            raise KeyError(f"Missing expected quantile column: {key}")
        q_val = float(quantiles[key])
        losses.append(quantile_loss(realized_val, q_val, tau))

    return float(np.mean(losses))


def compute_dual_crps(
    actual_low: float,
    actual_high: float,
    forecast_row: Dict[str, float]
) -> Tuple[float, float, float]:
    """
    Evaluates CRPS independently on downside stress tests (Low_p*) and upside momentum (High_p*).
    Returns (crps_low, crps_high, crps_total).
    """
    crps_low = compute_distribution_crps(actual_low, forecast_row, prefix="Low")
    crps_high = compute_distribution_crps(actual_high, forecast_row, prefix="High")
    crps_total = 0.5 * (crps_low + crps_high)
    return crps_low, crps_high, crps_total


def compute_coverage_penalty(
    actual_low: float,
    actual_high: float,
    forecast_row: Dict[str, float]
) -> Tuple[int, Dict[str, bool]]:
    """
    Evaluates whether the realized range breached the modeled core or tail bounds.

    Penalties:
    - 1-sigma Core Breach (Low < Low_p16 or High > High_p84): +25 points each
    - 2-sigma Tail Breach (Low < Low_p05 or High > High_p95): +100 points each
    """
    low_p05 = float(forecast_row["Low_p05"])
    low_p16 = float(forecast_row["Low_p16"])
    high_p84 = float(forecast_row["High_p84"])
    high_p95 = float(forecast_row["High_p95"])

    breaches = {
        "tail_low": actual_low < low_p05,
        "core_low": actual_low < low_p16,
        "core_high": actual_high > high_p84,
        "tail_high": actual_high > high_p95,
    }

    penalty = 0
    # Core penalties
    if breaches["core_low"]:
        penalty += 25
    if breaches["core_high"]:
        penalty += 25

    # Tail penalties (severe out-of-distribution penalty)
    if breaches["tail_low"]:
        penalty += 100
    if breaches["tail_high"]:
        penalty += 100

    return penalty, breaches


def compute_smad(
    actual_low: float,
    actual_high: float,
    forecast_row: Dict[str, float],
    base_anchor_s0: float = 69000.0
) -> float:
    """
    Computes Scaled Median Absolute Deviation (SMAD) relative to initial benchmark spot price S_0.
    Normalized as a percentage of initial spot capital.
    """
    low_p50 = float(forecast_row["Low_p50"])
    high_p50 = float(forecast_row["High_p50"])

    abs_err_low = abs(low_p50 - actual_low)
    abs_err_high = abs(high_p50 - actual_high)

    smad = 0.5 * ((abs_err_low / base_anchor_s0) + (abs_err_high / base_anchor_s0)) * 100.0
    return float(smad)


def compute_composite_score(
    crps_total: float,
    smad: float,
    coverage_penalty: int,
    w_crps: float = 0.45,
    w_smad: float = 0.35,
    w_cov: float = 0.20
) -> float:
    """
    Computes the unified Composite Performance Index (CPI).
    Lower score indicates a more accurate, disciplined distribution fit.
    """
    # Normalize CRPS by 1,000 to bring it into parity with percentage scales
    norm_crps = crps_total / 1000.0
    composite_index = (w_crps * norm_crps) + (w_smad * smad) + (w_cov * coverage_penalty)
    return float(composite_index)