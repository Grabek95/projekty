# blob_download.py
# Download pliku z Blob Storage i lista plików

from azure.storage.blob import BlobServiceClient

print("DOWNLOAD pliku z Azure Blob Storage")

CONNECTION_STRING = "YOUR_CONNECTION_STRING_HERE" # uzupełnić w domu o prawdziwy
container_name = "raw"

try:
    # krok 1 - poołączenie
    print("\nŁącze się z Azure Storage Account...")
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(container_name)
    print(f"Połączono z container: '{container_name}'")

    # krok 2 - lista plików
    print(f"\nLista plików w container: '{container_name}'")

    blobs = container_client.list_blobs()
    # list_blobs() zwraca iterator ze wszystkimi blobami
    # iterator = obiekt który zwraca elementy jeden po drugim

    blob_list = []

    for blob in blobs:
        # blob - obiekt BlobProperties z info o pliku
        print(f"    {blob.name}")
        print(f"    Rozmiar: {blob.size} bytes ({blob.size / 1024:.2f} KB)")
        print(f"    Utworzono: {blob.creation_time}")
        print(f"    Zmodyfikowano: {blob.last_modified}")
        print(f"    Content-Type: {blob.content_settings.content_type}")
        print()

        blob_list.append(blob.name)

    if not blob_list:
        print("Brak plików w containerze!")
        exit()

    print(f"Łącznie plików: {len(blob_list)}")

    # krok 3 - wybór pliku do pobrania
    print("\nWybór pliku do pobrania")

    # automatycznie wybierz pierwszy plik (lub ostatni - najnowszy)
    blob_to_download = blob_list[-1]
    print(f"Wybrany plik: {blob_to_download}")

    # nazwa pliku lokalnego
    local_file = f"downloaded_{blob_to_download}"

    # krok 4 - DOWNLOAD
    print(f"\nPobieram '{blob_to_download}' jako '{local_file}'...")

    blob_client = container_client.get_blob_client(blob_to_download)

    # download w trybie binarnym
    with open(local_file, "wb") as f:
        # wb = write binary
        download_stream = blob_client.download_blob()
        # download_blob() - zwraca stream danych (nie cały plik)
        f.write(download_stream.readall())
        # readall() - wczytaj wszystkie dane ze streamu

    print("Pobrano pomyślnie!")
    print(f"    Zapisano jako: {local_file}")

    # krok 5 - METADATA pobranego pliku
    print("\nSzczegółowe informacje o pliku")

    properties = blob_client.get_blob_properties()

    print(f"Nazwa: {blob_to_download}")
    print(f"Rozmiar: {properties.size} bytes")
    print(f"Content-type: {properties.content_settings.content_type}")
    print(f"Content-MD5: {properties.content_settings.content_md5 if properties.content_settings.content_md5 else 'N/A'}")
    # MD5 - hash pliku (do weryfikacji integralności)
    print(f"Utworzono: {properties.creation_time}")
    print(f"Ostatnia modyfikacja: {properties.last_modified}")
    print(f"ETag: {properties.etag}")
    print(f"Szyfrowanie: {'Tak' if properties.server_encrypted else 'Nie'}")
    print(f"Tier: {properties.blob_tier}")
    # tier - warstwa przechowywania (Hot, Cool, Archive)

    # krok 6 - weryfikacja - porównanie rozmiarów
    import os
    local_size = os.path.getsize(local_file)
    # getsize() = rozmiar pliku lokalnego

    print("\nWeryfikacja")
    print(f"Rozmiar w Blob: {properties.size} bytes")
    print(f"Rozmiar lokalny: {local_size} bytes")

    if properties.size == local_size:
        print("Rozmiary się zgadzają - plik pobrany poprawnie")
    else:
        print("Rozmiary różnią się - problem")

    print("\nWszystkie operacje zakończone pomyślnie!")

except Exception as e:
    print(f"Błąd: {e}")
    print("\nSprawdź:")
    print(f"    1. Czy Connection String jest poprawny")
    print(f"    2. Czy container '{container_name}' istnieje")
    print(f"    3. Czy pliki są w containerze")

input("\nNaciśnij Enter aby zakończyć...")