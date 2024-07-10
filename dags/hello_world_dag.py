from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from src.hello_world import hello_world

dag =DAG("hello_world",
         description="This will print Hello World",
         schedule_interval="* * * * *",
         start_date=datetime(2024,7,10),
         catchup=False
        )

start_dag= DummyOperator(task_id="start_dag",
                         dag=dag)

print_hello=PythonOperator(task_id="hello_world_task",
                           python_callable=hello_world,
                           dag=dag
                           )
end_dag= DummyOperator(task_id="end_dag",
                       dag=dag)

print_hello