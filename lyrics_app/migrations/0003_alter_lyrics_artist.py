# Generated by Django 3.2.9 on 2022-01-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics_app', '0002_auto_20220121_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='artist',
            field=models.CharField(help_text="Type 'Unkwown' if Artist name is unkwown", max_length=50),
        ),
    ]
