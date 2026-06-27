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

## Current working settings to preserve

- Closed loop: off for baseline idle/startup testing.
- Hot IAC Startup Parked Position: 35% at 160°F+.
- IAC Startup Hold Time: 1 sec.
- IAC Startup Decay Time: 3 sec.
- Hot idle screw position: keep where log 004/006 had it unless hot IAC remains consistently above ~15-20% after fully heat-soaked.
- Target idle AFR: 13.5 is reasonable for now.

## Candidate next change

Only if the next cold/warm start still sounds weak/lean below ~135°F:

- Add +3% to +5% coolant enrichment around 120-135°F.
- Do not change base fuel and coolant enrichment at the same time.
- Do not change hot IAC Startup settings unless hot restart flare returns.
