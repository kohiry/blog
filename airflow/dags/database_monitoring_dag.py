from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from os import environ


def check_condition(ti):
    query_result = ti.xcom_pull(task_ids='extract_data')
    if query_result and query_result[0] > 100:
        return 'send_notification'
    return 'end'

def send_telegram_message():
    pass

with DAG(
    dag_id='database_monitoring_dag',
    start_date=datetime(2024, 11, 3),
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'email_on_failure': False,
    },
) as dag:

    extract_data = PostgresOperator(
        task_id='extract_data',
        postgres_conn_id='postgres',
        sql="""
            SELECT views
            FROM posts 
            WHERE views > 100 and update_at >= {{ ds }}
        """,
    )

    check_condition = PythonOperator(
        task_id='check_condition',
        python_callable=check_condition,
    )

    send_notification = PythonOperator(
        task_id='send_notification',
        python_callable=send_telegram_message,
        trigger_rule='one_success',
    )

    extract_data >> check_condition >> [send_notification]
