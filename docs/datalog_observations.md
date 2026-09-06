# Datalog observations

These notes summarize the logs captured during the Sniper idle/startup tuning sequence.

## Summary metrics

| log | file | duration (s) | run segments | CTS run (°F) | peak RPM | end-20s IAC | end-20s RPM | valid AFR | target AFR | max CL comp | min battery |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 001-initial-cold-start-dies.csv | 35.928 | 9 | 89.1–89.3 | 1,023 | 100.0 | 788 | 15.99 | 12.57 | 50.0 | 7.67 |
| 2 | 002-header-gasket-cl-off-idle-screw-1turn.csv | 136.998 | 1 | 95.5–102.5 | 1,221 | 55.0 | 1,085 | 14.82 | 12.80 | 0.0 | 8.55 |
| 3 | 003-cl-off-full-warmup-tps-reset.csv | 359.388 | 1 | 118.2–212.7 | 2,002 | 0.0 | 1,139 | 13.55 | 13.36 | 0.0 | 8.83 |
| 4 | 004-iac-tuning-idle-screw-adjusted-hot-flare.csv | 115.722 | 1 | 184.4–209.8 | 3,071 | 6.1 | 980 | 13.60 | 13.52 | 0.0 | 8.15 |
| 5 | 005-hot-start-iac-35pct-short-cool-log.csv | 26.448 | 1 | 124.6–124.8 | 1,144 | 100.0 | 1,021 | 18.72 | 13.25 | 0.0 | 7.88 |
| 6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 429.478 | 2 | 124.3–201.3 | 1,146 | 27.7 | 1,056 | 14.38 | 13.41 | 0.0 | 8.27 |
| 7 | 007-full-warmup-vacuum-bleed-coolant-dead-cylinder.csv | 429.478 | 2 | 124.3–201.3 | 1,146 | 27.7 | 1,056 | 14.38 | 13.41 | 0.0 | 8.27 |
| 8 | 008-cold-warmup-new-plugs-fixed-exhaust-leaks.csv | 826.178 | 6 | 90.4–189.0 | 3,555 | 22.3 | 1,249 | 14.42 | 13.30 | 0.0 | 7.90 |
| 9 | 009-cold-start-enrichment-v1-stall.csv | 47.538 | 3 | 91.3–92.5 | 981 | 100.0 | 832 | 16.40 | 12.63 | 0.0 | 9.23 |
| 10 | 010-cold-warmup-enrichment-v2-full-success.csv | 493.774 | 1 | 95.4–161.1 | 1,132 | 26.6 | 1,001 | 14.13 | 13.22 | 0.0 | 7.86 |
| 11 | 011-cold-drivearound-first-drive.csv | 796.730 | 1 | 89.5–191.7 | 5,492 | 21.0 | 1,203 | 13.16 | 13.45 | 0.0 | 7.53 |
| 12 | 012-hot-restart-no-start.csv | 37.790 | 0 | — | — | — | — | — | — | — | 8.57 |
| 13 | 013-cold-drive-closed-loop-learning.csv | 680.942 | 1 | 95.9–193.1 | 5,179 | 16.9 | 1,061 | 13.54 | 13.49 | 50.0 | 7.95 |

## Per-log observations

### 001 — Initial start, idle, then dies

File: `logs/raw/001-initial-cold-start-dies.csv`

- Engine starts after cranking, idles briefly, then dies.
- IAC is pinned at 100% essentially the entire time.
- Closed loop is active and CL Comp reaches +50%, meaning the ECU is adding maximum correction fuel.
- AFR reads lean compared with target, but this was before known header leaks were improved.
- Early conclusion: idle air authority was insufficient and closed loop was likely chasing a questionable lean signal.

### 002 — Header gasket tightened/replaced, closed loop off, idle screw +1 turn

File: `logs/raw/002-header-gasket-cl-off-idle-screw-1turn.csv`

- Engine now starts and continues running.
- Closed loop is disabled; CL Comp stays at 0%.
- IAC improves but is still high by the end of the log.
- TPS reads around 1.9% at idle after the idle screw move, so TPS autoset/reset was needed.
- Conclusion: opening throttle blades helped significantly; fuel pressure was not the primary suspect.

### 003 — Closed loop off, full warmup after TPS reset

File: `logs/raw/003-cl-off-full-warmup-tps-reset.csv`

- TPS reset is effectively complete.
- Engine warms to full temperature and keeps running.
- Hot IAC falls to 0%, meaning the throttle blades are now too far open.
- Hot idle is mechanically held high at roughly 1,140 rpm.
- Conclusion: close the idle screw slightly and recheck hot IAC above 160°F.

### 004 — Idle screw adjusted, hot restart flare

File: `logs/raw/004-iac-tuning-idle-screw-adjusted-hot-flare.csv`

- Hot idle is now good: end-of-log IAC is around 6-8%, TPS near 0, RPM around 980.
- Startup/hot-restart behavior is bad: engine flares to ~3,071 rpm.
- TPS stays low during the flare, so the flare is from startup IAC airflow rather than throttle input.
- Conclusion: do not touch idle screw; tune IAC Startup Parked Position / Hold Time / Decay Time.

### 005 — Hot-start IAC settings changed, but test was only ~125°F

File: `logs/raw/005-hot-start-iac-35pct-short-cool-log.csv`

- Settings changed before this log: 160°F+ IAC parked position moved to 35%, startup hold set to 1 sec, decay set to 3 sec.
- This log is at ~125°F, so the 160°F row likely was not active.
- IAC is 100% and RPM only peaks around 1,144 rpm, so there is no runaway flare.
- AFR reads very lean for a short period, but the test is short and at low load.
- Conclusion: the hot-start fix did not cause a flare at this temperature; need a longer full warmup to judge AFR and IAC transition.

### 006 — Full warmup plus hot restart after IAC Startup changes

File: `logs/raw/006-full-warmup-hot-restart-after-iac-startup.csv`

- Warmup begins around 124°F and goes to roughly 200°F.
- AFR looks lean below about 135-140°F, then moves close to target as the engine warms.
- Hot restart is now fixed: peak RPM is only about 1,146 rpm instead of ~3,071 rpm.
- End-of-log hot IAC is around 20%, slightly higher than ideal but acceptable for now while the tune is stabilizing.
- Conclusion: leave hot-start IAC settings alone; consider a small coolant enrichment bump around 120-135°F.

### 007 — Full warmup after vacuum/coolant bleed; dead cylinder identified

File: `logs/raw/007-full-warmup-vacuum-bleed-coolant-dead-cylinder.csv`

Date: 2026-06-27

- Coolant system vacuum-bled before this session to address rapid overheating. Result: normal warm-up rate confirmed (124°F → 201°F over 7.2 min, no spike).
- Engine required manual throttle blips to stay alive in the first ~60 seconds, consistent with a misfiring cylinder.
- IAC stepped down correctly through the heat cycle: ~71% at 120-140°F, ~21% at 160-180°F, ~19% at 200°F+. Idle held 1015-1019 RPM throughout — IAC curve is working.
- Hot restart (engine off at 197°F, restarted 6 seconds later): fired immediately, RPM held at ~1080, AFR within 0.2 of target by +5 seconds, IAC decayed from 44% → 20% smoothly. Hot start is confirmed fixed.
- Coolant enrichment tapered correctly: +4.6% at 120-140°F, +1.7% at 140-160°F, neutral above 160°F.
- Entire log is 100% open loop — closed loop never enabled. AFR mean error +0.95 lean, worst spike +6.7 AFR lean. With CL off there is no correction; lean spikes go uncorrected.
- MAP at idle: 76.5 kPa avg (~7.3 inHg vacuum). Low vacuum consistent with aggressive cam overlap.
- **Dead cylinder identified via thermal camera**: one passenger-side header tube reads ~85.6°F (ambient) while all others are pegged over camera max range. A cold tube = no combustion in that cylinder. This directly explains the lean spikes in the AFR (unburned air passing the O2 sensor), the stumble/blip-to-survive at initial startup, and the rough idle character.
- Conclusion: do not change any EFI settings until the dead cylinder is diagnosed. Suspect fouled spark plug first (rich cold-start enrichment history), then spark wire/coil, then injector, then compression.

### 008 — Cold warmup from 90°F, new spark plugs, fixed exhaust leaks (2026-06-28)

File: `logs/raw/008-cold-warmup-new-plugs-fixed-exhaust-leaks.csv`

- First cold start from 90°F after replacing all four no-gauge-side spark plugs and fixing the exhaust flange leaks on that side.
- Engine stalled on first attempt after 8 seconds. Second attempt held. Driver had to blip throttle during initial cold idle to keep it alive — confirmed in TPS data (multiple revs to 9–28% TPS at t=46–55s).
- **Dead cylinder confirmed fixed**: at 160–180°F, RPM stdev=20.6 (vs 19.9 in log007), AFR mean error=+0.059, zero correlated misfire events. No rhythmic RPM dip pattern. Engine is mechanically healthy when warm.
- **No IAC flare on hot restart**: hot restart at 183°F settled cleanly to 980–1,093 RPM with TPS at 0.3%. All high-RPM events in that window (including 3,555 RPM peak) were driver revs confirmed by TPS (40–65%). RPM spikes at TPS<2% were engine coasting down after revs, not IAC-driven flares.
- **Cold idle lean condition identified as sole remaining issue**: engine runs 2–4 AFR lean from 90–130°F. Coolant enrichment adding +11.7% at 80–100°F is insufficient. AFR error by temp band:
  - 100–120°F: +2.39 lean, 48.5% of time >+2 lean
  - 120–140°F: +1.28 lean, 4.8% of time >+2 lean
  - 140–160°F: +0.53 lean, 0% >+2 lean
  - 160–180°F: +0.06 lean, 0% >+2 lean (effectively perfect)
- RPM roughness at cold temps is caused entirely by the lean condition — random misfire pattern, not rhythmic single-cylinder pattern.
- Conclusion: increase coolant enrichment at 80–130°F significantly. Engine is mechanically good; this is a calibration-only fix.

### 011 — First drive-around: clean cold start, warmup on target, clutch check inconclusive (2026-07-03)

File: `logs/raw/011-cold-drivearound-first-drive.csv`

- Best cold start on record with enrichment v2 (80°F→155%, 100°F→145%, 120°F→125%). From CTS 89.5°F: driver held ~56% throttle during cranking only, released within 1 s of fire, engine idled 850–990 RPM with zero throttle input and zero stalls — one continuous 785 s run segment over 13.3 min.
- Cold idle AFR error roughly halved vs log 008: +1.60 lean at 80–100°F (was +3 to +4), +0.80 at 100–120°F, +0.47 at 120–140°F, within ±0.15 above 140°F. Optionally add +5% at the 80–90°F cells; otherwise cold enrichment is calibrated.
- IAC pegged 100% below ~100°F (cannot reach cold idle target but idle is stable), stepped down to ~75% at 100–120°F, ~27% at 120–140°F, 23.8% at hot idle. Hot idle 1,089 RPM, AFR 12.96 vs 13.5 target, MAP 75.5 kPa. Warmup reached 160°F six minutes after start.
- **Rich at load**: at TPS>40%, AFR mean 11.59 vs target 13.66 (−2.07, dips to 9.6). Entire log open loop (CL Status 0 throughout) so nothing corrects it. Injector duty peaked at 32% — plenty of headroom. Warm engine confirmed healthy → time to enable closed loop per plan.
- **Clutch slip check inconclusive**: Speed channel is all zeros — no VSS wired to the Sniper, so direct RPM-vs-speed slip detection is impossible. Indirect evidence mildly suspicious: 3 flare-then-sag events (t≈485 s, 565 s, 600 s) where RPM surged 2,200–2,700 RPM/s for ~0.5 s at steady 36–51% TPS, then acceleration collapsed; at t≈485 s RPM fell ~700 while TPS held 46–51% and MAP steady ~82 kPa — classic slip-then-regrip signature, but low-gear acceleration in a light car plus hills can mimic it.
  - Definitive test without VSS: top gear at ~2,000 RPM, roll to full throttle and hold 3 s. If RPM jumps 800–1,000+ in the first second then sags, the clutch is slipping.
- **Cranking voltage worst yet: 7.53V** (7.86V in log 010, low 8s earlier). Charging healthy while running (13.8–14.5V). Battery/starter cable/ground needs attention — likely relevant to the hot-restart no-start captured in log 012.

### 012 — Hot-restart no-start (2026-07-03)

File: `logs/raw/012-hot-restart-no-start.csv`

- No sample exceeded the 400 RPM running threshold; the engine never caught.
- Battery recorded an 8.57V minimum at starter engagement. During samples with 50–400 RPM registered, voltage remained at or above 10.41V.
- Because the engine never ran, AFR and closed-loop channels cannot diagnose the cause. The file does not independently separate a brief electrical transient from hot-soak fueling or another restart issue.
- Conclusion: retain the battery/cable checks and capture dedicated 30-second and 5-minute heat-soak restart attempts after the next controlled drive.

### 013 — Cold drive with closed loop and learning active

File: `logs/raw/013-cold-drive-closed-loop-learning.csv`

- Clean start from 96°F after approximately 3 seconds of cranking with TPS near zero. The engine then ran continuously for 664.8 seconds and reached 193°F without overheating.
- Battery recorded one 7.95V sample at starter engagement, but sustained cranking voltage was much healthier at 10.76–11.22V. Running voltage averaged 14.29V. The electrical concern is improved but is not cleared, especially because no hot restart was attempted.
- Closed loop activated at t=18.15 seconds, only about 2 seconds after the engine fired and while CTS was still 96°F. It was active for 78% of the run and saturated at approximately +50% for 93 seconds during cold idle. This masked independent evaluation of the R2 coolant-enrichment curve.
- Learn remained inactive until approximately 160°F, then was active for 39% of the run. Visited cells showed `Current Learn` values from −16% to +37%. The table was already populated in earlier logs, so do not transfer this learned data into the base fuel table.
- Closed-loop cruise fueling was excellent: TPS 2–10% averaged 13.59 AFR against a 13.58 target. TPS 10–25% averaged 14.18 against 13.74 when closed loop was active.
- TPS>40% averaged 12.42 AFR against a 13.67 target, an improvement from approximately 11.62 in log 011 but still 1.25 AFR rich. The pulls were too short to separate acceleration enrichment from base-VE error. Closed loop removed as much as 20–27% fuel during some pulls, producing transient swings; do not edit the base table from this drive.
- Injector duty remained below 36%, leaving ample capacity.
- No sustained pull showed a clear flare-then-sag clutch-slip signature. Several pulls climbed smoothly past 4,000–5,000 RPM, weakening the suspicion from log 011. The conclusion remains non-definitive because Speed is still zero and a controlled top-gear test from approximately 2,000 RPM was not captured.
- End-of-log hot idle averaged approximately 1,060 RPM, 17% IAC, 74.7 kPa MAP, and 13.46 AFR against a 13.50 target. Leave the idle screw unchanged until fuel-control behavior is stabilized.
- No engine shutdown or restart occurred, so the hot-restart no-start remains unresolved.

## Temperature-bin summary

|   log_id | file                                              | cts_bin_f   |   rpm_avg |   iac_avg_pct |   map_avg_kpa |   afr_avg |   target_afr_avg |   coolant_enr_avg_pct |   afterstart_enr_avg_pct |
|---------:|:--------------------------------------------------|:------------|----------:|--------------:|--------------:|----------:|-----------------:|----------------------:|-------------------------:|
|        1 | 001-initial-cold-start-dies.csv                   | 80-100      |       788 |         100   |          79.8 |     15.99 |            12.57 |                 112.7 |                    118.6 |
|        2 | 002-header-gasket-cl-off-idle-screw-1turn.csv     | 80-100      |      1101 |          83.1 |          77.6 |     14.97 |            12.78 |                 110.8 |                    103.3 |
|        2 | 002-header-gasket-cl-off-idle-screw-1turn.csv     | 100-120     |      1085 |          54.9 |          77.5 |     14.19 |            12.85 |                 109.8 |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 100-120     |      1178 |          16   |          74.9 |     14.57 |            13.15 |                 106.3 |                    104.8 |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 120-130     |      1095 |           0   |          75.8 |     13.86 |            13.24 |                 105.3 |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 130-140     |      1122 |           0   |          75.6 |     13.39 |            13.37 |                 104.1 |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 140-150     |      1121 |           0   |          75.6 |     13.4  |            13.5  |                 102.2 |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 150-160     |      1134 |           0   |          75.5 |     13.39 |            13.5  |                 100.7 |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 160-180     |      1137 |           0   |          75.5 |     13.38 |            13.5  |                 100   |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 180-210     |      1139 |           0   |          75.6 |     13.03 |            13.5  |                 100   |                    100   |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              | 210-230     |      1139 |           0   |          75.8 |     12.86 |            13.5  |                 100   |                    100   |
|        4 | 004-iac-tuning-idle-screw-adjusted-hot-flare.csv  | 180-210     |      1278 |           3   |          71.9 |     13.6  |            13.52 |                 100   |                    100.3 |
|        5 | 005-hot-start-iac-35pct-short-cool-log.csv        | 120-130     |      1021 |         100   |          77.2 |     18.72 |            13.25 |                 105.3 |                    105.9 |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 120-130     |      1022 |          80.5 |          77.2 |     15.82 |            13.27 |                 105.1 |                    100.9 |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 130-140     |      1010 |          56   |          76.9 |     14.25 |            13.42 |                 103.7 |                    100   |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 140-150     |      1010 |          45.8 |          76.5 |     13.8  |            13.5  |                 102.4 |                    100   |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 150-160     |      1025 |          31.3 |          75.7 |     13.61 |            13.5  |                 100.7 |                    100   |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 160-180     |      1015 |          20.9 |          75.4 |     13.45 |            13.5  |                 100   |                    100   |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv | 180-210     |      1012 |          23.4 |          75.6 |     13.34 |            13.5  |                 100   |                    100.6 |
