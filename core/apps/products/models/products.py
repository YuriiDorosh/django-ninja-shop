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
        db_index=True,
        db_comment='Unique article of the product. Used for searching and identifying the product.',
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
        db_comment='New price of the product. If the new price is set, the product will be sold at the new price until \
            the end of the new price date.',
    )
    end_of_new_price = models.DateTimeField(
        verbose_name='End of New Price',
        blank=True,
        null=True,
        db_comment='The date when the new price will end. After this date, the product will be sold at the base price.',
    )
    replace_base_price_with_new_price = models.BooleanField(
        verbose_name='Replace Base Price With New Price',
        default=False,
        blank=True,
        null=True,
        db_comment='If true, the base price will be replaced with the new price after the end of the new price date.',
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
        db_comment='If true, the product is owned by the seller. If false, the product is not owned by the seller.',
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

        ordering = ('-created_at',)

        db_table = 'products_products'
        db_table_comment = 'Table of products'
