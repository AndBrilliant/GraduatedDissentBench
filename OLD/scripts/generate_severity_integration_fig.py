#!/usr/bin/env python3
"""Generate the severity integration conceptual figure."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

RET = '#c0392b'
CTRL = '#2980b9'
GREEN = '#27ae60'

import os
outdir = os.path.expanduser('~/Desktop/Academic/graduated_dissent_bench_v6/manuscripts/figures')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# Left: Without severity integration - everything looks the same
np.random.seed(42)
n_retracted = 8
n_control = 8

# Without severity: all findings cluster at similar "conviction" level (RLHF effect)
ret_x = np.random.uniform(0.4, 0.7, n_retracted)
ret_y = np.random.uniform(0.3, 0.7, n_retracted)
ctrl_x = np.random.uniform(0.3, 0.6, n_control)
ctrl_y = np.random.uniform(0.35, 0.75, n_control)

ax1.scatter(ret_x, ret_y, c=RET, s=80, alpha=0.7, label='Retracted paper findings', zorder=3)
ax1.scatter(ctrl_x, ctrl_y, c=CTRL, s=80, alpha=0.7, label='Control paper findings', zorder=3)
ax1.axhline(y=0.5, color='gray', linewidth=1, linestyle='--', alpha=0.5)
ax1.text(0.95, 0.52, 'threshold?', ha='right', fontsize=9, color='gray', style='italic')
ax1.set_xlabel('Finding specificity', fontweight='bold')
ax1.set_ylabel('Apparent conviction', fontweight='bold')
ax1.set_title('Without Severity Integration\n(RLHF formatting flattens confidence)', fontweight='bold', fontsize=11)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.legend(fontsize=8, loc='upper left')
ax1.text(0.5, 0.05, 'Cannot separate: all findings\npresented at same conviction level',
         ha='center', fontsize=9, style='italic', color='gray',
         transform=ax1.transAxes)

# Right: With severity integration - clear separation
np.random.seed(42)
# Retracted: some findings cluster HIGH (true RW), most moderate
ret_x2 = np.random.uniform(0.5, 0.9, n_retracted)
ret_y2_high = np.array([0.85, 0.9, 0.78])  # RW findings
ret_y2_mid = np.random.uniform(0.3, 0.55, n_retracted - 3)  # MajR/Minor
ret_y2 = np.concatenate([ret_y2_high, ret_y2_mid])

# Controls: all findings cluster MODERATE to LOW
ctrl_x2 = np.random.uniform(0.3, 0.8, n_control)
ctrl_y2 = np.random.uniform(0.15, 0.55, n_control)

ax2.scatter(ret_x2[:3], ret_y2[:3], c=RET, s=120, alpha=0.9, marker='*',
           label='Retracted: RW findings', zorder=4)
ax2.scatter(ret_x2[3:], ret_y2[3:], c=RET, s=60, alpha=0.5,
           label='Retracted: MajR/Minor', zorder=3)
ax2.scatter(ctrl_x2, ctrl_y2, c=CTRL, s=60, alpha=0.5,
           label='Control: MajR/Minor', zorder=3)

ax2.axhline(y=0.7, color=GREEN, linewidth=2, linestyle='--', alpha=0.8)
ax2.text(0.95, 0.72, 'RW threshold', ha='right', fontsize=9, color=GREEN, fontweight='bold')

ax2.fill_between([0, 1], 0.7, 1.0, color=RET, alpha=0.05)
ax2.fill_between([0, 1], 0, 0.7, color=CTRL, alpha=0.03)

ax2.set_xlabel('Finding specificity', fontweight='bold')
ax2.set_ylabel('Severity rating', fontweight='bold')
ax2.set_title('With Severity Integration\n(Provers externalize confidence)', fontweight='bold', fontsize=11)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.legend(fontsize=8, loc='upper left')
ax2.text(0.5, 0.05, 'Clean separation: only retracted papers\nhave findings above RW threshold',
         ha='center', fontsize=9, style='italic', color=GREEN,
         transform=ax2.transAxes)

plt.tight_layout()
plt.savefig(f'{outdir}/fig_key_severity_integration.png')
plt.savefig(f'{outdir}/fig_key_severity_integration.pdf')
print('Saved fig_key_severity_integration')
