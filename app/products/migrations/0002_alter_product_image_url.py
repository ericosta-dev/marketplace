# Generated by Django 4.2.1 on 2023-05-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image_url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
