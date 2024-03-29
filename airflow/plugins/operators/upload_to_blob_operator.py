from airflow.models import BaseOperator
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

class UploadToBlobOperator(BaseOperator):

    def __init__(
        self,
        blob_name,
        storage_account_name,
        storage_account_key,
        container_name,
        local_file_path,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.blob_name = blob_name
        self.storage_account_name = storage_account_name
        self.storage_account_key = storage_account_key
        self.container_name = container_name
        self.local_file_path = local_file_path

    def execute(self, context):
        self.log.info("Uploading file to Azure Blob Storage...")
        try:
            blob_service_client = BlobServiceClient.from_connection_string(
                f"DefaultEndpointsProtocol=https;AccountName={self.storage_account_name};"
                f"AccountKey={self.storage_account_key};EndpointSuffix=core.windows.net"
            )
            container_client = blob_service_client.get_container_client(self.container_name)
            blob_client = container_client.get_blob_client(self.blob_name)

            with open(self.local_file_path, "rb") as data:
                blob_client.upload_blob(data)

            self.log.info("File upload complete.")
            return True
        except Exception as e:
            self.log.error(f"Error uploading file to Azure Blob Storage: {str(e)}")
            return False
