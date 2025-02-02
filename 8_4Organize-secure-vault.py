
print("6D. Secure Vault style")
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

# Filter and modify data using SQL
sql = """
    SELECT Height, Weight, Indicator,
           CASE Indicator
               WHEN 1 THEN 'Pip'
               WHEN 2 THEN 'Norman'
               WHEN 3 THEN 'Grant'
               ELSE 'Sam'
           END AS Name
    FROM [Dim-BMI]
    WHERE Indicator > 2
    ORDER BY Height, Weight;
"""
dim_bmi_filtered = pd.read_sql_query(sql, conn1)

# Set 'Indicator' as the index
dim_bmi_filtered_index = dim_bmi_filtered.set_index("Indicator")

# Store the filtered data into a new table
dim_bmi_filtered_index.to_sql("Dim-BMI-Secure", conn2, if_exists="replace")

# Load the "Sam" data from the secure table
sam_data = pd.read_sql_query("SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';", conn2)

# Display the shape of the datasets
print(f"Full Data Set (Rows): {dim_bmi.shape[0]}, (Columns): {dim_bmi.shape[1]}")
print(f"Secure Data Set (Rows): {sam_data.shape[0]}, (Columns): {sam_data.shape[1]}")
print("Only Sam Data:")
print(sam_data.head())
