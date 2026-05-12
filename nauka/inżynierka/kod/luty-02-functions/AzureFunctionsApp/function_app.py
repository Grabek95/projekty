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

# konfiguracja z azure env variables
BLOB_CONNECTION = os.environ.get("AzureWebJobsStorage")
# AzureWebJobsStorage jest ustawione domyslnie przez azure

SQL_SERVER = os.environ.get("SQL_SERVER")
SQL_DB = os.environ.get("SQL_DB")
SQL_USER = os.environ.get("SQL_USER")
SQL_PASS = os.environ.get("SQL_PASS")

# timer - autoamtyczne wykonanie
@app.timer_trigger(
        schedule="0 0 9 * * *", # codziennie o 9:00 UTC
        arg_name="myTimer",
        run_on_startup=False, 
        use_monitor=False
        )
def TimerPipeline(myTimer: func.TimerRequest) -> None:
    """
    Automatyczne uruchomienie pipeline o 9:00 UTC codziennie.
    Schedule można zmienić w parametrze 'schedule
    """
    logging.info('Timer Trigger - Pipeline start')

    if myTimer.past_due:
        logging.info('The timer is past due!')

    try:
        # uruchom pipeline
        result = run_pipeline()
        logging.info(f'Pipeline SUCCESS: {result}')
    
    except Exception as e:
        logging.error(f'Pipeline FALSED: {str(e)}')
        raise # rzuc error dalej do azure

# http trigger, uruchamiany na żądanie
@app.route(route="pipeline", auth_level=func.AuthLevel.ANONYMOUS)
def HttpPipeline(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP Trigger - Uruchamia pipeline przez URL.
    URL: https://<function-app>.azurewebsites.net/api/pipeline
    """
    logging.info('HTTP Trigger - pipeline start')

    try:
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
    
# glowna logika: pobiera csv z blob, wstawia do sql
def run_pipeline():
    """
    ETL Pipeline: Blob to SQL
    Returns: podsumowanie operacji
    """
    logging.info('Pipeline execution started')

    # sprawdz czy wszystkie zmienne sa ustawione
    if not all([BLOB_CONNECTION, SQL_SERVER, SQL_DB, SQL_USER, SQL_PASS]):
        raise ValueError("Missing configuration! Check environment variables.")
    
    # polacz z blob storage
    logging.info('Connecting to Blob Storage')
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION)
    container = blob_service.get_container_client("raw")

    # lista plikow w raw
    blobs = list(container.list_blobs())
    if not blobs:
        return "No files in 'raw' container. Nothing to process."
    
    logging.info(f'Found {len(blobs)} files in raw container')

    # wez najnowszy plik
    latest_blob = sorted(blobs, key=lambda b: b.last_modified, reverse=True)[0]
    blob_name = latest_blob.name
    logging.info(f'Processing: {blob_name}')

    # pobierz i parsuj csv
    logging.info('Downloading and parsing CSV')
    blob_client = container.get_blob_client(blob_name)
    download_stream = blob_client.download_blob()
    csv_content = download_stream.readall().decode('utf-8-sig') # utf-8-sig dla polskich znakow

    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)
    logging.info(f'Parsed {len(rows)} rows')

    # insert do sql
    logging.info('Inserting to SQL Database')

    # polacz przez pymssql
    conn = pymssql.connect(
        server=SQL_SERVER,
        user=SQL_USER,
        password=SQL_PASS,
        database=SQL_DB
    )

    try:
        cursor = conn.cursor()

        # sprawdz ile jest przed
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

        # sprawdz ile jest po
        cursor.execute("SELECT COUNT(*) FROM TestSprzedaz")
        count_after = cursor.fetchone()[0]

        inserted = count_after - count_before
        logging.info(f'Inserted {inserted} records')

    finally:
        conn.close()

    # kopiuje do processed
    logging.info('Copying to processed container')
    processed_container = blob_service.get_container_client("processed")
    dest_blob = processed_container.get_blob_client(blob_name)
    dest_blob.start_copy_from_url(blob_client.url)
    logging.info('Copied to processed')

    # po skopiowaniu, przenosi do archive
    logging.info('Moving to archive container')
    archive_container = blob_service.get_container_client("archive")
    archive_blob = archive_container.get_blob_client(blob_name)
    archive_blob.start_copy_from_url(blob_client.url)

    # usuwam z raw
    blob_client.delete_blob()
    logging.info('Deleted from raw container')

    # pdsumowanie
    summary = f"""
Pipeline Execution Summary:
File: {blob_name}
Rows processed: {len(rows)}
Records inserted: {inserted}
Total records: {count_after}
Status: SUCCESS
"""
    
    logging.info('Pipeline completed successfully!')
    return summary