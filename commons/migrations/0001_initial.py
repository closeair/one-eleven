# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecureDocument',
            fields=[
                ('document_ptr', models.OneToOneField(primary_key=True, to='commons.Document', serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('commons.document',),
        ),
        migrations.CreateModel(
            name='SupportingDocument',
            fields=[
                ('document_ptr', models.OneToOneField(primary_key=True, to='commons.Document', serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('commons.document',),
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded_by',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
