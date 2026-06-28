# Visual Inspection — 2026-06-27

## Spark plugs

All 8 plugs pulled and placed in holder on top of engine, tips facing up. Photos in this folder.

### Fuel gauge side (center two exhaust leaks previously repaired)

File: `2026-06-27_plugs_fuel-gauge-side.heic`

- All four plugs show tan/light brown ceramic tips — normal firing color.
- Consistent with the repaired exhaust flanges on this side; cylinders have been burning cleanly.
- No action needed on these plugs.

### No fuel gauge side (exhaust leaks unrepaired; dead cylinder 2nd from left)

File: `2026-06-27_plugs_no-gauge-side.heic`

- All four plugs noticeably darker than the fuel-gauge side — grey/black ceramics.
- The two middle plugs are especially dark, consistent with the suspected exhaust flange leaks on those cylinders (leak air causes incomplete combustion and accelerated fouling).
- The 2nd-from-left plug (cold header tube cylinder) appears the most fouled — consistent with a cylinder that has not been firing at all, accumulating deposits from unburned fuel/oil with no combustion heat to clean it.

## Thermal camera findings (from earlier in this session)

- No-gauge side, 2nd-from-left header tube: ~85.6°F (ambient) while all other tubes pegged over camera max.
- Confirms that cylinder is not contributing combustion — not a partial miss, not an exhaust leak making it look cold. Genuinely not firing.
- Two middle cylinders on this side suspected to have exhaust flange leaks based on plug condition and prior history on the other side.

## Diagnosis

The contrast between the two sides is clear: the side with repaired flanges has clean plugs; the side with unrepaired flanges has fouled plugs. The dead cylinder's plug is the worst of the group.

The sustained AFR lean bias (+0.95 mean, spikes to +6.7) seen in log 007 is likely a combination of:
1. Dead cylinder (2nd from left, no-gauge side) sending unburned air past the O2 sensor
2. Exhaust flange leaks on the two middle cylinders of the same side pulling ambient air into the exhaust stream

## Action required

1. Replace all four plugs on the no-gauge side — do not reinstall the fouled ones.
2. Fix exhaust flange leaks on the no-gauge side middle two cylinders (same repair already done on fuel-gauge side center two).
3. Reinstall fresh plugs only after flanges are sealed — putting new plugs into leaking flanges will re-foul them.
4. Re-run full warmup log and recheck with thermal camera to confirm all four tubes heat evenly.
5. Only after all of the above: enable closed loop and begin AFR-based tuning.
