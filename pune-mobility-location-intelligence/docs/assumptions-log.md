# Assumptions Log (Traceability: Assumed | Cited | Derived)

> Purpose: Make all parameters explicit with Status, Rationale, Source/Ref (with URL+date), Range (Min/Default/Max), Sensitivity, and Validation Plan. Every assumption must be traceable.

## 1. Value of Time (VoT) — Commuters/Freight
| Parameter | Value (INR/hr) | Status (A/C/D) | Rationale | Source/Ref | URL | Retrieved | Min | Default | Max | Sensitivity | Validation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VoT_WhiteCollar_Pune | 225 | Assumed | IT corridor (Hinjewadi/Wakad) mid-level; conservative vs metro premium. Range reflects India urban studies context. | Pune market context (directional) | See refs in data-sources.md | 2026-10-04 | 150 | 225 | 300 | High (linear in savings) | Sensitivity table in ROI; cite national studies if refined later |
| VoT_BlueCollar | 150 | Assumed | Conservative | Contextual | See data-sources.md | 2026-10-04 | 120 | 150 | 200 | High | Sensitivity |
| VoT_Commercial_Freight | 250 | Assumed | Logistics/last-mile directional | Contextual | See data-sources.md | 2026-10-04 | 200 | 250 | 350 | High | Sensitivity |

## 2. Fuel Price & Consumption
| Parameter | Value | Status | Rationale | Source/Ref | URL | Retrieved | Min | Default | Max | Sensitivity | Validation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Fuel_Price_INR_per_L (Petrol/Diesel avg) | 105 | Assumed | Approximate Pune retail (directional). Keep configurable. | Directional (market context) | See data-sources.md | 2026-10-04 | 95 | 105 | 115 | Med | Config override; update quarterly |
| Fuel_Saved_Proxy | SUMO-based | Cited/Derived | Use SUMO fuel model if available (HBEFA), else fallback to distance/idle proxy. | SUMO Emissions | https://sumo.dlr.de/docs/Models/Emissions.html | 2026-10-04 | — | model | — | Med | Log which model used per run |

## 3. Emissions & Social Cost
| Parameter | Value (INR/kg or default) | Status | Rationale | Source/Ref | URL | Retrieved | Min | Default | Max | Sensitivity | Validation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CO2e_SocialCost_INR_per_kg | 40 | Assumed | Conservative social cost (directional). Not carbon market price. | Directional | See data-sources.md | 2026-10-04 | 20 | 40 | 80 | Low–Med | Explicitly flag as social cost (avoid overstating) |
| Emissions_Model | HBEFA (SUMO) | Cited | SUMO emissions model | SUMO | https://sumo.dlr.de/docs/Models/Emissions.html | 2026-10-04 | — | — | — | Med | Record per simulation run |

## 4. Economic Scaling
| Parameter | Value | Status | Rationale | Source/Ref | URL | Retrieved | Min | Default | Max | Sensitivity | Validation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Working_Days_per_Year | 250 | Assumed | Indian working days (conservative). Excludes holidays majorly. | Standard business | Contextual | 2026-10-04 | 240 | 250 | 260 | Med | Configurable |
| Peak_Hours_per_Day (Rep) | 2 | Assumed | AM+PM peak representative | Pune traffic context | See data-sources.md | 2026-10-04 | 1 | 2 | 3 | Med | Clearly note representative, not 24x7 |
| Vehicles_Affected_Catchment | Derived (from sim) | Derived | From routes/trips in simulation | Simulation | N/A | 2026-10-04 | — | sim | — | High | Export from sim outputs |

## 5. Location Premium Elasticity (Accessibility → Value)
| Parameter | Value (Range) | Status | Rationale | Source/Ref | URL | Retrieved | Min | Default | Max | Sensitivity | Validation Plan |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Price_Elasticity_Accessibility_ε | 0.05% – 0.40% price lift per 1% avg wait reduction | Assumed | Sparse Pune-specific junction elasticities. Conservative bounded range. Treat as directional hypothesis. | Location economics (directional) | Contextual + data-sources.md | 2026-10-04 | 0.05 | 0.15 | 0.40 | Very High | Sensitivity table (Low/Base/High). Do NOT hard-code point; always show range. Mark as unvalidated empirically. |
| Rental_Elasticity_Accessibility | 0.05% – 0.40% per 1% wait reduction | Assumed | Directional | Contextual | data-sources.md | 2026-10-04 | 0.05 | 0.15 | 0.40 | High | Sensitivity ranges |

## 6. Micro-Market Priority Selection
| Micro-Market | Rationale | Status | Source/Ref | URL | Retrieved | Priority | Notes |
|---|---|---|---|---|---|---|---|
| Wakad–Tathawade–Hinjewadi | IT hub, high migration, congestion, active infra, strong rental demand | Cited | ET, MagicBricks, Namrata, HT | See data-sources.md | 2026-10-04 | P0 | Primary cluster (developer-relevant) |
| Kharadi | IT/commercial, East Pune growth | Cited | ET/MagicBricks | See data-sources.md | 2026-10-04 | P1 | Secondary cluster |

## 7. Simulation Parameters (SUMO)
| Parameter | Value/Config | Status | Rationale | Source/Ref | URL | Retrieved | Notes |
|---|---|---|---|---|---|---|---|
| Network Type | Synthetic (grid+arterials) | Assumed | Full reproducibility (no external GIS dependency). Swappable to OSM later. | SUMO best practice | https://sumo.dlr.de/docs/Networks/Building_Networks.html | 2026-10-04 | Deterministic |
| Demand (Routes) | Generated flows (peak profile) | Assumed | Reproducible; configurable vehicle classes | SUMO Routes | https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html | 2026-10-04 | Peak-hour rep |
| Control Baseline | Fixed-time | Cited | Standard baseline | Traffic control | SUMO TLS | https://sumo.dlr.de/docs/Simulation/Traffic_Lights.html | Compare fairly |
| Control Adaptive | Max-Pressure | Cited | Proven, low compute, interpretable | Max-pressure literature (standard) | SUMO TraCI + standard | 2026-10-04 | Phase selection by pressure |
| Update Cadence | Phase/cycle threshold (configurable) | Assumed | Tune for stability | Design choice | TraCI | https://sumo.dlr.de/docs/TraCI.html | Configurable |
| Random Seed | Fixed (config) | Assumed | Determinism | Reproducibility | SUMO | https://sumo.dlr.de/docs/Basics/Randomness.html | Ensures comparison validity |

**Status Legend:** A=Assumed, C=Cited, D=Derived. All assumptions are bounded by ranges and tested via sensitivity. Results using elasticity (5.1) are explicitly treated as **directional** (hypothesis), not empirical prediction.
