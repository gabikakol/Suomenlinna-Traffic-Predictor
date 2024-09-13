import requests
import csv

# URL to fetch the ferry traffic data
base_url = "https://hsl.louhin.com/api/1.0/data/257001"

# Use this if you're including Authorization in the header
headers = {
    "Authorization": "LWS d59c041a-2ad1-4beb-b769-b9d7ea3a5628"
}


# Fetch data with offset and limit if needed
params = {
    "offset": 545844  # Starting point (you can adjust this)
    #"limit": 100  # Number of rows to retrieve (adjust if needed)
}

# Make the request
response = requests.get(base_url, headers=headers, params=params)

# Check the response status
if response.status_code == 200:
    # Get the CSV data as text
    csv_data = response.text

    # Save the data to a CSV file
    with open('HSL-data.csv', 'w', newline='', encoding='utf-8') as file:
        file.write(csv_data)

    print("CSV file created and saved as 'HSL-data.csv'")
else:
    print(f"Error: {response.status_code}, {response.text}")
