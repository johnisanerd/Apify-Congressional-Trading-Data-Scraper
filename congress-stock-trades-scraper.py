"""
Congress Trading API: A Quick Start Example
See more at: https://apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data?fpr=9n7kx3
Input schema: https://apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data/input-schema?fpr=9n7kx3

This script shows how to call the Congress Trading API on Apify from Python and
read its structured JSON output. It exercises several input parameters so you can
see what is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input. All fields are optional; combine them to narrow results.
# Billing is per transaction returned, so Max_Results is kept small to keep this
# first run inexpensive. Raise it once you have your own API key and budget.
run_input = {
    "Last_Name": "Pelosi",        # member surname (case-insensitive partial match)
    "Start_Date": "2024-01-01",   # earliest transaction date, YYYY-MM-DD (inclusive)
    "End_Date": "2024-12-31",     # latest transaction date, YYYY-MM-DD (inclusive)
    # "First_Name": "Nancy",      # optional: member first name
    # "Stock_Symbol": "NVDA",     # optional: ticker filter
    "Max_Results": 10,            # cap on rows returned; kept small to stay cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/us-congress-financial-disclosures-and-stock-trading-data").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset (one row per transaction)
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} transaction(s).\n")

# Show a few key fields from each transaction.
for item in items:
    member = f"{item.get('First_Name', '')} {item.get('Last_Name', '')}".strip()
    asset = item.get("Ticker") or item.get("Asset")
    print(
        f"{member} ({item.get('House')})  "
        f"type={item.get('Transaction_Type')}  {asset}  "
        f"{item.get('Amount_Range')}  on {item.get('Date')}"
    )
