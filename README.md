# Personal Finance Dashboard Project

## Introduction

This project aims to create a comprehensive personal finance dashboard using Google Sheets, Python, and Power BI. The goal is to visualize financial transactions to gain better insights into personal spending habits and financial health. This README file outlines the problem statements, deliverables, and technical details, including the Python code used to link Google Sheets with Power BI and the DAX formulas implemented to create the desired visualizations.

## Problem Statements

1. **Data Consolidation**: Collecting and managing all personal finance transactions in a single, organized Google Sheet.
2. **Multi-Currency**: Convert the data into PKR by fetching the daily conversion rate from the internet.
3. **Data Integration**: Automating the process of fetching data from Google Sheets and integrating it with Power BI for visualization.
4. **Visualization**: Creating interactive and insightful visualizations in Power BI to monitor income, expenses, savings, and investment trends.
5. **Insights Generation**: Utilizing DAX formulas to generate meaningful insights from the data.

## Deliverables

1. **Google Sheets Setup**: A well-structured Google Sheet for logging personal finance transactions.
2. **Python Script**: A Python script to link Google Sheets with Power BI.
3. **Power BI Dashboard**: An interactive dashboard in Power BI showcasing various financial metrics.
4. **DAX Formulas**: Custom DAX formulas to create calculated columns and measures for enhanced analysis.

## Python Code for Linking Google Sheets with Power BI

```python
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Your Google Sheet Name").sheet1

# Get all records from the sheet
data = sheet.get_all_records()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file for Power BI import
df.to_csv('personal_finance_data.csv', index=False)
```

## Power BI Dashboard

### DAX Formulas Used

Below are some of the DAX formulas used to create the calculated columns and measures in the Power BI dashboard:

1. **Total Income**
   ```DAX
   Total Income = SUM(Finance[Income])
   ```

2. **Total Expenses**
   ```DAX
   Total Expenses = SUM(Finance[Expenses])
   ```

3. **Net Savings**
   ```DAX
   Net Savings = [Total Income] - [Total Expenses]
   ```

4. **Monthly Average Income**
   ```DAX
   Monthly Average Income = AVERAGEX(SUMMARIZE(Finance, Finance[Month], "MonthlyIncome", [Total Income]), [MonthlyIncome])
   ```

5. **Monthly Average Expenses**
   ```DAX
   Monthly Average Expenses = AVERAGEX(SUMMARIZE(Finance, Finance[Month], "MonthlyExpenses", [Total Expenses]), [MonthlyExpenses])
   ```

6. **Expense Breakdown by Category**
   ```DAX
   Expense Breakdown = CALCULATE(SUM(Finance[Expenses]), ALLEXCEPT(Finance, Finance[Category]))
   ```

### Here is the screenshot representing the organization of all the DAX Measures

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/26ef75c5-86e1-47b7-af62-2b81c504280c)


### Screenshots

#### Google Sheets

_Here is a screenshot from the Google Sheet that has the transactions data_

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/b4010796-08b1-4188-a35f-65a9e8415c7f)


#### Power BI Dashboard

_Here is the screenshot from the [DRAFT] Power BI Dashboard_

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/708b6bbf-6010-4071-9ac5-269c85b229a8)


## Conclusion

This project demonstrates the effective use of Google Sheets, Python, and Power BI to manage and visualize personal finance data. The integration of these tools provides a powerful way to track financial health, identify spending patterns, and make informed financial decisions. The Python script and DAX formulas showcase the technical skills involved in automating data workflows and creating meaningful visualizations.

## Contact

For any queries or further information, please contact me at zohaib8989@gmail.com
