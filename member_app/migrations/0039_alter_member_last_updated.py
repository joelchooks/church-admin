# Generated by Django 3.2.9 on 2022-01-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0038_auto_20220119_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='last_updated',
            field=models.DateTimeField(),
        ),
    ]
