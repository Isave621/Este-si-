# Generated by Django 4.0.4 on 2022-07-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_alter_perfil_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
    ]
