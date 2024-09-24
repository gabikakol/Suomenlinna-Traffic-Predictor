import pandas as pd

# Read the CSV file
csv_file = ('data/combined-data.csv')  # Replace with your CSV file path
data = pd.read_csv(csv_file)

# Save the data to an Excel file
excel_file = 'data/combined-data.xlsx'  # Replace with your desired Excel file path
data.to_excel(excel_file, index=False)

print(f"CSV file '{csv_file}' has been converted to Excel file '{excel_file}'.")
