import sys
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator

sys.path.append('/opt/airflow/api-request')
from insert_records import main

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 10, 30),
    'catchup': False,
}

dag = DAG(
    dag_id = 'weather-api-orchestrator',
    default_args = default_args,
    schedule = timedelta(minutes=1),
)

with dag:
    task1 = PythonOperator(
        task_id = 'ingest_data_task',
        python_callable = main
    )