from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

def check_condition(ti):
    query_result = ti.xcom_pull(task_ids='extract_data')
    if query_result and query_result[0] > 100:
        return 'send_notification'
    return 'end'

def send_telegram_message():
    # Логика для отправки уведомления в Telegram
    pass

with DAG(
    dag_id='database_monitoring_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=timedelta(minutes=30),  # Запускаем каждые 30 минут
    catchup=False,
    default_args={
        'owner': 'data_team',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
) as dag:

    # Шаг 1: Извлечение данных
    extract_data = PostgresOperator(
        task_id='extract_data',
        postgres_conn_id='your_postgres_connection',  # ID подключения к базе в Airflow
        sql="""
            SELECT COUNT(*) 
            FROM posts 
        """,
    )

    # Шаг 2: Проверка условия
    check_condition = PythonOperator(
        task_id='check_condition',
        python_callable=check_condition,
    )

    # Шаг 3: Отправка уведомления
    send_notification = PythonOperator(
        task_id='send_notification',
        python_callable=send_telegram_message,
        trigger_rule='one_success',  # Выполнится, если хотя бы одна предыдущая задача завершится успехом
    )

    # Определяем последовательность выполнения
    extract_data >> check_condition >> [send_notification]
