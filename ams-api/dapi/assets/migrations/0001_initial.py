# Generated by Django 3.0.5 on 2020-04-30 20:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('client_id', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AssetsArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.IntegerField()),
                ('asignee_id', models.IntegerField()),
                ('issue_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
            ],
        ),
    ]
