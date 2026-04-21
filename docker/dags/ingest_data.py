import pandas as pd
from sqlalchemy import create_engine

# URL of dataset (small sample for now)
url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

# Read data
df = pd.read_csv(url, compression='gzip', nrows=100000)

# Create connection
engine = create_engine("postgresql://root:root@host.docker.internal:5432/ny_taxi")

# Load data into postgres
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

print("Data loaded successfully!")
