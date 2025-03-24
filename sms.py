import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_sms(to_number, message_body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        print(f"Message sent successfully! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")
        return False


if __name__ == "__main__":
    send_sms(
        to_number="+9189XXXXXXXX",
        message_body="Hello World! Test SMS from python via Twilio",
    )