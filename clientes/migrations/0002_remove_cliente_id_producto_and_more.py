# Generated by Django 5.0.1 on 2024-01-30 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id_producto',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_materno',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido_paterno',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='comuna',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='region',
            field=models.CharField(max_length=60),
        ),
    ]
