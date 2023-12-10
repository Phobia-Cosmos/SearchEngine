import pandas as pd

# Read the CSV file with the specified delimiter
file_path = "/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/basic_merged_result(delemeter_comma).csv"
data = pd.read_csv(file_path, delimiter=',')

# Save the data with a different delimiter
new_file_path = "/Users/liuzihao/Desktop/Full_Development/Projects/Crawler/RESTful-API-Crawler/RESTful-API-Crawler/Result/basic_merged_result.csv"
data.to_csv(new_file_path, sep='\t', index=False)
