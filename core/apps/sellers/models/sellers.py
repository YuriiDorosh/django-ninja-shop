from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.sellers.entities.sellers import Seller as SellerEntity
from core.apps.sellers.entities.sellers_application import SellerApplication as SellerApplicationEntity


class SellerApplication(TimedBaseModel):
    presentation_text = models.TextField(
        verbose_name='Presentation Text',
        blank=True,
        null=False,
    )
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
    )
    approved = models.BooleanField(
        verbose_name='Approved',
        default=False,
        db_comment='If true, the seller application is approved and the seller\
            (sellers_sellers) will be created with login and password from letter.',
    )

    def to_entity(self) -> SellerApplicationEntity:
        return SellerApplicationEntity(
            id=self.id,
            presentation_text=self.presentation_text,
            email=self.email,
            approved=self.approved,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self):
        return f"{self.email} - {'Approved' if self.approved else 'Pending'}"

    class Meta:
        verbose_name = 'Seller Application'
        verbose_name_plural = 'Seller Applications'

        ordering = ('-created_at',)

        db_table = 'sellers_seller_applications'
        db_table_comment = 'Table for storing seller applications. After approval, \
            the seller will be created.'


class Seller(TimedBaseModel):
    seller_application = models.OneToOneField(
        SellerApplication,
        on_delete=models.PROTECT,
        primary_key=True,
    )
    login = models.CharField(
        verbose_name='Login',
        max_length=255,
        unique=True,
        db_comment='Seller login for authentication. Automatically generated after \
            approval of the seller application.',
    )
    password = models.CharField(
        verbose_name='Password',
        max_length=255,
        db_comment='Seller password for authentication. Automatically generated \
            after approval of the seller application.',
    )
    company_name = models.CharField(
        verbose_name='Company Name',
        max_length=255,
        db_index=True,
    )
    description = models.TextField(
        verbose_name='Seller Description',
        blank=True,
        null=True,
    )
    website_url = models.URLField(
        verbose_name='Seller Website URL',
        blank=True,
        null=True,
    )
    contact_phone = models.CharField(
        verbose_name='Contact Phone',
        max_length=20,
        blank=True,
        null=True,
    )

    def to_entity(self) -> SellerEntity:
        return SellerEntity(
            id=self.id,
            company_name=self.company_name,
            description=self.description,
            website_url=self.website_url,
            contact_phone=self.contact_phone,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

        db_table = 'sellers_sellers'
        db_table_comment = 'Table for storing sellers. After approval, the seller will be created in this table.'
