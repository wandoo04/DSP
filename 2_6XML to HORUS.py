# Utility Start XML to HORUS =================================
# Standard Tools
print("B.	XML to HORUS Format")
import pandas as pd
import xml.etree.ElementTree as ET

# Function to convert XML to DataFrame
def xml2df(xml_data):
    root = ET.XML(xml_data)
    records = []
    for entry in root:
        record = {child.tag: child.text if child.text != 'nan' else 'n/a' for child in entry}
        records.append(record)
    return pd.DataFrame(records)

# Input file path
input_file = r"F:\MSC IT\Practical\DS\Prac2\Country_Code.xml"

# Read XML file
with open(input_file) as f:
    xml_data = f.read()

# Convert XML to DataFrame
data = xml2df(xml_data)

# Process Data
data.drop(['ISO-2-CODE', 'ISO-3-Code'], axis=1, inplace=True)
data.rename(columns={'Country': 'CountryName', 'ISO-M49': 'CountryNumber'}, inplace=True)
data.set_index('CountryNumber', inplace=True)

# Output file path
output_file = r"F:\MSC IT\Practical\DS\Prac2\HORUS-XML-Country.csv"

# Save to CSV
data.to_csv(output_file, index=False)

print("XML to HORUS - Done")
