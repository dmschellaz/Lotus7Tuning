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

1. **Dead cylinder** — one header tube cold on thermal camera. Likely a fouled spark plug from repeated cold-start rich enrichment. Diagnose in order: plug → wire/coil → injector → compression test.
2. **Closed loop still off** — AFR corrections are static. Mean AFR runs +0.95 lean at idle with CL disabled. Do not enable CL until the dead cylinder is fixed or CL will chase a phantom lean signal.
3. **Hot IAC slightly high** — settling around 19-20% above 160°F vs the 2-10% textbook target. Acceptable for now; recheck after CL is running.

## Immediate next step

1. Pull all four spark plugs, compare condition — the dead cylinder's plug will likely be fouled black/wet.
2. Replace bad plug(s), re-run a full warmup log, confirm all four header tubes heat evenly on thermal camera.
3. Once cylinder is confirmed healthy, enable closed loop above 160°F and log the AFR correction behavior.
4. Do not adjust base fuel, coolant enrichment, or IAC settings until after step 2 is complete.
