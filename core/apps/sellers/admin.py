from django.contrib import admin

from core.apps.sellers.models.seller_products import SellerProduct
from core.apps.sellers.models.sellers import (
    Seller,
    SellerApplication,
)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'created_at', 'updated_at')


@admin.register(SellerApplication)
class SellerApplicationAdmin(admin.ModelAdmin):
    list_display = ('email', 'approved', 'created_at', 'updated_at')
    list_filter = ('approved',)


@admin.register(SellerProduct)
class SellerProductAdmin(admin.ModelAdmin):
    ...
