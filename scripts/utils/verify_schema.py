import sqlite3

# Connect to the database
conn = sqlite3.connect('data/database.db')
cursor = conn.cursor()

# Fetch all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

if not tables:
    print("❌ No tables found in the database.")
else:
    print("✅ Tables found in the database:\n")
    for table in tables:
        table_name = table[0]
        print(f"🔹 {table_name}")

        # Fetch column names for each table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        for col in columns:
            print(f"    - {col[1]} ({col[2]})")  # col[1] = name, col[2] = datatype

# Close the connection
conn.close()

