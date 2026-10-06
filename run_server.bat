@echo off
title MEDICARE Hospital Infrastructure Command Center
echo ========================================================
echo   Starting MEDICARE Command Center (Python + Flask)
echo ========================================================
echo.

cd /d "%~dp0"

echo Checking Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    pause
    exit /b 1
)

echo Starting Flask Server on http://127.0.0.1:5000 ...
start http://127.0.0.1:5000
python app.py

pause
