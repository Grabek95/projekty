# blob_to_sql_pipeline.py
# pełny pipeline: CSV --> Blob --> SQL --> Blob (processed)

from azure.storage.blob import BlobServiceClient
from db_utils import AzureSQLConnection
from datetime import datetime
import csv
import io

print("PIPELINE: CSV -> Blob -> SQL -> Blob(Processed)")

# konfiguracja
# blob storage
BLOB_CONNECTION = "YOUR_BLOB_CONNECTION_HERE" # uzupełnic o prawdziwy

# Azure SQL
SQL_SERVER = 'sql-praca-mateusz.database.windows.net'
SQL_DB = 'db-praca-inzynierska'
SQL_USER = 'sqladmin'
SQL_PASS = 'YOUR_PASSWORD_HERE'  # uzupełnić w domu

# Pliki
LOCAL_CSV = "test_data.csv"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
BLOB_NAME = f"import_{TIMESTAMP}.csv"

try:
    # krok 1: upload csv do Blob (raw)
    print("\nKROK 1: Upload CSV do BLob Storage (container: raw)")

    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION)
    # połączenie z Blob Storage

    raw_container = blob_service.get_container_client("raw")
    # Container dla surowych danych

    print(f"Wgrywam '{LOCAL_CSV}' jako '{BLOB_NAME}'...")

    with open(LOCAL_CSV, "rb") as data:
        blob_client = raw_container.get_blob_client(BLOB_NAME)
        blob_client.upload_blob(data, overwrite=True)

    file_size = blob_client.get_blob_properties().size
    print(f"Wgrano pomyślnie! Rozmiar: {file_size} bytes")

    # krok 2: Download z BLob i parse CSV
    print("\nKROK 2: Download z Blob i parse CSV")