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

## Current working conclusions

1. The original no-stay-running problem improved dramatically after header work, disabling closed loop, and opening the throttle blades.
2. After the idle screw was adjusted and TPS reset, hot idle was brought into a much better range.
3. A hot restart flare to ~3,071 rpm was caused by IAC Startup settings, not by the idle screw.
4. The revised hot IAC Startup settings worked: hot restart peak dropped to ~1,146 rpm.
5. Remaining issue is mainly warmup behavior around 120-135°F, where AFR looks lean and IAC is high, but the engine improves as it warms.
6. Because of the loppy cam and prior header leaks, AFR at idle should be treated as a tuning clue, not absolute truth.

## Latest suggested next step

Leave the hot-start IAC settings alone. Consider adding only a small coolant enrichment bump of +3% to +5% around 120-135°F, then re-log a full warmup. Reintroduce closed loop carefully only after idle and exhaust sealing are stable.
