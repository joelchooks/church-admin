# Generated by Django 3.2.9 on 2021-12-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyrics_app', '0007_auto_20211220_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='category',
            field=models.CharField(choices=[('Praise Songs', 'Praise Songs'), ('Worship Songs', 'Worship Songs'), ('Christmas Songs', 'Christmas Songs'), ('Dr. Paul Songs', 'Dr. Paul Songs'), ('Hymns', 'Hymns')], default='Praise Songs', max_length=50),
        ),
    ]