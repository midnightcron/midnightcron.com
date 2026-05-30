"""Shared Jinja2Templates instance with a static cache-buster."""

from pathlib import Path

from fastapi.templating import Jinja2Templates

_STATIC_DIR = Path("app/static")


def _static_version() -> str:
    # Captured at import time. Each deploy rebuilds the container, refreshing
    # the mtime and producing a new ?v= on the CSS link. Defeats Cloudflare's
    # default 4-hour edge cache on /static/*. See kicker CLAUDE.md for the
    # original incident.
    try:
        latest = max(
            (p.stat().st_mtime for p in _STATIC_DIR.rglob("*") if p.is_file()),
            default=0,
        )
        return str(int(latest))
    except OSError:
        return "0"


templates = Jinja2Templates(directory="app/templates")
templates.env.globals["static_version"] = _static_version()
