# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20140816_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssentry',
            name='icon',
            field=models.ImageField(upload_to='sites/leifeng', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='site',
            name='icon',
            field=models.ImageField(upload_to='sites/leifeng', null=True),
        ),
    ]
