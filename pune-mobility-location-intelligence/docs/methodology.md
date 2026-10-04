# Methodology, Formulas & Validation

## 1. Overview
Quantitative comparison: Baseline (Fixed-Time) vs Adaptive (Max-Pressure) using identical demand/network. All KPIs computed from TraCI/SUMO outputs, logged per run.

## 2. Traffic Simulation Methodology
- **Microsimulation:** SUMO (time-discrete, car-following, lane-changing)
- **Control Interface:** TraCI (Python) for signal state queries/decisions
- **Baseline:** Fixed-time timings (defined in config/tls.add.xml or defaults)
- **Adaptive (Max-Pressure):** At controlled intersection, pressure for phase p: P_p = ∑ q_in,phase - ∑ q_out,phase (queues on inbound approaches of phase minus outbound). Select phase with max P_p subject to safety/min green/max green constraints.

## 3. KPI Definitions (from SUMO/TraCI)
| KPI | Definition | TraCI Reference (typical) | Notes |
|---|---|---|---|
| Avg Wait Time (s/veh) | Average time vehicle is stopped (waiting) over trip/interval | vehicle.getWaitingTime, edge/trip aggregates | Core accessibility proxy |
| Queue Length (veh) | Halting vehicles on lanes/edges (last step) | edge.getLastStepHaltingNumber, lane.getLastStepHaltingNumber | Pressure inputs |
| Travel Time (s/trip) | Trip duration from departure to arrival | tripinfo (XML) / aggregated | Network performance |
| Stops (count/veh) | Number of stops | vehicle.getStopState / aggregated | Reliability proxy |
| Throughput (veh/hr) | Completed trips per hour | tripinfo counts | Capacity/utilization |
| Fuel Consumption (L) | Total fuel consumed (if model enabled) | vehicle.getFuelConsumption / emissions sum | Monetized |
| CO2/NOx/PMx (kg) | Emissions totals | vehicle.getCO2Emission etc | Monetized (social cost) |

## 4. Formulas for Reduction & Savings

### 4.1 Percentage Reduction
$$
\%\ reduction = \frac{W_{fixed} - W_{adapt}}{W_{fixed}} \times 100,\quad (W_{fixed}>0)
$$
Applied to: avg wait, queue length, travel time.

### 4.2 Value of Time Saved (INR/peak hour)
$$
VoT_{saved} = \Delta t_{wait,hr} \times V_{affected} \times VoT_{avg,INR/hr}
$$
Where $\Delta t_{wait,hr}$ = average wait reduction per vehicle in hours (weighted). $V_{affected}$ = vehicles in catchment/trips affected (from sim).

### 4.3 Fuel Savings (INR/peak hour)
$$
Fuel_{saved,INR} = \Delta Fuel_L \times FuelPrice_{INR/L}
$$
$\Delta Fuel_L = Fuel_{fixed}(L) - Fuel_{adapt}(L)$ from SUMO (or proxy if unavailable).

### 4.4 Emissions Savings (INR/peak hour, social cost)
$$
Emis_{saved,INR} = \Delta CO2e_{kg} \times CO2eCost_{INR/kg}
$$
Flagged as social cost (separately from cash savings).

### 4.5 Total Economic Savings (Representative)
$$
Total_{peak,INR} = VoT_{saved} + Fuel_{saved,INR} + Emis_{saved,INR}
$$
Scaled: $Total_{annualized} \approx Total_{peak,INR} \times PeakHoursPerDay \times WorkingDaysPerYear \times ScopeFactor$ (explicit scope factor).

### 4.6 Accessibility → Location Premium (Directional)
$$
\Delta Price\%_{potential} \in [\epsilon_{low}, \epsilon_{high}] \times (\%\ reduction\ in\ avg\ wait)
$$
With $\epsilon \in [0.05, 0.40]$ per 1% wait reduction (default 0.15) — see assumptions-log.md. Results always shown as range + sensitivity.

## 5. Validation Approach
- **Determinism:** Fixed random seed; same demand/network.
- **Sanity Checks:** KPIs non-negative, throughput reasonable, no crashes.
- **Baseline Reasonableness:** Wait times in plausible Pune peak range (contextual).
- **A/A Consistency:** Re-run same config; metrics stable.
- **Traceability:** Log run metadata (SUMO version, git commit, config hash, timestamp).
- **Sensitivity:** Vary VoT, elasticity, fuel price, peak hours.

## 6. Limitations (Explicit)
- Synthetic network (first version) — not full Pune GIS. Good for method proof; swap OSM later.
- Elasticity is directional (literature gap). Never presented as point estimate.
- Emissions/fuel depend on SUMO model availability.
- Scaling to annual assumes representative peak (documented).
- Junction-level control only; broader network effects not modeled.

## 7. Implementation Notes
- Use TraCI subscription/selective queries to avoid overhead.
- Log stepwise + aggregated; export CSVs.
- Separate "cash" (VoT+Fuel) vs "social" (emissions) in dashboard.
- All configs in `config/`; no hard-coded magic numbers (read from params).
