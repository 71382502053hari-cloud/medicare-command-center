# PowerShell launcher for MEDICARE Command Center
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting MEDICARE Command Center (Python + Flask)     " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

Set-Location -Path $PSScriptRoot

try {
    $pyVersion = python --version
    Write-Host "Found: $pyVersion" -ForegroundColor Yellow
} catch {
    Write-Error "Python not found! Please ensure Python is installed and in PATH."
    exit 1
}

Start-Process "http://127.0.0.1:5000"
Write-Host "Launching server on http://127.0.0.1:5000 ..." -ForegroundColor Cyan
python app.py
