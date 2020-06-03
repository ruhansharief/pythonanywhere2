# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-03 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeroidModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=64)),
                ('tz', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='activityperoidmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='testapp.UserModel'),
        ),
    ]