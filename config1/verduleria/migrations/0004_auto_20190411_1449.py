# Generated by Django 2.0.6 on 2019-04-11 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verduleria', '0003_auto_20190411_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='fechaCompra',
            new_name='fechaVenta',
        ),
    ]