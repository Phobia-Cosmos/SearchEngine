import pandas as pd

# Read data from the CSV file
file_path = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/basic_merged_result(delemeter_comma).csv'
data = pd.read_csv(file_path, delimiter=',')

# Process the api_latency column
data['api_latency'] = data['api_latency'].replace({',': '', ' ms': ''}, regex=True)

# Change the update_time column's date delimiter to '-'
data['update_time'] = pd.to_datetime(data['update_time'], format='%Y/%m/%d').dt.strftime('%Y-%m-%d')

# Remove '%' from the api_service_level column
data['api_service_level'] = data['api_service_level'].replace({'%': ''}, regex=True)

# Fill null values in update_time column with '0000-00-00'
data['update_time'].fillna('1000-01-01', inplace=True)

# Replace ';' with '.' in all columns
data = data.replace({';': '.', '\n': ' '}, regex=True)

# Fill null values with 0 in specified columns
# columns_to_fill = ['api_popularity', 'api_latency', 'api_service_level']
# data[columns_to_fill] = data[columns_to_fill].fillna(0)

# Drop rows where all columns are empty
data = data.fillna(0).dropna(how='all')

# Write the updated data to a new CSV file with line terminator '\n'
new_file_path = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/basic_merged_result.csv'
data.to_csv(new_file_path, sep=';', index=False)
