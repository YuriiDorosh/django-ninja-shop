from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import CustomerEntity


class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=20,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    token = models.CharField(
        verbose_name='User Token',
        max_length=255,
        default=uuid4,
        unique=True,
    )

    def __str__(self) -> str:
        return f"Customer with phone {self.phone} and email {self.email}"

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            phone=self.phone,
            email=self.email,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
