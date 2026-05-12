# blob_to_sql_pipeline.py
# pelny pipeline: CSV -> Blob -> SQL -> Blob (processed)
# skrypt testowy - prototyp przed Azure Functions

from azure.storage.blob import BlobServiceClient
from db_utils import AzureSQLConnection
from datetime import datetime
import csv
import io

print("PIPELINE: CSV -> Blob -> SQL -> Blob(Processed)")

# konfiguracja
BLOB_CONNECTION = "YOUR_CONNECTION_STRING_HERE"
SQL_SERVER = 'sql-praca-mateusz.database.windows.net'
SQL_DB = 'db-praca-inzynierska'
SQL_USER = 'sqladmin'
SQL_PASS = 'YOUR_PASSWORD_HERE'

# pliki
LOCAL_CSV = "test_data.csv"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
BLOB_NAME = f"import_{TIMESTAMP}.csv"

try:
    # upload csv do blob (raw)
    print("\nUpload CSV to Blob (raw)")

    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION)
    raw_container = blob_service.get_container_client("raw")

    print(f"Uploading '{LOCAL_CSV}' as '{BLOB_NAME}'...")

    with open(LOCAL_CSV, "rb") as data:
        blob_client = raw_container.get_blob_client(BLOB_NAME)
        blob_client.upload_blob(data, overwrite=True)

    file_size = blob_client.get_blob_properties().size
    print(f"Uploaded! Size: {file_size} bytes")

    # pobierz i parsuj csv
    print("\nDownload and parse CSV")

    print(f"Downloading {BLOB_NAME}...")
    download_stream = blob_client.download_blob()
    
    # pobierz i dekoduj (utf-8-sig dla polskich znakow)
    csv_content = download_stream.readall().decode('utf-8-sig')
    print(f"Downloaded {len(csv_content)} characters")

    # parse csv w pamieci
    print("Parsing CSV...")
    csv_reader = csv.DictReader(io.StringIO(csv_content))
    rows = list(csv_reader)

    print(f"Loaded {len(rows)} rows")
    print(f"Columns: {list(rows[0].keys())}")

    # pokaz pierwsze 3
    print("\nFirst 3 rows:")
    for i, row in enumerate(rows[:3], 1):
        print(f"  {i}. {row['produkt']}: {row['ilosc']} x {row['cena']} PLN")

    # insert do sql
    print("\nINSERT to Azure SQL")
    print("Connecting to Azure SQL...")

    with AzureSQLConnection(SQL_SERVER, SQL_DB, SQL_USER, SQL_PASS) as db:
        print(f"Connected to {SQL_DB}")

        # sprawdz count przed
        count_before = db.get_count('TestSprzedaz')
        print(f"Records before INSERT: {count_before}")

        # przygotuj dane do bulk insert
        data = []
        for row in rows:
            produkt = row['produkt']
            ilosc = int(row['ilosc'])
            cena = float(row['cena'])
            data.append((produkt, ilosc, cena))

        print(f"Inserting {len(data)} records...")
        
        # bulk insert
        inserted_count = db.bulk_insert(
            table='TestSprzedaz',
            columns=['produkt', 'ilosc', 'cena'],
            data=data
        )

        print(f"Inserted {inserted_count} records")

        # sprawdz count po
        count_after = db.get_count('TestSprzedaz')
        print(f"Records after INSERT: {count_after}")
        print(f"Added: {count_after - count_before} records")

    # kopiuj do processed
    print("\nCopy to Blob (processed)")

    processed_container = blob_service.get_container_client("processed")
    dest_blob = processed_container.get_blob_client(BLOB_NAME)

    print(f"Copying '{BLOB_NAME}' from 'raw' to 'processed'...")

    # kopiuj blob w Azure (serverside)
    dest_blob.start_copy_from_url(blob_client.url)
    print("Copied to 'processed'!")

    # podsumowanie
    print("\nPIPELINE COMPLETED SUCCESSFULLY")
    print(f"\nSummary:")
    print(f"  Source file: {LOCAL_CSV}")
    print(f"  Blob name: {BLOB_NAME}")
    print(f"  CSV rows: {len(rows)}")
    print(f"  SQL inserts: {inserted_count}")
    print(f"  Status: SUCCESS")

    print(f"\nLocations:")
    print(f"  Blob (raw): {blob_client.url}")
    print(f"  Blob (processed): {dest_blob.url}")
    print(f"  SQL: {SQL_SERVER}/{SQL_DB}/TestSprzedaz")

except FileNotFoundError:
    print(f"\nERROR: File '{LOCAL_CSV}' not found!")
    print("Make sure the file is in the same folder as the script")

except Exception as e:
    print(f"\nERROR: {e}")
    print("\nCheck:")
    print("  1. Blob Storage connection string")
    print("  2. SQL Database password")
    print("  3. Containers 'raw' and 'processed' exist")
    print("  4. Table 'TestSprzedaz' exists")

input("\Press Enter to exit...")