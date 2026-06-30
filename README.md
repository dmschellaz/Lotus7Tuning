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

## Current status — 2026-06-29

**Cold start is working. Fine-tuning and closed loop enablement are next.**

First successful unassisted cold start confirmed in log 010 (2026-06-29): engine ran from 95°F to 161°F without stalling and without any throttle input. AFR mean error +0.91 lean open-loop; +0.03 lean at 160°F+. The engine is in good shape. Battery voltage dropped to 7.86V during cranking and needs attention before the next session.

## What has been solved

| Issue | Status |
|---|---|
| Engine wouldn't stay running | Fixed — header work + idle screw + TPS reset |
| Hot restart RPM flare to 3,071 rpm | Fixed — IAC startup position set to 35%, hold 1s, decay 3s |
| Rapid overheating | Fixed — coolant system vacuum-bled 2026-06-27 |
| Hot restart behavior | Confirmed good — fires immediately, stable RPM, AFR on target within 5s |
| IAC warmup curve | Working — steps down correctly from 100% cold to ~25% at 160°F |
| Dead cylinder (passenger side) | Fixed 2026-06-28 — new plugs + exhaust flange repair, zero misfire warm |
| Cold idle stall (80–130°F) | Fixed 2026-06-29 — coolant enrichment increased to 155%/145%/125% at 80/100/120°F |

## Current known issues

1. **Battery voltage low during cranking** — dropped to 7.86V in log 010. Check battery health, charge fully, and load test before next session. Low cranking voltage starves injector solenoids and may be contributing to the remaining cold lean condition.
2. **Cold zone still slightly lean (95–120°F)** — AFR runs +1.0 to +1.8 lean in this range open-loop. A small additional enrichment increase (80°F→160%, 100°F→150%) may help after battery is confirmed healthy.
3. **Closed loop still off** — hot zone is calibrated (+0.03 at 160°F+). Enable CL above 140°F once battery is confirmed good; it will self-correct the remaining lean offset in the 130–145°F zone.

## Immediate next steps

1. **Fix the battery first** — charge fully and load test. Do not tune against a weak battery.
2. **Enable closed loop above 140°F** — the hot zone is dialed in; CL will handle residual lean offset without further table changes.
3. **Optional enrichment fine-tune** — if 95–120°F zone still runs lean after CL is on, increase 80°F→160%, 100°F→150%.
4. Do not touch IAC, idle screw, or any coolant enrichment cells above 140°F — those are working correctly.
