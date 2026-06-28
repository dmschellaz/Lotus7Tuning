# Next steps checklist

## IMMEDIATE — Dead cylinder (as of 2026-06-27)

One header tube running at ambient temperature (~85.6°F on thermal camera vs all others pegged over max). Diagnose and fix before any further EFI tuning — lean AFR readings and rough idle will not be trustworthy until all four cylinders fire.

Diagnose in this order:

1. **Pull all four spark plugs** — compare condition. One will likely be black/wet (fouled from rich enrichment during cold starts). Replace fouled plug(s) with fresh plugs of correct heat range.
2. **Swap spark plug wire/coil** on the suspect cylinder with a known-good one — if the cold tube moves to a different cylinder, the wire/coil is the problem.
3. **Check injector** — with engine running, use a mechanic's stethoscope or long screwdriver to ear on each injector. Should hear rapid clicking. Silent injector = not firing.
4. **Compression test** — if spark and fuel are OK, do a wet/dry compression test. Low compression = mechanical issue (valve, ring).

The cold tube is on the passenger side. Identify which cylinder number it corresponds to before pulling plugs.

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
