import pandas as pd
################################################################
# InputFileName='IP_DATA_CORE.csv'
# OutputFileName='Retrieve_Router_Location.csv'
# Base='C:/VKHCG'
# print('4C. Averaging of Data')
# print('################################')
# print('Working Base :',Base, ' using ')
# print('################################')
# sFileName=Base + '/01-Vermeulen/00-RawData/' + InputFileName
# print('Loading :',sFileName)
# IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,
# usecols=['Country','Place Name','Latitude','Longitude'], encoding="latin-1")
# IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
# AllData=IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
# print(AllData)
# MeanData=AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
# print(MeanData)


import pandas as pd

# File paths
base = 'C:/VKHCG'
input_file = '01-Vermeulen/00-RawData/IP_DATA_CORE.csv'
output_file = 'Retrieve_Router_Location.csv'

# Load data
file_path = f'{base}/{input_file}'
data = pd.read_csv(file_path, usecols=['Country', 'Place Name', 'Latitude', 'Longitude'], encoding="latin-1")

# Clean and average latitude by country and place name
data.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
mean_data = data.groupby(['Country', 'Place_Name'])['Latitude'].mean()

# Display the result
print(mean_data)
