"""Project metadata for the landing grid and detail pages.

One dict per project. Order in PROJECTS is the display order on the landing page.
status values: live, migrating, wip, archived.
"""

from typing import Literal, TypedDict


class Project(TypedDict):
    slug: str
    name: str
    tagline: str
    description: str
    stack: list[str]
    status: Literal["live", "migrating", "wip", "archived"]
    live_url: str | None
    repo_url: str | None
    story: str


PROJECTS: list[Project] = [
    {
        "slug": "badi-monitor",
        "name": "Badi Monitor",
        "tagline": "Real-time occupancy for two Zürich indoor pools, with quietest-time predictions.",
        "description": (
            "Monitors Hallenbad Oerlikon and Hallenbad City through the CrowdMonitor "
            "WebSocket feed. Surfaces a mobile-first dashboard with 'best time today' "
            "and 'quietest in the next 7 days' recommendations driven by historical patterns."
        ),
        "stack": ["Python", "FastAPI", "TimescaleDB", "Docker", "Cloudflare Tunnel"],
        "status": "live",
        "live_url": "https://badi.midnightcron.com",
        "repo_url": "https://github.com/midnightcron/badi_attendance",
        "story": (
            "Started on Azure (ACI collector, Function App API, Table Storage). "
            "Migrated to a self-hosted Raspberry Pi stack running PostgreSQL with "
            "TimescaleDB to cut the monthly Azure bill and consolidate everything "
            "under a single host. Continuous aggregates drive the dashboard reads; "
            "a nightly job rebuilds the per-weekday slot averages that feed the "
            "recommendation cards."
        ),
    },
    {
        "slug": "kicker",
        "name": "Kicker",
        "tagline": "Office foosball 2v2 ELO tracker.",
        "description": (
            "Match entry, leaderboards, rating history, and season resets for a 2v2 "
            "foosball ladder. Built for low-friction logging during coffee breaks."
        ),
        "stack": ["FastAPI", "SQLite", "HTMX", "Pico.css", "Alembic"],
        "status": "live",
        "live_url": "https://kicker.midnightcron.com",
        "repo_url": "https://github.com/midnightcron/kicker",
        "story": (
            "ELO math adapted to 2v2 teams: the rating delta accounts for the team "
            "average rating but is distributed to each player individually. HTMX-only "
            "frontend, no build step. The trickiest bit ended up being not the math "
            "but a Cloudflare edge-cache fix for stale CSS after deploys (now solved "
            "with an mtime-derived ?v= query string on the stylesheet link)."
        ),
    },
    {
        "slug": "autoverlad",
        "name": "Autoverlad",
        "tagline": "Wait-time tracker for the Swiss car-train services.",
        "description": (
            "Tracks queue times at the Furka, Simplon, and Lötschberg Autoverlad "
            "stations. Polls the operators' public feeds and graphs the queue history "
            "so you can pick a less painful crossing time."
        ),
        "stack": ["Python", "FastAPI", "SQLite", "Chart.js"],
        "status": "migrating",
        "live_url": None,
        "repo_url": "https://github.com/midnightcron/autoverlad",
        "story": (
            "Started as a laptop daemon scraping a single RSS feed (Matterhorn "
            "Gotthard Bahn for the Furka), with a matplotlib dashboard. Migration "
            "in flight to the Pi with proper scheduling, multi-station coverage "
            "(Furka, Simplon, Lötschberg), and a FastAPI dashboard at "
            "autoverlad.midnightcron.com."
        ),
    },
    {
        "slug": "training-coach",
        "name": "Training Coach",
        "tagline": "Weekly training-load report with LLM-written coaching notes.",
        "description": (
            "Pulls workout history, computes load and recovery, then asks an LLM to "
            "draft the week's coaching summary against a prompt template. Runs as a "
            "scheduled job on the Pi."
        ),
        "stack": ["Airflow", "Postgres", "SQLite", "Python", "LLM"],
        "status": "wip",
        "live_url": None,
        "repo_url": None,
        "story": (
            "Live but mid-rework. Current report shape and prompt scaffold are not "
            "where they need to be. Planned: clearer load metrics, tighter prompts, "
            "and a leaner scheduler than Airflow once the DAG count stays at one."
        ),
    },
]


def project_by_slug(slug: str) -> Project | None:
    for p in PROJECTS:
        if p["slug"] == slug:
            return p
    return None
