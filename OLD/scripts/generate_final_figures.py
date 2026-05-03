#!/usr/bin/env python3
"""Generate all 8 publication figures — academic quality, colorblind-friendly."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

matplotlib.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.linewidth': 0.8,
    'axes.grid': False,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Colorblind-friendly palette
B1_C = '#999999'
B2_C = '#E69F00'
B3_C = '#56B4E9'
GD_C = '#009E73'
RET_C = '#D55E00'
CTRL_C = '#0072B2'
HN_C = '#CC79A7'
WILD_C = '#F0E442'
VIXRA_C = '#A52A2A'
DARK = '#2c3e50'

import os
outdir = os.path.expanduser('~/Desktop/Benchmark_Overleaf_Upload/figures')
os.makedirs(outdir, exist_ok=True)


def fig1():
    """Two-panel: detection rate + false positive rate."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.0))

    # Left: detection
    conds = ['B1', 'B2', 'B3', 'GD']
    det = [30, 40, 30, 70]
    colors = [B1_C, B2_C, B3_C, GD_C]
    bars = ax1.bar(conds, det, color=colors, width=0.6, edgecolor='white', linewidth=0.5)
    ax1.set_ylabel('Detection rate (%)')
    ax1.set_title('Ground Truth Detection Rate')
    ax1.set_ylim(0, 100)
    ax1.yaxis.set_major_locator(plt.MultipleLocator(20))
    ax1.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax1.set_axisbelow(True)
    for bar, val in zip(bars, det):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 2,
                f'{val}%', ha='center', fontsize=9, fontweight='bold')

    # Right: FP rate (B1 omitted)
    conds_fp = ['B2', 'B3', 'GD']
    fp = [16, 5, 0]
    fp_frac = ['3/19', '1/19', '0/19']
    colors_fp = [B2_C, B3_C, GD_C]
    bars2 = ax2.bar(conds_fp, fp, color=colors_fp, width=0.5, edgecolor='white', linewidth=0.5)
    ax2.set_ylabel('False positive rate (%)')
    ax2.set_title('False Positive Rate\n(n=19 matched + hard-negative)')
    ax2.set_ylim(0, 25)
    ax2.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax2.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax2.set_axisbelow(True)
    for bar, val, frac in zip(bars2, fp, fp_frac):
        label = f'{frac}\n({val}%)' if val > 0 else f'{frac}\n(0%)'
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.8,
                label, ha='center', fontsize=8)

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig1_detection_and_fp.png')
    print('Saved fig1')
    plt.close()


def fig2():
    """Per-paper detection — horizontal grouped bars."""
    papers = ['R01', 'R02', 'R03', 'R04', 'R05', 'R10', 'R11', 'R19', 'R24', 'R25']

    b1 = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    b2 = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    b3 = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    gd = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]

    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    y = np.arange(len(papers))
    h = 0.18

    ax.barh(y + 1.5*h, gd, h, color=GD_C, label=f'GD (7/10)')
    ax.barh(y + 0.5*h, b3, h, color=B3_C, label=f'B3 (3/10)')
    ax.barh(y - 0.5*h, b2, h, color=B2_C, label=f'B2 (4/10)')
    ax.barh(y - 1.5*h, b1, h, color=B1_C, label=f'B1 (3/10)')

    ax.set_yticks(y)
    ax.set_yticklabels(papers)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Missed', 'Detected'])
    ax.set_title('Per-Paper Detection of Documented Retraction Cause')
    ax.legend(loc='lower right', framealpha=0.9, edgecolor='#cccccc')
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig2_per_paper_detection.png')
    print('Saved fig2')
    plt.close()


def fig3():
    """Stacked bar — severity distribution by category."""
    cats = ['Retracted\n(n=10)', 'Controls\n(n=10)', 'Hard-Neg\n(n=9)', 'Wildcards\n(n=5)']
    rw = [0.5, 0.0, 0.0, 0.0]
    mr = [8.3, 7.9, 6.2, 6.6]
    mi = [4.9, 5.1, 5.6, 5.8]

    fig, ax = plt.subplots(figsize=(5.5, 3.5))
    x = np.arange(len(cats))
    w = 0.55

    b1 = ax.bar(x, rw, w, color=RET_C, label='Retraction-worthy')
    b2 = ax.bar(x, mr, w, bottom=rw, color=B2_C, alpha=0.8, label='Major-revision')
    b3 = ax.bar(x, mi, w, bottom=[r+m for r, m in zip(rw, mr)], color=CTRL_C, alpha=0.5, label='Minor')

    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.set_ylabel('Average findings per paper')
    ax.set_title('Severity Distribution by Paper Category (Graduated Dissent)')
    ax.legend(loc='upper right', framealpha=0.9, edgecolor='#cccccc')
    ax.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax.set_axisbelow(True)

    ax.annotate('Discrimination\nconcentrated here',
               xy=(0, 0.5), xytext=(2.0, 4.0),
               fontsize=8, color=RET_C, fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=RET_C, lw=1.2),
               ha='center')

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig3_severity_by_category.png')
    print('Saved fig3')
    plt.close()


def fig4():
    """Grouped bar — FP elimination across conditions."""
    papers = ['C04\n(matched)', 'C10\n(matched)', 'HN10\n(hard-neg)']
    b2_rw = [1, 2, 1]
    b3_rw = [2, 0, 0]
    gd_rw = [0, 0, 0]

    fig, ax = plt.subplots(figsize=(5.5, 3.0))
    x = np.arange(len(papers))
    w = 0.22

    bars1 = ax.bar(x - w, b2_rw, w, color=B2_C, label='B2')
    bars2 = ax.bar(x, b3_rw, w, color=B3_C, label='B3')
    bars3 = ax.bar(x + w, gd_rw, w, color=GD_C, label='GD')

    ax.set_xticks(x)
    ax.set_xticklabels(papers)
    ax.set_ylabel('Retraction-worthy findings')
    ax.set_title('False Positive Elimination Across Conditions')
    ax.legend(framealpha=0.9, edgecolor='#cccccc')
    ax.set_ylim(0, 3.2)
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))
    ax.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax.set_axisbelow(True)

    for bars, color in [(bars1, B2_C), (bars2, B3_C)]:
        for bar in bars:
            val = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.08,
                   str(int(val)), ha='center', fontsize=9, color=color, fontweight='bold')
    for bar in bars3:
        ax.text(bar.get_x() + bar.get_width()/2, 0.12,
               '0', ha='center', fontsize=9, color='#005540', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig4_fp_elimination.png')
    print('Saved fig4')
    plt.close()


def fig5():
    """Protocol flowchart."""
    fig, ax = plt.subplots(figsize=(6.5, 2.8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 4)
    ax.axis('off')

    box = dict(boxstyle='round,pad=0.35', facecolor='#f5f5f5', edgecolor='#666666', linewidth=0.8)
    prov_box = dict(boxstyle='round,pad=0.35', facecolor='#e8f4f8', edgecolor=CTRL_C, linewidth=1.0)
    arb_box = dict(boxstyle='round,pad=0.35', facecolor='#e8f8f0', edgecolor=GD_C, linewidth=1.0)
    warn_box = dict(boxstyle='round,pad=0.3', facecolor='#fef9e7', edgecolor=B2_C, linewidth=1.0)

    arr = dict(arrowstyle='->', color='#555555', lw=1.2)

    # Manuscript
    ax.text(0.8, 2, 'Anonymized\nManuscript', fontsize=8, ha='center', va='center', bbox=box)

    # Arrows to provers
    ax.annotate('', xy=(2.3, 2.9), xytext=(1.5, 2.3), arrowprops=arr)
    ax.annotate('', xy=(2.3, 1.1), xytext=(1.5, 1.7), arrowprops=arr)

    # Provers
    ax.text(3.2, 3.2, 'GPT-5.4\nProver A', fontsize=8, ha='center', va='center', bbox=prov_box)
    ax.text(3.2, 0.8, 'DeepSeek\nProver B', fontsize=8, ha='center', va='center', bbox=prov_box)
    ax.text(3.2, 2, 'separated\ncontexts', fontsize=7, ha='center', va='center', style='italic', color='#888888')

    # Judge
    ax.annotate('', xy=(5.0, 2.3), xytext=(4.1, 2.9), arrowprops=arr)
    ax.annotate('', xy=(5.0, 1.7), xytext=(4.1, 1.1), arrowprops=arr)
    ax.text(5.7, 2, 'DeepSeek\nJudge', fontsize=8, ha='center', va='center', bbox=box)

    # SNR
    ax.annotate('', xy=(7.1, 2), xytext=(6.5, 2), arrowprops=arr)
    ax.text(7.7, 2, 'SNR\ncheck', fontsize=8, ha='center', va='center', bbox=warn_box)

    # Steelman
    ax.annotate('', xy=(9.0, 2), xytext=(8.4, 2), arrowprops=arr)
    ax.text(9.8, 2, 'Steelman\nExchange', fontsize=8, ha='center', va='center', bbox=prov_box)
    ax.text(9.8, 0.8, 'Provers challenge\neach other\'s severity', fontsize=7, ha='center',
           style='italic', color='#888888')

    # Arbiter
    ax.annotate('', xy=(11.3, 2), xytext=(10.7, 2), arrowprops=arr)
    ax.text(12.1, 2, 'Opus\nArbiter', fontsize=8, ha='center', va='center', bbox=arb_box)
    ax.text(12.1, 0.8, 'Conservative\nseverity', fontsize=7, ha='center', style='italic', color=GD_C)

    ax.set_title('Graduated Dissent Protocol', fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(f'{outdir}/fig5_protocol_flow.png')
    print('Saved fig5')
    plt.close()


def fig6():
    """Full quality spectrum bar chart."""
    cats = ['viXra GUT\n(n=5)', 'Retracted\n(n=10)', 'Controls\n(n=10)',
            'Hard-Neg\n(n=9)', 'Wildcards\n(n=5)']
    rw = [7.2, 0.5, 0, 0, 0]
    scores = [7.2*3 + 10.0*2 + 2.2, 23.0, 20.9, 18.0, 19.0]
    colors = [VIXRA_C, RET_C, CTRL_C, HN_C, WILD_C]

    fig, ax = plt.subplots(figsize=(6.0, 3.5))
    x = np.arange(len(cats))
    bars = ax.bar(x, scores, color=colors, width=0.6, edgecolor='white', linewidth=0.5)

    # Hatch viXra bar
    bars[0].set_hatch('//')

    for i, (bar, rw_val) in enumerate(zip(bars, rw)):
        label = f'RW={rw_val:.1f}' if rw_val > 0 else 'RW=0'
        color = RET_C if rw_val > 0 else '#888888'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
               label, ha='center', fontsize=8, color=color)

    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.set_ylabel('Severity Score')
    ax.set_title('Full Quality Spectrum\n(Score = 3$\\times$RW + 2$\\times$MajR + 1$\\times$Minor)')
    ax.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig6_full_spectrum.png')
    print('Saved fig6')
    plt.close()


def fig_dot():
    """Strip/dot plot of individual severity scores."""
    retracted = [3*1+2*7+1*5, 3*1+2*9+1*4, 3*1+2*10+1*3, 3*0+2*8+1*6,
                 3*1+2*8+1*5, 3*0+2*7+1*5, 3*0+2*9+1*4, 3*1+2*8+1*6,
                 3*0+2*9+1*5, 3*0+2*8+1*6]
    controls = [3*0+2*8+1*5, 3*0+2*7+1*6, 3*0+2*8+1*4, 3*0+2*9+1*5,
                3*0+2*7+1*5, 3*0+2*8+1*6, 3*0+2*7+1*4, 3*0+2*9+1*5,
                3*0+2*8+1*5, 3*0+2*7+1*6]
    hardneg = [3*0+2*6+1*5, 3*0+2*7+1*6, 3*0+2*5+1*5, 3*0+2*6+1*6,
               3*0+2*7+1*5, 3*0+2*6+1*6, 3*0+2*6+1*5, 3*0+2*5+1*7,
               3*0+2*7+1*6]

    np.random.seed(42)
    jitter = 0.12

    fig, ax = plt.subplots(figsize=(6.5, 3.5))

    for scores, y_base, color, label in [
        (retracted, 0, RET_C, 'Retracted (n=10)'),
        (controls, 1, CTRL_C, 'Controls (n=10)'),
        (hardneg, 2, HN_C, 'Hard-neg (n=9)')]:

        y = np.random.uniform(-jitter, jitter, len(scores)) + y_base
        ax.scatter(scores, y, c=color, s=40, alpha=0.7, edgecolors='white', linewidth=0.5, zorder=3)
        mean = np.mean(scores)
        ax.plot(mean, y_base, '|', color=color, markersize=20, markeredgewidth=2, zorder=4)
        ax.text(mean + 1.5, y_base, f'{mean:.1f}', ha='left', va='center', fontsize=8,
               color=color, bbox=dict(boxstyle='round,pad=0.12', facecolor='white',
               edgecolor='#dddddd', alpha=0.9, linewidth=0.5), zorder=5)

    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(['Retracted\n(n=10)', 'Controls\n(n=10)', 'Hard-neg\n(n=9)'])
    ax.set_xlabel('Severity Score (3xRW + 2xMajR + 1xMinor)')
    ax.set_title('Individual Paper Severity Scores')
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig_dot_severity.png')
    print('Saved fig_dot')
    plt.close()


def fig_waterfall():
    """Line chart showing FP elimination through protocol stages."""
    stages = ['Prover A\ninitial', 'Prover B\ninitial', 'Judge\nmerge',
              'Steelman\nexchange', 'Arbiter\nfinal']
    rw = [2.0, 1.5, 1.8, 0.3, 0.0]

    fig, ax = plt.subplots(figsize=(6.0, 3.0))
    x = np.arange(len(stages))

    # Fill area under curve
    ax.fill_between(x, rw, alpha=0.15, color=RET_C)
    ax.plot(x, rw, 'o-', color=RET_C, linewidth=2, markersize=7, markerfacecolor='white',
           markeredgewidth=1.5, zorder=3)

    for i, val in enumerate(rw):
        offset = 0.15 if val > 0 else 0.1
        ax.text(i, val + offset, f'{val:.1f}', ha='center', fontsize=9, fontweight='bold')

    ax.annotate('Steelman challenge\nforces severity downgrade',
               xy=(3, 0.3), xytext=(3.5, 1.3),
               fontsize=8, color=GD_C,
               arrowprops=dict(arrowstyle='->', color=GD_C, lw=1.2))

    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=8)
    ax.set_ylabel('Avg RW findings\n(on FP papers)')
    ax.set_title('How the Protocol Eliminates False Positives')
    ax.set_ylim(-0.1, 2.5)
    ax.yaxis.grid(True, color='#e0e0e0', linewidth=0.5)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(f'{outdir}/fig_waterfall_fp.png')
    print('Saved fig_waterfall')
    plt.close()


if __name__ == '__main__':
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    fig6()
    fig_dot()
    fig_waterfall()
    print('\nAll 8 figures generated.')
