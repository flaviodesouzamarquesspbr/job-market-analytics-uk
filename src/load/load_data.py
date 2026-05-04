import pandas as pd

# Load silver data
df = pd.read_parquet("data/silver/jobs_clean.parquet")

# Save to gold as CSV
df.to_csv("data/gold/jobs_gold.csv", index=False)

print("Gold CSV created successfully!")