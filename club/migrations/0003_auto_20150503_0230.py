# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20150321_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bylaw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_designator', models.CharField(max_length=255)),
                ('article_title', models.CharField(max_length=255)),
                ('body', django_markdown.models.MarkdownField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='minutes',
            options={'verbose_name_plural': 'Minutes'},
        ),
    ]
