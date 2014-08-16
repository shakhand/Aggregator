# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssentry',
            name='site',
            field=models.ForeignKey(null=True, to='books.Site'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='rssentry',
            name='source_site',
        ),
    ]
