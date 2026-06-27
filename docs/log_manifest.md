# Log manifest

| ID | Repo filename | Original source filename | Test context |
|---:|---|---|---|
| 1 | `001-initial-cold-start-dies.csv` | `sniper_0170.V4.csv` | Initial cold/warm start attempt: starts, idles briefly, then dies; closed loop active; IAC pinned 100%; CL Comp reaches +50%. |
| 2 | `002-header-gasket-cl-off-idle-screw-1turn.csv` | `sniper_0172.V4.csv` | After tightening/replacing header gasket, closed loop disabled, idle screw turned 1 full turn clockwise. Engine stays running; IAC improved but still high; TPS needed reset. |
| 3 | `003-cl-off-full-warmup-tps-reset.csv` | `3 CL off, full warm up.csv` | Full warmup after TPS reset. Hot IAC ended at 0%, showing throttle blades too far open; recommended closing idle screw slightly. |
| 4 | `004-iac-tuning-idle-screw-adjusted-hot-flare.csv` | `4 IAC tuning idle screw adj.csv` | Idle screw adjusted to get hot IAC in range; hot restart flared to ~3,071 rpm due to IAC Startup settings. |
| 5 | `005-hot-start-iac-35pct-short-cool-log.csv` | `5 IAC tuning hot start delays 35 perc.csv` | After IAC Startup changes: hot 160°F+ parked row moved to 35%, hold 1 sec, decay 3 sec. Test was only ~125°F, so 160°F row likely inactive; IAC 100%, AFR lean-looking. |
| 6 | `006-full-warmup-hot-restart-after-iac-startup.csv` | `6 IAC full warmup, no changes.csv` | Full warmup plus hot restart after IAC Startup changes. Hot restart no longer flares; warmup AFR lean-looking only below ~135-140°F. |
