import streamlit as st

st.title("Automated Financial Reports Tool")
st.markdown("Real-time stock data → ratios → forecasts → DCF → PDF + PPTX reports")

st.markdown("[Run the full notebook (one click)](https://colab.research.google.com/github/GeorgeKGM2058/automated-financial-reports-tool/blob/main/01_financial_analysis_demo.ipynb)")

st.subheader("Sample Outputs")
col1, col2 = st.columns(2)
with col1:
    st.download_button("Download Sample PDF", "valuation_report.pdf", "valuation_report.pdf")
with col2:
    st.download_button("Download Sample PPTX", "presentation.pptx", "presentation.pptx")
