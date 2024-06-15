#AIRFLOW UNTUK TRANSFORMDATA EXCEL

from datetime import datetime, timedelta
import subprocess
from airflow import DAG
from airflow.operators.python import PythonOperator # type: ignore
from airflow.operators.bash import BashOperator
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
##def run_pyspark_script():
    ###subprocess.run(["python3", "/home/arviano/spark_script/write_dwh.py"], check=True)

# Mendefinisikan DAG
with DAG(
    'write_dwh_fix',
    default_args=default_args,
    description='write_dwh',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    start = DummyOperator(
        task_id='start',
    
        dag=dag
    )

    # Task untuk membaca dan memproses data
    write_dwh = BashOperator(
        task_id='data_staging',
        bash_command='python3 /home/arviano/spark_script/write_dwh.py',
        dag=dag,
    )


    end = DummyOperator(
        task_id='end',
    
        dag=dag
    )
    # Menentukan urutan tugas
start >> write_dwh >> end