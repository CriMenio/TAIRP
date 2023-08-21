from azure.storage.blob import BlobServiceClient
import os

storage_account_key = "LpL15OtYO7ds7Eq9CyxZ24mu1zZqWw2M+3RGt9/Fy/zOGTB/PqjtFtYmk3vXgK4CMFVC80C6CpOh+AStYtTLfQ=="
storage_account_name = "crimeniostorage"
connection_string = "DefaultEndpointsProtocol=https;AccountName=crimeniostorage;AccountKey=LpL15OtYO7ds7Eq9CyxZ24mu1zZqWw2M+3RGt9/Fy/zOGTB/PqjtFtYmk3vXgK4CMFVC80C6CpOh+AStYtTLfQ==;EndpointSuffix=core.windows.net"
container_name = "uploadedfiles"

download_directory = "C:\\Users\\Krishnakant\\Desktop\\Blob"

def download_files():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Ensure the download directory exists
    os.makedirs(download_directory, exist_ok=True)

    # Download and save each blob to the local directory
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob)
        blob_data = blob_client.download_blob()
        blob_file_path = os.path.join(download_directory, blob.name)

        with open(blob_file_path, "wb") as blob_file:
            blob_file.write(blob_data.readall())

        print(f"Downloaded: {blob.name}")

if __name__ == "__main__":
    download_files()
    print("Download process completed.")
