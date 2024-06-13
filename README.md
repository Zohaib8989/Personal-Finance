# Personal Finance Dashboard Project

## Introduction

In this project, I used Google Sheets to store transactional data, linked to Power BI via the web connector. Utilizing Power Query, I cleaned and transformed the data, then modeled it with various date tables. I took daily conversion rates to convert transactions into the home currency (PKR). Using DAX, I created custom KPIs and developed insightful charts and graphs in Power BI to visualize multi-currency transactions. The final dashboard employs the scheduled refresh feature, ensuring users always see the most up-to-date information. This summary is part of the README file in the GitHub repository, showcasing my skills in data integration, modeling, and visualization.

### Problem Statement

- **Challenge:** Managing personal finances is challenging, especially with transactions in multiple currencies.
- **Data Issues:** Scattered data and complex currency conversion issues hinder clear and timely financial insights.
- **Traditional Tools:** Traditional tools fall short in providing real-time, actionable information.
- **Project Solution:**
  - Integrates, models, and visualizes financial data from Google Sheets in Power BI.
  - Converts all transactions into the home currency (PKR) for consistency.
  - Utilizes a dynamic dashboard with scheduled refreshes to offer real-time insights.

### Deliverables

- **Integrated Data Platform:** Google Sheets integrated with Power BI via web connector for seamless data flow.
- **Data Modeling:** Utilization of Power Query for cleaning and transforming raw transactional data.
- **Currency Conversion:** Implementation of daily conversion rates to unify transactions into PKR.
- **Dynamic Dashboard:** Creation of interactive charts and graphs in Power BI to visualize financial insights.
- **Scheduled Refresh:** Setup of scheduled refresh feature to ensure the dashboard reflects real-time data updates.

## Python Code for Linking Google Sheets with Power BI

```python
import gspread
import pandas as pd

# Copy and paste the content of your JSON file here
service_account_info = { JSON file content }

# Authenticate using the service account key content
gc = gspread.service_account_from_dict(service_account_info)

# Open the Google Sheets spreadsheet named "Personal Finance"
sh = gc.open("Personal Finance")

# Select the worksheet named "Transactions"
transactions_sheet = sh.worksheet("Transactions")

# Get all the values from the "Transactions" worksheet, excluding the first row
transactions_values = transactions_sheet.get_all_values()[1:]
# Use the first row as column headers for "Transactions"
transactions_headers = transactions_values[0]

# Create a list of dictionaries with keys from the headers for "Transactions"
transactions_data = [dict(zip(transactions_headers, row)) for row in transactions_values[1:]]

# Convert the list of dictionaries to a Pandas DataFrame for "Transactions"
transactions_df = pd.DataFrame(transactions_data)

# Select the worksheet named "USD/PKR"
usd_pkr_sheet = sh.worksheet("USD/PKR")

# Get all the values from the "USD/PKR" worksheet, including the first row
usd_pkr_values = usd_pkr_sheet.get_all_values()

# Use the first row as column headers for "USD/PKR"
usd_pkr_headers = usd_pkr_values[0]

# Create a list of dictionaries with keys from the headers for "USD/PKR"
usd_pkr_data = [dict(zip(usd_pkr_headers, row)) for row in usd_pkr_values[1:]]

# Convert the list of dictionaries to a Pandas DataFrame for "USD/PKR"
usd_pkr_df = pd.DataFrame(usd_pkr_data)

# Convert the "Rate" column to a numeric data type with 2 decimal places
usd_pkr_df["Rate"] = pd.to_numeric(usd_pkr_df["Rate"], errors="coerce").round(2)

# Print the DataFrames
print("Transactions DataFrame:")
print(transactions_df)
print("\nUpdated USD/PKR DataFrame:")
print(usd_pkr_df)
```

## Power BI Dashboard

### DAX Formulas Used

Below are some of the DAX formulas used to create the calculated columns and measures in the Power BI dashboard:

1. **Total Income**
   ```DAX
   Total Income = 
    CALCULATE(
        SUM(Transactions[Transaction Amount]),  // Calculate the sum of 'Transaction Amount' for Total Income
        CONTAINSSTRING(Transactions[Type], "Getting")  // Filter transactions where 'Type' contains the substring "Getting"
    )
   ```

2. **Total Expenses**
   ```DAX
   Total Spending = ABS(  // Calculate the absolute value of Total Spending
    CALCULATE(
        SUM(Transactions[Transaction Amount]),  // Calculate the sum of 'Transaction Amount' for Total Spending
        CONTAINSSTRING(Transactions[Type], "Spending")  // Filter transactions where 'Type' contains the substring "Spending"
    ))
   ```

3. **Net Savings**
   ```DAX
   Total Spending = ABS(  // Calculate the absolute value of Total Spending
    CALCULATE(
        SUM(Transactions[Transaction Amount]),  // Calculate the sum of 'Transaction Amount' for Total Spending
        CONTAINSSTRING(Transactions[Type], "Spending")  // Filter transactions where 'Type' contains the substring "Spending"
    ))
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

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/60319095-f9a3-4be4-b92c-ad0a0ede4a4b)



## Conclusion

This project demonstrates the effective use of Google Sheets, Python, and Power BI to manage and visualize personal finance data. The integration of these tools provides a powerful way to track financial health, identify spending patterns, and make informed financial decisions. The Python script and DAX formulas showcase the technical skills involved in automating data workflows and creating meaningful visualizations.

## Contact

For any queries or further information, please contact me at zohaib8989@gmail.com
