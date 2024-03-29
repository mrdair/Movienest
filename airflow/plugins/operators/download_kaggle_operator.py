from airflow.models import BaseOperator
from kaggle.api.kaggle_api_extended import KaggleApi
import os

class DownloadKaggleOperator(BaseOperator):

    def __init__(
        self,
        kaggle_dataset_name,
        kaggle_username,
        kaggle_key,
        download_path,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.kaggle_dataset_name = kaggle_dataset_name
        self.kaggle_username = kaggle_username
        self.kaggle_key = kaggle_key
        self.download_path = download_path

    def execute(self, context):
        self.log.info("Downloading dataset from Kaggle...")
        api = KaggleApi()
        api.authenticate(self.kaggle_username, self.kaggle_key)
        api.dataset_download_files(self.kaggle_dataset_name, path=self.download_path)
        self.log.info("Download complete.")

        downloaded_files = os.listdir(self.download_path)
        self.log.info(f"Downloaded files: {downloaded_files}")

        return downloaded_files
