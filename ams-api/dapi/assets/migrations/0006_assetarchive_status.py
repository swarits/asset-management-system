# Generated by Django 3.0.5 on 2020-05-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20200501_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetarchive',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
