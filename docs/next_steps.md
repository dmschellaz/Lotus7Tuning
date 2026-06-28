# Next steps checklist

## IMMEDIATE — Cold idle enrichment (as of 2026-06-28)

Mechanical repairs complete (log 008, 2026-06-28). New plugs installed, exhaust leaks fixed on no-gauge side. Engine confirmed mechanically healthy when warm — zero misfire events above 160°F, AFR within +0.06 of target. Hot restart IAC working correctly.

**One remaining issue: cold idle runs lean from 90–130°F.**

The coolant enrichment table does not add enough fuel when the engine is cold. The engine stalls on first start attempt and needs driver throttle blips to survive until ~130°F.

### AFR deficit at cold temps (from log 008)

| Temp | AFR error | Action needed |
|---|---|---|
| 80–100°F | ~+3 to +4 lean | Large enrichment increase needed |
| 100–120°F | +2.39 lean | Large increase needed |
| 120–140°F | +1.28 lean | Moderate increase needed |
| 140–160°F | +0.53 lean | Small increase or leave for CL |
| 160°F+ | +0.06 lean | Leave alone — working perfectly |

### What to change

In the Holley Sniper software, increase **Coolant Enrichment** at the 80°F, 90°F, 100°F, 110°F, and 120°F cells. Start with +15% at 80°F tapering to +5% at 120°F, then re-log a cold start from below 100°F.

Do not touch anything above 140°F — that range is calibrated correctly.

## After dead cylinder is fixed

1. Re-run a full warmup log to confirm AFR lean spikes are gone.
2. Enable closed loop — at 197°F the engine should absolutely be in CL. AFR mean error was +0.95 lean open-loop; CL will self-correct this.
3. Consider +3% to +5% coolant enrichment at 120-135°F only if idle still sounds lean/weak after CL is on.
4. Leave all IAC and hot-start settings unchanged — they are working correctly.

## Closed loop reintroduction plan

Do not enable closed loop until the dead cylinder is fixed — CL will try to compensate for a misfiring cylinder by adding global fuel, masking the real problem.

Once cylinder is healthy:

- Enable closed loop above 160°F first, verify CL Comp stays within ±10% at idle.
- If CL Comp pegs high positive immediately, re-check for remaining exhaust leak or wrong idle AFR target cells.
- Start with conservative learn authority.

## Items to keep watching

- Cranking voltage has dipped into the low 8V range in several logs. The engine starts, but EFI power/ground/starter cables/battery should be checked.
- MAP at idle: 76.5 kPa (~7.3 inHg vacuum). Low, but consistent with aggressive cam. Recheck after cylinder fix — a misfiring cylinder artificially lowers manifold vacuum.
- Hot idle IAC target from the manual is generally 2-10% above 160°F; current 19-20% is slightly high but acceptable until CL is running.

## Do not change yet

- Do not change base fuel table based on current lean AFR readings — they are caused by the dead cylinder, not a calibration error.
- Do not chase hot-start IAC settings — hot restart is confirmed fixed.
- Do not lower idle speed aggressively; this engine may prefer roughly 950-1,000 rpm.
