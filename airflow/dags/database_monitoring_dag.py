import os

import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

TOKEN, CHAT_ID = os.environ['TOKEN'], os.environ['CHAT_ID']

def transform_data(ti):
    query_result = ti.xcom_pull(task_ids='extract_data')
    query_result.sort()
    msg = "Most popular posts here with date { ds }: \n" + '\n'.join(
        [
            f"title={query[0]} content={query[1]} views={query[2]}"
            for query in query_result
        ]
    )
    ti.xcom_push(key='query_result', value=msg)


def send_telegram_message(ti):
    query_result = ti.xcom_pull(task_ids='transform_data', key='query_result')
    url = (f"https://api.telegram.org/bot{TOKEN}"
           f"/sendMessage?chat_id={CHAT_ID}&text={query_result}")
    requests.get(url)
    return 'end'


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
            SELECT title, content, views
            FROM posts 
            WHERE views > 1 and updated_at >= '{{ ds }}'
        """,
        do_xcom_push=True,
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
        op_args=['{{ ds }}'],
        trigger_rule='all_done',
    )

    send_notification = PythonOperator(
        task_id='send_notification',
        python_callable=send_telegram_message,
        trigger_rule='all_done',
    )

    extract_data >> transform_data >> [send_notification]
