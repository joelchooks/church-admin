# Generated by Django 3.2.9 on 2022-01-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0009_auto_20220102_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberattendance',
            name='overall_total',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
