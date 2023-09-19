import pandas as pd

df = pd.read_csv('parquet.csv')
df.to_parquet('iceberg.parquet')
