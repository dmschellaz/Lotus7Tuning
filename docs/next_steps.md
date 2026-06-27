# Next steps checklist

## Immediate next test

1. Leave hot IAC Startup settings unchanged:
   - 160°F+ IAC parked position: 35%.
   - Startup hold: 1 sec.
   - Startup decay: 3 sec.
2. Leave idle screw alone unless fully heat-soaked hot IAC remains above ~15-20%.
3. Consider adding +3% to +5% coolant enrichment around 120-135°F if the next warm start sounds lean or weak.
4. Run another full warmup log from the coolest available starting temperature.
5. Note subjective symptoms during the log:
   - Lean popping / weak idle / stumble.
   - Rich smell / eye burn / loading up.
   - RPM flare or stall.
   - Exhaust leak sound.

## Closed loop reintroduction plan

Do not let closed loop immediately control the questionable idle area until exhaust sealing and base idle are reliable.

Options to test later:

- Enable closed loop only above 160°F.
- Consider open-loop below idle/low RPM if the loppy cam creates false lean readings.
- Start with conservative learn settings.
- Watch CL Comp: if it immediately pegs high positive at idle, suspect false lean, exhaust leak, or wrong idle cells before accepting the correction.

## Items to keep watching

- Cranking voltage has dipped into the low 8V range in several logs. The engine starts, but EFI power/ground/starter cables/battery should be checked.
- MAP at idle remains around 75-78 kPa, consistent with a loppy low-vacuum idle but still worth checking for vacuum leaks.
- Header sealing remains important before trusting idle AFR fully.
- Hot idle IAC target from the manual is generally 2-10% above 160°F, but a loppy cam may not be perfectly textbook.

## Do not change yet

- Do not add large amounts of base fuel based only on brief 18-20 AFR readings at idle.
- Do not chase hot-start IAC settings further unless the hot flare returns.
- Do not lower idle speed aggressively; this engine may prefer roughly 950-1,000 rpm.
