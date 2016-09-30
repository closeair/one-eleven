# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_auto_20150826_0253'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipapplication',
            name='address',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='atp',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='bfr_expiration',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='birth_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='cfi',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='city',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='commercial',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='criminal_convictions',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='email',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='faa_certificate_number',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='if_no_where',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='inconsistencies',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='information_verified_by',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='medical_expiration',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='notes',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='other',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='private',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='reference_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='reference_phone',
            field=models.CharField(max_length=11, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='reference_relation',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='state_abbreviation',
            field=models.CharField(max_length=2, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='student',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='submitted_at',
            field=models.DateField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='total_flight_hours',
            field=models.CharField(max_length=4, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='united_states_citizen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membershipapplication',
            name='zipcode',
            field=models.CharField(max_length=9, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='drivers_license_report',
            field=models.FileField(null=True, upload_to=b'documents/%Y/%m/%d/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='membershipapplication',
            name='phone',
            field=models.CharField(max_length=11, null=True),
            preserve_default=True,
        ),
    ]
