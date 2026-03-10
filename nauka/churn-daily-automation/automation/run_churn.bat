@echo off
cd /d "D:\projekty\churn-daily-automation\backend\scripts"
"C:\Users\mateusz.grabinski\AppData\Local\Programs\Python\Python314\python.exe" "churn_daily.py"
REM Pause tylko gdy są błędy
if %ERRORLEVEL% NEQ 0 pause