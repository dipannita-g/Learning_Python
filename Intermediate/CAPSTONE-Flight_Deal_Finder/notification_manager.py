import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(r"C:\fakepath\.env")

class NotificationManager:

    def __init__(self):

        self.client = Client(os.getenv("twilio_account_sid"), os.getenv("twilio_auth_token"))

    def send_whatsapp(self, message_body):

        message = self.client.messages.create(
            body=message_body,
            from_="whatsapp:+1XXXXXXXXXX",
            to="whatsapp:+44XXXXXXXXXX",
        )
        print(message.status)
