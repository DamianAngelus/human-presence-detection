# database_setup.py

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('detection_reports.db')
cursor = conn.cursor()

# Create a table to store detection events
cursor.execute('''
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    detection_status TEXT,
    frame_path TEXT
)
''')

conn.commit()
conn.close()
print("Database and table created successfully.")