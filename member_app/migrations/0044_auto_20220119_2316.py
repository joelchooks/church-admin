# Generated by Django 3.2.9 on 2022-01-19 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0043_member_other_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='done_foundation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='done_maturity',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_baptized',
            field=models.BooleanField(default=True),
        ),
    ]
