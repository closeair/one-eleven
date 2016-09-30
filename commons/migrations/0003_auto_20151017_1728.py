# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0002_auto_20150503_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploaded_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
