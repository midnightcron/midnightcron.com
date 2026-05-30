"""FastAPI entry point for midnightcron.com.

Static content surface: landing, about, per-project pages. No DB, no auth.
All project content lives in app/projects.py.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

from app.projects import PROJECTS, project_by_slug
from app.templating import templates

app = FastAPI(title="midnightcron", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def index(request: Request) -> Response:
    return templates.TemplateResponse(request, "index.html", {"projects": PROJECTS})


@app.get("/about")
def about(request: Request) -> Response:
    return templates.TemplateResponse(request, "about.html", {})


@app.get("/projects/{slug}")
def project_detail(request: Request, slug: str) -> Response:
    project = project_by_slug(slug)
    if project is None:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse(request, "project_detail.html", {"project": project})
