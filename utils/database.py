import sqlite3

conn = sqlite3.connect("data/waste_data.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS waste_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT,
    confidence REAL,
    co2_saved REAL,
    timestamp TEXT
)
""")

conn.commit()

def insert_record(label, confidence, co2_saved, timestamp):
    cursor.execute("""
    INSERT INTO waste_records (label, confidence, co2_saved, timestamp)
    VALUES (?, ?, ?, ?)
    """, (label, confidence, co2_saved, str(timestamp)))

    conn.commit()
