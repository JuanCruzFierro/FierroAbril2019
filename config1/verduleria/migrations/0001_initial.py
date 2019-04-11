# Generated by Django 2.0.6 on 2019-04-11 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=254)),
                ('facturaNum', models.IntegerField(null=True)),
                ('fechaCompra', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('tipo', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto', to='verduleria.Producto'),
        ),
    ]