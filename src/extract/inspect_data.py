import pandas as pd

df = pd.read_parquet("data/bronze/jobs.parquet")

print("\n=== HEAD ===")
print(df.head().to_string())

print("\n=== COLUMNS ===")
print(df.head().to_string())

print("\n=== INFO ===")
print(df.head().to_string())