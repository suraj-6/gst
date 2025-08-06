# GST & Tax Compliance Assistant
This project is a Python-based tool for managing transaction data with tax calculations for GST, TDS, and VAT, performing compliance checks, generating draft filing reports, and visualizing/reporting via a Streamlit web app.

Features
Load and process transaction data with different tax types

Dynamic GST, TDS, and VAT calculations using configurable rules

Compliance checker to flag missing GSTIN, mismatch in tax computations, and other errors

Generates draft filing-ready summary reports (CSV & Excel) for GST returns, TDS summaries, and VAT returns

Interactive Streamlit dashboard to:

Preview transaction data and tax reports

Download GST, TDS, and VAT reports as CSV files
<img width="1492" height="627" alt="Screenshot 2025-08-06 211701" src="https://github.com/user-attachments/assets/60bfd4b8-6ccd-4528-aa8d-52297b7367b9" />
Prerequisites
Python 3.7+

Required Python packages (install with pip)

bash
pip install -r requirements.txt
Example requirements.txt content:

text
pandas
numpy
streamlit
openpyxl

# Usage
Process Tax Data & Compliance Checks

Run the main processing script to calculate taxes, run compliance checks, and generate summary reports:

bash
python tax_processing.py
This will:

Read transaction data from data/sample_transactions.csv (or generate sample data)

Calculate GST, TDS, and VAT amounts dynamically as per tax rules

Check for compliance issues (missing GSTIN, calculation mismatches)

Export processed CSV with compliance status and remarks

Generate draft GST, TDS, and VAT reports in CSV and Excel formats under output/ folder
Run the Streamlit Dashboard

Start an interactive dashboard to view transactions and tax report summaries:

bash
streamlit run app.py
The dashboard provides:

A transaction data preview table

GST, TDS, and VAT summarized tables

CSV export buttons for reports

Access the dashboard locally (usually at http://localhost:8501).
Sample Data Format

<img width="1306" height="933" alt="Screenshot 2025-08-06 211441" src="https://github.com/user-attachments/assets/4bd1ba13-55fa-48e3-893c-69bd89e505d7" />

<img width="1067" height="836" alt="Screenshot 2025-08-06 211454" src="https://github.com/user-attachments/assets/d454fb3b-300a-46ee-b983-a7933696cbe6" />

How It Works
Tax Rules: Stored in JSON format inside the code (can be externalized). Includes GST rates for goods and services, TDS slabs, VAT rates.

Dynamic Calculations: Based on tax type and category, rates are applied to transaction amounts.

Compliance Checks: Flags missing GSTIN for GST/VAT entries, mismatched tax amounts, and other issues.

Reports: Aggregated taxable amounts and tax collected per GSTIN grouped by categories, saved as CSV and Excel files.

Dashboard: Uses Streamlit for interactive exploration and report download.
License
Feel free to modify and use this project as per your requirements.

Contact
For questions or improvements, please open an issue or submit a pull request in the GitHub repository.

