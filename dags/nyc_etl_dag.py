from airflow import DAG # type: ignore
from airflow.operators.bash import BashOperator  # type: ignore
from datetime import datetime

with DAG(
    dag_id="nyc_accidents_etl",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    transform = BashOperator(
        task_id="transform_dataset",
        bash_command="python /opt/airflow/etl/transform_nyc.py"
    )

    transform
