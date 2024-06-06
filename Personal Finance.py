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