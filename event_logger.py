# event_logger.py

import sqlite3
from datetime import datetime

def log_detection_event(detection_status, frame_path):
    conn = sqlite3.connect('detection_reports.db')
    cursor = conn.cursor()
    
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Insert detection event into the database
    cursor.execute('''
    INSERT INTO reports (timestamp, detection_status, frame_path)
    VALUES (?, ?, ?)
    ''', (timestamp, detection_status, frame_path))
    
    conn.commit()
    conn.close()
    print("Detection event logged successfully.")

# Example usage
# log_detection_event("Human Detected", "frames/frame_100.jpg")