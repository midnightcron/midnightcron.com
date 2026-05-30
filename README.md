# midnightcron.com

Personal site and project hub. FastAPI + Jinja2 + Pico.css, deployed on a
Raspberry Pi 4 behind a Cloudflare Tunnel.

Live at https://midnightcron.com.

## Stack

- **Backend**: FastAPI, Jinja2
- **Styling**: Pico.css (dark) + custom monospace overlay (`app/static/css/site.css`)
- **Edge**: Caddy reverse proxy + Cloudflare Tunnel
- **Runtime**: Docker Compose on a Raspberry Pi
- **Deps**: managed by [uv](https://docs.astral.sh/uv/)

## Routes

| Path                | Description                          |
| ------------------- | ------------------------------------ |
| `/`                 | Landing: short intro + projects grid |
| `/about`            | Longer-form about page               |
| `/projects/<slug>`  | Per-project writeup                  |
| `/health`           | Liveness check                       |

All project content lives in [`app/projects.py`](app/projects.py). Adding
a project: append a `Project` dict, drop a writeup paragraph into the
`story` field, push.

## First-time setup on a new device

Linux / macOS:

```
git clone git@github.com:midnightcron/midnightcron.com.git
cd midnightcron.com
bash scripts/setup-dev.sh
```

Windows:

```powershell
git clone git@github.com:midnightcron/midnightcron.com.git
cd midnightcron.com
.\scripts\setup-dev.ps1
```

Then:

```
uv run uvicorn app.main:app --reload   # http://localhost:8000
uv run pytest -q                       # tests
uv run ruff check .                    # lint
```

## Before launch checklist

- [ ] Replace the LinkedIn URL placeholder in `app/templates/base.html`
- [ ] Fill the day-job sentence in `app/templates/about.html`
- [ ] Create the GitHub repo `midnightcron/midnightcron.com` and push
- [ ] Set up the Cloudflare Tunnel route: `midnightcron.com` &rarr; Pi `:80`
- [ ] Set `TUNNEL_TOKEN` in `.env` on the Pi
- [ ] `./scripts/deploy.sh` on the Pi

## Deploy

```
tailscale ssh pi@rpi 'cd /home/pi/coding/midnightcron.com && ./scripts/deploy.sh'
```

Idempotent. Re-running is safe.

## Adding a new project

1. Append a dict to `PROJECTS` in `app/projects.py`.
2. Pick a unique `slug` (used in the URL).
3. Set `status` to one of `live`, `migrating`, `wip`, `archived`.
4. Commit + push + deploy.

No template or CSS changes needed for routine additions.
