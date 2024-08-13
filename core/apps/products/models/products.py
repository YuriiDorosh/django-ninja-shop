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
    article = models.UUIDField(
        verbose_name='Product Article',
        unique=True,
        db_index=True,
    )
    price = models.DecimalField(
        verbose_name='Product Price',
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    new_price = models.DecimalField(
        verbose_name='Product New Price',
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    end_of_new_price = models.DateTimeField(
        verbose_name='End of New Price',
        blank=True,
        null=True,
    )
    main_img = models.ImageField(
        verbose_name='Main Image',
        upload_to='products',
        blank=True,
        null=True,
    )
    is_owned = models.BooleanField(
        verbose_name='Is Owned',
        default=False,
        db_index=True,
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
