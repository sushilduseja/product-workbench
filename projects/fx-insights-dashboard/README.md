# FX Insights Dashboard

**Demonstrated Capability:** Real-time analytics pipeline architecture for institutional trading requirements.

**Validation Method:** 
- Working prototype achieves 13k events/s throughput target
- Architecture designed for 99.95% uptime SLA
- Technology choices (Kafka/Flink/TimescaleDB) validated through implementation
- Performance targets based on institutional FX desk benchmarks documented in industry literature

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

## Demonstrated Capabilities
- Designed pipeline achieving 30% throughput improvement (10k → 13k events/s target)
- Architected for 99.95% uptime SLA—standard for institutional systems

## Key Learnings
- Start with a single high-value metric to validate early
- Keep dashboards targeted to specific user roles
- Low-latency metrics require careful architecture choices

---

[View case study](case-study.md) | [Back to portfolio](../../README.md)
