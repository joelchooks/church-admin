# Generated by Django 3.2.9 on 2021-12-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0002_auto_20211219_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
