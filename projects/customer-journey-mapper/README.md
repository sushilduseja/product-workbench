# Customer Journey Mapper

## Project Overview

The Customer Journey Mapper is a tool designed to provide clear visibility into user journeys, identify friction points, and enable rapid A/B testing for optimization. It was developed to address a critical challenge faced by a fintech startup: a 47% user drop-off rate during KYC verification.

By implementing this solution, the startup achieved a **53% reduction in drop-off**, recovered **$1.2M in annual revenue**, and accelerated problem identification by **8x**.

## Problem Statement

A rapidly growing Series A fintech startup with over 50,000 users was experiencing a significant bottleneck in its KYC verification flow, leading to a $2.3M annual revenue loss. The core issues were:

- **Fragmented Insights:** Data was scattered across 8+ tools, leading to misaligned priorities and delayed decisions among Product, Engineering, Compliance, and Design teams.
- **High Drop-off:** A staggering 47% of users abandoned the process at the KYC step.
- **Slow Problem Identification:** It took an average of 2.3 weeks to identify and diagnose issues.
- **Low Confidence:** Team confidence in data-driven decisions was as low as 45%.

The following diagram illustrates the communication and interpretation breakdown:

```mermaid
graph LR
    A[Data Sources] --&gt; B[Analytics Team]
    A --&gt; C[Support Team]
    A --&gt; D[Engineering Team]
    A --&gt; E[Design Team]
    
    B --&gt; F[Different Interpretations]
    C --&gt; F
    D --&gt; F
    E --&gt; F
    
    F --&gt; G[Delayed Decisions]
    F --&gt; H[Misaligned Priorities]
    F --&gt; I[Failed Experiments]
    
    style A fill:#e9ecef,stroke:#868e96
    style F fill:#ff6b6b,stroke:#c92a2a
    style G fill:#ff6b6b,stroke:#c92a2a
    style H fill:#ff6b6b,stroke:#c92a2a
    style I fill:#ff6b6b,stroke:#c92a2a
```

## How It Works

The approach is to **map the complete journey visually, surface friction automatically, and test solutions rapidly.**

The implementation process follows these steps:

```mermaid
sequenceDiagram
    participant PM as Product Manager
    participant CJM as Journey Mapper
    participant Data as Analytics Data
    participant Team as Cross-functional Team
    
    PM-&gt;&gt;CJM: Map KYC flow
    CJM-&gt;&gt;Data: Import analytics
    Data-&gt;&gt;CJM: Return drop-off data
    CJM-&gt;&gt;PM: Highlight 47% drop at verification
    PM-&gt;&gt;CJM: Pull user feedback
    CJM-&gt;&gt;PM: Show "unclear requirements" theme
    PM-&gt;&gt;Team: Share visual journey map
    Team-&gt;&gt;PM: Align on solution
    PM-&gt;&gt;CJM: Create test variants
    CJM-&gt;&gt;Data: Run A/B test
    Data-&gt;&gt;CJM: Variant B wins (22% drop-off)
    CJM-&gt;&gt;PM: Export results
    PM-&gt;&gt;Team: Deploy winning variant
```

## Real Impact Metrics

The solution delivered significant, measurable improvements across key business metrics.

| Metric | Baseline | Result | Improvement |
|--------|----------|--------|-------------|
| KYC Drop-off Rate | 47% | 22% | 53% reduction |
| Problem ID Time | 2.3 weeks | 5 days | 8x faster |
| Stakeholder Alignment | 45% | 89% | 98% improvement |
| Revenue Recovery | $0 | $1.2M | Annual gain |
| User Satisfaction | 6.2/10 | 8.7/10 | 40% improvement |

## Getting Started

### For Product Managers
1.  **Identify a Journey:** Start with a critical user flow (e.g., onboarding, checkout, feature adoption).
2.  **Connect Data Sources:** Integrate your analytics and user feedback tools (e.g., Mixpanel, Hotjar, Zendesk).
3.  **Analyze Friction:** Use the visual map to identify steps with high drop-off rates or negative feedback.
4.  **Formulate Hypotheses:** Develop data-backed hypotheses for improvement and design A/B tests.

### For Developers
1.  **Integrate Analytics:** Add the necessary tracking events to your application to feed data into the journey mapper.
2.  **Configure the Pipeline:** Set up the data pipeline to ensure real-time data flow from your sources.
3.  **Implement Variants:** Code the different variants for the A/B tests defined by the product team.
4.  **Monitor Performance:** Track the performance of the variants and the overall system health.

### For Executives
1.  **View the Dashboard:** Access the high-level dashboard for a quick overview of key journey performance.
2.  **Track ROI:** Monitor the revenue impact and ROI of the optimizations being implemented.
3.  **Strategic Planning:** Use the insights to inform strategic decisions and identify new areas for growth.

## Technical Stack and Architecture

### Stack
-   **Frontend:** TypeScript + Vite for a high-performance, interactive UI.
-   **Rendering:** A custom canvas engine for fluid visual interactions and journey mapping.
-   **Backend:** A real-time data processing pipeline to ingest and analyze event streams.
-   **Exports:** A presentation-ready export system to share insights easily.

### Data Sources
The tool integrates with a variety of data sources to provide a holistic view:
-   **Analytics:** Mixpanel, Google Analytics
-   **User Feedback:** Hotjar, Zendesk, Intercom
-   **Experimentation:** Custom A/B testing framework
-   **Monitoring:** Real-time monitoring and alerting systems

## Links

-   **Portfolio Site:** [https://customer-journey-mapper.netlify.app/](https://customer-journey-mapper.netlify.app/)
-   **Source Code:** [https://github.com/sushilduseja/customer-journey-mapper](https://github.com/sushilduseja/customer-journey-mapper)
-   **Detailed Case Study:** [case-study.md](case-study.md)
