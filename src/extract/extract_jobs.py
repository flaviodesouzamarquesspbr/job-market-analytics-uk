import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

results = []

for page in range(1, 20):
    print(f"Fetching page {page}...")

    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/{page}"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 50
    }

    response = requests.get(url, params=params)
    data = response.json()

    # DEBUG
    print(f"Page {page} results:", len(data.get("results", [])))

    if "results" in data and len(data["results"]) > 0:
        results.extend(data["results"])
    else:
        print("No more results, stopping...")
        break

    time.sleep(1)  # evita bloqueio da API

print(f"Total jobs collected: {len(results)}")

df = pd.DataFrame(results)

df.to_parquet("data/bronze/jobs.parquet", index=False)

print("Bronze layer updated!")

