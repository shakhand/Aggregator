# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20140816_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rssentry',
            old_name='icon',
            new_name='image',
        ),
    ]
