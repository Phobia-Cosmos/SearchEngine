import os
import pandas as pd
import configparser

def merge_and_rename(delimiter='\t', rename_columns=None):
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Get input and output directories from the config file
    input_basic_dir = config['Directories']['input_basic']
    input_detail_dir = config['Directories']['input_detail']
    output_basic_dir = config['Directories']['output_basic']
    output_detail_dir = config['Directories']['output_detail']

    # Get column names from the config file
    basic_columns = config['Columns']['basic_columns'].split(', ')
    detail_columns = config['Columns']['detail_columns'].split(', ')

    # Merge and rename for basic data
    merge_and_rename_files(input_basic_dir, output_basic_dir, basic_columns, delimiter=delimiter, rename_columns=rename_columns)

    # Merge and rename for detail data
    merge_and_rename_files(input_detail_dir, output_detail_dir, detail_columns, delimiter=delimiter, rename_columns=rename_columns)

def merge_and_rename_files(input_dir, output_dir, columns, delimiter='\t', rename_columns=None):
    # Get a list of all CSV files in the input directory
    csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

    # Initialize an empty DataFrame to store the merged data
    merged_df = pd.DataFrame()

    # Loop through each CSV file and append its data to the merged DataFrame
    for csv_file in csv_files:
        file_path = os.path.join(input_dir, csv_file)
        df = pd.read_csv(file_path, delimiter=delimiter)
        merged_df = pd.concat([merged_df, df], ignore_index=True)

    # Add a new column (e.g., 'api_id') based on the length of the DataFrame
    merged_df.insert(0, 'id', range(1, len(merged_df) + 1))

    # # Rename columns
    # if rename_columns:
    #     merged_df.columns = rename_columns


    # Save the merged DataFrame to a new CSV file in the output directory
    output_file = os.path.join(output_dir, f'{output_dir.split("/")[-1]}_{delimiter}.csv')
    merged_df.to_csv(output_file, sep=delimiter, index=False)

    print(f"Merged and renamed data saved to {output_file}")

if __name__ == '__main__':
    merge_and_rename()
