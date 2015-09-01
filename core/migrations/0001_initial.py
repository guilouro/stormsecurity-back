# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('picture', models.ImageField(upload_to=b'', verbose_name='Imagem')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'G\xeanero',
                'verbose_name_plural': 'Generos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('resume', models.TextField(verbose_name='Sinopse')),
                ('picture', models.ImageField(upload_to=b'', verbose_name='Imagem')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('actor', models.ManyToManyField(to='core.Actor', verbose_name='Ator')),
                ('genre', models.ManyToManyField(to='core.Genre', verbose_name='G\xeanero')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
            bases=(models.Model,),
        ),
    ]
