# Next steps checklist

## IMMEDIATE — Mechanical repairs required before any EFI tuning (as of 2026-06-27)

Plugs pulled and inspected 2026-06-27. See `docs/inspections/2026-06-27_visual_inspection.md` for full notes and photos.

### What was found

- **Fuel gauge side** — plugs tan/normal. That side's repaired exhaust flanges are working. No action needed.
- **No gauge side** — all four plugs dark/fouled. The 2nd-from-left plug (cold header tube cylinder) is the worst. The two middle plugs are also heavily fouled, consistent with exhaust flange leaks on those cylinders.

### Fix sequence (do not skip steps or reorder)

1. **Replace all four plugs on the no-gauge side** with fresh plugs of correct heat range. Do not reinstall the fouled ones.
2. **Fix exhaust flange leaks on the no-gauge side** — same repair already completed on the fuel-gauge side center two cylinders. The two middle cylinders on this side are the primary suspects.
3. **Reinstall fresh plugs only after flanges are sealed** — new plugs into leaking flanges will re-foul immediately.
4. **Re-run full warmup log** and recheck with thermal camera. All four header tubes on both sides should heat evenly.
5. **Enable closed loop** only after step 4 confirms all cylinders firing cleanly.

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
