# Lotus7Tuning

Holley Sniper EFI tuning journal for the Lotus 7 / 300 cid V8 setup.

This repo folder was prepared on 2026-06-27 from the datalogs and setting-change notes captured during startup and idle tuning.

## Vehicle / EFI context

- Engine: 300 cubic inch V8
- Cam: loppy / low-vacuum idle behavior
- EFI: Holley Sniper EFI 4150-style setup
- Fuel pressure note: gauge at Sniper unit showed ~60 psi key-on, dropping to ~52 psi after pump stops
- Exhaust note: header-to-head leaks were present initially; gasket was replaced/tightened during this tuning session
- Tuning approach during these logs: closed loop disabled for baseline idle and startup testing

## Manual references used

- Holley Sniper EFI manual: https://documents.holley.com/techlibrary_199r11031r-1.pdf
- Holley Sniper troubleshooting guide: https://documents.holley.com/199r11369.pdf

## Folder structure

```text
logs/raw/                Raw Holley CSV datalogs, renamed in sequence
logs/summaries/          Generated metric summaries from the raw logs
docs/                    Tuning notes, observations, settings history, next steps
scripts/                 Helper script to regenerate summary CSVs
```

## Current status — 2026-06-27

**Blocked on mechanical: dead cylinder identified. Do not change EFI settings until resolved.**

Thermal camera inspection showed one passenger-side header tube running at ambient temperature (~85°F) while all others were pegged hot. That means one cylinder is not contributing combustion at all. This explains the lean AFR spikes (up to +6.7 AFR), the rough idle, and the need to blip the throttle to keep it alive during warm-up.

## What has been solved

| Issue | Status |
|---|---|
| Engine wouldn't stay running | Fixed — header work + idle screw + TPS reset |
| Hot restart RPM flare to 3,071 rpm | Fixed — IAC startup position set to 35%, hold 1s, decay 3s |
| Rapid overheating | Fixed — coolant system vacuum-bled 2026-06-27 |
| Hot restart behavior | Confirmed good — fires immediately, stable RPM, AFR on target within 5s |
| IAC warmup curve | Working — steps down correctly 71% → 19% as temps rise 120°F → 200°F |

## Current known issues

1. **Cold idle runs lean (80–130°F)** — engine stalls on first cold start attempt and needs throttle blips to survive until ~130°F. Coolant enrichment table needs +15% at 80°F tapering to +5% at 120°F. Above 140°F the engine is calibrated correctly and runs well.
2. **Closed loop still off** — enable after cold enrichment is fixed and a clean cold start log is confirmed.

## What was fixed (2026-06-28)

- Replaced all four spark plugs on the no-gauge side
- Fixed exhaust flange leaks on the no-gauge side
- **Result**: zero misfire events when warm, AFR +0.06 of target at 160°F+, hot restart clean at ~1,080 RPM

## Immediate next step

1. Increase coolant enrichment in the Holley Sniper software at 80–120°F cells (+15% at 80°F, taper to +5% at 120°F as a starting point).
2. Cold start from below 100°F and log a full warmup — engine should hold idle without throttle blips.
3. Enable closed loop once cold start is clean.
4. Do not touch IAC, idle screw, or any settings above 140°F — those are working correctly.
