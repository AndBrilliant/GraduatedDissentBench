# Protocol Thresholds

## Agreement Threshold (θ_accept = 0.90)

If the judge rates semantic agreement between provers at ≥ 0.90, the protocol accepts without escalation (Level 0). This threshold was set prior to evaluation based on pilot testing during protocol development.

## Noise Floor (θ_noise = 0.15)

The minimum disagreement expected from RLHF-trained models reviewing any manuscript. Models will always find some concerns; disagreement below this level is considered noise rather than signal.

## SNR Check

Signal-to-noise ratio = (1.0 - agreement) / θ_noise

- SNR < 1.0: Disagreement is below noise floor (Level 1, no escalation)
- SNR ≥ 1.0: Disagreement exceeds noise floor → steelman exchange triggered (Level 2)

## Escalation Levels

| Level | Condition | Action |
|-------|-----------|--------|
| L0 | Agreement ≥ 0.90 | Accept without escalation |
| L1 | SNR < 1.0 | Accept (disagreement is noise) |
| L2 | SNR ≥ 1.0 | Steelman exchange → Arbiter |

## Arbiter Severity Threshold

The arbiter is instructed: "When in doubt, MAJOR-REVISION." This is a conservative calibration optimized for specificity (zero false positives) at the cost of sensitivity. The same architecture supports more permissive calibrations by modifying only the arbiter instructions.
