import sqlite3

conn = sqlite3.connect("data/sap_transactions.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS purchase_orders;
CREATE TABLE purchase_orders (
    po_id TEXT PRIMARY KEY,
    vendor_id TEXT,
    amount REAL,
    status TEXT,
    date TEXT
);

DROP TABLE IF EXISTS invoices;
CREATE TABLE invoices (
    invoice_id TEXT PRIMARY KEY,
    po_id TEXT,
    amount REAL,
    status TEXT,
    due_date TEXT
);

DROP TABLE IF EXISTS vendors;
CREATE TABLE vendors (
    vendor_id TEXT PRIMARY KEY,
    name TEXT,
    compliance_score INTEGER
);
""")

pos = [
    ("PO001", "V001", 150000, "pending", "2025-05-01"),
    ("PO002", "V002", 95000, "approved", "2025-04-12"),
    ("PO003", "V001", 120000, "delayed", "2025-03-28"),
]
cursor.executemany("INSERT INTO purchase_orders VALUES (?, ?, ?, ?, ?)", pos)

invoices = [
    ("INV001", "PO001", 150000, "unpaid", "2025-06-01"),
    ("INV002", "PO002", 95000, "paid", "2025-04-30"),
]
cursor.executemany("INSERT INTO invoices VALUES (?, ?, ?, ?, ?)", invoices)

vendors = [
    ("V001", "Vendor A", 65),
    ("V002", "Vendor B", 90),
]
cursor.executemany("INSERT INTO vendors VALUES (?, ?, ?)", vendors)

conn.commit()
conn.close()
