# Generated by Django 4.0.2 on 2022-02-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vendor_business_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
