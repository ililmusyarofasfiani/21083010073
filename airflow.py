#AIRFLOW UNTUK TRANSFORMDATA EXCEL

from datetime import datetime, timedelta
import subprocess
from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from airflow.operators.dummy import DummyOperator

# Default arguments untuk DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Fungsi untuk memanggil script PySpark
def run_pyspark_script():
    subprocess.run(["python3", "/home/arviano/spark_script/from_pyspark.py"], check=True)

# Mendefinisikan DAG
with DAG(
    'transform_data',
    default_args=default_args,
    description='Baca_table_tranksaksi',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    # Dummy operator to mark the start and end
    start = DummyOperator(
        task_id='start',
        dag=dag,
    )


    # Task untuk membaca dan memproses data
    transform_data_task = PythonOperator(
        task_id='transform_data_task',
        python_callable=run_pyspark_script,
    )


    end = DummyOperator(
        task_id='end',
        dag=dag,
    )

    # Menentukan urutan tugas
start >> transform_data_task >> end