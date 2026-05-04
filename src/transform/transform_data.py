import pandas as pd

# Load bronze data
df = pd.read_parquet("data/bronze/jobs.parquet")

# -------------------------------
# Extract nested fields
# -------------------------------
df["company_name"] = df["company"].apply(
    lambda x: x.get("display_name") if isinstance(x, dict) else None
)

df["location_name"] = df["location"].apply(
    lambda x: x.get("display_name") if isinstance(x, dict) else None
)

df["category_name"] = df["category"].apply(
    lambda x: x.get("label") if isinstance(x, dict) else None
)

# -------------------------------
# Handle null values
# -------------------------------
df["contract_type"] = df["contract_type"].fillna("Unknown")
df["contract_time"] = df["contract_time"].fillna("Unknown")

# -------------------------------
# Handle salary (0 → None)
# -------------------------------
df["salary_min"] = df["salary_min"].replace(0, None)
df["salary_max"] = df["salary_max"].replace(0, None)

# -------------------------------
# Create salary average (row-level)
# -------------------------------
df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2

# -------------------------------
# Add currency
# -------------------------------
df["currency"] = "GBP"

# -------------------------------
# Select final columns (IMPORTANT)
# -------------------------------
df_clean = df[
    [
        "title",
        "company_name",
        "location_name",
        "category_name",
        "salary_min",
        "salary_max",
        "salary_avg",
        "contract_type",
        "contract_time",
        "currency",
    ]
]

# -------------------------------
# Preview
# -------------------------------
print(df_clean.head())

# -------------------------------
# Save to silver layer
# -------------------------------
df_clean.to_parquet("data/silver/jobs_clean.parquet", index=False)

print("Silver layer created successfully!")