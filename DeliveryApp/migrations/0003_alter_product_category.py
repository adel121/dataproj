# Generated by Django 3.2 on 2021-06-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0002_alter_bill_bill_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='none', max_length=30, unique=True),
        ),
    ]
