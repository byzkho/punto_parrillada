import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from domain.protocol.mail_protocol import MailProtocol
import os

class MailGateway(MailProtocol):
    def send_mail(self, subject: str, html_content: str, recipient: str) -> None:
        sender_email = os.getenv('HOST_USER')
        sender_password = os.getenv('HOST_PASSWORD')
        sender = "Private Person <hello@zentrabook.com>"
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(html_content, 'html'))
        
        with smtplib.SMTP(os.getenv("HOST_EMAIL"), os.getenv("HOST_EMAIL_PORT")) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender, recipient, message.as_string())
            server.quit()
            print('Email sent successfully')