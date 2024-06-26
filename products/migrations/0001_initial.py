# Generated by Django 4.2.13 on 2024-05-18 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="products_images"
                    ),
                ),
                (
                    "stripe_product_price_id",
                    models.CharField(blank=True, max_length=128, null=True),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategory",
                    ),
                ),
            ],
        ),
    ]
