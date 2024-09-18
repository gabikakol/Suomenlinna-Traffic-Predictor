import pandas as pd

# Load the CSV file
file_path = 'data/weather-data.csv'  # Update with the correct path to your file
df = pd.read_csv(file_path)

# Convert the 'Time [Local time]' column from XX:XX to XX
df['Time [Local time]'] = df['Time [Local time]'].apply(lambda x: x.split(':')[0])

# Rename the 'Time [Local time]' column to 'Hour'
df.rename(columns={'Time [Local time]': 'Hour'}, inplace=True)
df.rename(columns={'Average temperature [°C]': 'Average temperature'}, inplace=True)
df.rename(columns={'Wind speed [m/s]': 'Wind speed'}, inplace=True)
df.rename(columns={'Precipitation [mm]': 'Precipitation'}, inplace=True)

df["Hour"] = pd.to_numeric(df["Hour"], errors='coerce').fillna(0).astype(int)

# Remove the 'Observation station' column
df.drop(columns=['Observation station'], inplace=True)

# Save the modified dataframe back to a new CSV file
output_file_path = 'weather-data-cleaned.csv'  # Update with desired output file path
df.to_csv(output_file_path, index=False)

print("Time column updated, renamed to 'Hour', and 'Observation station' column removed. Saved to:", output_file_path)
