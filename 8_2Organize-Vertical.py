
print("6B. Vertical style")
import os
import sqlite3 as sq
import pandas as pd
import sys

# Set base path
base = "C:/VKHCG" if sys.platform != "linux" else os.path.expanduser("~") + "/VKHCG"
print(f"Working Base: {base} using {sys.platform}")

# Setup paths
company = "01-Vermeulen"
data_warehouse_dir = f"{base}/99-DW"
os.makedirs(data_warehouse_dir, exist_ok=True)

# Connect to databases
conn1 = sq.connect(f"{data_warehouse_dir}/datawarehouse.db")
conn2 = sq.connect(f"{data_warehouse_dir}/datamart.db")

# Load data from Dim-BMI table
sql_query = "SELECT * FROM [Dim-BMI];"
dim_bmi = pd.read_sql_query(sql_query, conn1)

# Select specific columns
sql_query = "SELECT Height, Weight, Indicator FROM [Dim-BMI];"
dim_bmi_filtered = pd.read_sql_query(sql_query, conn1)

# Set 'Indicator' as the index
dim_bmi_filtered_index = dim_bmi_filtered.set_index("Indicator")

# Store in Dim-BMI-Vertical table
dim_bmi_filtered_index.to_sql("Dim-BMI-Vertical", conn2, if_exists="replace")

# Load the vertical data set
vertical_data = pd.read_sql_query("SELECT * FROM [Dim-BMI-Vertical];", conn2)

# Display shape of the datasets
print(f"Full Data Set (Rows): {dim_bmi.shape[0]}, (Columns): {dim_bmi.shape[1]}")
print(f"Vertical Data Set (Rows): {vertical_data.shape[0]}, (Columns): {vertical_data.shape[1]}")
