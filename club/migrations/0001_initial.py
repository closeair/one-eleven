# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('minutes_text', models.TextField()),
                ('minutes_file', models.FileField(upload_to='')),
                ('minutes_date', models.DateTimeField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
