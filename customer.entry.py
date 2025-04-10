import tkinter as tk
from tkinter import ttk
import sqlite3

# --- DATABASE SETUP ---
conn = sqlite3.connect("customers.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birthday TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    contact_method TEXT
)
""")
conn.commit()
conn.close()

# --- FUNCTION TO SUBMIT DATA ---
def submit_data():
    data = [entry.get() for entry in entries]
    data.append(contact_method.get())

    conn = sqlite3.connect("customers.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO customers (name, birthday, email, phone, address, contact_method)
        VALUES (?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()

    # Clear the fields
    for entry in entries:
        entry.delete(0, tk.END)
    contact_method.set(contact_options[0])

# --- GUI SETUP ---
root = tk.Tk()
root.title("Customer Information Form")

fields = ["Name", "Date of Birth (YYYY-MM-DD)", "Email", "Phone", "Address"]
entries = []

for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Contact Method dropdown
tk.Label(root, text="Preferred Contact Method:").grid(row=len(fields), column=0, padx=10, pady=5, sticky="e")
contact_options = ["Email", "Phone", "Mail"]
contact_method = tk.StringVar(value=contact_options[0])
ttk.OptionMenu(root, contact_method, *contact_options).grid(row=len(fields), column=1, padx=10, pady=5, sticky="w")

# Submit button
tk.Button(root, text="Submit", command=submit_data).grid(row=len(fields)+1, columnspan=2, pady=15)

root.mainloop()
