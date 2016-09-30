# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_by',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
