# reporting_module.py

from event_logger import log_detection_event
from generate_text_report import generate_text_report
from generate_html_report import generate_html_report

def log_event_and_generate_reports(detection_status, frame_path):
    # Log the detection event
    log_detection_event(detection_status, frame_path)
    
    # Generate text and HTML reports
    generate_text_report()
    generate_html_report()

# Example usage
# log_event_and_generate_reports("Human Detected", "frames/frame_101.jpg")
