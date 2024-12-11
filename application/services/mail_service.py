from domain.protocol.mail_protocol import MailProtocol


class MailService:
    def __init__(self, mail_gateway: MailProtocol):
        self.mail_gateway = mail_gateway
        
    def send_mail(self, subject: str, html_content: str, recipient: str):
        self.mail_gateway.send_mail(subject, html_content, recipient)
    