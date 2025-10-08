# Algorithmic Trading Simulator

**Safe sandbox for building and testing trading algorithms**

## Problem
No safe, realistic environment to prototype algorithms with market-like data. High risk and long validation cycles for new strategies.

## Solution
Replay engine with simulated market microstructure and plugin-based strategy runner.

**Technical Stack:**
- Python for strategy engine
- Docker for isolated environments
- PostgreSQL for market data replay
- Web UI for visualization

## Impact
- Faster experiment cycles
- Reduced risk in production rollouts
- Reproducible testing with recorded market sessions

## Key Learnings
- Deterministic replay is critical for debugging
- Market microstructure simulation matters more than just price data
- Plugin architecture enables rapid strategy iteration

---

[View case study](case-study.md) | [Back to portfolio](../../README.md)
