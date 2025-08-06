import streamlit as st
import pandas as pd

# Load your processed transactions CSV
df = pd.read_csv('data/sample_transactions.csv')

st.title("GST & Tax Compliance Dashboard")

# Show all transactions data preview
st.write("## All Transactions")
st.dataframe(df)

# GST Return Report
gst_report = df[df['tax_type'] == 'GST'].groupby(['GSTIN', 'GST_category']).agg({
    'amount': 'sum',
    'GST_amount': 'sum'
}).reset_index()

st.write("## GST Return Report")
st.dataframe(gst_report)

st.download_button(
    label="Download GST Report (CSV)",
    data=gst_report.to_csv(index=False),
    file_name='gst_report.csv',
    mime='text/csv'
)

# TDS Summary Report
tds_report = df[df['tax_type'] == 'TDS'].groupby(['GSTIN']).agg({
    'amount': 'sum',
    'TDS_amount': 'sum'
}).reset_index()

st.write("## TDS Summary Report")
st.dataframe(tds_report)

st.download_button(
    label="Download TDS Report (CSV)",
    data=tds_report.to_csv(index=False),
    file_name='tds_report.csv',
    mime='text/csv'
)

# VAT Return Report
vat_report = df[df['tax_type'] == 'VAT'].groupby(['GSTIN']).agg({
    'amount': 'sum',
    'VAT_amount': 'sum'
}).reset_index()

st.write("## VAT Return Report")
st.dataframe(vat_report)

st.download_button(
    label="Download VAT Report (CSV)",
    data=vat_report.to_csv(index=False),
    file_name='vat_report.csv',
    mime='text/csv'
)
