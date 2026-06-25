@echo off
setlocal

cd /d "%~dp0frontend"

echo.
echo ========================================
echo   Edge AI Wearable Health Monitor
echo   Frontend - React
echo ========================================
echo.

if not exist node_modules (
    echo Installing npm packages...
    npm install
)

echo.
echo Starting React development server...
echo.

npm start

pause
