# Log manifest

| ID | Repo filename | Original source filename | Test context |
|---:|---|---|---|
| 1 | `001-initial-cold-start-dies.csv` | `sniper_0170.V4.csv` | Initial cold/warm start attempt: starts, idles briefly, then dies; closed loop active; IAC pinned 100%; CL Comp reaches +50%. |
| 2 | `002-header-gasket-cl-off-idle-screw-1turn.csv` | `sniper_0172.V4.csv` | After tightening/replacing header gasket, closed loop disabled, idle screw turned 1 full turn clockwise. Engine stays running; IAC improved but still high; TPS needed reset. |
| 3 | `003-cl-off-full-warmup-tps-reset.csv` | `3 CL off, full warm up.csv` | Full warmup after TPS reset. Hot IAC ended at 0%, showing throttle blades too far open; recommended closing idle screw slightly. |
| 4 | `004-iac-tuning-idle-screw-adjusted-hot-flare.csv` | `4 IAC tuning idle screw adj.csv` | Idle screw adjusted to get hot IAC in range; hot restart flared to ~3,071 rpm due to IAC Startup settings. |
| 5 | `005-hot-start-iac-35pct-short-cool-log.csv` | `5 IAC tuning hot start delays 35 perc.csv` | After IAC Startup changes: hot 160°F+ parked row moved to 35%, hold 1 sec, decay 3 sec. Test was only ~125°F, so 160°F row likely inactive; IAC 100%, AFR lean-looking. |
| 6 | `006-full-warmup-hot-restart-after-iac-startup.csv` | `6 IAC full warmup, no changes.csv` | Full warmup plus hot restart after IAC Startup changes. Hot restart no longer flares; warmup AFR lean-looking only below ~135-140°F. |
| 7 | `007-full-warmup-vacuum-bleed-coolant-dead-cylinder.csv` | — | Full warmup after coolant vacuum bleed. Required throttle blips to stay alive cold. Dead cylinder identified via thermal camera (passenger-side tube at ambient temp). IAC and hot restart confirmed working. |
| 8 | `008-cold-warmup-new-plugs-fixed-exhaust-leaks.csv` | — | First cold start from 90°F after replacing no-gauge-side spark plugs and fixing exhaust flange leaks. Dead cylinder confirmed fixed — zero misfire events above 160°F, AFR +0.06 of target. Cold idle lean condition (90–130°F) identified as sole remaining issue. |
| 9 | `009-cold-start-enrichment-v1-stall.csv` | `1_tuneadjustcoolantenrichment.csv` | First attempt with enrichment increase (80°F→130%, 100°F→120%, 120°F→111%). Engine fired and ran 20s at 850–950 RPM then stalled. AFR mean +4.30 lean. IAC pegged 100%. Battery dropped to 10.82V. Enrichment still insufficient. |
| 10 | `010-cold-warmup-enrichment-v2-full-success.csv` | `2_tuneadjustcoolantenrichment.csv` | Second attempt with enrichment increased further (80°F→155%, 100°F→145%, 120°F→125%). Engine ran full warmup 95→161°F without stalling and without throttle input. AFR mean +0.91 lean; +0.03 at 160°F+. IAC stepped down correctly from 100% to 25% at 160°F. Battery dropped to 7.86V cranking — flagged for attention. |
