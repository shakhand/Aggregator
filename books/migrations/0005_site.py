# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20140813_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='sites')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
