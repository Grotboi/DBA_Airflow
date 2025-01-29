from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models import Variable
import sqlalchemy as sa

# Тут пометка настройки DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='repeat_query_dag',
    default_args=default_args,
    schedule_interval=None,  
    catchup=False,
) as dag:
    
    
    # Соединение с моей бд, в моем случае PostgreSQL
 engine = sa.create_engine('postgresql://postgres:root@localhost:8887/Dag')
metadata = sa.MetaData(bind=engine)


new_table = sa.Table(
    'new_table', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('column1', sa.String),
    sa.Column('column2', sa.DateTime),
    sa.Column('column3', sa.Float),
)

metadata.create_all(engine)



# Сохранение запроса
Variable.set("my_sql_query", """
    SELECT column1, column2, column3
    FROM old_table
    WHERE condition;
""")


execute_query_task = PostgresOperator(
    task_id="execute_query",
    postgres_conn_id="my_postgres_connection",
    sql="{{ var.value.my_sql_query }}",
    autocommit=True,
    dag=dag,
)

insert_into_new_table_task = PostgresOperator(
    task_id="insert_into_new_table",
    postgres_conn_id="my_postgres_connection",
    sql="""
        INSERT INTO new_table (column1, column2, column3)
        VALUES (%s, %s, %s);
    """,
    parameters=[('{{ ti.xcom_pull(task_ids="execute_query") }}')],  
    autocommit=True,
    dag=dag,
)


#Порядок выполнения 
execute_query_task >> insert_into_new_table_task

