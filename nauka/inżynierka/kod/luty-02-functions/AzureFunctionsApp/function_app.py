# function_app.py 
# Azure Functions - Automatyczny pipeline ETL 
import azure.functions as func
from datetime import datetime
import json
import logging
from azure.storage.blob import BlobServiceClient
import pymssql
import csv
import io
import os

app = func.FunctionApp()

# KONFIGURACJA - (z environment variables)
BLOB_CONNECTION = os.environ.get("AzureWebJobsStorage")
# AzureWebJobsStorage = domyślna zmienna w Functions
# Automatycznie ustawiona gdy deploy Azure

SQL_SERVER = os.environ.get("SQL_SERVER")
SQL_DB = os.environ.get("SQL_DB")
SQL_USER = os.environ.get("SQL_USER")
SQL_PASS = os.environ.get("SQL_PASS")

# TIME TRIGGER
@app.timer_trigger(
        schedule="0 0 9 * * *", # codziennie o 9:00 UTC
        arg_name="myTimer",
        run_on_startup=False,   # nie uruchamiaj przy starcie (tylko dla testów)
        use_monitor=False
        )
def TimerPipeline(myTimer: func.TimerRequest) -> None:
    """
    Timer Trigger - Uruchamia pipeline automatycznie.
    
    CRON: 0 0 9 * * * = Codziennie o 9:00 UTC
    Zmień na: 0 */30 * * * * = Co 30 minut
    """
    logging.info('Timer Trigger - Pipeline START')

    if myTimer.past_due:
        logging.info('The timer is past due!')

    try:
        # uruchom pipeline
        result = run_pipeline()
        logging.info(f'Pipeline SUCCESS: {result}')
    
    except Exception as e:
        logging.error(f'Pipeline FALSED: {str(e)}')
        raise # Re-reaise żeby Azure wiedziało, że failed

# HTTP TRIGGER - Uruchamia się na żądanie
@app.route(route="pipeline", auth_level=func.AuthLevel.ANONYMOUS)
def HttpPipeline(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP Trigger - Uruchamia pipeline przez URL.
    
    URL: https://<function-app>.azurewebsites.net/api/pipeline
    Metoda: GET lub POST
    """
    logging.info('HTTP Trigger - Pipeline START')

    try:
        # uruchom pipeline
        result = run_pipeline()

        return func.HttpResponse(
            f"Pipeline SUCCESS!\n\n{result}",
            status_code=200
        )
    
    except Exception as e:
        logging.error(f'Pipeline FAILED: {str(e)}')

        return func.HttpResponse(
            f"Pipeline FAILED!\n\nError: {str(e)}",
            status_code=500
        )
    
# GŁÓWNA LOGIKA PIPELINE
def run_pipeline():
    """
    ETL Pipeline: Blob → SQL
    
    Returns:
        str: Podsumowanie operacji
    """
    logging.info('Pipeline execution started')

    # sprawdz konfiguracje
    if not all([BLOB_CONNECTION, SQL_SERVER, SQL_DB, SQL_USER, SQL_PASS]):
        raise ValueError("Missing configuration! Check environment variables.")
    
    # KROK 1: Połącz z Blob Storage
    logging.info('Step 1: Connecting to Blob Storage')
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION)
    container = blob_service.get_container_client("raw")

    # Lista plików
    blobs = list(container.list_blobs())
    if not blobs:
        return "No files in 'raw' container. Nothing to process."
    
    logging.info(f'Found {len(blobs)} files in raw container')

    # weź najnowszy plik
    latest_blob = sorted(blobs, key=lambda b: b.last_modified, reverse=True)[0]
    blob_name = latest_blob.name
    logging.info(f'Processing: {blob_name}')

    # KROK 2: Pobierz i parsuj CSV
    logging.info('Step 2: Downloading and parsing CSV')
    blob_client = container.get_blob_client(blob_name)
    download_stream = blob_client.download_blob()
    csv_content = download_stream.readall().decode('utf-8-sig')

    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)
    logging.info(f'Parsed {len(rows)} rows')

    # KROK 3: INSERT do SQL
    logging.info('Step 3: Inserting to SQL Database')

    # Połącz przez pymssql (bez ODBC Driver)
    conn = pymssql.connect(
        server=SQL_SERVER,
        user=SQL_USER,
        password=SQL_PASS,
        database=SQL_DB
    )

    try:
        cursor = conn.cursor()

        # sprawdź ile jest przed
        cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
        count_before = cursor.fetchone()[0]

        # przygotuj dane
        data = []
        for row in rows:
            produkt = row['produkt']
            ilosc = int(row['ilosc'])
            cena = float(row['cena'])
            data.append((produkt, ilosc, cena))

        # bulk insert
        cursor.executemany(
            "INSERT INTO TestSprzedaz (produkt, ilosc, cena) VALUES (%s, %s, %s)",
            data
        )
        conn.commit()

        # sprawdź ile jest po
        cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
        count_after = cursor.fetchone()[0]

        inserted = count_after - count_before
        logging.info(f'Inserted {inserted} records')

    finally:
        conn.close()

    # KROK 4: Kopiuj do processed
    logging.info('Step 4: Copying to processed container')
    processed_container = blob_service.get_container_client("processed")
    dest_blob = processed_container.get_blob_client(blob_name)
    dest_blob.start_copy_from_url(blob_client.url)
    logging.info('Copied to processed')

    # PODSUMOWANIE
    summary = f"""
Pipeline Execution Summary:
===========================
File: {blob_name}
Rows processed: {len(rows)}
Records inserted: {inserted}
Total records: {count_after}
Status: SUCCESS
"""
    
    logging.info('Pipeline completed successfully!')
    return summary