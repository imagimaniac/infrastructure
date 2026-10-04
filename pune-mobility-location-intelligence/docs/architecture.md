# Architecture & Design

## 1. System Architecture (High-Level)
```text
generate_synthetic.py  ->  config/*.xml (network, routes, tls, sumocfg)
baseline_fixed.py      ->  SUMO + TraCI -> data/metrics_baseline.csv
adaptive_pressure.py   ->  SUMO + TraCI -> data/metrics_adaptive.csv
utils/metrics.py       ->  KPI calc, ROI, CSV I/O, logging
utils/viz.py           ->  Plots (matplotlib/plotly)
dashboard.py (Streamlit) -> Reads CSVs -> ROI tables/charts + WIFM
README*.md + docs/*.md  -> Documentation (traceability)
```

## 2. Data Flow
1. **Input:** Config XMLs (network.net.xml, routes.rou.xml, tls.add.xml, simulation.sumocfg)
2. **Execution:** SUMO runs with TraCI controller (baseline or adaptive)
3. **Telemetry:** Per-step + aggregated metrics via TraCI/tripinfo
4. **Processing:** utils/metrics.py computes deltas, ROI, exports CSVs
5. **Visualization/Reporting:** utils/viz.py + scripts/dashboard.py
6. **Docs:** All parameters traced to assumptions-log.md

## 3. Component Design
- **Separation of Concerns:** Config, logic (scripts), utilities, data, outputs, docs
- **Reproducibility:** Deterministic (seeded), config-driven
- **Extensibility:** Easy to swap network (synthetic→OSM), swap control (max-pressure→RL), add KPIs
- **Traceability:** Run metadata logged; every assumption externalized
- **Local-first:** No external cloud required; runs on macOS/Linux/Win locally

## 4. File Responsibilities
| Path | Responsibility |
|---|---|
| config/ | SUMO XML configs (network/routes/tls/sumocfg). All versioned. |
| data/ | CSV outputs (metrics_baseline.csv, metrics_adaptive.csv, roi_summary.csv). Git-ignored large? but small here. |
| outputs/ | figures/, reports/ (PNG/HTML/CSV exports) |
| scripts/ | Runnable entrypoints (generate, baseline, adaptive, dashboard) |
| utils/ | Reusable (metrics.py, viz.py) |
| docs/ | Traceable documentation (data-sources, methodology, assumptions, architecture) |
| references/ | Research notes/snapshots (to avoid blind reliance) |
| notebooks/ | Exploratory analysis (optional) |

## 5. Design Principles
- **Document-as-you-go** (URLs+dates)
- **Assumptions explicit** (A/C/D)
- **Pyramid documentation** (README summary → DETAIL deep dive)
- **Developer ROI lens** (strategic, not just civic)
- **Conservative by default** (ranges, sensitivity)
