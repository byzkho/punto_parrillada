from injector import Module, provider, singleton
from application.services.mail_service import MailService
from domain.protocol.mail_protocol import MailProtocol
from infrastructure.impl.mail_gateway import MailGateway


class MailModule(Module):
    @singleton
    @provider
    def provide_mail_service(self) -> MailService:
        return MailService()
    
    @singleton
    @provider
    def provide_mail_gateway(self) -> MailProtocol:
        return MailGateway()