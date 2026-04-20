# NYC Taxi Data Engineering Pipeline

## Problem Description

This project builds an end-to-end data pipeline to process NYC taxi trip data and generate daily analytical insights such as total trips and average distance.

---

## Architecture

Data Source → Docker → PostgreSQL → Airflow → Transformation → Data Quality Check → Dashboard

---

## Tech Stack

* Docker
* PostgreSQL
* Apache Airflow
* Python (pandas, sqlalchemy)
* Google Looker Studio

---

## Pipeline Workflow

1. Data ingestion using Python script
2. Data stored in PostgreSQL (`yellow_taxi_data`)
3. Airflow DAG orchestrates the pipeline
4. SQL transformation creates summary table (`taxi_summary`)
5. Data quality check ensures correctness

---

## Dashboard

🔗 <https://datastudio.google.com/reporting/e3ff2938-4c36-457f-a827-7a116410aa40
>

The dashboard includes:

* Time series of total trips
* Average trip distance per day

---

## Screenshots

### Airflow DAG
<img width="1464" height="798" alt="airflow" src="https://github.com/user-attachments/assets/2e3a8a68-e963-4bd8-8ed5-cc385a56c0d0" />


### Graph View
<img width="1457" height="780" alt="graph" src="https://github.com/user-attachments/assets/c6ae2bf5-18a6-43d2-897d-e7d9857f028b" />


### Postgres Output
<img width="356" height="159" alt="postgres" src="https://github.com/user-attachments/assets/adf49402-b28a-4000-bdff-76e4c55e9ee3" />


### Dashboard
<img width="834" height="459" alt="dashboard" src="https://github.com/user-attachments/assets/03a78044-906a-4547-9f71-83057c1ddcb8" />


---

## Airflow Login Credentials

After running the project, open Airflow at:

http://localhost:8080

Use the following credentials:

* **Username:** airflow
* **Password:** airflow


## Project Structure

* `docker/` → Airflow + PostgreSQL setup
* `ingestion/` → data ingestion logic
* `dags/` → Airflow pipeline

## 📁 Project Structure

```
datazoomcamp_project/
│
├── docker/
│   ├── docker-compose.yml
│   └── dags/
│       └── ingest_dag.py
│
├── ingestion/
│   ├── Dockerfile
│   └── ingest_data.py
│
├── README.md
├── .gitignore
```

## Learnings

* Built an end-to-end data pipeline
* Implemented workflow orchestration using Airflow
* Performed data transformation and aggregation
* Created a dashboard for data visualization

---

## 🚀 Unique Features

* Fully containerized pipeline
* Automated workflow with Airflow
* Data quality validation step
* Analytical transformation for insights
