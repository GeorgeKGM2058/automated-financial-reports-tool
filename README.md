# Automated Financial Analysis & Reporting Pipeline

This tool was created to shorten the time of manually pulling live financials from Yahoo Finance every time I wanted to look at a stock.
It grabs income statements, balance sheets, and cash flows, calculates useful ratios, runs a two-stage DCF with live country risk premiums from Damodaran and exports a PDF report, PowerPoint and CSV per stock.

Disclaimer: This is for learning and quick analysis. Data comes from Yahoo Finance and may contain errors or delays and the DCF is a simplified model. Should not be used for investment decisions, not financial advice.


## What it actually does

For each ticker you throw in:

1. Pulls the following statements, income statement, balance sheet and cash flow. (annual by default, TTM is experimental)
2. Converts everything to USD if it's a non-US stock (using live exchange rates)
3. Computes 14 ratios: margins, ROE/ROA, liquidity stuff, leverage, FCF, etc.
4. Runs a two-stage DCF (5-year forecast based on historical revenue CAGR, then terminal value)
4. Creates 3 charts: revenue history + forecast, a key ratios bar chart and a cash flow waterfall
5. Finally it exports the PDF, PPTX, and even a CSV in the `Financial_Results` folder.

I default to annual mode because TTM can be flaky on international tickers — quarterly data on Yahoo isn't always clean.
TTM mode is available by changing `use_ttm=False` to `use_ttm=True` in the last cell. 
Tested it on TSLA, NVDA, AAPL, MSFT and a few international tickers (6301.T, 6501.T, 000333.SZ, SAP.DE, NESN.SW, ASML.AS).


## How to run

### Option 1 - Google Colab - Easiest way with no setup at all
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeorgeKGM2058/automated-financial-reports-tool/blob/main/financial_analysis_tool.ipynb)
Just click here and run all cells. Outputs will appear in the `Financial_Results/` folder on the left.

### Option 2 — Local way (Jupyter or VS Code)

```bash
git clone https://github.com/GeorgeKGM2058/automated-financial-reports-tool.git
cd automated-financial-reports-tool
pip install -r requirements.txt         # Python 3.7+
jupyter notebook financial_analysis_tool.ipynb
```


## DCF methodology

I kept the model pretty straightforward, avoided getting too complicated:

Risk-free rate ~4.19% (early 2026 10y Treasury)
Equity risk premium 5%
Country risk premium pulled live from Damodaran
Revenue growth capped between 3–15%
Terminal growth 3%

Beta comes from yfinance, so it's US-centric, but the country premium helps a bit for international names. 
Terminal value is a big chunk of the total (WACC & terminal growth assumptions).


## Live Sample Reports

Here are a few generated reports produced by the tool: 

 000333.SZ  [000333.SZ_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/000333.SZ_ANNUAL_FINAL.pdf)
 6301.T     [6301.T_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/6301.T_ANNUAL_FINAL.pdf)
 AAPL       [AAPL_ANNUAL_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/AAPL_ANNUAL_FINAL.pdf)
 NVDA       [NVDA_TTM_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/NVDA_TTM_FINAL.pdf)
 TSLA       [TSLA_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/TSLA_TTM_FINAL.pdf)
 SAP.DE     [SAP.DE_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/SAP.DE_TTM_FINAL.pdf)

If something breaks, it's probably because Yahoo changed the data formats.


Started building this over a few months to get better at handling real financial data across markets, analyze them and view the result lighting-fast. 