import requests
import csv

API_KEY = 'c679e8985d0a44649e46737b5268b72f'
url = f'https://api.weatherbit.io/v2.0/history/subhourly?lat=35.775&city=Syracuse,NY&start_date=2024-04-09&end_date=2024-04-10&tz=local&key={API_KEY}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['data']  #This line extracts the JSON data from the API response and assigns it to the data variable. It assumes that the JSON response has a key named 'data' containing a list of dictionaries, where each dictionary represents a row of data.
    filepath = 'weather_data_subhourly_syracuse.csv'
    # write the data to a csv file 
    with open(filepath, mode='w', newline='') as file: #This line opens the CSV file in write mode. The newline='' argument is used to ensure that no extra newline characters are added between rows.
        # This line creates a DictWriter object, which allows writing dictionaries as rows in the CSV file. It uses the keys of the first dictionary in the data list as the column headers (field names) for the CSV file.
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()  #This line writes the header row (column names) to the CSV file.
        for item in data: #This line iterates over each dictionary (item) in the data list.
            writer.writerow(item)  #This line writes each dictionary (item) as a row in the CSV file.
    print(f'Data saved to {filepath}')
else:
    print(f'Failed to fetch data: {response.status_code}')