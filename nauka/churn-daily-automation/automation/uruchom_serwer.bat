@echo off
start cmd /k "cd D:\projekty\churn-daily-automation\backend && uvicorn api.main:app --reload"
start cmd /k "cd D:\projekty\churn-daily-automation\frontend && npm start"