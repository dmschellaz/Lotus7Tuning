# Next steps checklist

## IMMEDIATE — controlled validation after log 013

Log 013 started cleanly from 96°F and cruised nearly on target, but closed loop engaged during cold warmup and saturated near +50% for approximately 93 seconds. Learn activated at 160°F against a previously populated table. Use the following procedure without making other tune changes.

### Before starting

1. Fully charge the battery. Check and tighten the battery terminals, engine-to-battery ground, Sniper power/ground connections, and starter cables.
2. Save the current ECU tune under a new dated filename. Photograph or export the existing Learn Table. **Do not transfer learned data to Base Fuel.**
3. Set:
   - Closed Loop: **Enabled**
   - Enable Minimum CTS: **Enabled**
   - Minimum CTS: **160°F**
   - Learn: **Disabled**
   - Closed Loop Limit: **±10%**
   - Closed Loop Speed: **leave unchanged**
4. Do not clear the existing Learn Table yet. Disabling Learn freezes it; clearing it could produce a large immediate fuel change.
5. Leave coolant enrichment, IAC, idle screw, Base Fuel, acceleration enrichment, and Target AFR unchanged.

### Cold start and warmup

1. Start the datalog before touching the key.
2. Turn the key on and wait at least 2.5 seconds for the fuel-prime event. Do not pump the throttle.
3. Start normally and avoid touching the throttle unless the engine is about to stall.
4. Let the engine idle without assistance to 160°F. Record cranking voltage, first-attempt success, IAC, AFR versus Target AFR, and any stumble or stall.
5. At 160°F, confirm Closed Loop becomes active while Learn remains `NoLearn`. Remain parked for 60–90 seconds. Desired result: stable RPM and AFR, with CL Comp generally inside ±5–10% rather than pinned at the limit.

### Road portion

1. Drive gently for approximately five minutes, mainly at 1,800–2,800 RPM and light throttle. Capture several steady 10–15 second cruise periods.
2. Perform two moderate-load tests: begin near 2,000 RPM in third or top gear, smoothly apply 25–35% throttle, hold 4–5 seconds, then allow at least 20 seconds before repeating.
3. If AFR and engine behavior remain stable, perform two stronger tests: begin near 2,000–2,500 RPM, smoothly apply 50–60% throttle, and hold 3 seconds.
4. Do not use full throttle yet. First review the Target AFR table and the moderate-load data.
5. For the clutch check, compare engine sound/RPM with vehicle acceleration during the higher-gear tests. RPM suddenly rising without matching acceleration suggests slip. Lift immediately if this occurs. A VSS signal is still required for a definitive log-based diagnosis.
6. Do not watch the handheld while driving; use a passenger or review the log afterward.

### Stop conditions

Lift immediately for audible detonation, severe misfire, fuel smell, loss of power, running voltage below approximately 12.5V, coolant above 210°F and continuing upward, AFR above approximately 14.5 for more than one second under significant load, or AFR below approximately 10.5 with bogging.

### Hot-restart tests

1. Return with coolant at or above 185°F and idle for 30 seconds.
2. Shut down for 30 seconds, then make one normal restart attempt while logging.
3. If successful, run another 30–60 seconds, shut down for five minutes, and make one more logged restart attempt.
4. If a restart fails, stop after one approximately five-second crank attempt. Do not repeatedly cycle the key because each prime event can add fuel. Record the battery minimum and whether RPM continued registering.
5. Save the drive and each hot-restart attempt separately, then export a fresh post-drive tune.

## PREVIOUS — Cold idle enrichment (as of 2026-06-28, resolved by v2 changes; verified in logs 010–011)

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

## Historical plan after the dead cylinder repair

1. Re-run a full warmup log to confirm AFR lean spikes are gone.
2. Enable closed loop — at 197°F the engine should absolutely be in CL. AFR mean error was +0.95 lean open-loop; CL will self-correct this.
3. Consider +3% to +5% coolant enrichment at 120-135°F only if idle still sounds lean/weak after CL is on.
4. Leave the IAC hot-start settings unchanged — the excessive RPM flare was fixed. The later hot-restart no-start in log 012 is a separate unresolved problem.

## Historical closed-loop reintroduction plan

Do not enable closed loop until the dead cylinder is fixed — CL will try to compensate for a misfiring cylinder by adding global fuel, masking the real problem.

Once cylinder is healthy:

- Enable closed loop above 160°F first, verify CL Comp stays within ±10% at idle.
- If CL Comp pegs high positive immediately, re-check for remaining exhaust leak or wrong idle AFR target cells.
- Start with conservative learn authority.

## Items to keep watching

- Cranking voltage has dipped into the low 8V range in several logs. The engine starts, but EFI power/ground/starter cables/battery should be checked.
- MAP at idle: 76.5 kPa (~7.3 inHg vacuum). Low, but consistent with aggressive cam. Recheck after cylinder fix — a misfiring cylinder artificially lowers manifold vacuum.
- Hot idle IAC target from the manual is generally 2-10% above 160°F; current 19-20% is slightly high but acceptable until CL is running.

## Do not change during the next validation drive

- Do not edit Base Fuel from log 013; the higher-load events were too short to separate acceleration enrichment from steady-state VE error.
- Do not transfer the current Learn Table into Base Fuel; it contains modifiers gathered across different mechanical and tuning states.
- Do not chase hot-start IAC settings; the former RPM flare is fixed, while the no-start needs a dedicated heat-soak log.
- Do not lower idle speed aggressively; this engine may prefer roughly 950-1,000 rpm.
