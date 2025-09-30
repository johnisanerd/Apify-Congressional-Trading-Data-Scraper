# Apify Congressional Trading Data Scraper

[Scrape the US Congressional trading data:  get transactions from both the House and the Senate.](https://apify.com/johnvc/apify-us-congress-financial-disclosures-and-stock-trading-data?fpr=9n7kx3)


> **The most efficient, reliable, and developer-friendly Google Jobs search scraper**

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Congressional-Trading-Data-Scraper.git
   cd Apify-Congressional-Trading-Data-Scraper
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using venv (Python 3.3+)
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install from requirements.txt
   pip install -r requirements.txt

   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python congress-stock-trades-scraper.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python congress-stock-trades-scraper.py
```

You can see more documentation on how to use the [Congressional stock tradesscraper here.](https://apify.com/johnvc/apify-us-congress-financial-disclosures-and-stock-trading-data?fpr=9n7kx3)


[**Made with ❤️**](https://apify.com/johnvc?fpr=9n7kx3)

*Transform your search automation with the most reliable and efficient Congressional stock trades scraper on the market.*
Last Updated: 2025.09.30
