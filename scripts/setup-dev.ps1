# First-time dev setup for a new device (Windows). Idempotent.
#
# Usage: .\scripts\setup-dev.ps1

$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)

Write-Host "==> Checking Python..."
try {
    $pyver = (python --version 2>&1) -replace 'Python ', ''
    Write-Host "    Python $pyver"
} catch {
    Write-Error "python not found. Install Python 3.11+ first (https://www.python.org/downloads/)."
    exit 1
}

$parts = $pyver.Split('.')
if ([int]$parts[0] -lt 3 -or ([int]$parts[0] -eq 3 -and [int]$parts[1] -lt 11)) {
    Write-Error "Python 3.11+ required, found $pyver"
    exit 1
}

Write-Host "==> Checking uv..."
$uvCmd = $null
try {
    $uvVer = (uv --version 2>&1)
    $uvCmd = 'uv'
    Write-Host "    $uvVer"
} catch {
    try {
        $uvVer = (python -m uv --version 2>&1)
        $uvCmd = 'python -m uv'
        Write-Host "    $uvVer (via python -m uv)"
    } catch {
        Write-Host "    uv not found, installing via pip..."
        python -m pip install --user uv
        $uvCmd = 'python -m uv'
    }
}

Write-Host "==> Installing project dependencies..."
Invoke-Expression "$uvCmd sync"

Write-Host "==> Setting up .env..."
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "    Created .env from .env.example."
    Write-Host "    Set TUNNEL_TOKEN before deploying (dev runs do not need it)."
} else {
    Write-Host "    .env already exists, leaving it."
}

Write-Host ""
Write-Host "==> Done."
Write-Host "    Start the app with: $uvCmd run uvicorn app.main:app --reload"
Write-Host "    Run tests with:     $uvCmd run pytest -q"
