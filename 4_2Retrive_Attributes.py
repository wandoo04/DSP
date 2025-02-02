################################################################
# -*- coding: utf-8 -*-
################################################################

print("5A. Topic: Program to retrieve different types of attributes")
import os
import pandas as pd

# Set base path and file names
base = 'C:/VKHCG'
input_file = '/01-Vermeulen/00-RawData/IP_DATA_ALL.csv'
output_dir = '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'

# Load data
file_path = f'{base}{input_file}'
data = pd.read_csv(file_path, encoding="latin-1")

# Create output directory if it doesn't exist
os.makedirs(f'{base}{output_dir}', exist_ok=True)

# Print data shape
print(f'Rows: {data.shape[0]}, Columns: {data.shape[1]}')

# Display columns and their types
print('### Raw Data Set ###')
for col in data.columns:
    print(f'{col}: {type(col)}')

# Fix column names (replace spaces with dots)
data.columns = [col.strip().replace(" ", ".") for col in data.columns]

# Set index name
data.index.name = 'RowID'

# Save the fixed data
output_file = f'{base}{output_dir}/Retrieve_IP_DATA.csv'
data.to_csv(output_file, index=True, encoding="latin-1")

print('### Done!! ###')
