# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rssentry_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssentry',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
