import pandas as pd
import os

# Define the data types for each column
# dtypes = {
#     'api_name': str,
#     'api_link': str,
#     'api_host': str,
#     'endpoint_name': str,
#     'endpoint_description': str,
#     'endpoint_category': str,
#     'endpoint_required_params': str,
#     'endpoint_optional_params': str
# }
# ----------------------------------------------------------------统计行数
csv_directory = "/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/Basic"

total_rows = 0

# Loop through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(csv_directory, filename)

        # Read the CSV file and count rows
        df = pd.read_csv(filepath)
        rows_in_file = len(df)

        if total_rows == 0:
            print(df.head(1))

        # Increment the total row count
        total_rows += rows_in_file

# Print the total number of rows across all CSV files
print(f"Total Rows: {total_rows}")

# ----------------------------------------------------------------统计空值
# Read data from the CSV file with specified data types
file_path = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/detail_merged_result(delemeter_comma).csv'
df = pd.read_csv(file_path, delimiter=',')

null_summary = df.isnull().sum()

# Display the summary
print(null_summary)
