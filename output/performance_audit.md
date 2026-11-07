# Forward 12-Month Bitcoin Pricing Models: Empirical Performance Audit

## 1. Executive Cumulative Leaderboard

| Rank | Model | Mean Composite Loss | Mean CRPS | Mean SMAD (%) | Total Coverage Penalty (ECP) | Status |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **#1** | `regimeecho` | **10.98** | 6,035.2 | 9.34% | 150 | Active Anchor |
| **#2** | `gatekeeper` | **11.46** | 5,356.8 | 9.19% | 175 | Active Anchor |
| **#3** | `echophase` | **16.17** | 9,264.6 | 17.62% | 175 | Under Review |
| **#4** | `truetether` | **29.54** | 13,754.8 | 26.24% | 425 | Under Review |
| **#5** | `tailwhip` | **30.51** | 14,751.9 | 27.72% | 425 | Under Review |
| **#6** | `chamberlain` | **31.02** | 14,791.8 | 26.74% | 450 | Under Review |

---

## 2. Monthly Performance Matrix

| Month | 1st Place | 2nd Place | 3rd Place | 4th Place | 5th Place | 6th Place | Realized Range |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2026-05** | `truetether` | `tailwhip` | `regimeecho` | `echophase` | `gatekeeper` | `chamberlain` | $72,436 -$82,792 |
| **2026-06** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | $58,076 -$73,970 |
| **2026-07** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `tailwhip` | `chamberlain` | $57,748 -$66,910 |
| **2026-08** | `gatekeeper` | `regimeecho` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $62,227 -$81,347 |
| **2026-09** | `regimeecho` | `gatekeeper` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $74,945 -$87,364 |
| **2026-10** | `regimeecho` | `gatekeeper` | `echophase` | `truetether` | `chamberlain` | `tailwhip` | $76,190 -$87,146 |

---

## 3. Model Diagnostic Inferences

### `regimeecho` (Cumulative Rank #1)
- **Mean Composite Loss**: 10.9831
- **Continuous Ranked Probability Score (CRPS)**: 6,035.21
- **Scaled Median Absolute Deviation (SMAD)**: 9.34%
- **Total Empirical Coverage Penalty (ECP)**: 150 points
- **Diagnostic Assessment**: Demonstrates market-leading fidelity by maintaining strict stationarity around empirical Era 4 residual increments. Avoided parameter runaway entirely during the summer liquidity slump, producing competitive median error (9.34% SMAD) and minimal tail violations.

### `gatekeeper` (Cumulative Rank #2)
- **Mean Composite Loss**: 11.4607
- **Continuous Ranked Probability Score (CRPS)**: 5,356.81
- **Scaled Median Absolute Deviation (SMAD)**: 9.19%
- **Total Empirical Coverage Penalty (ECP)**: 175 points
- **Diagnostic Assessment**: Achieved top-tier probabilistic calibration (lowest CRPS and 9.19% SMAD) by successfully gating volatility against institutional rebalancing windows, though early boundary penalties during May absorption kept coverage penalties at 175 points.

### `echophase` (Cumulative Rank #3)
- **Mean Composite Loss**: 16.1701
- **Continuous Ranked Probability Score (CRPS)**: 9,264.61
- **Scaled Median Absolute Deviation (SMAD)**: 17.62%
- **Total Empirical Coverage Penalty (ECP)**: 175 points
- **Diagnostic Assessment**: Successfully tracked the 285-day sub-annual rebalancing harmonic. While starting slightly elevated during the May-June drawdown, it converged directly into median actuals by September-October, demonstrating strong mid-cycle dynamic elasticity with a competitive 17.62% SMAD.

### `truetether` (Cumulative Rank #4)
- **Mean Composite Loss**: 29.5407
- **Continuous Ranked Probability Score (CRPS)**: 13,754.78
- **Scaled Median Absolute Deviation (SMAD)**: 26.24%
- **Total Empirical Coverage Penalty (ECP)**: 425 points
- **Diagnostic Assessment**: Continuous Ornstein-Uhlenbeck mean reversion provided structural bounds, but constant secular drift pressure created an upward bias (+$19,709 median offset), triggering recurrent core boundary breaches during prolonged horizontal absorption (Total ECP: 425).

### `tailwhip` (Cumulative Rank #5)
- **Mean Composite Loss**: 30.5058
- **Continuous Ranked Probability Score (CRPS)**: 14,751.92
- **Scaled Median Absolute Deviation (SMAD)**: 27.72%
- **Total Empirical Coverage Penalty (ECP)**: 425 points
- **Diagnostic Assessment**: Discontinuous Poisson jumps injected excessive tail dispersion into quiet summer trading blocks. The model over-estimated downside tail risk while lifting median paths, resulting in elevated CRPS loss and repeated core band penalties (425 ECP).

### `chamberlain` (Cumulative Rank #6)
- **Mean Composite Loss**: 31.0158
- **Continuous Ranked Probability Score (CRPS)**: 14,791.79
- **Scaled Median Absolute Deviation (SMAD)**: 26.74%
- **Total Empirical Coverage Penalty (ECP)**: 450 points
- **Diagnostic Assessment**: Coupled stochastic volatility architecture struggled with the low-volatility summer grind. Negative leverage correlation assumptions produced diffusive spread widening rather than tight compression, accumulating a high composite penalty index (31.02).
