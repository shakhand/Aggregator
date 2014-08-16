# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20140816_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rssentry',
            options={'ordering': ['publication_date']},
        ),
    ]
