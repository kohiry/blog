from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta


def send_telegram_message(ti):
    query_result = ti.xcom_pull(task_ids='extract_data')
    print(query_result)
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
            SELECT views
            FROM posts 
            WHERE views > 1 and update_at >= {{ ds }}
        """,
    )

    send_notification = PythonOperator(
        task_id='send_notification',
        python_callable=send_telegram_message,
        trigger_rule='one_success',
    )

    extract_data >> [send_notification]
