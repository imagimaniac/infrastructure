#!/usr/bin/env python3
"""Offline demo (no SUMO binary required) to generate CSVs for dashboard."""
from __future__ import annotations
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
UTILS = BASE / "utils"
if str(UTILS) not in sys.path:
    sys.path.insert(0, str(UTILS))

from metrics import write_metrics_csv, write_roi_summary, compute_deltas


def main():
    baseline = {
        "avg_wait_s": 42.5,
        "max_queue_veh": 28.0,
        "avg_queue_veh": 12.3,
        "travel_time_avg_s": 185.0,
        "stops_avg": 6.8,
        "throughput_veh_hr": 2400,
        "fuel_l": 125.4,
        "co2_kg": 328.0,
        "vehicles_total": 2400,
    }
    adaptive = {
        "avg_wait_s": 28.9,
        "max_queue_veh": 18.5,
        "avg_queue_veh": 7.9,
        "travel_time_avg_s": 152.0,
        "stops_avg": 4.2,
        "throughput_veh_hr": 2480,
        "fuel_l": 98.7,
        "co2_kg": 258.5,
        "vehicles_total": 2480,
    }
    write_metrics_csv([dict(scenario="baseline", duration_s=3600, **baseline)], "metrics_baseline.csv")
    write_metrics_csv([dict(scenario="adaptive", duration_s=3600, **adaptive)], "metrics_adaptive.csv")
    d = compute_deltas({k: baseline[k] for k in baseline}, {k: adaptive[k] for k in adaptive})
    roi = {
        "avg_wait_pct_red": {"value": round(d.get("avg_wait_s_pct_red", 0), 2), "unit": "%", "notes": "vs baseline"},
        "queue_avg_pct_red": {"value": round(d.get("avg_queue_veh_pct_red", 0), 2), "unit": "%", "notes": "vs baseline"},
        "fuel_saved_l_per_peak_hr": {"value": round(baseline["fuel_l"] - adaptive["fuel_l"], 2), "unit": "L", "notes": "directional demo"},
        "co2e_avoided_kg_per_peak_hr": {"value": round(baseline["co2_kg"] - adaptive["co2_kg"], 2), "unit": "kg", "notes": "directional demo"},
        "note": {"value": "offline_demo", "unit": "", "notes": "Generated without SUMO binary (TraCI-only env); replace with real sim"},
    }
    write_roi_summary(roi)
    print("Offline demo CSVs written to data/")


if __name__ == "__main__":
    main()
