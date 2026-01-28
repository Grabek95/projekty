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

    print(f"Pobieram {BLOB_NAME} z Blob...")

    download_stream = blob_client.download_blob()
    # pobierz plik jako stream

    csv_content = download_stream.readall().decode('utf-8')
    # readall() = wczytaj wszystko jako bytes
    # decode('utf-8') = zamień bytes na string
    # utf-8 = kodowanie znaków (obsługuje polskie znaki)

    print(f"Pobrano {len(csv_content)} znaków")

    # parse CSV z pamięci (bez zapisywania na dysku)
    print("Parsuję CSV...")

    csv_reader = csv.DictReader(io.StringIO(csv_content))
    # io.StringIO() = tworzy "plik" w pamięci ze stringa
    # csv.DictReader() = czyta CSV jako słowniki
    # każy wiersz = {'produkt': 'Laptop', 'ilosc': '2', 'cena': '4999.99'}

    rows = list(csv_reader)
    # zamień iterator na listę

    print(f"Wczytano {len(rows)} wierszy danych")
    print(f"Kolumny: {list(rows[0].keys())}")
    # rows[0].keys() = nazwy kolumn z pierwszego wiersza

    # pokaż pierwsze 3 wiersze
    print("\nPierwsze 3 wiersze:")
    for i, row in enumerate(rows[:3], 1):
        # enumerate(lista, 1) = numeruj od 1
        print(f"    {i}. {row['produkt']}: {row['ilosc']} szt. x {row['cena']} zł")

    # krok 3 INSERT do Azure SQL
    print("\nKROK 3: INSERT danych do Azure SQL Database")

    print("Łączę się z Azure SQL...")

    with AzureSQLConnection(SQL_SERVER, SQL_DB, SQL_USER, SQL_PASS) as db:
        # context manager - automatycznie zamknięcie i commit

        print(f"Połączona z bazą {SQL_DB}")

        # sprawdz ile rekordow przed
        count_before = db.get_count('TestSprzedaz')
        print(f"Rekordów przed INSERT: {count_before}")

        # przygotuj dane do bulk insert
        # zamień słowniki na tuple (produkt, ilosc, cena)
        data = []
        for row in rows:
            produkt = row['produkt']
            ilosc = int(row['ilosc']) # zamien string na int
            cena = float(row['cena']) # zamien string na float
            data.append((produkt, ilosc, cena))

        print(f"Wstawiam {len(data)} rekordów...")
        