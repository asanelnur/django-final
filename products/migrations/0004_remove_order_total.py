# Generated by Django 3.2.16 on 2023-05-02 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_basket_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]