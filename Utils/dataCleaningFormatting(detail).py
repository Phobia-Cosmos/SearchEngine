import pandas as pd

# Read data from the CSV file
file_path = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/detail_merged_result(delemeter_comma).csv'
data = pd.read_csv(file_path, delimiter=',')

# data = data.replace({'|': '&&'}, regex=True)
data = data.replace({'\n': ' ', '\t': ''}, regex=True)

# Fill null values in update_time column with '0000-00-00'
data['endpoint_category'].fillna('General', inplace=True)
data['endpoint_description'].fillna('None', inplace=True)

# Write the updated data to a new CSV file with line terminator '\n'
new_file_path = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/detail_merged_result.csv'
data.to_csv(new_file_path, sep='\t', index=False)
