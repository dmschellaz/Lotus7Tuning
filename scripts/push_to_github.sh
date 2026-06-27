#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   1. Clone your repo somewhere local:
#      git clone https://github.com/dmschellaz/Lotus7Tuning.git
#   2. Copy this prepared folder's contents into the cloned repo root.
#   3. Run this script from inside the repo root:
#      bash scripts/push_to_github.sh

branch="efi-tuning-log-2026-06-27"

git checkout -b "$branch" || git checkout "$branch"
git add README.md docs logs scripts
git commit -m "Add Holley Sniper EFI tuning logs and observations"
git push -u origin "$branch"

echo "Pushed branch: $branch"
echo "Open a pull request on GitHub to merge into main."
