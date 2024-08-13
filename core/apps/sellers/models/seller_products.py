from django.db import models

from core.apps.sellers.entities.seller_products import SellerProducts as SellerProductsEntity


class SellerProduct(models.Model):
    seller = models.ForeignKey(
        'sellers.Seller',
        on_delete=models.CASCADE,
        related_name='products',
        primary_key=True,
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='sellers',
    )

    def to_entity(self) -> SellerProductsEntity:
        return SellerProductsEntity(
            seller_id=self.seller.id,
            product_id=self.product.id,
        )

    def __str__(self):
        return f"{self.seller.company_name} - {self.product.title}"

    class Meta:
        verbose_name = 'Seller Product'
        verbose_name_plural = 'Seller Products'

        db_table = 'sellers_seller_products'
        db_table_comment = 'Table for storing seller products(many-to-many)'
        unique_together = ('seller', 'product')
