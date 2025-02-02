
print("8A. Building data warehouse")
import sys
import os
import pandas as pd
import sqlite3 as sq
from datetime import datetime
from pytz import timezone
import uuid

# Set base directory based on the platform
Base = "C:/VKHCG" if sys.platform != "linux" else os.path.expanduser("~") + "/VKHCG"
print(f"Working Base: {Base} using {sys.platform}")

# Directory paths
sDataBaseDir = os.path.join(Base, "01-Vermeulen", "04-Transform", "SQLite")
sDataVaultDir = os.path.join(Base, "88-DV")
sDataWarehouseDir = os.path.join(Base, "99-DW")

# Ensure directories exist
os.makedirs(sDataBaseDir, exist_ok=True)
os.makedirs(sDataVaultDir, exist_ok=True)
os.makedirs(sDataWarehouseDir, exist_ok=True)

# Connect to databases
conn1 = sq.connect(os.path.join(sDataBaseDir, "Vermeulen.db"))
conn2 = sq.connect(os.path.join(sDataVaultDir, "datavault.db"))
conn3 = sq.connect(os.path.join(sDataWarehouseDir, "datawarehouse.db"))

# Fetch DateTime data
DateData = pd.read_sql_query("SELECT DateTimeValue FROM [Hub-Time];", conn2).head(1000)

# Time Dimension Processing
BirthZone = ["Atlantic/Reykjavik", "Europe/London", "UCT"]
TimeFrame = []

for i, row in DateData.iterrows():
    BirthDateUTC = datetime.strptime(row["DateTimeValue"], "%Y-%m-%d %H:%M:%S")
    BirthDateZoneUTC = BirthDateUTC.replace(tzinfo=timezone("UTC"))

    for zone in BirthZone:
        BirthDate = BirthDateZoneUTC.astimezone(timezone(zone))
        IDTimeNumber = str(uuid.uuid4())
        
        TimeFrame.append({
            "TimeID": IDTimeNumber,
            "UTCDate": BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S"),
            "LocalTime": BirthDate.strftime("%Y-%m-%d %H:%M:%S"),
            "TimeZone": zone
        })

# Create and store Time Dimension
DimTime = pd.DataFrame(TimeFrame)
DimTimeIndex = DimTime.set_index("TimeID")
DimTimeIndex.to_sql("Dim-Time", conn1, if_exists="replace")
DimTimeIndex.to_sql("Dim-Time", conn3, if_exists="replace")

# Person Dimension Processing
PersonData = pd.read_sql_query("SELECT FirstName, SecondName, LastName, BirthDateKey FROM [Hub-Person];", conn2).head(1000)

PersonFrame = []

for i, row in PersonData.iterrows():
    FirstName = row["FirstName"]
    SecondName = row["SecondName"] if len(row["SecondName"]) > 0 else ""
    LastName = row["LastName"]
    BirthDateKey = row["BirthDateKey"]
    IDPersonNumber = str(uuid.uuid4())

    PersonFrame.append({
        "PersonID": IDPersonNumber,
        "FirstName": FirstName,
        "SecondName": SecondName,
        "LastName": LastName,
        "Zone": "UTC",
        "BirthDate": BirthDateKey
    })

# Create and store Person Dimension
DimPerson = pd.DataFrame(PersonFrame)
DimPersonIndex = DimPerson.set_index("PersonID")
DimPersonIndex.to_sql("Dim-Person", conn1, if_exists="replace")
DimPersonIndex.to_sql("Dim-Person", conn3, if_exists="replace")

print("Data processing completed and stored in the warehouse.")
