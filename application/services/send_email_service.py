import os

email_sender = os.getenv("EMAIL_HOST_USER")
email_password = os.getenv("EMAIL_HOST_PASSWORD")
email_port = os.getenv("EMAIL_PORT")

class SendEmailService:
    def send_email(self, email: str, subject: str, message: str):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg["From"] = email_sender
        msg["To"] = email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", email_port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email, msg.as_string())
        server.quit()