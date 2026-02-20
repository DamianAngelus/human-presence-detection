from twilio.rest import Client

def send_sms():
    # Twilio credentials
    account_sid = ''  # Replace with your Twilio Account SID
    auth_token = ''    # Replace with your Twilio Auth Token
    twilio_phone_number = '+15076237175'  # Replace with your Twilio phone number

    # List of recipient phone numbers in E.164 format
    recipient_phone_numbers = ['+91']  # Add multiple phone numbers here

    # Initialize the Twilio Client
    client = Client(account_sid, auth_token)

    # Message to be sent
    message_body = "WARNING⚠️ \nHuman presence has been detected in the CCTV!"

    # Loop through the list of recipient numbers and send the message to each
    for recipient_phone_number in recipient_phone_numbers:
        try:
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to=recipient_phone_number
            )
            print(f"Message sent successfully to {recipient_phone_number}. SID: {message.sid}")
        except Exception as e:

            print(f"Failed to send message to {recipient_phone_number}: {e}")
