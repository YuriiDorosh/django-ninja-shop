# Generated by Django 5.0 on 2024-08-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('title', models.CharField(max_length=255, verbose_name='Product Title')),
                ('description', models.TextField(blank=True, verbose_name='Product Description')),
                ('article', models.UUIDField(blank=True, db_comment='Unique article of the product. Used for searching and identifying the product.', db_index=True, unique=True, verbose_name='Product Article')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Product Price')),
                ('new_price', models.DecimalField(db_comment='New price of the product. If the new price is set, the product will be sold at the new price until the end of the new price date.', decimal_places=2, default=0, max_digits=10, verbose_name='Product New Price')),
                ('end_of_new_price', models.DateTimeField(blank=True, db_comment='The date when the new price will end. After this date, the product will be sold at the base price.', null=True, verbose_name='End of New Price')),
                ('replace_base_price_with_new_price', models.BooleanField(blank=True, db_comment='If true, the base price will be replaced with the new price after the end of the new price date.', default=False, null=True, verbose_name='Replace Base Price With New Price')),
                ('main_img', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Main Image')),
                ('is_owned', models.BooleanField(db_comment='If true, the product is owned by the seller. If false, the product is not owned by the seller.', db_index=True, default=False, verbose_name='Is Owned')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Is Visible')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products_products',
                'db_table_comment': 'Table of products',
                'ordering': ('-created_at',),
            },
        ),
    ]
