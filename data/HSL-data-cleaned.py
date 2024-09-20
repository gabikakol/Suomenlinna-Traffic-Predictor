import pandas as pd

# Load the dataset
df = pd.read_csv('~/data/Suomenlinna-Traffic-Predictor/data/HSL-data.csv', delimiter=';', low_memory=False)

# Print column names to verify
print("Original columns:", df.columns.tolist())

# Select the relevant columns
filtered_df = df[['VUOSI', 'KUUKAUSI', 'KUUKAUSIPÄIVÄ', 'TUNTI', 'SUUNTA', 'PYSÄKKI', 'NOUSIJAT']]

# Convert relevant columns to numeric, setting errors='coerce' to handle non-numeric values
for col in ['VUOSI', 'KUUKAUSI', 'KUUKAUSIPÄIVÄ', 'TUNTI', 'SUUNTA', 'PYSÄKKI', 'NOUSIJAT']:
    filtered_df[col] = pd.to_numeric(filtered_df[col], errors='coerce').fillna(0).astype(int)

# Rename columns
filtered_df.rename(columns={
    'VUOSI': 'Year',
    'KUUKAUSI': 'Month',
    'KUUKAUSIPÄIVÄ': 'Day',
    'TUNTI': 'Hour',
    'SUUNTA': 'Direction',
    'PYSÄKKI': 'Stop',
    'NOUSIJAT': 'Passengers'
}, inplace=True)

# Verify new column names
print("Renamed columns:", filtered_df.columns.tolist())

# Filter the rows where Stop is 98 or 99
filtered_df = filtered_df[filtered_df['Stop'].isin([98, 99])]

# Save the filtered data to a new CSV file
filtered_df.to_csv('HSL_filtered_data.csv', index=False)

print("Filtered data has been saved to 'HSL_filtered_data.csv'")
