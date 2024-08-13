# Generated by Django 5.0 on 2024-08-13 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerApplication',
            fields=[
                ('id', models.BigIntegerField(db_comment='Unix timestamp ID for the model', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Unix Timestamp ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('presentation_text', models.TextField(blank=True, verbose_name='Presentation Text')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('approved', models.BooleanField(db_comment='If true, the seller application is approved and the seller            (sellers_sellers) will be created with login and password from letter.', default=False, verbose_name='Approved')),
            ],
            options={
                'verbose_name': 'Seller Application',
                'verbose_name_plural': 'Seller Applications',
                'db_table': 'sellers_seller_applications',
                'db_table_comment': 'Table for storing seller applications. After approval,             the seller will be created.',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigIntegerField(db_comment='Unix timestamp ID for the model', editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Unix Timestamp ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('login', models.CharField(db_comment='Seller login for authentication. Automatically generated after             approval of the seller application.', max_length=255, unique=True, verbose_name='Login')),
                ('password', models.CharField(db_comment='Seller password for authentication. Automatically generated             after approval of the seller application.', max_length=255, verbose_name='Password')),
                ('company_name', models.CharField(db_index=True, max_length=255, verbose_name='Company Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Seller Description')),
                ('website_url', models.URLField(blank=True, null=True, verbose_name='Seller Website URL')),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Contact Phone')),
                ('seller_application', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='sellers.sellerapplication')),
            ],
            options={
                'verbose_name': 'Seller',
                'verbose_name_plural': 'Sellers',
                'db_table': 'sellers_sellers',
                'db_table_comment': 'Table for storing sellers. After approval, the seller will be created in this table.',
            },
        ),
        migrations.CreateModel(
            name='SellerProduct',
            fields=[
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='products', serialize=False, to='sellers.seller')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='products.product')),
            ],
            options={
                'verbose_name': 'Seller Product',
                'verbose_name_plural': 'Seller Products',
                'db_table': 'sellers_seller_products',
                'db_table_comment': 'Table for storing seller products(many-to-many)',
                'unique_together': {('seller', 'product')},
            },
        ),
    ]
