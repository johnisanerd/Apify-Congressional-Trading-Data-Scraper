# 🏛️ Congress Trading API: US Congressional Stock Trades and Disclosures in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the Congress Trading API.

**Actor page:** [apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data](https://apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data/input-schema](https://apify.com/johnvc/us-congress-financial-disclosures-and-stock-trading-data/input-schema?fpr=9n7kx3)

The Congress Trading API returns US Congressional Periodic Transaction Reports (PTRs) as clean, structured JSON. Each row is one disclosed transaction: the member name and chamber, state and district, asset and ticker, transaction type, reported amount range, transaction and notification dates, ownership, and filing IDs. Filter by member name, ticker, an exact date, or a date range. Data is normalized from official US House and Senate financial disclosure filings under the STOCK Act.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Congressional-Trading-Data-Scraper.git
   cd Apify-Congressional-Trading-Data-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python congress-stock-trades-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python congress-stock-trades-scraper.py
```

## Why Use This Congress Trading API?

**Both chambers, one schema.** House and Senate Periodic Transaction Reports are normalized into a single, queryable shape, so you analyze all of Congress with one parser instead of two filing systems.

**Powerful filters.** Narrow by member first or last name, by stock ticker, by an exact transaction date, or by a date range. Combine them to answer questions like "every NVDA trade this member made in 2024."

**Audit-ready structured JSON.** One row per transaction, with the reported amount range exactly as filed, plus filing and document IDs and per-run search metadata for traceable, reproducible pulls.

**Predictable, pay-per-use pricing.** Billing is per run plus per transaction returned, with no monthly rental. You control cost directly with `Max_Results`.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can pull Congressional trades for you on demand.

## Features

### Core Capabilities
- **Filter by member, ticker, or date** (exact date or range)
- **Both chambers**: House and Senate filings in one dataset
- **Asset types** including stock, options, ETF, mutual fund, bond, and crypto
- **Ownership attribution** for member, spouse, dependent child, or joint holdings
- **Pre-built dataset views** for purchases, sales, options trades, and stock trades

### Data Quality
- **One row per PTR transaction** with member, chamber, asset, ticker, type, amount range, and dates
- **Amount ranges exactly as filed** (members report brackets, not exact values)
- **Filing and document IDs** for tracing back to the source disclosure
- **Per-run search metadata** (timestamp, query timing, result count) for audit trails
- **Normalized** from official US House Clerk and Senate eFD filings under the STOCK Act

## Usage Examples

### Basic Example
The most recent disclosures across all members. This is the cheapest way to try the API.
```json
{
  "Max_Results": 10
}
```

### By member and date range
Every disclosed transaction for a member within a date window.
```json
{
  "Last_Name": "Pelosi",
  "Start_Date": "2024-01-01",
  "End_Date": "2024-12-31",
  "Max_Results": 50
}
```

### By ticker
Every Congress member who traded a given ticker.
```json
{
  "Stock_Symbol": "AAPL",
  "Max_Results": 50
}
```

## Input Parameters

All parameters are optional. Run with no input to get the most recent transactions; combine fields to narrow results.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `First_Name` | `string` | No | (none) | Member first name (case-insensitive partial match). |
| `Last_Name` | `string` | No | (none) | Member last name (case-insensitive partial match). |
| `Date_Reported` | `string` | No | (none) | Exact transaction date, `YYYY-MM-DD`. Use Start/End for a range instead. |
| `Start_Date` | `string` | No | (none) | Earliest transaction date to include (inclusive), `YYYY-MM-DD`. |
| `End_Date` | `string` | No | (none) | Latest transaction date to include (inclusive), `YYYY-MM-DD`. |
| `Stock_Symbol` | `string` | No | (none) | Ticker filter, e.g. `AAPL`, `MSFT`, `NVDA` (case-insensitive partial match). |
| `Max_Results` | `integer` | No | `100` | Maximum rows to return per run (1 to 1000). |

## Output Format

One transaction returned as a single dataset row.

```json
{
  "id": "3b454411-9bfb-5545-8568-b14e596503e3",
  "Owner": "SP",
  "Asset": "Palo Alto Networks, Inc. (PANW)",
  "Ticker": "PANW",
  "Asset_Type_Code": "OP",
  "Transaction_Type": "P",
  "Date": "2024-02-21",
  "Notification_Date": "2024-02-21",
  "Amount_Range": "$100,001 - $250,000",
  "Capital_Gains_Over_200": "No",
  "Details": "Purchased 20 call options with a strike price of $200 and an expiration date of 1/17/25.",
  "First_Name": "Nancy",
  "Last_Name": "Pelosi",
  "State_District": "CA11",
  "House": "House",
  "Filing_ID": "20024542",
  "DocID": "20024542",
  "Year": "2024",
  "PDF_Quality": "text",
  "created_at": "2025-09-04T13:08:13.253936+00:00",
  "search_metadata": {
    "last_name": "Pelosi",
    "max_results": 100,
    "search_timestamp": "2025-09-05T11:08:47.827456",
    "total_results_found": 10,
    "query_execution_time": 5.30
  }
}
```

### Field reference

| Field | Meaning |
|-------|---------|
| `Transaction_Type` | `P` = purchase, `S` = sale, `S (partial)` = partial sale, `E` = exchange |
| `Asset_Type_Code` | `ST` stock, `OP` options, `MF` mutual fund, `BD` bond, `ET` ETF, `CT` crypto |
| `Owner` | `SP` spouse, `DC` dependent child, `JT` joint, blank = the member |
| `Amount_Range` | Reporting bracket, e.g. `$1,001 - $15,000`. Members report ranges, not exact values |
| `House` | `House` or `Senate` |
| `PDF_Quality` | `text` (machine-readable filing) or `image` (OCR-required filing) |

---

## Use as an MCP tool

You can load the Congress Trading API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Congress Trading API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Congress Trading API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Congress Trading API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/us-congress-financial-disclosures-and-stock-trading-data`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data`, using OAuth when prompted.
5. Ask Claude to run the Congress Trading API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Congress Trading API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/us-congress-financial-disclosures-and-stock-trading-data`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Congress Trading API to power transparency, research, and compliance workflows with reliable, structured results.*

Last Updated: 2026.05.30
