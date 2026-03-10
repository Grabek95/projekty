@echo off
REM Uruchom backend
start "Backend - FastAPI" cmd /k "cd /d D:\projekty\churn-daily-automation\backend && uvicorn api.main:app --reload"

REM Poczekaj 3 sekundy (backend musi się uruchomić)
timeout /t 5 /nobreak

REM Uruchom frontend
start "Frontend - React" cmd /k "cd /d D:\projekty\churn-daily-automation\frontend && npm start"

REM Poczekaj 5 sekund (React musi się skompilować)
timeout /t 10 /nobreak

echo.
echo ====================================
echo  Serwery uruchomione!
echo  Backend: http://127.0.0.1:8000
echo  Frontend: http://localhost:3000
echo ====================================