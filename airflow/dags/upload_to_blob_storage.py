from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from operators.upload_to_blob_operator import UploadToBlobOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'upload_to_blob_storage',
    default_args=default_args,
    description='DAG to upload dataset to Azure Blob Storage',
    schedule_interval=None,
)

upload_to_blob_task = UploadToBlobOperator(
    task_id='upload_to_blob_storage',
    blob_name='example_dataset.csv',
    storage_account_name=Variable.get('storage_account_name'),
    storage_account_key=Variable.get('storage_account_key'),
    container_name='datasets',
    local_file_path='/tmp/example_dataset.csv',
    dag=dag,
)

upload_to_blob_task
