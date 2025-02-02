import pandas as pd

# Input file path
input_file = r"F:\MSC IT\Practical\DS\Prac2\Country_Code.csv"

# Read CSV file
data = pd.read_csv(input_file, encoding="latin-1")

# Remove unnecessary columns and rename the others
data = data.drop(columns=['ISO-2-CODE', 'ISO-3-Code'])
data = data.rename(columns={'Country': 'CountryName', 'ISO-M49': 'CountryNumber'})

# Set the index and sort by CountryName
data.set_index('CountryName', inplace=True)
data.sort_index(ascending=False, inplace=True)

# Output file path
output_file = r"F:\MSC IT\Practical\DS\Prac2\HORUSCountry_Code.csv"

# Save the processed data to a new CSV
data.to_csv(output_file)

print("CSV to HORUS - Done")
