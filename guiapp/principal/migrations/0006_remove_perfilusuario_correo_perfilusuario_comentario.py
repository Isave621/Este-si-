# Generated by Django 4.0.4 on 2022-07-09 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_perfilusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='correo',
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
