from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from operators.load_to_snowflake_operator import LoadToSnowflakeOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'load_to_snowflake',
    default_args=default_args,
    description='DAG to load dataset from Azure Blob Storage to Snowflake Data Warehouse',
    schedule_interval=None,
)

load_to_snowflake_task = LoadToSnowflakeOperator(
    task_id='load_to_snowflake',
    snowflake_account=Variable.get('snowflake_account'),
    snowflake_user=Variable.get('snowflake_user'),
    snowflake_password=Variable.get('snowflake_password'),
    snowflake_database='your_database',
    snowflake_schema='public',
    snowflake_table='example_table',
    azure_blob_storage_account=Variable.get('storage_account_name'),
    azure_blob_container='datasets',
    azure_blob_file_name='example_dataset.csv',
    dag=dag,
)

load_to_snowflake_task
