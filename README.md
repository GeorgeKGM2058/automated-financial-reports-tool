# Financial Analysis & Valuation Tool

Automated Python tool that pulls real-time financial data from Yahoo Finance, computes key ratios, forecasts revenue using CAGR, performs basic DCF valuation, and generates professional PDF + PPTX reports with executive summaries, tables, and charts.

Supports global tickers (US, Japan, China, Europe) with automatic currency conversion to USD.

## Disclaimer
- This tool is for educational and informational purposes only. It uses publicly available data from Yahoo Finance, which may contain errors, delays, or inaccuracies. The DCF valuations and forecasts are based on simplified models (e.g., historical CAGR without advanced adjustments) and may not reflect real-world market conditions—results can vary significantly from professional analyses.
- **Not Financial Advice**: Do not use this tool for investment decisions. Consult a qualified financial advisor before making any investments. The author assumes no responsibility or liability for any errors, omissions, or losses incurred from using this tool.

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
- yfinance (data fetching)
- pandas, numpy (processing)
- matplotlib (charts)
- reportlab (PDF), python-pptx (PowerPoint)
- Currency conversion via Yahoo forex tickers

## How to Run

You can run the tool in two ways: directly in Google Colab (easiest, no installation needed) or locally on your computer.

### Option 1: Run in Google Colab (Recommended for quick testing)
1. Open the notebook directly in Colab:
   [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeorgeKGM2058/automated-financial-reports-tool/blob/main/financial-analysis-tool.ipynb)

2. Run all cells (Runtime → Run all).
   - The cell installs all dependencies automatically.
   - Change the `tickers` list at the bottom to analyze your own stocks.
   - Outputs (PDFs, PPTX, CSVs) will appear in the `Financial_Results/` folder in the Colab's file browser — right-click to download them from there.

### Option 2: Run Locally (Jupyter Notebook or VS Code)
1. Clone the repository:
   ```bash
   git clone https://github.com/GeorgeKGM2058/financial-analysis-tool.git
   cd automated-financial-reports-tool

Remember to edit the tickers list at the bottom to analyze your own favourite stocks!

