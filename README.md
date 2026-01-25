# Financial Analysis & Valuation Tool

Automated Python tool that pulls real-time financial data from Yahoo Finance, computes key ratios, forecasts revenue using CAGR, performs basic DCF valuation, and generates professional PDF + PPTX reports with executive summaries, tables, and charts.

Supports global tickers (US, Japan, China, Europe) with automatic currency conversion to USD.

## Features
- Fetches income statements, balance sheets, cash flows via **yfinance**
- Calculates core ratios: ROE, ROA, margins, liquidity, leverage, FCF, P/E
- Revenue forecasting using **CAGR** (compound annual growth rate) with two-stage projection
- Basic **DCF valuation**: 5-year explicit FCF + Gordon terminal value, WACC from CAPM
- Multi-format output: PDF (reportlab), PPTX (python-pptx), CSV metrics export
- Clean executive commentary with DCF upside/downside signals
- Tested on: TSLA, NVDA, AAPL, MSFT, 6301.T (Komatsu), 000333.SZ (Midea), SAP.DE, NESN.SW (Nestlé), ASML.AS, etc.

## Tech Stack
- Python 3
- yfinance (data), pandas & numpy (processing), matplotlib (charts)
- statsmodels (optional fallback), reportlab (PDF), python-pptx (PowerPoint)
- Currency conversion via Yahoo forex tickers

## How to Run

You can run the tool in two ways: directly in Google Colab (easiest, no installation needed) or locally on your computer.

### Option 1: Run in Google Colab (Recommended for quick testing)
1. Open the notebook directly in Colab:
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SimoDeMores/financial-analysis-tool/blob/main/financial_analysis_tool.ipynb)

2. Run cell (Or Runtime → Run all).
   - The cell installs all dependencies automatically.
   - Change the `tickers` list at the bottom to analyze your own stocks.
   - Outputs (PDFs, PPTX, CSVs) will appear in the `Financial_Results/` folder in Colab's file browser — download them from there.

### Option 2: Run Locally (Jupyter or VS Code)
1. Clone the repository:
   ```bash
   git clone https://github.com/SimoDeMores/financial-analysis-tool.git
   cd financial-analysis-tool

Remember to edit the tickers list and outdir at the bottom to analyze your own stocks!
