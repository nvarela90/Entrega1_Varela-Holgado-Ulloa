# Generated by Django 4.1.3 on 2022-11-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_jugador_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='autor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='jugador',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='jugadores'),
        ),
    ]
