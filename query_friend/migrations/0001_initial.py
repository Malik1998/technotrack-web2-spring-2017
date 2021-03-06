# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 16:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signed', models.BooleanField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
                ('responser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
