class MailService:
    def __init__(self, mail_gateway):
        self.mail_gateway = mail_gateway
        
    def send_mail(self, mail):
        self.mail_gateway.send_mail(mail)
        
    