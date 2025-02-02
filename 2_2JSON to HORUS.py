# Utility Start JSON to HORUS ================================= 
# # Standard Tools 
# #============================================================ 
print("C. JSON to HORUS Format")
import pandas as pd

# Input file path
input_file = r"F:\MSC IT\Practical\DS\Prac2\Country_Code.json"

# Read JSON file
data = pd.read_json(input_file, orient='index', encoding="latin-1")

# Remove unnecessary columns and rename others
data = data.drop(columns=['ISO-2-CODE', 'ISO-3-Code'])
data = data.rename(columns={'Country': 'CountryName', 'ISO-M49': 'CountryNumber'})

# Set the index and sort by CountryName
data.set_index('CountryNumber', inplace=True)
data.sort_values('CountryName', ascending=False, inplace=True)

# Output file path
output_file = r"F:\MSC IT\Practical\DS\Prac2\HORUS-JSON-Country.csv"

# Save the processed data to a new CSV
data.to_csv(output_file, index=False)

print("JSON to HORUS - Done")
