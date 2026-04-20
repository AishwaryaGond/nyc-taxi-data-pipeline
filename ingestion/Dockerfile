FROM python:3.9-slim

WORKDIR /app

COPY ingest_data.py .

RUN pip install pandas sqlalchemy psycopg2-binary

CMD ["python", "ingest_data.py"]