# Generated by Django 3.2.9 on 2022-01-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0010_memberattendance_overall_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberattendance',
            name='overall_total',
        ),
        migrations.AddField(
            model_name='service',
            name='overall_total',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
