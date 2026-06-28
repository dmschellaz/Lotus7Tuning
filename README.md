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

1. **No-gauge side needs mechanical work** — plugs pulled 2026-06-27 and inspected. All four plugs on this side are fouled (dark/black). The 2nd-from-left plug (cold header tube cylinder) is the worst. Two middle cylinders suspected to have exhaust flange leaks matching the prior issue on the fuel-gauge side. See `docs/inspections/2026-06-27_visual_inspection.md`.
2. **Closed loop still off** — do not enable until mechanical repairs are complete and all cylinders confirmed firing on thermal camera.
3. **AFR data not trustworthy yet** — lean bias (+0.95 mean, spikes to +6.7) is a combination of the dead cylinder and exhaust leak air reaching the O2 sensor. Not a calibration issue.

## Immediate next step

1. Replace all four plugs on the no-gauge side with fresh plugs.
2. Fix exhaust flange leaks on the no-gauge side (same repair done on fuel-gauge side center two cylinders).
3. Reinstall plugs only after flanges are sealed.
4. Re-run full warmup log + thermal camera check — all 8 header tubes should be hot.
5. Enable closed loop and begin AFR-based tuning.
