#!/usr/bin/env python3
"""Adaptive control: Max-Pressure (improved skeleton with basic metrics)."""
from __future__ import annotations
import sys
import os
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CFG = BASE / "config"
UTILS = BASE / "utils"

if str(UTILS) not in sys.path:
    sys.path.insert(0, str(UTILS))

from metrics import ensure_dirs, write_metrics_csv  # type: ignore


def detect_sumo_home():
    if os.environ.get("SUMO_HOME"):
        return
    for c in ["/opt/homebrew/opt/sumo/share/sumo", "/usr/local/opt/sumo/share/sumo", "/usr/share/sumo"]:
        if Path(c).exists():
            os.environ["SUMO_HOME"] = c
            return


def run_adaptive():
    ensure_dirs()
    try:
        import traci
    except Exception as e:
        print("TraCI import failed:", e)
        print("Skipping run (SUMO/TraCI not installed).")
        return

    sumocfg = CFG / "simulation.sumocfg"
    if not sumocfg.exists():
        print("Missing sumocfg. Run generate_synthetic.py first.")
        return

    detect_sumo_home()
    traci.start(["sumo", "-c", str(sumocfg), "--no-step-log", "--random"])
    step = 0
    max_queue = 0.0
    queue_sum = 0.0
    wait_sum = 0.0
    wait_count = 0
    steps = 0
    end = 3600

    edges = []
    try:
        for e in traci.edge.getIDList():
            if not e.startswith(":"):
                edges.append(e)
    except Exception:
        edges = []

    controlled_tls = []
    try:
        controlled_tls = traci.trafficlight.getIDList()
    except Exception:
        controlled_tls = []

    while step < end:
        traci.simulationStep()
        step += 1
        steps += 1
        q = 0.0
        for e in edges:
            try:
                q += traci.edge.getLastStepHaltingNumber(e)
            except Exception:
                pass
        if q > max_queue:
            max_queue = q
        queue_sum += q
        try:
            for v in traci.vehicle.getIDList():
                try:
                    w = traci.vehicle.getWaitingTime(v)
                    if w > 0:
                        wait_sum += w
                        wait_count += 1
                except Exception:
                    pass
        except Exception:
            pass

    try:
        vehicles = traci.simulation.getDepartedNumber()
    except Exception:
        vehicles = 0
    traci.close(False)

    avg_queue = queue_sum / steps if steps > 0 else 0.0
    avg_wait = wait_sum / wait_count if wait_count > 0 else 0.0
    rows = [{
        "scenario": "adaptive",
        "duration_s": float(end),
        "vehicles_total": vehicles,
        "avg_wait_s": round(avg_wait, 3),
        "max_queue_veh": round(max_queue, 3),
        "avg_queue_veh": round(avg_queue, 3),
        "travel_time_avg_s": 0.0,
        "stops_avg": 0.0,
        "throughput_veh_hr": round(vehicles, 3) if vehicles else 0.0,
        "fuel_l": 0.0,
        "co2_kg": 0.0,
        "nox_kg": 0.0,
        "pmx_kg": 0.0,
    }]
    fp = write_metrics_csv(rows, "metrics_adaptive.csv")
    print(f"Wrote {fp}")


if __name__ == "__main__":
    run_adaptive()
