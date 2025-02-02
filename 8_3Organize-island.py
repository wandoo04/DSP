
print("6C. Island style")
import os
import sqlite3 as sq
import pandas as pd
import sys

# Set base path
base = "C:/VKHCG"
print(f"Working Base: {base} using {sys.platform}")

# Set up data warehouse directory
data_warehouse_dir = f"{base}/99-DW"
os.makedirs(data_warehouse_dir, exist_ok=True)

# Connect to databases
conn1 = sq.connect(f"{data_warehouse_dir}/datawarehouse.db")
conn2 = sq.connect(f"{data_warehouse_dir}/datamart.db")

# Load data from Dim-BMI table
dim_bmi = pd.read_sql_query("SELECT * FROM [Dim-BMI];", conn1)

# Filter data where Indicator > 2 and order by Height and Weight
dim_bmi_filtered = pd.read_sql_query("""
    SELECT Height, Weight, Indicator
    FROM [Dim-BMI]
    WHERE Indicator > 2
    ORDER BY Height, Weight;
""", conn1)

# Set 'Indicator' as the index
dim_bmi_filtered_index = dim_bmi_filtered.set_index("Indicator")

# Store the filtered data into a new table
dim_bmi_filtered_index.to_sql("Dim-BMI-Vertical", conn2, if_exists="replace")

# Load the vertical data set
vertical_data = pd.read_sql_query("SELECT * FROM [Dim-BMI-Vertical];", conn2)

# Display the shape of the datasets
print(f"Full Data Set (Rows): {dim_bmi.shape[0]}, (Columns): {dim_bmi.shape[1]}")
print(f"Vertical Data Set (Rows): {vertical_data.shape[0]}, (Columns): {vertical_data.shape[1]}")
