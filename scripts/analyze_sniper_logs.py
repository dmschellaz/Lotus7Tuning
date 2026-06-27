#!/usr/bin/env python3
"""Generate basic summaries for Holley Sniper CSV datalogs.

Run from the repository root:
    python scripts/analyze_sniper_logs.py
"""
from pathlib import Path
import pandas as pd

RAW_DIR = Path("logs/raw")
OUT_DIR = Path("logs/summaries")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def read_sniper_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, encoding="latin1", low_memory=False)
    df.columns = [str(c).replace("\x00", "").strip() for c in df.columns]
    for c in ["RTC","RPM","IAC Position","TPS","AFR","Target AFR","CL Comp","CL Status","Fuel Flow","MAP","CTS","MAT","Battery","Afterstart Enr","Coolant Enr","Base Fuel VE"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df.dropna(subset=["RTC"]).reset_index(drop=True)

def run_segments(df: pd.DataFrame, threshold=400):
    running = df["RPM"] > threshold
    segments = []
    in_seg = False
    start = None
    for i, val in enumerate(running):
        if val and not in_seg:
            in_seg = True
            start = i
        elif not val and in_seg:
            segments.append((start, i - 1))
            in_seg = False
    if in_seg:
        segments.append((start, len(df) - 1))
    return segments

def summarize_file(path: Path, log_id: int):
    df = read_sniper_csv(path)
    run = df[df["RPM"] > 400]
    segs = run_segments(df)
    end = run[run["RTC"] >= run["RTC"].max() - 20] if len(run) else pd.DataFrame()
    valid_afr = run[run["AFR"].between(5, 30)] if len(run) else pd.DataFrame()
    return {
        "log_id": log_id,
        "file": path.name,
        "duration_sec": round(float(df["RTC"].max()), 3),
        "run_segments": len(segs),
        "cts_min_run_f": round(float(run["CTS"].min()), 1) if len(run) else None,
        "cts_max_run_f": round(float(run["CTS"].max()), 1) if len(run) else None,
        "rpm_peak_running": round(float(run["RPM"].max()), 0) if len(run) else None,
        "iac_end20_avg_pct": round(float(end["IAC Position"].mean()), 1) if len(end) else None,
        "rpm_end20_avg": round(float(end["RPM"].mean()), 0) if len(end) else None,
        "afr_valid_avg": round(float(valid_afr["AFR"].mean()), 2) if len(valid_afr) else None,
        "target_afr_valid_avg": round(float(valid_afr["Target AFR"].mean()), 2) if len(valid_afr) else None,
        "cl_comp_max_pct": round(float(run["CL Comp"].max()), 1) if len(run) else None,
        "battery_min_v": round(float(df["Battery"].min()), 2) if "Battery" in df else None,
    }

if __name__ == "__main__":
    rows = [summarize_file(p, i) for i, p in enumerate(sorted(RAW_DIR.glob("*.csv")), start=1)]
    pd.DataFrame(rows).to_csv(OUT_DIR / "log_summary.csv", index=False)
    print(f"Wrote {OUT_DIR / 'log_summary.csv'}")
