import pandas as pd

# Load the dataset
df = pd.read_csv('data/HSL-data.csv', delimiter=';', low_memory=False)

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

filtered_df.rename(columns={'VUOSI': 'Year'}, inplace=True)
filtered_df.rename(columns={'KUUKAUSI': 'Month'}, inplace=True)
filtered_df.rename(columns={'KUUKAUSIPÄIVÄ': 'Day'}, inplace=True)
filtered_df.rename(columns={'TUNTI': 'Hour'}, inplace=True)
filtered_df.rename(columns={'SUUNTA': 'Direction'}, inplace=True)
filtered_df.rename(columns={'PYSÄKKI': 'Stop'}, inplace=True)
filtered_df.rename(columns={'NOUSIJAT': 'Passengers'}, inplace=True)


# Save the filtered data to a new CSV file
filtered_df.to_csv('HSL-data-cleaned.csv', index=False)

print("Cleaned data has been saved")
