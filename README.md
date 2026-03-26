# Automated Financial Analysis & Reporting Tool

This tool was created to shorten the time of manually pulling live financials from Yahoo Finance every time I wanted to check a stock's KPIs.
It grabs income statements, balance sheets and cash flows, then calculates useful ratios, 
runs a two-stage DCF with live country risk premiums from Damodaran and finally exports a PDF report, PowerPoint and CSV per stock.

Disclaimer: 
This is for learning and quick analysis. 
Data comes from Yahoo Finance and may contain errors or delays. 
Also the DCF is a simplified model. 
The results should not be used for investment decisions, not financial advice.


## What the project does

For each ticker you throw in it is designed to pull the income statement, balance sheet and cash flow 
(annual by default, TTM is an experimental mode). 
Then is converts everything to USD if it's a non-US stock (it uses live exchange rates). 
It will compute 14 ratios: margins, ROE/ROA, liquidity stuff, leverage, FCF, etc. 
Then is will run a two-stage DCF with a 5-year forecast based on historical revenue CAGR and terminal value after that.
Finally it creates 3 charts: revenue history & forecast, a key ratios bar chart and a cash flow "waterfall".
For each stock everything is put into a PDF and PPTX file and it will even produce a CSV, all in the `Financial_Results` folder.

I default to annual mode because TTM often has issues on international tickers, quarterly data on Yahoo isn't always clean. 
The TTM mode is available by changing `use_ttm=False` to `use_ttm=True` in the last cell. 
Tested it on TSLA, NVDA, AAPL, MSFT and a few international tickers (6301.T, 6501.T, 000333.SZ, SAP.DE, NESN.SW, ASML.AS).


## How to run

### Option 1 - Google Colab - Easiest way with no setup at all
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeorgeKGM2058/automated-financial-reports-tool/blob/main/financial_analysis_tool.ipynb)
Just click here and run all cells. Outputs will appear in the `Financial_Results/` folder on the left.

### Option 2 - Local way (Jupyter or VS Code)

```bash
git clone https://github.com/GeorgeKGM2058/automated-financial-reports-tool.git
cd automated-financial-reports-tool
pip install -r requirements.txt         # Python 3.7+
jupyter notebook financial_analysis_tool.ipynb
```


## DCF methodology

I avoided getting too complicated with the model:

Risk-free rate ~4.19% (early 2026 10y treasury) 
Equity risk premium 5% 
Country risk premium pulled live from Damodaran 
Revenue growth capped between 3–15% 
Terminal growth 3% 
Beta comes from yfinance, so it's US-centric, but the country premium helps a bit for international tickers. 
Terminal value is a big chunk of the total (WACC and terminal growth assumptions). 
If something breaks, it's probably because Yahoo changed the data formats.


## Live sample reports

Here are a few generated reports produced by the tool: 

 000333.SZ  [000333.SZ_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/000333.SZ_ANNUAL_FINAL.pdf)
 6301.T     [6301.T_ANNUAL_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/6301.T_ANNUAL_FINAL.pdf)
 AAPL       [AAPL_ANNUAL_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/AAPL_ANNUAL_FINAL.pdf)
 NVDA       [NVDA_TTM_FINAL.pdf](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/NVDA_TTM_FINAL.pdf)
 TSLA       [TSLA_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/TSLA_TTM_FINAL.pdf)
 SAP.DE     [SAP.DE_TTM_FINAL.pptx](https://github.com/GeorgeKGM2058/automated-financial-reports-tool/blob/main/sample_reports/SAP.DE_TTM_FINAL.pdf)


By GeorgeKGM2058. 
I started building this project to get better at handling live financial data across markets, 
analyze them and get presentable results fast. 