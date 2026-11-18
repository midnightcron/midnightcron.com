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
        "slug": "alpenpasse",
        "name": "Alpenpässe",
        "tagline": "Cycling logbook for alpine passes, per person and per trip.",
        "description": (
            "Pick a pass from the catalogue (country, canton, climb category, summit "
            "elevation, ascent, length, gradient), record who rode it and when, and "
            "watch each rider's collection grow: distinct passes, ascent metres per side "
            "climbed, canton and country completion, and achievement badges. GPX and FIT "
            "tracks import straight into a ride, and a trip logbook ties rides together "
            "with dates, participants, notes, photos, and a read-only public share link."
        ),
        "stack": ["FastAPI", "SQLModel", "HTMX", "Pico.css", "Alembic"],
        "status": "live",
        "live_url": "https://alpenpasse.midnightcron.com",
        "repo_url": "https://github.com/midnightcron/alps-passes",
        "story": (
            "Cloned from a sibling app that came with auth, sessions, rate limiting, "
            "and the Docker + Caddy + Cloudflare Tunnel deploy pattern already wired "
            "up, so the platform work was mostly plumbing. Everything after that is "
            "features: pass catalogue, ride logging, trip logbook, badges, CSV export. "
            "The fiddliest part was track import: working out which side of a pass "
            "was climbed (Grimsel from Oberwald or from Gletsch?) from the elevation "
            "profile, and counting each side's ascent only once. In production and "
            "invite-only; friend invites and a shareable passport are next on the list."
        ),
    },
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
            "Match entry, leaderboard, and a rolling 30-day rating chart for a 2v2 "
            "foosball ladder. Built for low-friction logging during coffee breaks: "
            "pick both teams from two tap grids and submit."
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
            "with an mtime-derived ?v= query string on the stylesheet link). Since "
            "hardened with CSRF tokens, rate limiting, and stricter session cookies."
        ),
    },
    {
        "slug": "training-coach",
        "name": "Training Coach",
        "tagline": "Garmin-fed training coach with weekly reports and a Telegram chat.",
        "description": (
            "A weekly Airflow pipeline pulls Garmin activities and wellness data (HRV, "
            "sleep, body battery), analyses FIT files of quality sessions, and has "
            "Claude write a coaching report every Monday, published to Notion and "
            "Telegram. Between reports, a tool-using coach bot answers questions from "
            "the same data, and a morning brief follows each weigh-in."
        ),
        "stack": ["Python", "Airflow", "SQLite", "Claude", "Telegram", "Notion"],
        "status": "live",
        "live_url": None,
        "repo_url": None,
        "story": (
            "Started as a single weekly report with a fixed prompt. Grew into a "
            "holistic coach: the chat bot calls read-only tools (activities, weekly "
            "totals, FIT analysis in my own zones, wellness, training status) as often "
            "as it needs before answering, and keeps context across turns. It also "
            "reads what Tania (the nutrition coach) logged, so fueling advice is based "
            "on what I actually ate. Private repo, since it is wired to my own accounts."
        ),
    },
    {
        "slug": "tania",
        "name": "Tania",
        "tagline": "Nutrition coach on Telegram: send a meal photo, get it logged.",
        "description": (
            "Send Tania a text (\"2 slices bread with quark, banana\") or a photo of a "
            "meal or nutrition label. Claude splits it into items with quantity, meal, "
            "and nutrients, and after you confirm, each item becomes a row in a Notion "
            "food log. Each save comes back with the day's running totals against "
            "targets for the day type (rest, training, or double), worked out from "
            "Garmin and the weekly plan."
        ),
        "stack": ["Python", "Claude", "Telegram", "Notion", "SQLite"],
        "status": "live",
        "live_url": None,
        "repo_url": None,
        "story": (
            "Lives next to Training Coach as its own bot and container. A food memory "
            "keeps repeat items consistent and offers one-tap favourites, so only new "
            "food costs a model call. An iPhone shortcut uploads photos straight to her "
            "through a Cloudflare Tunnel, and she saves them with Edit and Undo "
            "buttons. A small benchmark scores a cheap model against a stronger one, "
            "using logged nutrition labels as ground truth."
        ),
    },
    {
        "slug": "coffee",
        "name": "Coffee",
        "tagline": "Espresso grind log: time versus output weight, per bean.",
        "description": (
            "Log a shot (bean, grind setting, grind time, output weight) and see a "
            "scatter plot per bean with a linear fit, so dialling in a new bag is a "
            "glance at a chart instead of a notebook page of scribbles."
        ),
        "stack": ["FastAPI", "SQLModel", "HTMX", "Chart.js", "Pico.css"],
        "status": "live",
        "live_url": "https://coffee.midnightcron.com",
        "repo_url": "https://github.com/midnightcron/coffee",
        "story": (
            "Designed on paper first (an architecture doc reviewed before any code), "
            "then scaffolded on the kicker stack in a day. Pushes to main auto-deploy "
            "to the Pi over Tailscale SSH."
        ),
    },
    {
        "slug": "whine-or-wine",
        "name": "Whine or Wine",
        "tagline": "Group bike-trip tracker: every deed is a wine or a whine.",
        "description": (
            "Built for a cycling trip in France. Pick a rider and a deed they were "
            "caught doing; each deed counts as a wine (worth celebrating) or a whine "
            "(worth groaning about), and the leaderboard tallies them up. Ends with a "
            "trip-highlights page and a printable quote-wall poster."
        ),
        "stack": ["FastAPI", "SQLModel", "HTMX", "Chart.js", "Pico.css"],
        "status": "live",
        "live_url": "https://winenotwhine.midnightcron.com",
        "repo_url": "https://github.com/peterbraden/whine-or-wine",
        "story": (
            "A group effort with friends from the trip, several humans and several "
            "Claude Code instances committing in parallel, coordinated through a "
            "shared standup file in the repo. Its auth, sessions, and deploy setup "
            "later became the base for Alpenpässe. The trip is over; the site stays "
            "up as a souvenir."
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
        "status": "wip",
        "live_url": None,
        "repo_url": None,
        "story": (
            "Started as a laptop daemon scraping a single RSS feed (Matterhorn "
            "Gotthard Bahn for the Furka), with a matplotlib dashboard. The move to "
            "the Pi (proper scheduling, Furka, Simplon, and Lötschberg coverage, a "
            "FastAPI dashboard) is planned but parked while other projects took "
            "priority."
        ),
    },
]


def project_by_slug(slug: str) -> Project | None:
    for p in PROJECTS:
        if p["slug"] == slug:
            return p
    return None
