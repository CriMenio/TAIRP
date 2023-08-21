from azure.storage.blob import BlobServiceClient
import os


#change cridentials detils with your's details 
storage_account_key = "LpL15OtYO7ds7Eq9CyxZ24mu1zZqWw2M+3RGt9/Fy/zOGTB/PqjtFtYmk3vXgK4CMFVC80C6CpOh+AStYtTLfQ=="
storage_account_name = "crimeniostorage"
connection_string = "DefaultEndpointsProtocol=https;AccountName=crimeniostorage;AccountKey=LpL15OtYO7ds7Eq9CyxZ24mu1zZqWw2M+3RGt9/Fy/zOGTB/PqjtFtYmk3vXgK4CMFVC80C6CpOh+AStYtTLfQ==;EndpointSuffix=core.windows.net"
container_name = "uploadedfiles"

def uploadToBlobStorage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client =blob_service_client.get_blob_client(container=container_name,blob=file_name)

    with open(file_path,"rb") as data:
        blob_client.upload_blob(data)
        print("Upload "+file_name+" file")

uploadToBlobStorage('C:\\Users\\Krishnakant\\Desktop\\Task\\TAsk.jpg','Task')    

    
