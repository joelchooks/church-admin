# Generated by Django 3.2.9 on 2022-01-19 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0035_auto_20220119_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='last_updated',
            field=models.DateField(default=datetime.datetime(2022, 1, 19, 19, 39, 26, 861129)),
        ),
    ]
