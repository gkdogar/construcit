# Generated by Django 3.2 on 2022-02-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_vendor_videofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='videofile',
            field=models.FileField(blank=True, null=True, upload_to='landing/videos'),
        ),
    ]
