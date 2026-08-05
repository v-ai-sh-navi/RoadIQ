import sqlite3

DB_PATH = "database/roadlens.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Fetch all table names
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\n========== DATABASE TABLES ==========\n")

for table in tables:
    print(table[0])

conn.close()
