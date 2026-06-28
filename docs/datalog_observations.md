# Datalog observations

These notes summarize the logs captured during the Sniper idle/startup tuning sequence.

## Summary metrics

|   log_id | file                                              |   duration_sec |   run_segments |   cts_min_run_f |   cts_max_run_f |   rpm_peak_running |   iac_end20_avg_pct |   rpm_end20_avg |   afr_end20_avg |   target_afr_end20_avg |   cl_comp_max_pct |   cl_status_max |
|---------:|:--------------------------------------------------|---------------:|---------------:|----------------:|----------------:|-------------------:|--------------------:|----------------:|----------------:|-----------------------:|------------------:|----------------:|
|        1 | 001-initial-cold-start-dies.csv                   |         35.928 |              1 |            89.1 |            89.3 |               1023 |               100   |             788 |           15.99 |                  12.57 |                50 |               1 |
|        2 | 002-header-gasket-cl-off-idle-screw-1turn.csv     |        136.998 |              1 |            95.5 |           102.5 |               1221 |                55   |            1085 |           14.19 |                  12.85 |                 0 |               0 |
|        3 | 003-cl-off-full-warmup-tps-reset.csv              |        359.388 |              1 |           118.2 |           212.7 |               2002 |                 0   |            1139 |           12.86 |                  13.5  |                 0 |               0 |
|        4 | 004-iac-tuning-idle-screw-adjusted-hot-flare.csv  |        115.722 |              1 |           184.4 |           209.8 |               3071 |                 6.1 |             980 |           13.2  |                  13.5  |                 0 |               0 |
|        5 | 005-hot-start-iac-35pct-short-cool-log.csv        |         26.448 |              1 |           124.6 |           124.8 |               1144 |               100   |            1021 |           18.72 |                  13.25 |                 0 |               0 |
|        6 | 006-full-warmup-hot-restart-after-iac-startup.csv |        429.478 |              2 |           124.3 |           201.3 |               1146 |                27.7 |            1056 |           13.31 |                  13.5  |                 0 |               0 |
|        7 | 007-full-warmup-vacuum-bleed-coolant-dead-cylinder.csv |        429.5 |              2 |           124.3 |           201.3 |               1093 |                19.5 |            1010 |           13.33 |                  13.5  |                 0 |               0 |

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
