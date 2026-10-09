# Forward 12-Month Bitcoin Pricing Models: Empirical Performance Audit

## 1. Executive Cumulative Leaderboard

| Rank | Model | Mean Composite Loss | Mean CRPS | Mean SMAD (%) | Total Coverage Penalty (ECP) | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **#1** | `regimeecho` | **12.34** | 4,827.4 | 11.90% | 150 | Active Anchor |
| **#2** | `echophase` | **16.66** | 6,641.2 | 19.06% | 175 | Active Anchor |
| **#3** | `truetether` | **29.74** | 9,717.7 | 26.75% | 400 | Under Review |
| **#4** | `tailwhip` | **30.47** | 10,330.9 | 28.07% | 400 | Under Review |
| **#5** | `chamberlain` | **31.51** | 10,940.6 | 27.39% | 425 | Under Review |
| **#6** | `gatekeeper` | **50.66** | 22,226.6 | 59.03% | 400 | Under Review |

---

## 2. Monthly Performance & Macro Ledger Matrix

| Month | 1st Place | 2nd Place | 3rd Place | 4th Place | 5th Place | 6th Place | Realized Range | Macro Regime |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-05** | `truetether` | `tailwhip` | `regimeecho` | `echophase` | `chamberlain` | $72,436 -$82,792 | Absorption |
| **2026-06** | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | `gatekeeper` | $58,076 -$73,970 | Liquidation |
| **2026-07** | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | `gatekeeper` | $57,748 -$66,910 | Consolidation |
| **2026-08** | `regimeecho` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | `gatekeeper` | $62,227 -$81,347 | Rebalancing |
| **2026-09** | `regimeecho` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | `gatekeeper` | $74,945 -$87,364 | Expansion |

---

## 3. Model Diagnostic Inferences

### `regimeecho` (Cumulative Rank #1)
- **Mean Composite Loss**: 12.3370
- **Continuous Ranked Probability Score (CRPS)**: 4,827.36
- **Scaled Median Absolute Deviation (SMAD)**: 11.90%
- **Total Empirical Coverage Penalty (ECP)**: 150 points
- **Diagnostic Assessment**: Demonstrates market-leading fidelity by maintaining strict stationarity around the empirical Era 4 residual increments. Avoided parameter runaway entirely during the summer liquidity slump, producing the lowest average error (11.90% SMAD) and minimal tail penalty violations.

### `echophase` (Cumulative Rank #2)
- **Mean Composite Loss**: 16.6594
- **Continuous Ranked Probability Score (CRPS)**: 6,641.23
- **Scaled Median Absolute Deviation (SMAD)**: 19.06%
- **Total Empirical Coverage Penalty (ECP)**: 175 points
- **Diagnostic Assessment**: Successfully tracked the 285-day sub-annual rebalancing harmonic. While starting slightly elevated during the May-June drawdown, it converged directly into the median actuals by September-October, demonstrating strong mid-cycle dynamic elasticity with a competitive 19.06% SMAD.

### `truetether` (Cumulative Rank #3)
- **Mean Composite Loss**: 29.7361
- **Continuous Ranked Probability Score (CRPS)**: 9,717.72
- **Scaled Median Absolute Deviation (SMAD)**: 26.75%
- **Total Empirical Coverage Penalty (ECP)**: 400 points
- **Diagnostic Assessment**: Continuous Ornstein-Uhlenbeck mean reversion provided reasonable structural bounds, but constant secular drift pressure created an upward bias (+$17,982 median offset), triggering recurrent core boundary breaches during prolonged horizontal absorption (Total ECP: 400).

### `tailwhip` (Cumulative Rank #4)
- **Mean Composite Loss**: 30.4737
- **Continuous Ranked Probability Score (CRPS)**: 10,330.92
- **Scaled Median Absolute Deviation (SMAD)**: 28.07%
- **Total Empirical Coverage Penalty (ECP)**: 400 points
- **Diagnostic Assessment**: Discontinuous Poisson jumps injected excessive tail dispersion into quiet summer trading blocks. The model over-estimated downside tail risk while simultaneously lifting median paths, resulting in elevated CRPS loss and repeated core band penalties (400 ECP).

### `chamberlain` (Cumulative Rank #5)
- **Mean Composite Loss**: 31.5091
- **Continuous Ranked Probability Score (CRPS)**: 10,940.58
- **Scaled Median Absolute Deviation (SMAD)**: 27.39%
- **Total Empirical Coverage Penalty (ECP)**: 425 points
- **Diagnostic Assessment**: Coupled stochastic volatility architecture struggled with the low-volatility summer grind. Negative leverage correlation assumptions produced diffusive spread widening rather than tight compression, accumulating a high composite penalty index (31.51).

### `gatekeeper` (Cumulative Rank #6)
- **Mean Composite Loss**: 50.6623
- **Continuous Ranked Probability Score (CRPS)**: 22,226.62
- **Scaled Median Absolute Deviation (SMAD)**: 59.03%
- **Total Empirical Coverage Penalty (ECP)**: 400 points
- **Diagnostic Assessment**: Suffered from severe positive feedback runaway in the SDE drift equation. Exponential cubic boundaries acted as an unintended accelerator when residuals deviated, driving extreme drift error (59.03% SMAD) and detaching the simulation from macro reality.
