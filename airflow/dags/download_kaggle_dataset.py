from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from operators.download_kaggle_operator import DownloadKaggleOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'download_kaggle_dataset',
    default_args=default_args,
    description='DAG to download dataset from Kaggle',
    schedule_interval=None,
)

download_kaggle_task = DownloadKaggleOperator(
    task_id='download_kaggle_data',
    kaggle_dataset_name=Variable.get('kaggle_dataset_name'),
    kaggle_username=Variable.get('kaggle_username'),
    kaggle_key=Variable.get('kaggle_key'),
    download_path='/tmp',
    dag=dag,
)

download_kaggle_task
