import os
import pandas as pd

directory = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/Detail'
output_file = '/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/detail_merged_result(delemeter_comma).csv'

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

# Initialize an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Loop through each CSV file and append its data to the merged DataFrame
for csv_file in csv_files:
    file_path = os.path.join(directory, csv_file)
    # print(file_path)
    df = pd.read_csv(file_path)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

merged_df.insert(0, 'id', range(1, len(merged_df) + 1))

# Rename columns
# merged_df.columns = ['id', 'api_link', 'update_time', 'author', 'api_name', 'api_description', 'api_popularity',
#                      'api_latency', 'api_service_level']

# Rename columns
merged_df.columns = ['api_id', 'api_name', 'api_link', 'api_host', 'endpoint_name', 'endpoint_description',
                     'endpoint_category', 'endpoint_required_params', 'endpoint_optional_params']

# Convert 'update_time' to datetime format and format it as 'yyyy-mm-dd'
# merged_df['update_time'] = pd.to_datetime(merged_df['update_time'], errors='coerce').dt.strftime('%Y-%m-%d')

# # Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)

# Save the merged DataFrame to a new tab-separated file
# merged_df.to_csv(output_file, sep='\t', index=False)

print(merged_df.shape)

print(f"Merged data saved to {output_file}")
