# blob_upload.py
# upload pliku CSV do Azure Blob Storage

from azure.storage.blob import BlobServiceClient
from datetime import datetime

print("UPLOAD pliku do Azure Blob Storage")

# konfiguracja
CONNECTION_STRING = "YOUR_CONNECTION_STRING_HERE" # uzupełnić w domu o prawdziwy

local_file = "test_data.csv" # nazwa pliku lokalnego

blob_name = f"sprzedaz_{datetime.now():%Y%m%d_%H%M%S}.csv" # nazwa w blob storage wraz z data i godzina

container_name = "raw" # container docelowy

try: 
    # krok 1 - połączenie z Storage Account
    print("\nŁącze się z Azure Storage Account...")
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    # główny obiekt do zarządzania Storage Account, from_connection_string - metoda fabrykująca, tworzy klienta z connection string
    print("Połączono z Storage Account!")

    # krok 2 - wybór container
    print(f"\nWybieram container: '{container_name}'")
    container_client = blob_service_client.get_container_client(container_name)
    # get_container_client() - pobiera klienta dla konkretnego containera, nie tworzy go - zakłada, że już istnieje
    print(f"Container: '{container_client}' wybrany")

    # krok 3 - upload pliku
    print(f"\nWgrywam plik '{local_file}' jako '{blob_name}'...")

    # otwórz plik w trybie binarnym (rb = read binary) - działa ze wszystkim (CSV, excel, obrazy itd.)
    with open(local_file, "rb") as data:
        # pobierz klienta dla konkretnego blob
        blob_client = container_client.get_blob_client(blob_name)
        # get_blob_client() - klient dla konkretnego pliku w containerze

        # upload
        blob_client.upload_blob(data, overwrite=True)
        # upload_blob()- wgrywa dane, overwrite=True - nadpisuje jeśli plik istnieje, False to błąd jeśli istenieje - jest to domyślne

    print("Plik wgrany pomyślnie!")

    # krok 4 - weryfikacja
    print("\nInformacje o wgranym pliku:")

    properties = blob_client.get_blob_properties()
    # get_blob_properties() - pobiera metadata z pliku

    print(f"    Nazwa: {blob_name}")
    print(f"    Rozmiar: {properties.size} bytes ({properties.size / 1024:.2f} KB)")
    print(f"    Content-Type: {properties.content_settings.content_type}")
    print(f"    Utworzono: {properties.creation_time}")
    print(f"    Zmodyfikowano: {properties.last_modified}")
    print(f"    ETag: {properties.etag}")
    # ETag - unikalny id wersji pliku (zmienia się przy każdej modyfikacji)

    # krok 5 - URL do pliku
    print("\nURL do pliku:")
    print(f"    {blob_client.url}")

    print("\nWszystkie operacje zakończone pomyślnie!")

except FileNotFoundError:
    # błąd gdy plik lokalny nie istnieje
    print(f"\nBłąd: Plik '{local_file}' nie istnieje!")
    print("Upewnij się, że plik jest w tym samym folderze co skrypt")

except Exception as e:
    print(f"\nBłąd: {e}")
    print("\nSprawdź:")
    print(f"    1. Czy Connection String jest poprawny")
    print(f"    2. Czy container '{container_name}' istnieje")
    print(f"    3. Czy masz dostęp do internetu")

input("\nNaciśnij Enter aby zakończyć...")