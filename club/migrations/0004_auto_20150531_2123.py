# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_auto_20150503_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bylaw',
            name='article_designator',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
