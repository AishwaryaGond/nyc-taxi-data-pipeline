from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="ingestion_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    run_ingestion = BashOperator(
        task_id="run_ingestion_script",
        bash_command="docker run --rm ingestion_image"
    )

    run_transformation = BashOperator(
    task_id="run_transformation",
    bash_command="""
    docker exec zoomcamp_postgres psql -U root -d ny_taxi -c "
    CREATE TABLE IF NOT EXISTS taxi_summary AS 
    SELECT
        DATE(tpep_pickup_datetime) AS date,
        COUNT(*) AS total_trips,
        AVG(trip_distance) AS avg_distance,
        CASE 
            WHEN AVG(trip_distance) < 2 THEN 'short'
            WHEN AVG(trip_distance) < 10 THEN 'medium'
            ELSE 'long'
        END AS trip_type
    FROM yellow_taxi_data
    GROUP BY date;"
    """
    )

    data_quality_check = BashOperator(
    task_id="data_quality_check",
    bash_command="""
    docker exec zoomcamp_postgres psql -U root -d ny_taxi -c "
    SELECT COUNT(*) FROM taxi_summary;"
    """
    )

    run_ingestion >> run_transformation >> data_quality_check

