import pandas as pd

# Load the two CSV files into pandas DataFrames
hsl_data = pd.read_csv('data/HSL-data-cleaned.csv')
weather_data = pd.read_csv('data/weather-data-cleaned.csv')

# Define the common keys for merging
merge_keys = ['Year', 'Month', 'Day', 'Hour']

# Merge the datasets on the common key values
merged_data = pd.merge(hsl_data, weather_data, on=merge_keys, how='inner')

for col in ['Average temperature', 'Wind speed', 'Precipitation']:
    merged_data[col] = pd.to_numeric(merged_data[col], errors='coerce').fillna(0).astype(float)

# Check the first few rows of the merged dataset
print(merged_data.head())

# Save the merged dataset to a new CSV file
merged_data.to_csv('data/combined-data.csv', index=False)

print("Merged data saved to 'combined-data.csv'")
