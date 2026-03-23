# Automated Financial Analysis & Reporting Pipeline

A Python tool that pulls live financial statements from Yahoo Finance, computes key ratios, runs a two-stage DCF valuation with live country risk premiums and exports a PDF report, PowerPoint deck and CSV per ticker.

Disclaimer: This tool is for educational purposes only. Data comes from Yahoo Finance and may contain errors or delays. DCF outputs are based on simplified models and should not be used for investment decisions. Not financial advice.


## What it does

For each ticker:

1. Fetches income statement, balance sheet and cash flow data via `yfinance` — with automatic FX conversion to USD for non-US tickers (JPY, CNY, EUR, CHF, etc.) using live Yahoo Finance exchange rates
2. Computes 14 financial ratios: gross profit, gross/net margins, ROE, ROA, current ratio, cash ratio, debt to equity, net debt, FCF, cash flow reliability, P/E, EV/EBITDA, Net Debt/EBITDA
3. Runs a two-stage DCF using CAPM-derived WACC, with country risk premiums pulled live from Damodaran's NYU Stern page and applied per company based on its registered country
4. Generates 3 charts: revenue history + 5-year CAGR forecast, key ratios bar chart, cash flow breakdown (Net Income → Operating CF → Free CF)
5. Exports: `TICKER_FINAL.pdf`, `TICKER_FINAL.pptx`, `TICKER_metrics.csv` and the three chart PNGs — all in the `Financial_Results` folder.

Runs in Annual mode by default. TTM mode (trailing twelve months, summing the 4 most recent quarterly filings) is available by changing `use_ttm=False` to `use_ttm=True` in the last cell. Quarterly data coverage on yfinance is thinner for non-US tickers, so TTM mode works mo
**TTM mode is experimental.** It may fail completely or return incorrect/incomplete numbers for many non-US and some international tickers because quarterly filings are not always available or properly structured on Yahoo Finance. Use Annual mode (default) for reliable results on international stocks.

Tested on TSLA, NVDA, AAPL, MSFT and several international tickers (6301.T, 6501.T, 000333.SZ, SAP.DE, NESN.SW, ASML.AS).


## How to run

### Option 1 — Google Colab (no setup needed)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeorgeKGM2058/automated-financial-reports-tool/blob/main/financial_analysis_tool.ipynb)

Run all cells (Runtime → Run all). Dependencies install automatically in the first cell. Outputs appear in the `Financial_Results/` folder in the Colab file browser — right-click to download.

### Option 2 — Local (Jupyter or VS Code)

```bash
git clone https://github.com/GeorgeKGM2058/automated-financial-reports-tool.git
cd automated-financial-reports-tool
pip install -r requirements.txt         # Python 3.7+
jupyter notebook financial_analysis_tool.ipynb
```

To change tickers or switch to TTM mode, edit the last cell:

```python
# Annual (default)
run_everything(["NVDA", "AAPL", "SAP.DE"], "Financial_Results", use_ttm=False)

# TTM
run_everything(["NVDA", "AAPL", "SAP.DE"], "Financial_Results", use_ttm=True)
```


## Tickers supported

Any ticker on Yahoo Finance. Includes the following by default:

| Market | Examples |
|---|---|
| US equities | `NVDA`, `AAPL`, `MSFT`, `TSLA` |
| Japan | `6501.T` (Hitachi), `6301.T` (Komatsu) |
| China A-shares | `000333.SZ` (Midea) |
| Europe | `SAP.DE`, `NESN.SW`, `ASML.AS` |

All monetary outputs are converted to USD automatically.


## DCF methodology

This is a simplified DCF — not a professional model. The goal was to get something methodologically defensible while keeping the code readable. Assumptions:

| Parameter | Value | Notes |
|---|---|---|
| Risk-free rate | 4.19% | 10-year US Treasury, early 2026 — update `risk_free` in `compute_dcf()` as needed |
| Equity risk premium | 5.00% | Damodaran implied ERP, Jan 2026 |
| Country risk premium | Live | Fetched at runtime from Damodaran's NYU Stern page; 0% fallback for developed markets |
| Revenue CAGR | Historical, 3–15% cap | Floor 3% (nominal GDP minimum). Ceiling 15% prevents hyper‑growth phase forever |
| FCF margin | Current year, held constant | Known simplification, an expanded model would reduce this in years 3–5 |
| Forecast horizon | 5 years | Explicit FCF projection period |
| Terminal growth | 3.00% | Conservative, roughly in line with long-run nominal GDP |

A few things to be aware of: beta is sourced from yfinance (5-year monthly vs S&P 500), so it's a US-benchmarked figure for all tickers — the CRP partially compensates for this on non-US names but doesn't fully solve it. Terminal value also ends up being a large share of the total, so the output is quite sensitive to the WACC and terminal growth assumptions.


## Project structure

```
financial_analysis_tool.ipynb   ← all logic lives here
requirements.txt
.gitignore
Financial_Results/              ← git-ignored, created at runtime
  NVDA/
    NVDA_FINAL.pdf
    NVDA_FINAL.pptx
    NVDA_metrics.csv
    revenue_forecast.png
    key_ratios.png
    cash_flow.png
  TSLA/
  ...
```


## Stack

`Python 3.7+` · `yfinance` · `pandas` · `numpy` · `matplotlib` · `reportlab` · `python-pptx` · `requests`


## Sample output — NVIDIA (Annual FY2026)

| Metric | Value |
|---|---|
| Gross margin | 71.1% |
| Net margin | 55.6% |
| ROE | 76.3% |
| ROA | 58.1% |
| Current ratio | 3.91 |
| D/E | 0.07 |
| Net debt | −$51.52B |
| Free cash flow | $96.68B |
| P/E | 35.4× |
| EV/EBITDA | 29× |
| DCF intrinsic value | $50.63 / share |
| vs. current price ($174.68) | −71.1% overvalued on conservative DCF |


## Live Sample Reports

Here are a few generated reports produced by the tool (as of March 2026):
All links below are PDFs. GitHub renders them directly in your browser.  
(The PowerPoint versions are also in the same `sample_reports/` folder but must be downloaded to open.)

| Ticker       | Mode     | File Type | Direct Link |
|--------------|----------|-----------|-------------|
| **000333.SZ**| Annual   | PDF       | [000333.SZ_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/000333.SZ_ANNUAL_FINAL.pdf) |
| **6301.T**   | Annual   | PDF       | [6301.T_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/6301.T_ANNUAL_FINAL.pdf) |
| **AAPL**     | Annual   | PDF       | [AAPL_ANNUAL_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/AAPL_ANNUAL_FINAL.pdf) |
| **NVDA**     | TTM      | PDF       | [NVDA_TTM_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/NVDA_TTM_FINAL.pdf) |
| **TSLA**     | TTM      | PDF       | [TSLA_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/TSLA_TTM_FINAL.pdf) |
| **SAP.DE**   | TTM      | PDF       | [SAP.DE_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/SAP.DE_TTM_FINAL.pdf) |

All files include the three charts, full metrics table, DCF valuation and executive summary commentary, exactly as the notebook generates them.


*Built by GeorgeKGM2058. Started this to get comfortable pulling and processing real financial data across different markets. The report generation side grew from there.*
