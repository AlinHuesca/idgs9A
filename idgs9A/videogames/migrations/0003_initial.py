# Generated by Django 4.0.5 on 2022-06-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('videogames', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videogame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='videogames', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edicion')),
            ],
            options={
                'verbose_name': 'videogames',
                'verbose_name_plural': 'videogames',
                'ordering': ['-created'],
            },
        ),
    ]
