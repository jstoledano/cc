# Generated by Django 5.0.7 on 2024-07-22 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.SmallIntegerField()),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Entidades',
                'ordering': ['entidad'],
            },
        ),
        migrations.CreateModel(
            name='DistritoLocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distrito_local', models.SmallIntegerField()),
                ('cabecera', models.CharField(max_length=100)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.entidad')),
            ],
            options={
                'verbose_name_plural': 'Distritos Locales',
                'ordering': ['distrito_local'],
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabecera', models.CharField(max_length=100)),
                ('distrito', models.SmallIntegerField()),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.entidad')),
            ],
            options={
                'verbose_name_plural': 'Distritos',
                'ordering': ['distrito'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.SmallIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.entidad')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'ordering': ['municipio'],
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localidad', models.SmallIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.municipio')),
            ],
            options={
                'verbose_name_plural': 'Localidades',
                'ordering': ['municipio', 'localidad'],
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.SmallIntegerField()),
                ('activa', models.BooleanField(default=True)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.distrito')),
                ('distrito_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.distritolocal')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bgd.municipio')),
            ],
            options={
                'verbose_name_plural': 'Secciones',
                'ordering': ['distrito', 'distrito_local', 'municipio', 'seccion'],
            },
        ),
    ]
