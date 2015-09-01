# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(default='', upload_to=b'', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
