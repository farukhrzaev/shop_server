# Generated by Django 4.2.13 on 2024-05-19 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "product", "verbose_name_plural": "products"},
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
    ]