# Generated by Django 3.2.9 on 2022-01-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0030_member_member_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_age',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
