# blob_upload.py
# upload pliku CSV do Azure Blob Storage

from azure.storage.blob import BlobServiceClient
from datetime import datetime

print("UPLOAD - CSV to Azure Blob Storage")

# konfiguracja
CONNECTION_STRING = "YOUR_CONNECTION_STRING_HERE"

local_file = "test_data.csv"
blob_name = f"sprzedaz_{datetime.now():%Y%m%d_%H%M%S}.csv"
container_name = "raw"

try:
    # polaczenie z storage account
    print("\nConnecting to Azure Storage Account...")
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    print("Connected!")

    # wybor container
    print(f"\nSelecting container: '{container_name}'")
    container_client = blob_service_client.get_container_client(container_name)

    # upload pliku
    print(f"\nUploading '{local_file}' as '{blob_name}'...")

    with open(local_file, "rb") as data:
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data, overwrite=True)

    print("Upload successful!")

    # weryfikacja
    print("\nFile properties:")
    properties = blob_client.get_blob_properties()

    print(f"  Name: {blob_name}")
    print(f"  Size: {properties.size} bytes ({properties.size / 1024:.2f} KB)")
    print(f"  Content-Type: {properties.content_settings.content_type}")
    print(f"  Created: {properties.creation_time}")
    print(f"  Modified: {properties.last_modified}")
    print(f"  ETag: {properties.etag}")

    # url do pliku
    print("\nBlob URL:")
    print(f"  {blob_client.url}")

    print("\nAll operations completed successfully!")

except FileNotFoundError:
    print(f"\nERROR: File '{local_file}' not found!")
    print("Make sure the file is in the same folder as the script")

except Exception as e:
    print(f"\nERROR: {e}")
    print("\nCheck:")
    print("  1. Connection string is correct")
    print(f"  2. Container '{container_name}' exists")
    print("  3. Internet connection")

input("\nPress Enter to exit...")