#!/usr/bin/env python3
"""Streamlit ROI Dashboard."""
from __future__ import annotations
import sys
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
UTILS = BASE / "utils"

if str(UTILS) not in sys.path:
    sys.path.insert(0, str(UTILS))

try:
    import streamlit as st
except Exception as e:
    print("Streamlit not installed. pip install streamlit")
    sys.exit(1)


def load_csv(p: Path) -> pd.DataFrame:
    if p.exists():
        return pd.read_csv(p)
    return pd.DataFrame()


def main():
    st.set_page_config(page_title="Pune Mobility Location Intelligence - ROI", layout="wide")
    st.title("Pune Mobility Location Intelligence")
    st.caption("Mobility → Accessibility → Location Premium → Developer ROI")

    df_b = load_csv(DATA / "metrics_baseline.csv")
    df_a = load_csv(DATA / "metrics_adaptive.csv")
    df_r = load_csv(DATA / "roi_summary.csv")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Baseline Metrics")
        st.dataframe(df_b)
    with col2:
        st.subheader("Adaptive Metrics")
        st.dataframe(df_a)

    if not df_r.empty:
        st.subheader("ROI Summary")
        st.dataframe(df_r)
    else:
        st.info("No roi_summary.csv yet. Run baseline + adaptive first.")

    st.subheader("What's In It For Me (WIFM)")
    wifm = pd.DataFrame([
        {"Stakeholder": "PMC / Traffic Police", "Value": "Measurable KPIs, improved mobility"},
        {"Stakeholder": "Infrastructure Consultancy", "Value": "Defensible numbers for DPRs, client-ready dashboard"},
        {"Stakeholder": "Real Estate Developers", "Value": "Location intelligence, absorption/support, quantified premium ranges"},
        {"Stakeholder": "Commuters/Businesses", "Value": "Time/fuel savings, reliability"},
        {"Stakeholder": "ESG/Policy", "Value": "Quantified emissions avoided (social cost)"},
    ])
    st.table(wifm)

    st.markdown("---")
    st.markdown("**Note:** Elasticity-based premium is directional (assumption ranges). See `docs/assumptions-log.md` (Assumed|Cited|Derived).")


if __name__ == "__main__":
    main()
