# Generated by Django 4.2.3 on 2023-08-20 21:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politicas', '0008_acercade'),
    ]

    operations = [
        migrations.CreateModel(
            name='terminos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
