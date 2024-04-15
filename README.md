# Data-Extraction
Source: Weather bit API
API link: f"https://api.weatherbit.io/v2.0/history/subhourly?lat=35.775&city=Syracuse,NY&start_date=2024-04-09&end_date=2024-04-10&tz=local&key={API_KEY}"

Libraries used in this code:
requests: The requests library in Python is a popular HTTP library for making HTTP requests to web servers. It provides a simple and elegant way to interact with websites and web services. With requests, you can send GET, POST, PUT, DELETE, and other HTTP requests, handle cookies, headers, and authentication, and parse JSON responses easily. 

csv: In Python, csv is both a module and a file format. As a module, csv provides functionality for reading and writing CSV (Comma-Separated Values) files. It allows you to easily handle CSV data, parse CSV files into Python data structures, and vice versa. The csv module is part of the Python standard library, so you don't need to install any additional packages to use it.

pandas: A Pandas DataFrame is a 2-dimensional labeled data structure with columns of potentially different data types. It is similar to a spreadsheet or SQL table, where each column represents a different variable, and each row represents a different observation.

The index=False parameter is used when writing a Pandas DataFrame to a CSV file to exclude the row indexes from being written to the file. When index=False is specified, the DataFrame is written without the index column, and only the data columns are included in the output CSV file. This can be useful when you don't want to include the index values as a separate column in the CSV file.
