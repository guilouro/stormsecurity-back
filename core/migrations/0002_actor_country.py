# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='country',
            field=django_countries.fields.CountryField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
