#!/usr/bin/env bash
# Deploy midnightcron.com on the Pi. Idempotent.
#
# Usage (from any device on the tailnet):
#   tailscale ssh pi@rpi 'cd /home/pi/coding/midnightcron.com && ./scripts/deploy.sh'
#
# Or directly on the Pi:
#   cd /home/pi/coding/midnightcron.com && ./scripts/deploy.sh

set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Repo state before pull:"
git log -1 --oneline

echo "==> Fetching origin..."
git fetch origin

echo "==> Pulling main (fast-forward only)..."
git pull --ff-only origin main

echo "==> Rebuilding and starting containers..."
docker compose up -d --build

echo "==> Container status:"
docker compose ps

echo "==> Recent logs (last 30 lines):"
docker compose logs --tail=30

echo
echo "==> Deploy complete."
echo "    HEAD: $(git log -1 --oneline)"
echo "    Live at: https://midnightcron.com"
