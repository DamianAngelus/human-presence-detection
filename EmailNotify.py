import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipients):
    # Email configuration
    sender_email = "humandetection024@gmail.com"
    password = "qvni bhay ljqd hang"  # Use an app password if 2FA is enabled

    # Convert the list of recipients to a comma-separated string
    recipients_string = ", ".join(recipients)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipients_string  # Add recipients as a string
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create a secure SSL context
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            # Send the email to all recipients
            server.sendmail(sender_email, recipients, msg.as_string())
            print(f"Email sent successfully to: {recipients_string}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# List of recipients
recipients_list = [
    "damianangelus12@gmail.com",
    "damianangelus18@gmail.com"
]


