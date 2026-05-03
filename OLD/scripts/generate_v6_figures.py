#!/usr/bin/env python3
"""Generate publication figures for v6 benchmark results."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

RET = '#c0392b'
CTRL = '#2980b9'
GREEN = '#27ae60'
WARN = '#e67e22'
DARK = '#2c3e50'
LIGHT = '#ecf0f1'
PURPLE = '#8e44ad'

import os
outdir = os.path.expanduser('~/Desktop/Academic/graduated_dissent_bench_v6/manuscripts/figures')
os.makedirs(outdir, exist_ok=True)


def fig1_ground_truth_and_fp():
    """THE money figure: ground truth detection + false positive rates."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Ground truth detection
    conditions = ['B1\nSingle model\nno rubric', 'B2\nSingle model\n+ rubric', 'B3\nMulti-model\nno steelman', 'Graduated\nDissent']
    detection = [30, 40, 30, 70]
    colors = [WARN, WARN, PURPLE, GREEN]

    bars = ax1.bar(conditions, detection, color=colors, alpha=0.85, edgecolor='white', linewidth=2)
    ax1.set_ylabel('Ground truth detection (%)', fontweight='bold')
    ax1.set_title('Detection of Documented\nRetraction-Causing Errors', fontweight='bold')
    ax1.set_ylim(0, 100)
    for bar, val in zip(bars, detection):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 2,
                f'{val}%', ha='center', fontweight='bold', fontsize=13)
    ax1.axhline(y=50, color='gray', linewidth=0.5, linestyle='--', alpha=0.3)

    # Right: False positive rate
    conditions_fp = ['B1\nSingle model\nno rubric', 'B2\nSingle model\n+ rubric', 'B3\nMulti-model\nno steelman', 'Graduated\nDissent']
    fp_rate = [0, 12.5, 4.2, 0]  # B1 has no severity so N/A; B3 = 1/24 ≈ 4.2%
    fp_colors = ['gray', RET, PURPLE, GREEN]

    bars2 = ax2.bar(conditions_fp, fp_rate, color=fp_colors, alpha=0.85, edgecolor='white', linewidth=2)
    ax2.set_ylabel('False positive rate (%)', fontweight='bold')
    ax2.set_title('False Retraction-Worthy\nClassifications on Controls', fontweight='bold')
    ax2.set_ylim(0, 25)
    for bar, val in zip(bars2, fp_rate):
        label = 'N/A' if val == 0 and bar.get_facecolor()[:3] == matplotlib.colors.to_rgb('gray') else f'{val:.0f}%'
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.5,
                label, ha='center', fontweight='bold', fontsize=13)

    # Add annotations
    ax2.annotate('3 of 24 controls\nfalsely flagged', xy=(1, 12.5), xytext=(1.8, 20),
                fontsize=9, color=RET, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=RET, lw=1.5))
    ax2.annotate('1 of 24', xy=(2, 4.2), xytext=(2, 8),
                fontsize=9, color=PURPLE, fontweight='bold',
                ha='center',
                arrowprops=dict(arrowstyle='->', color=PURPLE, lw=1.5))
    ax2.annotate('0 of 24', xy=(3, 0.5), fontsize=9, color=GREEN, fontweight='bold',
                ha='center')

    fig.suptitle('Graduated Dissent: Higher Detection, Zero False Positives',
                fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig1_detection_and_fp.png')
    plt.savefig(f'{outdir}/fig1_detection_and_fp.pdf')
    print('Saved fig1')


def fig2_per_paper_detection():
    """Per-paper ground truth detection across conditions."""
    papers = ['R01', 'R02', 'R03', 'R04', 'R05', 'R10', 'R11', 'R19', 'R24', 'R25']

    # Detection: 1 = found ground truth, 0 = missed
    b1_det = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]  # 3/10
    b2_det = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]  # 4/10
    b3_det = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]  # 3/10
    gd_det = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]  # 7/10

    fig, ax = plt.subplots(figsize=(12, 5))

    y = np.arange(len(papers))
    height = 0.19

    ax.barh(y + 1.5*height, gd_det, height, color=GREEN, alpha=0.85, label='Graduated Dissent (7/10)')
    ax.barh(y + 0.5*height, b3_det, height, color=PURPLE, alpha=0.8, label='B3: Multi-model, no steelman (3/10)')
    ax.barh(y - 0.5*height, b2_det, height, color=WARN, alpha=0.7, label='B2: Single + rubric (4/10)')
    ax.barh(y - 1.5*height, b1_det, height, color='gray', alpha=0.5, label='B1: Single, no rubric (3/10)')

    ax.set_yticks(y)
    ax.set_yticklabels(papers, fontweight='bold')
    ax.set_xlabel('Ground Truth Error Detected', fontweight='bold')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Missed', 'Found'])
    ax.set_title('Per-Paper Detection of Documented Retraction Cause', fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig2_per_paper_detection.png')
    plt.savefig(f'{outdir}/fig2_per_paper_detection.pdf')
    print('Saved fig2')


def fig3_severity_by_category():
    """Stacked bar showing severity distribution by paper category."""
    categories = ['Retracted\n(n=10)', 'Controls\n(n=10)', 'Hard-Neg\n(n=9)', 'Wildcards\n(n=5)']
    rw = [0.5, 0.0, 0.0, 0.0]
    mr = [8.3, 7.9, 6.2, 6.6]
    mi = [4.9, 5.1, 5.6, 5.8]

    fig, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(categories))
    width = 0.6

    b1 = ax.bar(x, rw, width, color=RET, alpha=0.9, label='Retraction-worthy')
    b2 = ax.bar(x, mr, width, bottom=rw, color=WARN, alpha=0.7, label='Major-revision')
    b3 = ax.bar(x, mi, width, bottom=[r+m for r,m in zip(rw, mr)], color=CTRL, alpha=0.5, label='Minor')

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontweight='bold')
    ax.set_ylabel('Average findings per paper', fontweight='bold')
    ax.set_title('Severity Distribution by Paper Category\n(Graduated Dissent Protocol)', fontweight='bold')
    ax.legend(loc='upper right')

    # Annotate the RW difference
    ax.annotate('Discrimination\nconcentrated here',
               xy=(0, 0.25), xytext=(2.5, 3),
               fontsize=9, color=RET, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=RET, lw=1.5))

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig3_severity_by_category.png')
    plt.savefig(f'{outdir}/fig3_severity_by_category.pdf')
    print('Saved fig3')


def fig4_fp_elimination():
    """Show how GD eliminates B2's false positives."""
    papers = ['C04\n(control)', 'C10\n(control)', 'HN10\n(hard-neg)']
    b2_rw = [1, 2, 1]
    b3_rw = [2, 0, 0]
    gd_rw = [0, 0, 0]

    fig, ax = plt.subplots(figsize=(9, 4))

    x = np.arange(len(papers))
    width = 0.25

    bars1 = ax.bar(x - width, b2_rw, width, color=RET, alpha=0.85,
                   label='B2: Single model + rubric', edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x, b3_rw, width, color=PURPLE, alpha=0.85,
                   label='B3: Multi-model, no steelman', edgecolor='white', linewidth=1.5)
    bars3 = ax.bar(x + width, gd_rw, width, color=GREEN, alpha=0.85,
                   label='Graduated Dissent', edgecolor='white', linewidth=1.5)

    ax.set_xticks(x)
    ax.set_xticklabels(papers, fontweight='bold')
    ax.set_ylabel('Retraction-worthy findings', fontweight='bold')
    ax.set_title('False Positive Elimination\nSteelman exchange removes overblown severity ratings',
                fontweight='bold')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 3.5)

    for bar, val in zip(bars1, b2_rw):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.1,
               str(val), ha='center', fontweight='bold', fontsize=12, color=RET)
    for bar, val in zip(bars2, b3_rw):
        ax.text(bar.get_x() + bar.get_width()/2, val + 0.1,
               str(val), ha='center', fontweight='bold', fontsize=12, color=PURPLE)
    for bar in bars3:
        ax.text(bar.get_x() + bar.get_width()/2, 0.1,
               '0', ha='center', fontweight='bold', fontsize=12, color=GREEN)

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig4_fp_elimination.png')
    plt.savefig(f'{outdir}/fig4_fp_elimination.pdf')
    print('Saved fig4')


def fig5_protocol_flow():
    """Clean protocol flowchart."""
    fig, ax = plt.subplots(figsize=(14, 4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4)
    ax.axis('off')

    box = dict(boxstyle='round,pad=0.4', facecolor=LIGHT, edgecolor=DARK, linewidth=1.5)
    highlight = dict(boxstyle='round,pad=0.4', facecolor='#eaf2f8', edgecolor=CTRL, linewidth=2)
    arbiter_box = dict(boxstyle='round,pad=0.4', facecolor='#e8f8f5', edgecolor=GREEN, linewidth=2)

    # Paper
    ax.text(0.8, 2, 'Anonymized\nManuscript', fontsize=9, ha='center', va='center', bbox=box, fontweight='bold')

    # Provers
    ax.annotate('', xy=(2.2, 2.8), xytext=(1.5, 2.3), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.annotate('', xy=(2.2, 1.2), xytext=(1.5, 1.7), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.text(3.2, 3.2, 'GPT-5.4\n+severity', fontsize=8, ha='center', va='center', bbox=highlight)
    ax.text(3.2, 0.8, 'DeepSeek\n+severity', fontsize=8, ha='center', va='center', bbox=highlight)
    ax.text(3.2, 2, 'separated\ncontexts', fontsize=7, ha='center', va='center', style='italic', color='gray')

    # Judge
    ax.annotate('', xy=(5, 2.3), xytext=(4.2, 2.9), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.annotate('', xy=(5, 1.7), xytext=(4.2, 1.1), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.text(5.8, 2, 'DeepSeek\nJudge', fontsize=8, ha='center', va='center', bbox=box)

    # SNR check
    ax.annotate('', xy=(7.2, 2), xytext=(6.6, 2), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.text(7.8, 2, 'SNR\ncheck', fontsize=8, ha='center', va='center',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9e7', edgecolor=WARN, linewidth=1.5), fontweight='bold')

    # Steelman
    ax.annotate('', xy=(9.2, 2), xytext=(8.5, 2), arrowprops=dict(arrowstyle='->', color=WARN, lw=1.5))
    ax.text(10, 2, 'Steelman\nExchange', fontsize=8, ha='center', va='center', bbox=highlight, fontweight='bold')
    ax.text(10, 1, 'Provers challenge\neach other\'s severity', fontsize=7, ha='center', style='italic', color='gray')

    # Arbiter
    ax.annotate('', xy=(11.5, 2), xytext=(10.9, 2), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
    ax.text(12.3, 2, 'Opus\nArbiter', fontsize=9, ha='center', va='center', bbox=arbiter_box, fontweight='bold')
    ax.text(12.3, 0.8, 'Conservative\nseverity', fontsize=7, ha='center', style='italic', color=GREEN)

    ax.set_title('Graduated Dissent Protocol (v6)', fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig5_protocol_flow.png')
    plt.savefig(f'{outdir}/fig5_protocol_flow.pdf')
    print('Saved fig5')


def fig6_full_spectrum():
    """Full quality spectrum from viXra GUT to clean."""
    categories = ['viXra GUT\n(avg, n=5)', 'Retracted\n(avg, n=10)', 'Controls\n(avg, n=10)',
                  'Hard-Neg\n(avg, n=9)', 'Wildcards\n(avg, n=5)']
    rw = [7.2, 0.5, 0, 0, 0]
    mr = [10.0, 8.3, 7.9, 6.2, 6.6]
    mi = [2.2, 4.9, 5.1, 5.6, 5.8]
    scores = [7.2*3+10.0*2+2.2, 23.0, 20.9, 18.0, 19.0]

    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.arange(len(categories))

    # Use score as bar height, color by dominant severity
    colors = [RET, WARN, CTRL, CTRL, CTRL]
    bars = ax.bar(x, scores, color=colors, alpha=0.8, edgecolor='white', linewidth=2)

    # Add RW count annotation
    for i, (bar, rw_val) in enumerate(zip(bars, rw)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
               f'RW={rw_val}' if isinstance(rw_val, int) else f'RW={rw_val:.1f}',
               ha='center', fontweight='bold', fontsize=9,
               color=RET if rw_val > 0 else 'gray')

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontweight='bold')
    ax.set_ylabel('Severity Score (3xRW + 2xMR + 1xMinor)', fontweight='bold')
    ax.set_title('Full Quality Spectrum\nProtocol calibrates severity across the range', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig6_full_spectrum.png')
    plt.savefig(f'{outdir}/fig6_full_spectrum.pdf')
    print('Saved fig6')


if __name__ == '__main__':
    fig1_ground_truth_and_fp()
    fig2_per_paper_detection()
    fig3_severity_by_category()
    fig4_fp_elimination()
    fig5_protocol_flow()
    fig6_full_spectrum()
    print('\nAll figures generated.')
