# Generated by Django 4.1.2 on 2022-11-05 23:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]