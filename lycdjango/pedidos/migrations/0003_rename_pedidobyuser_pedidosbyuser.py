# Generated by Django 4.2 on 2023-10-13 00:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidos', '0002_pedidobyuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PedidoByUser',
            new_name='PedidosByUser',
        ),
    ]