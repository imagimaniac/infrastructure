#!/usr/bin/env python3
"""Metrics, logging, and ROI calculations."""
from __future__ import annotations
import csv
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
OUT = BASE / "outputs"


@dataclass
class RunMetrics:
    scenario: str  # baseline|adaptive
    duration_s: float
    vehicles_total: int
    avg_wait_s: float
    max_queue_veh: float
    avg_queue_veh: float
    travel_time_avg_s: float
    stops_avg: float
    throughput_veh_hr: float
    fuel_l: float = 0.0
    co2_kg: float = 0.0
    nox_kg: float = 0.0
    pmx_kg: float = 0.0


def ensure_dirs():
    DATA.mkdir(parents=True, exist_ok=True)
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    (OUT / "reports").mkdir(parents=True, exist_ok=True)


def write_metrics_csv(rows: List[Dict[str, Any]], filename: str):
    ensure_dirs()
    fp = DATA / filename
    if not rows:
        return fp
    with fp.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)
    return fp


def write_roi_summary(roi: Dict[str, Any]):
    ensure_dirs()
    fp = DATA / "roi_summary.csv"
    with fp.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metric", "value", "unit", "notes"])
        for k, v in roi.items():
            unit = v.get("unit", "") if isinstance(v, dict) else ""
            val = v.get("value", v) if isinstance(v, dict) else v
            notes = v.get("notes", "") if isinstance(v, dict) else ""
            w.writerow([k, val, unit, notes])
    return fp


def compute_deltas(baseline: Dict[str, float], adaptive: Dict[str, float]) -> Dict[str, float]:
    out = {}
    for k in set(baseline) | set(adaptive):
        b = baseline.get(k, 0.0) or 0.0
        a = adaptive.get(k, 0.0) or 0.0
        out[f"{k}_delta"] = a - b  # adaptive - baseline
        if b > 0:
            out[f"{k}_pct_red"] = max(-9999.0, (b - a) / b * 100.0)
        else:
            out[f"{k}_pct_red"] = 0.0
    return out
