# FX Insights Dashboard

**Real-time analytics for institutional trading desks**

## Problem
Manual, slow analytics prevented traders from acting on short-lived opportunities. Fragmented data sources meant traders missed intraday opportunities.

## Solution
Real-time stream processing with focused dashboards for desks and risk teams.

**Technical Stack:**
- Kafka for event streaming
- Flink/Beam for real-time processing
- TimescaleDB for time-series storage
- React + D3 for visualization

## Impact
- **30% increase** in processing efficiency (10k → 13k events/s)
- **99.95% uptime** SLA maintained
- **Seconds vs minutes** mean time to insight

## Key Learnings
- Start with a single high-value metric to validate early
- Keep dashboards targeted to specific user roles
- Low-latency metrics require careful architecture choices

---

[View case study](case-study.md) | [Back to portfolio](../../README.md)
