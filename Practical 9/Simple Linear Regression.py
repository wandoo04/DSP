################################################################
# C:\VKHCG\01-Vermeulen\04-Transform\ Transform-BMI.py
# Simple Linear Regression
################################################################
import sys
import os
import pandas as pd
import sqlite3 as sq
import matplotlib.pyplot as plt

# Set base directory
Base = "C:/VKHCG" if sys.platform != "linux" else os.path.expanduser("~") + "/VKHCG"
print(f"Working Base: {Base} using {sys.platform}")

# Directory paths
Company = "01-Vermeulen"
sDataBaseDir = os.path.join(Base, Company, "04-Transform", "SQLite")
sDataVaultDir = os.path.join(Base, "88-DV")
sDataWarehouseDir = os.path.join(Base, "99-DW")

# Ensure directories exist
os.makedirs(sDataBaseDir, exist_ok=True)
os.makedirs(sDataVaultDir, exist_ok=True)
os.makedirs(sDataWarehouseDir, exist_ok=True)

# Database connections
conn1 = sq.connect(os.path.join(sDataBaseDir, "Vermeulen.db"))
conn2 = sq.connect(os.path.join(sDataVaultDir, "datavault.db"))
conn3 = sq.connect(os.path.join(sDataWarehouseDir, "datawarehouse.db"))

# Generate BMI Data
data = []
for heightSelect in range(100, 300, 10):
    for weightSelect in range(30, 300, 5):
        height = round(heightSelect / 100, 3)
        weight = int(weightSelect)
        bmi = weight / (height ** 2)

        # BMI Categories
        if bmi <= 18.5:
            BMI_Result = 1
        elif bmi < 25:
            BMI_Result = 2
        elif bmi < 30:
            BMI_Result = 3
        else:
            BMI_Result = 4

        data.append([str(len(data)), height, weight, bmi, BMI_Result])

# Create DataFrame
DimPerson = pd.DataFrame(data, columns=["PersonID", "Height", "Weight", "bmi", "Indicator"]).set_index("PersonID")

# Store to databases
DimPerson.to_sql("Transform-BMI", conn1, if_exists="replace")
DimPerson.to_sql("Person-Satellite-BMI", conn2, if_exists="replace")
DimPerson.to_sql("Dim-BMI", conn3, if_exists="replace")

# Plotting BMI categories
fig = plt.figure()

# Plot different BMI categories
for indicator, marker in zip([1, 2, 3, 4], [".", "o", "+", "^"]):
    subset = DimPerson[DimPerson["Indicator"] == indicator]
    plt.plot(subset["Height"], subset["Weight"], marker, label=f"Indicator {indicator}")

# Customize plot
plt.title("BMI Curve")
plt.xlabel("Height (m)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.tight_layout()
plt.show()
