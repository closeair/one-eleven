# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20150531_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationdocument',
            name='membership_application',
        ),
        migrations.RemoveField(
            model_name='membershipapplication',
            name='applicant',
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='drivers_license_report',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='phone',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
