import sys
import os
import pandas as pd
import sqlite3 as sq

print("6A. Horizontal style")
import os
import sqlite3 as sq
import pandas as pd
import sys

# Set base path depending on the platform
base = "C:/VKHCG" if sys.platform != "linux" else os.path.expanduser("~") + "/VKHCG"
print(f"Working Base: {base} using {sys.platform}")

# Setup paths
company = "01-Vermeulen"
data_warehouse_dir = f"{base}/99-DW"
os.makedirs(data_warehouse_dir, exist_ok=True)

# Connect to databases
conn1 = sq.connect(f"{data_warehouse_dir}/datawarehouse.db")
conn2 = sq.connect(f"{data_warehouse_dir}/datamart.db")

# SQL query to load data from Dim-BMI table
sql_query = "SELECT PersonID, Height, Weight, bmi, Indicator FROM [Dim-BMI] WHERE Height > 1.5 AND Indicator = 1 ORDER BY Height, Weight"
dim_person = pd.read_sql_query(sql_query, conn1)

# Set PersonID as the index
dim_person_index = dim_person.set_index("PersonID")

# Store in Dim-BMI-Horizontal table
dim_person_index.to_sql("Dim-BMI-Horizontal", conn2, if_exists="replace")

# Load the horizontal data set
horizontal_data = pd.read_sql_query("SELECT * FROM [Dim-BMI-Horizontal];", conn2)

# Display shape of the datasets
print(f"Full Data Set (Rows): {dim_person.shape[0]}, (Columns): {dim_person.shape[1]}")
print(f"Horizontal Data Set (Rows): {horizontal_data.shape[0]}, (Columns): {horizontal_data.shape[1]}")
