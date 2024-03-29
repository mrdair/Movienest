from airflow.models import BaseOperator
from snowflake.connector import connect, Error
import os

class LoadToSnowflakeOperator(BaseOperator):

    def __init__(
        self,
        snowflake_account,
        snowflake_user,
        snowflake_password,
        snowflake_database,
        snowflake_schema,
        snowflake_table,
        azure_blob_storage_account,
        azure_blob_container,
        azure_blob_file_name,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.snowflake_account = snowflake_account
        self.snowflake_user = snowflake_user
        self.snowflake_password = snowflake_password
        self.snowflake_database = snowflake_database
        self.snowflake_schema = snowflake_schema
        self.snowflake_table = snowflake_table
        self.azure_blob_storage_account = azure_blob_storage_account
        self.azure_blob_container = azure_blob_container
        self.azure_blob_file_name = azure_blob_file_name

    def execute(self, context):
        self.log.info("Loading data from Azure Blob Storage to Snowflake...")

        try:
            # Connect to Snowflake
            connection = connect(
                user=self.snowflake_user,
                password=self.snowflake_password,
                account=self.snowflake_account,
                database=self.snowflake_database,
                schema=self.snowflake_schema
            )

            # Create cursor
            cursor = connection.cursor()

            # Execute Snowflake copy command
            copy_command = f"COPY INTO {self.snowflake_table} FROM 'azure://{self.azure_blob_storage_account}/{self.azure_blob_container}/{self.azure_blob_file_name}' CREDENTIALS=(AZURE_SAS_TOKEN='{self.get_azure_sas_token()}') FILE_FORMAT=(TYPE=CSV FIELD_DELIMITER=',' SKIP_HEADER=1)"
            cursor.execute(copy_command)

            # Commit the transaction
            connection.commit()

            self.log.info("Data load to Snowflake complete.")
            return True
        except Exception as e:
            self.log.error(f"Error loading data to Snowflake: {str(e)}")
            return False
        finally:
            if connection:
                connection.close()

    def get_azure_sas_token(self):
        # Code to generate Azure SAS token for authentication (implementation may vary based on your setup)
        sas_token = "<your_azure_sas_token>"
        return sas_token
