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

## Current status — after log 013

**Cold start and normal cruise are working. Closed-loop gating, stale learn data, hot restart, and controlled load testing are next.**

Log 013 started cleanly from 96°F with no throttle and ran continuously to 193°F. Closed-loop cruise fueling was essentially on target, but closed loop also operated during cold warmup and remained near +50% correction for about 93 seconds. Learning activated above 160°F against a previously populated Learn Table. Freeze learning and gate closed loop at 160°F for the next controlled validation drive.

## What has been solved

| Issue | Status |
|---|---|
| Engine wouldn't stay running | Fixed — header work + idle screw + TPS reset |
| Hot restart RPM flare to 3,071 rpm | Fixed — IAC startup position set to 35%, hold 1s, decay 3s |
| Rapid overheating | Fixed — coolant system vacuum-bled 2026-06-27 |
| Hot restart RPM flare | Fixed — fires without the former 3,071 rpm flare when it starts |
| IAC warmup curve | Working — steps down correctly from 100% cold to ~25% at 160°F |
| Dead cylinder (passenger side) | Fixed 2026-06-28 — new plugs + exhaust flange repair, zero misfire warm |
| Cold idle stall (80–130°F) | Fixed 2026-06-29 — coolant enrichment increased to 155%/145%/125% at 80/100/120°F |

## Current known issues

1. **Hot restart no-start** — log 012 captured a failed hot restart; log 013 did not retest it.
2. **Closed loop active too early** — in log 013 it activated at 96°F and saturated near +50% during cold warmup.
3. **Stale/large Learn Table modifiers** — observed values span approximately −16% to +37%; do not transfer them to Base Fuel.
4. **High-load transient fueling** — TPS>40% averaged 12.42 AFR against a 13.67 target, but the pulls were too short to distinguish acceleration enrichment from base VE.
5. **Cranking voltage** — log 013 recorded one 7.95V starter-engagement sample, although sustained cranking improved to 10.76–11.22V.

## Immediate next steps

1. Save a fresh tune and preserve the existing Learn Table without transferring it.
2. Enable the Closed Loop minimum CTS gate at 160°F; set the Closed Loop Limit to ±10% for validation and disable Learn.
3. Run the structured cold-start, cruise, moderate-load, and hot-restart procedure in `docs/next_steps.md`.
4. Leave coolant enrichment, IAC, idle screw, base fuel, acceleration enrichment, and target AFR unchanged during this test.
