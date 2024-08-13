from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from django.conf import settings

from twilio.rest import Client

from core.apps.customers.entities import CustomerEntity


class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        ...


class DummySenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f'Code to user: {customer}, sent: {code}')


class EmailSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f'sent code {code} to user email: customeremail')


class PushSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f'sent push notification with {code} fcm_token')


class TwilloSenderService(BaseSenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        twillo_service: Client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        twillo_service.messages.create(
            body=f'Your code is {code}',
            from_=settings.TWILIO_NUMBER,
            to=customer.phone,
        )


@dataclass
class ComposedSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer, code)
