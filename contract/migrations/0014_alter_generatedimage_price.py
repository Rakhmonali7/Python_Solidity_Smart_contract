# Generated by Django 5.0.3 on 2024-06-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contract", "0013_generatedimage_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="generatedimage",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=5, max_digits=18, null=True
            ),
        ),
    ]