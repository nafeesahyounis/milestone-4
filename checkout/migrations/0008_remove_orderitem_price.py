# Generated by Django 3.0.9 on 2020-10-21 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
