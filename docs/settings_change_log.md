# Settings and change log

## Baseline mechanical notes

- Engine: 300 cid V8 with loppy cam.
- Known issue at beginning: slight exhaust leaks at header-to-head connection.
- Fuel pressure measured at Sniper unit: ~60 psi at key-on, then ~52 psi after pump stops.
- Because of loppy cam and prior header leaks, idle AFR readings can be falsely lean.

## Change sequence

### Change 1 — Header leak improvement + closed loop off + idle screw opened

Before log: `002-header-gasket-cl-off-idle-screw-1turn.csv`

- Tightened/replaced header gasket.
- Disabled closed loop.
- Turned idle screw 1 full turn clockwise.

Observed result:

- Engine stayed running instead of dying.
- IAC came down compared with the original log but was still high.
- TPS no longer read 0, so TPS reset/autoset was required.

### Change 2 — TPS reset

Before log: `003-cl-off-full-warmup-tps-reset.csv`

- TPS reset/autoset completed.

Observed result:

- TPS returned near zero.
- Engine fully warmed up and stayed running.
- Hot IAC fell to 0%, so the throttle blades were too far open.

### Change 3 — Idle screw closed to bring hot IAC into range

Before log: `004-iac-tuning-idle-screw-adjusted-hot-flare.csv`

- Idle screw adjusted while watching IAC.
- Goal: hot idle IAC approximately 2-10% above 160°F.

Observed result:

- Hot idle baseline improved: IAC around 6-8%, RPM around 980, TPS near zero.
- Hot restart flared to ~3,071 rpm, showing IAC Startup settings were too aggressive.

### Change 4 — IAC Startup hot settings reduced

Before log: `005-hot-start-iac-35pct-short-cool-log.csv` and retained for `006-full-warmup-hot-restart-after-iac-startup.csv`

- IAC Startup Hold Time: 1 sec.
- IAC Startup Decay Time: 3 sec.
- IAC Parked Position at 160°F+ moved to 35% across the hot row.

Observed result:

- Hot restart no longer flares violently.
- In the full warmup/hot-restart log, hot restart peak was ~1,146 rpm.

### Change 5 — Coolant enrichment first increase (2026-06-29)

Before log: `009-cold-start-enrichment-v1-stall.csv`

- Coolant enrichment table adjusted: 80°F 115%→130%, 100°F 110%→120%, 120°F 106%→111%.

Observed result:

- Engine fired and ran at 850–950 RPM for ~20 seconds then stalled.
- AFR mean +4.30 lean (16.94 vs target 12.65). IAC pegged at 100%.
- Enrichment improved from baseline but still far short. Battery dropped to 10.82V cranking.

### Change 6 — Coolant enrichment second increase (2026-06-29)

Before log: `010-cold-warmup-enrichment-v2-full-success.csv`

- Coolant enrichment table adjusted: 80°F 130%→155%, 100°F 120%→145%, 120°F 111%→125%.

Observed result:

- Engine ran full warmup 95°F→161°F without stalling and without throttle input. First successful unassisted cold start.
- AFR mean error +0.91 lean across entire run (open loop). At 160°F+: +0.03 lean — effectively on target.
- IAC stepped down from 100% at cold to 25% at 160°F — warmup curve working correctly.
- Battery dropped to 7.86V during cranking — flagged as a concern.

Tune snapshot: `Tunes/062926_R2_CoolantTempEnrichment.sniper` (Sniper software 2.0 Build 15, saved 2026-06-29 at 17:46:55). The matching `.info.txt` metadata file is retained beside it.

### Runtime state observed in log 013

These are observations from the datalog, not confirmed changes stored in the June 29 tune snapshot:

- Closed loop was enabled without a minimum coolant-temperature gate and became active at 96°F.
- Closed-loop compensation reached its +50% ceiling during cold idle.
- Learn became active once coolant enrichment reached 100% at approximately 160°F.
- The existing Learn Table contains large, old modifiers and must not be transferred to the base fuel table from this drive.

## Current working settings to preserve

- Coolant enrichment: 80°F=155%, 100°F=145%, 120°F=125%, 140°F+=leave alone.
- Hot IAC Startup Parked Position: 35% at 160°F+.
- IAC Startup Hold Time: 1 sec.
- IAC Startup Decay Time: 3 sec.
- Hot idle screw position: unchanged from log 004/006.
- Target idle AFR: 13.5.

## Candidate next changes after log 013

In priority order:

1. Save a fresh pre-test tune and preserve the existing Learn Table; do not transfer it into Base Fuel.
2. Keep Closed Loop enabled, enable its minimum CTS gate at 160°F, and use a conservative ±10% Closed Loop Limit for the validation drive. Leave Closed Loop Speed unchanged.
3. Disable Learn for the validation drive so the existing table is frozen. Do not clear it yet because removing the applied modifiers could create a large immediate fuel change.
4. Leave coolant enrichment, IAC settings, idle screw, base fuel, acceleration enrichment, and target AFR unchanged for this test.
5. Review the high-load Target AFR table before attempting full throttle or leaning high-load fuel cells. The recorded target of roughly 13.5–14.0 AFR at 80–86 kPa and 3,500–5,200 RPM should be an intentional choice, not accepted blindly.
