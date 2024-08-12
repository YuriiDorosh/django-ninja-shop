from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product as ProductEntity


class Product(TimedBaseModel):
    title = models.CharField(
        verbose_name='Product Title',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Product Description',
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name='Is Visible',
        default=True,
    )

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
