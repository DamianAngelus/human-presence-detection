import os
import sqlite3

def generate_html_report():
    conn = sqlite3.connect('detection_reports.db')
    cursor = conn.cursor()
    
    # Retrieve all events from the database
    cursor.execute("SELECT * FROM reports")
    rows = cursor.fetchall()
    conn.close()
    
    # Write the report to an HTML file
    with open("detection_report.html", "w") as report_file:
        report_file.write("<html><head><title>Detection Report</title></head><body>")
        report_file.write("<h1>Detection Report</h1><hr><br>")
        
        for row in rows:
            report_file.write(f"<p><b>ID:</b> {row[0]}<br>")
            report_file.write(f"<b>Timestamp:</b> {row[1]}<br>")
            report_file.write(f"<b>Detection Status:</b> {row[2]}<br>")
            if row[3]:  # Check if frame path exists
                report_file.write(f'<b>Frame:</b> <a href="/static/frames/{os.path.basename(row[3])}" target="_blank">View Frame</a><br>')
            report_file.write("<br></p><hr>")
        
        report_file.write("</body></html>")
    
    print("HTML report generated: detection_report.html")

# Example usage
# generate_html_report()