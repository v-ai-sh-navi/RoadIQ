import os
import sqlite3
import pandas as pd
import geopandas as gpd

# ----------------------------------
# Project Paths
# ----------------------------------

DATA_PATH = "data/Bengaluru"
DB_PATH = "database/roadlens.db"

ROADS_FILE = os.path.join(DATA_PATH, "roads.kml")
POTHOLES_FILE = os.path.join(DATA_PATH, "potholes.kml")
REPAIRS_FILE = os.path.join(DATA_PATH, "repairs.csv")
WARDS_FILE = os.path.join(DATA_PATH, "wards.csv")

os.makedirs("database", exist_ok=True)

# ----------------------------------
# Load datasets
# ----------------------------------

print("Loading datasets...")

roads = gpd.read_file(ROADS_FILE)
potholes = gpd.read_file(POTHOLES_FILE)
repairs = pd.read_csv(REPAIRS_FILE)
wards = pd.read_csv(WARDS_FILE)

print("Datasets loaded successfully!\n")

# ----------------------------------
# Clean column names
# ----------------------------------

roads.columns = roads.columns.str.strip().str.replace(" ", "_")

potholes.columns = potholes.columns.str.strip().str.replace(" ", "_")

repairs.columns = repairs.columns.str.strip().str.replace(" ", "_")

wards.columns = wards.columns.str.strip().str.replace(" ", "_")

# ----------------------------------
# Show basic information
# ----------------------------------

print("Roads:", roads.shape)
print("Potholes:", potholes.shape)
print("Repairs:", repairs.shape)
print("Wards:", wards.shape)

# ----------------------------------
# SQLite
# ----------------------------------

conn = sqlite3.connect(DB_PATH)

roads.drop(columns="geometry", errors="ignore").to_sql(
    "Roads",
    conn,
    if_exists="replace",
    index=False
)

potholes.drop(columns="geometry", errors="ignore").to_sql(
    "Potholes",
    conn,
    if_exists="replace",
    index=False
)

repairs.to_sql(
    "Repairs",
    conn,
    if_exists="replace",
    index=False
)

wards.to_sql(
    "Wards",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nSQLite Database Created Successfully!")