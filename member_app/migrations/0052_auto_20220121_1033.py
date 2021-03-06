# Generated by Django 3.2.9 on 2022-01-21 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0051_alter_member_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='member',
            name='other_number',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='Value Must Be Numeric And Up To 11 Digits', regex='^\\d{11,11}$')]),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='Value Must Be Numeric And Up To 11 Digits', regex='^\\d{11,11}$')]),
        ),
    ]
