import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from domain.protocol.mail_protocol import MailProtocol
import os

class MailGateway(MailProtocol):
    def send(self, message: str, recipient: str) -> None:
        sender_email = os.getenv('HOST_USER')
        sender_password = os.getenv('HOST_PASSWORD')
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = 'Order Confirmation'
        message.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP(os.getenv('HOST_EMAIL'), os.getenv('HOST_EMAIL_PORT'))
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, message.as_string())
        server.quit()
        print('Email sent successfully')