# NYC Taxi Data Engineering Pipeline

## 📌 Problem Description

This project builds an end-to-end data pipeline to process NYC taxi trip data and generate daily analytical insights such as total trips and average distance.

---

## Architecture

Data Source → Docker → PostgreSQL → Airflow → Transformation → Data Quality Check → Dashboard

---

## ⚙️ Tech Stack

* Docker
* PostgreSQL
* Apache Airflow
* Python (pandas, sqlalchemy)
* Google Looker Studio

---

## 🔄 Pipeline Workflow

1. Data ingestion using Python script
2. Data stored in PostgreSQL (`yellow_taxi_data`)
3. Airflow DAG orchestrates the pipeline
4. SQL transformation creates summary table (`taxi_summary`)
5. Data quality check ensures correctness

---

## 📊 Dashboard

🔗 <https://datastudio.google.com/reporting/e3ff2938-4c36-457f-a827-7a116410aa40
>

The dashboard includes:

* Time series of total trips
* Average trip distance per day

---

## 📸 Screenshots

### Airflow DAG
![Airflow](screenshots/airflow.png)

### Graph View
![Graph](screenshots/graph.png)

### Postgres Output
![Postgres](screenshots/postgres.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

---

## ▶️ How to Run

```bash
docker-compose up -d
```

Open Airflow:
http://localhost:8080

---

## 📁 Project Structure

* `docker/` → Airflow + PostgreSQL setup
* `ingestion/` → data ingestion logic
* `dags/` → Airflow pipeline

---

## 💡 Learnings

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
