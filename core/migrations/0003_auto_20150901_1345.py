# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_movie_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['name'], 'verbose_name': 'Ator', 'verbose_name_plural': 'Atores'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'G\xeanero', 'verbose_name_plural': 'Generos'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title'], 'verbose_name': 'Filme', 'verbose_name_plural': 'Filmes'},
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome'),
        ),
    ]
