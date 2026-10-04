#!/usr/bin/env python3
"""Plotting helpers (matplotlib/plotly)."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
FIGS = BASE / "outputs" / "figures"


def ensure_dirs():
    FIGS.mkdir(parents=True, exist_ok=True)


def bar_comparison(df: pd.DataFrame, x: str, y: str, title: str, outfile: str):
    try:
        import matplotlib.pyplot as plt
        ensure_dirs()
        ax = df.plot.bar(x=x, y=y, title=title)
        plt.tight_layout()
        plt.savefig(FIGS / outfile, dpi=150)
        plt.close()
    except Exception as e:
        print("viz.bar_comparison skipped:", e)


def line_timeseries(df: pd.DataFrame, x: str, y: str, title: str, outfile: str):
    try:
        import matplotlib.pyplot as plt
        ensure_dirs()
        ax = df.plot.line(x=x, y=y, title=title)
        plt.tight_layout()
        plt.savefig(FIGS / outfile, dpi=150)
        plt.close()
    except Exception as e:
        print("viz.line_timeseries skipped:", e)
