import pandas as pd

# Load the dataset
df = pd.read_csv('~/datascience/Suomenlinna-Traffic-Predictor/data/HSL-data.csv', delimiter=';', low_memory=False)

# Select the relevant columns
filtered_df = df[['VUOSI', 'KUUKAUSI', 'KUUKAUSIPÄIVÄ', 'TUNTI', 'SUUNTA', 'PYSÄKKI', 'NOUSIJAT']]

# Convert relevant columns to numeric, setting errors='coerce' to handle non-numeric values
filtered_df['VUOSI'] = pd.to_numeric(filtered_df['VUOSI'], errors='coerce').fillna(0).astype(int)
filtered_df['KUUKAUSI'] = pd.to_numeric(filtered_df['KUUKAUSI'], errors='coerce').fillna(0).astype(int)
filtered_df['KUUKAUSIPÄIVÄ'] = pd.to_numeric(filtered_df['KUUKAUSIPÄIVÄ'], errors='coerce').fillna(0).astype(int)
filtered_df['TUNTI'] = pd.to_numeric(filtered_df['TUNTI'], errors='coerce').fillna(0).astype(int)
filtered_df['SUUNTA'] = pd.to_numeric(filtered_df['SUUNTA'], errors='coerce').fillna(0).astype(int)
filtered_df['PYSÄKKI'] = pd.to_numeric(filtered_df['PYSÄKKI'], errors='coerce').fillna(0).astype(int)
filtered_df['NOUSIJAT'] = pd.to_numeric(filtered_df['NOUSIJAT'], errors='coerce').fillna(0).astype(int)

# Save the filtered data to a new CSV file
filtered_df.to_csv('HSL_filtered_data.csv', index=False)

print("Filtered data has been saved to 'HSL_filtered_data.csv'")
