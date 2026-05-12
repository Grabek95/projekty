# blob_download.py
# download pliku z Azure Blob Storage i lista plikow

from azure.storage.blob import BlobServiceClient

print("DOWNLOAD - file from Azure Blob Storage")

CONNECTION_STRING = "YOUR_CONNECTION_STRING_HERE"
container_name = "raw"

try:
    # polaczenie
    print("\nConnecting to Azure Storage Account...")
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(container_name)
    print(f"Connected to container: '{container_name}'")

    # lista plikow
    print(f"\nFiles in container '{container_name}':")

    blobs = container_client.list_blobs()
    blob_list = []

    for blob in blobs:
        print(f"  {blob.name}")
        print(f"    Size: {blob.size} bytes ({blob.size / 1024:.2f} KB)")
        print(f"    Created: {blob.creation_time}")
        print(f"    Modified: {blob.last_modified}")
        print(f"    Content-Type: {blob.content_settings.content_type}")
        print()

        blob_list.append(blob.name)

    if not blob_list:
        print("No files in container!")
        exit()

    print(f"Total files: {len(blob_list)}")

    # wybor pliku
    print("\nSelecting file to download:")

    # automatycznie wybierz ostatni (najnowszy)
    blob_to_download = blob_list[-1]
    print(f"Selected: {blob_to_download}")

    # nazwa lokalna
    local_file = f"downloaded_{blob_to_download}"

    # download
    print(f"\nDownloading '{blob_to_download}' as '{local_file}'...")

    blob_client = container_client.get_blob_client(blob_to_download)

    # download w trybie binarnym
    with open(local_file, "wb") as f:
        download_stream = blob_client.download_blob()
        f.write(download_stream.readall())

    print("Download successful!")
    print(f"  Saved as: {local_file}")

    # metadata
    print("\nFile properties:")

    properties = blob_client.get_blob_properties()

    print(f"  Name: {blob_to_download}")
    print(f"  Size: {properties.size} bytes")
    print(f"  Content-Type: {properties.content_settings.content_type}")
    print(f"  Content-MD5: {properties.content_settings.content_md5 if properties.content_settings.content_md5 else 'N/A'}")
    print(f"  Created: {properties.creation_time}")
    print(f"  Modified: {properties.last_modified}")
    print(f"  ETag: {properties.etag}")
    print(f"  Encrypted: {'Yes' if properties.server_encrypted else 'No'}")
    print(f"  Tier: {properties.blob_tier}")

    # weryfikacja rozmiaru
    import os
    local_size = os.path.getsize(local_file)

    print("\nVerification:")
    print(f"  Blob size: {properties.size} bytes")
    print(f"  Local size: {local_size} bytes")

    if properties.size == local_size:
        print("  Sizes match - file downloaded correctly!")
    else:
        print("  Sizes differ - potential problem!")

    print("\nAll operations completed successfully!")

except Exception as e:
    print(f"\nError: {e}")
    print("\nCheck:")
    print("  1. Connection string is correct")
    print(f"  2. Container '{container_name}' exists")
    print("  3. Files are in the container")

input("\nPress Enter to exit...")