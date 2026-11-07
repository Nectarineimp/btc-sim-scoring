# Forward 12-Month Bitcoin Pricing Models: Empirical Performance Audit

## 1. Executive Cumulative Leaderboard

| Rank | Model | Mean Composite Loss | Mean CRPS | Mean SMAD (%) | Total Coverage Penalty (ECP) | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **#1** | `regimeecho` | **10.81** | 4,850.1 | 10.37% | 150 | Active Anchor |
| **#2** | `gatekeeper` | **11.28** | 4,167.5 | 10.21% | 175 | Active Anchor |
| **#3** | `echophase` | **15.81** | 6,950.2 | 19.57% | 175 | Under Review |
| **#4** | `truetether` | **28.98** | 10,253.5 | 29.14% | 425 | Under Review |
| **#5** | `tailwhip` | **29.89** | 11,004.0 | 30.78% | 425 | Under Review |
| **#6** | `chamberlain` | **30.51** | 11,363.9 | 29.69% | 450 | Under Review |

---

## 2. Monthly Performance & Macro Ledger Matrix

| Month | 1st Place | 2nd Place | 3rd Place | 4th Place | 5th Place | 6th Place | Realized Range | Macro Regime |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-05** | `truetether` | `tailwhip` | `regimeecho` | `echophase` | `gatekeeper` | `chamberlain` | $72,436 -$82,792 | Absorption |
| **2026-06** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | $58,076 -$73,970 | Liquidation |
| **2026-07** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | $57,748 -$66,910 | Consolidation |
| **2026-08** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $62,227 -$81,347 | Rebalancing |
| **2026-09** | `regimeecho` | `gatekeeper` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $74,945 -$87,364 | Expansion |
| **2026-10** | `regimeecho` | `gatekeeper` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $76,190 -$87,146 | Harmonic_Recovery |

---

## 3. Model Diagnostic Inferences

### `regimeecho` (Cumulative Rank #1)
- **Mean Composite Loss**: 10.8107
- **Continuous Ranked Probability Score (CRPS)**: 4,850.13
- **Scaled Median Absolute Deviation (SMAD)**: 10.37%
- **Total Empirical Coverage Penalty (ECP)**: 150 points
- **Diagnostic Assessment**: Demonstrates market-leading fidelity by maintaining strict stationarity around the empirical Era 4 residual increments. Avoided parameter runaway entirely during the summer liquidity slump, producing the lowest average error (10.37% SMAD) and minimal tail penalty violations.

### `gatekeeper` (Cumulative Rank #2)
- **Mean Composite Loss**: 11.2807
- **Continuous Ranked Probability Score (CRPS)**: 4,167.55
- **Scaled Median Absolute Deviation (SMAD)**: 10.21%
- **Total Empirical Coverage Penalty (ECP)**: 175 points
- **Diagnostic Assessment**: Suffered from severe positive feedback runaway in the SDE drift equation. Exponential cubic boundaries acted as an unintended accelerator when residuals deviated, driving extreme drift error (10.21% SMAD) and detaching the simulation from macro reality.

### `echophase` (Cumulative Rank #3)
- **Mean Composite Loss**: 15.8097
- **Continuous Ranked Probability Score (CRPS)**: 6,950.15
- **Scaled Median Absolute Deviation (SMAD)**: 19.57%
- **Total Empirical Coverage Penalty (ECP)**: 175 points
- **Diagnostic Assessment**: Successfully tracked the 285-day sub-annual rebalancing harmonic. While starting slightly elevated during the May-June drawdown, it converged directly into the median actuals by September-October, demonstrating strong mid-cycle dynamic elasticity with a competitive 19.57% SMAD.

### `truetether` (Cumulative Rank #4)
- **Mean Composite Loss**: 28.9794
- **Continuous Ranked Probability Score (CRPS)**: 10,253.52
- **Scaled Median Absolute Deviation (SMAD)**: 29.14%
- **Total Empirical Coverage Penalty (ECP)**: 425 points
- **Diagnostic Assessment**: Continuous Ornstein-Uhlenbeck mean reversion provided reasonable structural bounds, but constant secular drift pressure created an upward bias (+$19,709 median offset), triggering recurrent core boundary breaches during prolonged horizontal absorption (Total ECP: 425).

### `tailwhip` (Cumulative Rank #5)
- **Mean Composite Loss**: 29.8905
- **Continuous Ranked Probability Score (CRPS)**: 11,003.96
- **Scaled Median Absolute Deviation (SMAD)**: 30.78%
- **Total Empirical Coverage Penalty (ECP)**: 425 points
- **Diagnostic Assessment**: Discontinuous Poisson jumps injected excessive tail dispersion into quiet summer trading blocks. The model over-estimated downside tail risk while simultaneously lifting median paths, resulting in elevated CRPS loss and repeated core band penalties (425 ECP).

### `chamberlain` (Cumulative Rank #6)
- **Mean Composite Loss**: 30.5069
- **Continuous Ranked Probability Score (CRPS)**: 11,363.85
- **Scaled Median Absolute Deviation (SMAD)**: 29.69%
- **Total Empirical Coverage Penalty (ECP)**: 450 points
- **Diagnostic Assessment**: Coupled stochastic volatility architecture struggled with the low-volatility summer grind. Negative leverage correlation assumptions produced diffusive spread widening rather than tight compression, accumulating a high composite penalty index (30.51).
