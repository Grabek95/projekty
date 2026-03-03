# Główny plik FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import sys
import os

from .database import get_db_connection
from .models import ChurnRecord, ChurnResponse, PLKManualInput

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Tworzymy apke FastAPI
app = FastAPI(
    title="Churn Daily API",
    description="API for automated churn data collection and reporting",
    version="1.0.0"
)

# CORS - pozwala React łączyć się z API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # w produkcji: tylko konkretne domeny
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Pierwszy endpoint - test czy API działa
@app.get("/")
def read_root():
    return {
        "message": "Churn Daily API is running!",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Główny endpoint - pobierz wszystkie dane churn
@app.get("/api/churn/all", response_model=ChurnResponse)
def get_all_churn():
    """
    Pobiera wszystkie dane churn z bazy

    Returns:
        ChurnResponse: Lista rekordów + total count
    """
    try:
        conn = get_db_connection()
        if conn is None:
            raise HTTPException(status_code=500, detail="Database connection failed")
        
        query = "SELECT * FROM db_work_dwn.Churn_Daily ORDER BY MIESIAC DESC, SPOLKA, PRODUKT"
        df = pd.read_sql(query, conn)
        conn.close()

        df['DATA_RAPORTU'] = df['DATA_RAPORTU'].astype(str)

        records = df.to_dict('records')

        return {
            "records": records,
            "total": len(records)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
# Refresh wszystkich danych - tak jak Task Scheduler
@app.post("/api/churn_refresh/all")
def refresh_all_data():
    """
    Ręczne uruchomienie całego procesu zbierania danych.
    To samo co uruchomienie skryptu churn_daily.py
    """
    try:
        import scripts.churn_daily as churn_module
        from scripts.churn_daily import (
            outlook_connect,
            Teradata_connect,
            pobierz_plk,
            pobierz_cp,
            pobierz_netia,
            zapisz_do_bazy,
            update_last_cp,
            update_last_netia
        )
        from datetime import datetime

        # uruchom cały proces
        churn_module.dzis = datetime.now().strftime("%Y-%m-%d")

        churn_module.inbox = outlook_connect()
        if churn_module.inbox is None:
            raise HTTPException(status_code=500, detail="Outlook connection failed")
        
        conn = Teradata_connect()
        if conn is None:
            raise HTTPException(status_code=500, detail="Teradata connecion failed")
        
        # Pobierz dane ze wszystkich źródeł
        dane_plk = pobierz_plk()
        dane_cp = pobierz_cp(conn)
        dane_netia = pobierz_netia()

        # zapisz do bazy (UPSERT)
        zapisz_do_bazy(conn, dane_plk, dane_cp, dane_netia)

        # Aktualizuj poprzednie miesiące
        update_last_cp(conn, dane_cp)
        update_last_netia(conn, dane_netia)

        conn.close()

        return {
            "message": "Data refresh completed successfully",
            "timestamp": churn_module.dzis  
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    
@app.post("/api/update/cp")
def update_cp_only():
    """Tylko aktualizacja poprzedniego miesiaca CP"""
    try:
        from scripts.churn_daily import Teradata_connect, pobierz_cp, update_last_cp

        conn = Teradata_connect()
        if conn is None:
            raise HTTPException(status_code=500, detail="Database connection failed")
        
        dane_cp = pobierz_cp(conn)
        if dane_cp is None:
            raise HTTPException(status_code=500, detail="No CP data found")
        
        update_last_cp(conn, dane_cp)
        conn.close()

        return {"message": "CP previous month updated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/api/update/netia")
def update_netia_previous_month():
    """
    Aktualizacja poprzedniego miesiąca tylko dla Netia
    """
    try:
        import scripts.churn_daily as churn_module
        from scripts.churn_daily import outlook_connect, pobierz_netia, update_last_netia, Teradata_connect
        from datetime import datetime
        
        churn_module.dzis = datetime.now().strftime("%Y-%m-%d")
        churn_module.inbox = outlook_connect()
        
        inbox = outlook_connect()
        if inbox is None:
            raise HTTPException(status_code=500, detail="Outlook connection failed")
        
        conn = Teradata_connect()
        if conn is None:
            raise HTTPException(status_code=500, detail="Database connection failed")
        
        dane_netia = pobierz_netia()
        if dane_netia is None:
            raise HTTPException(status_code=404, detail="No Netia data found")
        
        update_last_netia(conn, dane_netia)
        conn.close()
        
        return {"message": "Netia previous month updated successfully"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


@app.post("/api/plk/manual")
def manual_plk_input(data: PLKManualInput):
    """Ręczne wpisanie wartości PLK - TODO"""
    # TODO: Implementacja później
    return {"message": "Not implemented yet"}