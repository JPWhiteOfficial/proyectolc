# Generated by Django 4.2 on 2023-07-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto_fecha_carga'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='calificacion',
            field=models.FloatField(default=0.0),
        ),
    ]
