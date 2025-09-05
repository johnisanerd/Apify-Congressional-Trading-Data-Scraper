"""
Congressional Stock Trades Scraper: A Quick Start Example
Scrape the US Congressional trading data:  get transactions from both the House and the Senate.
See more at https://apify.com/johnvc/apify-us-congress-financial-disclosures-and-stock-trading-data?fpr=9n7kx3

This script demonstrates how to use the Congressional Stock Trades Scraper Actor
to search Congressional stock trades and retrieve structured search results.

https://docs.apify.com/api/client/python/docs/overview/introduction


"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input.  In this case we are going to search for Congressional Stock Trades in January of 2025.
run_input = {
  "Start_Date": "2025-01-01",
  "End_Date": "2025-01-31",
  "Max_Results": 100
}

# Run the Actor and wait for it to finish
run = client.actor("xxCgm38ifv9HcLl9z").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)