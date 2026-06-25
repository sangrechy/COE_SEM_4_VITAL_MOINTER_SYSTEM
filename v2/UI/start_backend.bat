@echo off
setlocal

cd /d "%~dp0backend"

echo.
echo ========================================
echo   Edge AI Wearable Health Monitor
echo   Backend - FastAPI + Bleak
echo ========================================
echo.

python --version

python -c "import fastapi" >nul 2>&1
if errorlevel 1 (
    echo Installing Python dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting backend on http://localhost:8000
echo.

python main.py

pause
