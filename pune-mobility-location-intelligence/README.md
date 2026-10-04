# Pune Mobility Location Intelligence
> Strategic Lens: Quantifying how traffic accessibility impacts real estate value to demonstrate developer ROI

## 1. Executive Overview (Level 1 - Highest Level of Understanding)

### 1.1 Problem Statement (1.1)
Pune's peak-hour congestion directly impacts commuter accessibility, creating an unquantified cost for developers, buyers, and businesses. Most real estate feasibility studies focus on location, amenities, and infrastructure announcements, but rarely quantify the economic impact of travel time variability on property value in measurable terms.

### 1.2 Strategic Differentiator (1.2)
This project bridges mobility engineering (traffic simulation) with location economics (real estate value). Instead of measuring civic benefits alone, it translates wait-time reductions into developer ROI metrics (absorption rate lift, rental yield impact, and price premium potential) - a strategic lens rarely applied by Pune real estate stakeholders.

### 1.3 Objectives & Success Criteria (1.3)
- **Primary:** Quantify the link between adaptive traffic control and location accessibility premium for selected Pune micro-markets.
- **Secondary:** Create an investor/developer-facing narrative that connects technical simulation outputs to business value.
- **Success Criteria:** Reproducible, traceable simulation with clearly separated Assumed/Cited/Derived parameters, fully documented data sources, and a pyramid-structured knowledge base.

## 2. Approach & Lens (Level 2 - Mid Granularity)

### 2.1 Core Hypothesis (2.1)
Improving junction-level accessibility (reduced average wait time, queue length, travel time) creates a measurable location premium for residential/commercial properties in the affected catchment area, which can be quantified and translated into developer ROI.

### 2.2 Conceptual Framework (2.2)
This project models a three-layer value chain connecting traffic operations to business outcomes.

#### 2.2.1 Mobility → Accessibility (2.2.1)
Traffic microsimulation (Eclipse SUMO + TraCI) measures operational KPIs under Baseline (Fixed-Time) vs Adaptive (Max-Pressure) control at priority junction clusters. Key outputs: average wait time (s/veh), queue length (veh), travel time (s/trip), stops, throughput.

#### 2.2.2 Accessibility → Location Premium (2.2.2)
Accessibility improvement is mapped to location value through a parameterized elasticity framework. The magnitude is treated as a testable assumption range (documented with citations where available), linking commute reliability to willingness-to-pay/rent.

#### 2.2.3 Location Premium → Developer ROI (2.2.3)
Location premium is translated to developer-relevant metrics: estimated price/rental lift potential, absorption support, and per-junction economic impact. These are framed as directional (not predictive guarantees) with full sensitivity ranges.

### 2.3 Scope & Boundaries (2.3)
- **Geographic Scope (Initial):** Priority Pune micro-markets - Wakad, Tathawade, Hinjewadi (West Pune IT corridor) with Kharadi (East Pune IT) as secondary, tied to specific junction clusters.
- **Time Scope:** Peak-hour representative demand (AM/PM) for reproducible comparison.
- **Approach:** Rule-based adaptive (Max-Pressure) first; RL kept optional/future. Synthetic network first for full reproducibility; OSM slice optional later.
- **Boundary:** Focused on junction-level signal control impact on accessibility. Broader land-use changes are out of scope.

## 3. Execution Blueprint (Level 3 - Granular, Summarized)

### 3.1 Tools, Languages & Environment (3.1)

#### 3.1.1 Core Simulation Stack (3.1.1)
- **Eclipse SUMO** (OSS): Traffic microsimulation engine
- **TraCI (Python)** (ships with SUMO): Real-time signal control & telemetry
- **Gymnasium** (OSS, optional/future): RL environment wrapper

#### 3.1.2 Data, Analysis & Visualization Stack (3.1.2)
- **Python 3.x** (Language): Core logic, control, analysis
- **pandas, numpy** (OSS): Metrics aggregation, calculations
- **matplotlib, plotly** (OSS): Static & interactive visualizations
- **Streamlit** (OSS): Local ROI Dashboard

#### 3.1.3 Infrastructure, Workflow & Documentation (3.1.3)
- **SUMO Tools** (netconvert, sumo, sumo-gui): Network/route generation & validation
- **venv + pip** (Tooling): Isolated local environment
- **Git** (VCS): Version control & traceability
- **Markdown (GFM)**: Documentation (README, Detail, Docs)
- **WebSearch** (session tool): Market/intel validation (documented with retrieval dates)

### 3.2 Data Sources (3.2) - Summarized
Market/infra references (MagicBricks, Square Yards, Economic Times, Hindustan Times, Indian Express, Pune Pulse, PMRDA, NHAI, Namrata Group, FirstPremises, Tracxn) inform Pune assumptions and micro-market selection. Technical references (SUMO Docs, OpenStreetMap). **Full inventory** with URLs, publisher, retrieval date, license, purpose, preprocessing in `docs/data-sources.md`. Classification: Cited/Derived/Assumed.

### 3.3 Methodology Summary (3.3)
- **Baseline:** Fixed-time signal control
- **Adaptive:** Max-Pressure (pressure = inbound halting queues − outbound capacity/queues by phase) with configurable update cadence
- **KPIs:** Avg wait (s/veh), queue length (veh), travel time (s/trip), stops, throughput, fuel/emissions (SUMO models), vehicle trips completed
- **ROI Mapping:** Value-of-Time + fuel + emissions (social cost) → peak-hour & scalable annualized view, with sensitivity ranges
- **Traceability:** All parameters logged in `docs/assumptions-log.md` (Assumed | Cited | Derived)

### 3.4 Outputs, Metrics & ROI Mapping (3.4)
Simulation exports: `data/metrics_baseline.csv`, `data/metrics_adaptive.csv`, `data/roi_summary.csv`. Visuals in `outputs/figures/`, reports in `outputs/reports/`. Dashboard (`scripts/dashboard.py`) surfaces "What's In It For Me" (WIFM) for PMC/Traffic Police, Infrastructure Consultancy, Developers, Commuters/Business, ESG.

### 3.5 How To Reproduce (High-Level) (3.5)
1. Create/activate Python venv & install dependencies (`requirements` flow via pip)
2. Install/configure SUMO; set `SUMO_HOME` (path varies by OS)
3. Generate synthetic Pune-like network/routes (`scripts/generate_synthetic.py`)
4. Run Baseline (`scripts/baseline_fixed.py`) → export metrics
5. Run Adaptive (`scripts/adaptive_pressure.py`) → export metrics
6. Launch ROI Dashboard (`streamlit run scripts/dashboard.py`)
Full, step-by-step commands + environment notes in `README_DETAIL.md` (Chapter 3.5+).

## Appendix: Quick Navigation
- **Full Detail (Chapters 1.1.1 onward):** [`README_DETAIL.md`](./README_DETAIL.md)
- **Data Sources (exhaustive, every 3rd-party):** [`docs/data-sources.md`](./docs/data-sources.md)
- **Methodology, Formulas & Validation:** [`docs/methodology.md`](./docs/methodology.md)
- **Assumptions Log (Assumed | Cited | Derived + rationale):** [`docs/assumptions-log.md`](./docs/assumptions-log.md)
- **Architecture & Design:** [`docs/architecture.md`](./docs/architecture.md)
