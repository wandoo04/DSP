import pandas as pd
################################################################
print('4D. Outlier Detection')
import pandas as pd

# File paths
base = 'C:/VKHCG'
input_file = '01-Vermeulen/00-RawData/IP_DATA_CORE.csv'

# Load data
file_path = f'{base}/{input_file}'
data = pd.read_csv(file_path, usecols=['Country', 'Place Name', 'Latitude', 'Longitude'], encoding="latin-1")

# Clean column names and filter data for London
data.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
london_data = data[data['Place_Name'] == 'London']

# Calculate mean and standard deviation for Latitude
mean_latitude = london_data['Latitude'].mean()
std_latitude = london_data['Latitude'].std()

# Calculate upper and lower bounds
upper_bound = mean_latitude + std_latitude
lower_bound = mean_latitude - std_latitude

# Detect outliers
outliers_higher = london_data[london_data['Latitude'] > upper_bound]
outliers_lower = london_data[london_data['Latitude'] < lower_bound]
outliers_not = london_data[(london_data['Latitude'] >= lower_bound) & (london_data['Latitude'] <= upper_bound)]

# Print results
print(f"Outliers Higher than {upper_bound}:", outliers_higher)
print(f"Outliers Lower than {lower_bound}:", outliers_lower)
print("Not Outliers:", outliers_not)
