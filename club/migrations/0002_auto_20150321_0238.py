# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationDocument',
            fields=[
                ('securedocument_ptr', models.OneToOneField(primary_key=True, to='commons.SecureDocument', serialize=False, auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('commons.securedocument',),
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('occured_at', models.DateField(blank=True)),
                ('minutes', models.ForeignKey(to='club.Minutes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('applicant', models.OneToOneField(to='commons.Pilot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('made_by', models.OneToOneField(to='commons.Pilot', related_name='motions_made')),
                ('seconded_by', models.OneToOneField(to='commons.Pilot', related_name='motions_seconded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('made_by', models.OneToOneField(to='commons.Pilot')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('survey', models.ForeignKey(to='club.Survey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('member', models.OneToOneField(to='commons.Pilot')),
                ('question', models.ForeignKey(to='club.SurveyQuestion')),
                ('survey', models.ForeignKey(to='club.Survey')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('member', models.OneToOneField(to='commons.Pilot')),
                ('motion', models.ForeignKey(to='club.Motion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attendence',
            name='meeting',
            field=models.ForeignKey(to='club.Meeting'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendence',
            name='member',
            field=models.OneToOneField(to='commons.Pilot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicationdocument',
            name='membership_application',
            field=models.ForeignKey(to='club.MembershipApplication'),
            preserve_default=True,
        ),
    ]
