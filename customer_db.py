import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect("customers.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the customers table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    contact_method TEXT
)
""")

# Save the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")