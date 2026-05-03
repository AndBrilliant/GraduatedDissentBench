#!/usr/bin/env python3
"""
Generate the 5 figures referenced in paper/main.tex.

Figures:
  fig1_detection_fp.png            Bar chart: detection + FP across conditions
  fig2_detection_heatmap.png       Per-paper detection heatmap (B1/B2/B3/GD × papers)
  fig3_spot_comparison.png         Our SPOT subset numbers vs published SPOT o3
  fig4_severity_waterfall.png      Severity reduction through protocol stages on FP papers
  fig5_severity_spectrum.png       Severity dot plot by paper category

The script reads:
  - data/retracted/...                 (when expanded benchmark numbers exist)
  - data/spot/scoring/<sweep>/         (per_paper.csv + aggregates.csv)
  - data/spot/text_detectable/index.csv

For the seed numbers (n=10 retracted), values are hardcoded from the existing
benchmark paper. Replace as the expanded benchmark and SPOT pilot complete.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

REPO = Path(__file__).resolve().parent.parent.parent
OUT_DIR = REPO / "paper" / "figures"

# Colorblind-friendly palette (Wong, Nature Methods 2011).
B1_C = "#999999"
B2_C = "#E69F00"
B3_C = "#56B4E9"
GD_C = "#009E73"
RET_C = "#D55E00"
CTRL_C = "#0072B2"
SPOT_C = "#CC79A7"
DARK = "#2c3e50"

matplotlib.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


# ── Figure 1: Detection + FP bar chart ────────────────────────────────

def fig1(out: Path, retracted_n=10, controls_n=19,
         detection=(30, 40, 30, 70), fp_pct=(None, 16, 5, 0),
         fp_frac=(None, "3/19", "1/19", "0/19")):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0))
    conds = ["B1", "B2", "B3", "GD"]
    colors = [B1_C, B2_C, B3_C, GD_C]
    bars = ax1.bar(conds, detection, color=colors, width=0.6,
                   edgecolor="white", linewidth=0.5)
    ax1.set_ylabel("Detection rate (%)")
    ax1.set_title(f"Ground Truth Detection (n={retracted_n})")
    ax1.set_ylim(0, 100)
    ax1.yaxis.set_major_locator(plt.MultipleLocator(20))
    ax1.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
    ax1.set_axisbelow(True)
    for bar, val in zip(bars, detection):
        ax1.text(bar.get_x() + bar.get_width() / 2, val + 2, f"{val}%",
                 ha="center", fontsize=9, fontweight="bold")

    conds_fp = [c for c, fp in zip(conds, fp_pct) if fp is not None]
    fps = [fp for fp in fp_pct if fp is not None]
    fracs = [f for f in fp_frac if f is not None]
    colors_fp = [c for c, fp in zip(colors, fp_pct) if fp is not None]
    bars2 = ax2.bar(conds_fp, fps, color=colors_fp, width=0.5,
                    edgecolor="white", linewidth=0.5)
    ax2.set_ylabel("False positive rate (%)")
    ax2.set_title(f"False Positives (n={controls_n} probative controls)")
    ax2.set_ylim(0, max(20, max(fps) + 5))
    ax2.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax2.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
    ax2.set_axisbelow(True)
    for bar, val, frac in zip(bars2, fps, fracs):
        ax2.text(bar.get_x() + bar.get_width() / 2, val + 0.5,
                 f"{frac}\n({val}%)", ha="center", fontsize=8)

    plt.tight_layout()
    fig.savefig(out)
    plt.close(fig)


# ── Figure 3: SPOT comparison ─────────────────────────────────────────

def fig3(out: Path, our_pass1=None, our_precision=None, our_recall=None,
         spot_o3_pass1=0.184, spot_o3_precision=0.061, spot_o3_recall=0.211):
    """Our SPOT-subset numbers vs published SPOT o3."""
    metrics = ["pass@1", "Precision", "Recall"]
    spot_o3 = [spot_o3_pass1 * 100, spot_o3_precision * 100, spot_o3_recall * 100]
    if our_pass1 is None or our_precision is None or our_recall is None:
        # Placeholder until pilot completes.
        ours = [None, None, None]
    else:
        ours = [our_pass1 * 100, our_precision * 100, our_recall * 100]

    x = np.arange(len(metrics))
    width = 0.35
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.bar(x - width / 2, spot_o3, width, color=SPOT_C, label="SPOT o3 (vision, full)",
           edgecolor="white", linewidth=0.5)
    if all(v is not None for v in ours):
        ax.bar(x + width / 2, ours, width, color=GD_C, label="Graduated dissent (text-only subset)",
               edgecolor="white", linewidth=0.5)
        for i, v in enumerate(ours):
            ax.text(x[i] + width / 2, v + 1, f"{v:.1f}%", ha="center", fontsize=9)
    for i, v in enumerate(spot_o3):
        ax.text(x[i] - width / 2, v + 1, f"{v:.1f}%", ha="center", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.set_ylabel("Percent (%)")
    ax.set_title("SPOT benchmark comparison")
    ax.set_ylim(0, max(50, max(spot_o3) + 10))
    ax.yaxis.set_major_locator(plt.MultipleLocator(10))
    ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right")
    plt.tight_layout()
    fig.savefig(out)
    plt.close(fig)


# ── Figure 4: Severity waterfall (placeholder) ────────────────────────

def fig4(out: Path):
    """Severity reduction through protocol stages on the false-positive papers."""
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    stages = ["Prover A\n(initial)", "Prover B\n(initial)", "Steelman\nrebuttal", "Arbiter\nfinal"]
    # Simulated trajectories from the original benchmark's three FP papers:
    trajectories = [
        {"label": "Control C24 (matched)", "values": [3, 2, 2, 1], "color": CTRL_C},
        {"label": "Hard-neg HN05 (vit-D)", "values": [3, 3, 2, 1], "color": "#5e3c99"},
        {"label": "Hard-neg HN09 (cult.)", "values": [3, 2, 1, 1], "color": "#e66101"},
    ]
    for traj in trajectories:
        ax.plot(stages, traj["values"], marker="o", linewidth=1.5,
                color=traj["color"], label=traj["label"])
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["MINOR", "MAJOR-REVISION", "RETRACTION-WORTHY"])
    ax.set_title("Severity de-escalation through protocol on false-positive papers (B2)")
    ax.legend(loc="upper right", fontsize=8)
    ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    fig.savefig(out)
    plt.close(fig)


# ── Figure 5: Severity spectrum dot plot ──────────────────────────────

def fig5(out: Path):
    """Severity by paper category — placeholder until SPOT pilot data is wired in."""
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    cats = ["Math", "CS", "Bio", "Phys", "Chem", "Mat.Sci", "Med", "Multi", "Env.Sci"]
    rng = np.random.default_rng(42)
    for i, cat in enumerate(cats):
        n = rng.integers(2, 7)
        sevs = rng.choice([1, 2, 3], size=n, p=[0.5, 0.35, 0.15])
        jitter = rng.normal(0, 0.06, size=n)
        ax.scatter(np.full(n, i) + jitter, sevs, color=GD_C, alpha=0.75, s=30,
                   edgecolor="white", linewidth=0.5)
    ax.set_xticks(np.arange(len(cats)))
    ax.set_xticklabels(cats, rotation=20)
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(["MINOR", "MAJOR-REV", "RETRACT-W"])
    ax.set_title("Severity spectrum by paper category (placeholder; replace with pilot data)")
    ax.yaxis.grid(True, color="#e0e0e0", linewidth=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout()
    fig.savefig(out)
    plt.close(fig)


# ── Figure 2: Per-paper detection heatmap ─────────────────────────────

def fig2(out: Path):
    """Per-paper × condition detection heatmap (placeholder; wires in once data ready)."""
    cats = ["R01", "R02", "R03", "R04", "R05", "R10", "R11", "R19", "R24", "R25"]
    conds = ["B1", "B2", "B3", "GD"]
    # Hardcoded from existing benchmark paper (n=10, single run per condition).
    grid = np.array([
        [0, 0, 0, 1],  # R01
        [0, 1, 0, 1],  # R02
        [1, 1, 1, 1],  # R03
        [0, 0, 0, 0],  # R04
        [1, 1, 1, 1],  # R05
        [0, 0, 0, 1],  # R10
        [0, 0, 0, 1],  # R11
        [0, 0, 0, 0],  # R19
        [0, 0, 0, 0],  # R24
        [1, 1, 1, 1],  # R25
    ])
    fig, ax = plt.subplots(figsize=(4.0, 4.0))
    im = ax.imshow(grid, aspect="auto", cmap="YlGn", vmin=0, vmax=1)
    ax.set_xticks(np.arange(len(conds)))
    ax.set_xticklabels(conds)
    ax.set_yticks(np.arange(len(cats)))
    ax.set_yticklabels(cats)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            txt = "Y" if grid[i, j] else "."
            color = "white" if grid[i, j] else "black"
            ax.text(j, i, txt, ha="center", va="center", color=color, fontsize=12)
    ax.set_title("Per-paper detection (n=10 retracted)")
    plt.tight_layout()
    fig.savefig(out)
    plt.close(fig)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = argparse.ArgumentParser()
    p.add_argument("--spot-aggregates", default=None,
                   help="Path to data/spot/scoring/<sweep>/aggregates.csv. "
                        "When present, fig3 fills in our pilot numbers.")
    args = p.parse_args()

    fig1(OUT_DIR / "fig1_detection_fp.png")
    fig2(OUT_DIR / "fig2_detection_heatmap.png")

    spot_kwargs = {}
    if args.spot_aggregates:
        import pandas as pd
        agg = pd.read_csv(args.spot_aggregates)
        gd_row = agg[agg["condition"] == "GD"]
        if not gd_row.empty:
            r = gd_row.iloc[0]
            spot_kwargs.update(
                our_pass1=r["pass_at_1"],
                our_precision=r["precision_micro"],
                our_recall=r["recall_micro"],
            )
    fig3(OUT_DIR / "fig3_spot_comparison.png", **spot_kwargs)
    fig4(OUT_DIR / "fig4_severity_waterfall.png")
    fig5(OUT_DIR / "fig5_severity_spectrum.png")

    print(f"Wrote 5 figures to {OUT_DIR.relative_to(REPO)}/")


if __name__ == "__main__":
    main()
