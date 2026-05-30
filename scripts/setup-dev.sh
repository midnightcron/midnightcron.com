#!/usr/bin/env bash
# First-time dev setup for a new device (Linux / macOS). Idempotent.
#
# Usage: bash scripts/setup-dev.sh

set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Checking Python..."
if ! command -v python3 &>/dev/null; then
    echo "ERROR: python3 not found. Install Python 3.11+ first." >&2
    exit 1
fi
PYVER=$(python3 -c 'import sys; print(f"{sys.version_info[0]}.{sys.version_info[1]}")')
echo "    Python $PYVER"

MAJOR=$(echo "$PYVER" | cut -d. -f1)
MINOR=$(echo "$PYVER" | cut -d. -f2)
if [[ "$MAJOR" -lt 3 ]] || { [[ "$MAJOR" -eq 3 ]] && [[ "$MINOR" -lt 11 ]]; }; then
    echo "ERROR: Python 3.11+ required, found $PYVER" >&2
    exit 1
fi

echo "==> Checking uv..."
if ! command -v uv &>/dev/null; then
    echo "    uv not on PATH, installing via the official installer..."
    curl -fsSL https://astral.sh/uv/install.sh | sh
    if [[ -f "$HOME/.local/bin/uv" ]]; then
        export PATH="$HOME/.local/bin:$PATH"
    fi
fi
echo "    $(uv --version)"

echo "==> Installing project dependencies..."
uv sync

echo "==> Setting up .env..."
if [[ ! -f .env ]]; then
    cp .env.example .env
    echo "    Created .env from .env.example."
    echo "    Set TUNNEL_TOKEN before deploying (dev runs do not need it)."
else
    echo "    .env already exists, leaving it."
fi

echo
echo "==> Done."
echo "    Start the app with: uv run uvicorn app.main:app --reload"
echo "    Run tests with:     uv run pytest -q"
