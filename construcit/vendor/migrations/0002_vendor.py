# Generated by Django 4.0.2 on 2022-02-25 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_no', models.CharField(max_length=250, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('business_name', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]