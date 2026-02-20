#generate_text_report.py

import sqlite3

def generate_text_report():
    conn = sqlite3.connect('detection_reports.db')
    cursor = conn.cursor()
    
    # Retrieve all events from the database
    cursor.execute("SELECT * FROM reports")
    rows = cursor.fetchall()
    conn.close()
    
    # Write the report to a text file
    with open("detection_report.txt", "w") as report_file:
        report_file.write("Detection Report\n")
        report_file.write("================\n\n")
        
        for row in rows:
            report_file.write(f"ID: {row[0]}\n")
            report_file.write(f"Timestamp: {row[1]}\n")
            report_file.write(f"Detection Status: {row[2]}\n")
            report_file.write(f"Frame Path: {row[3]}\n")
            report_file.write("\n")
    
    print("Text report generated: detection_report.txt")

# Example usage
# generate_text_report()
