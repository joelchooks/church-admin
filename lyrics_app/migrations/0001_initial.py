# Generated by Django 3.2.9 on 2021-12-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lyrics',
            fields=[
                ('lyrics_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.CharField(max_length=50)),
                ('song_lyrics', models.TextField()),
                ('artist', models.CharField(blank=True, max_length=50)),
                ('album', models.CharField(blank=True, max_length=50)),
                ('song_year', models.CharField(blank=True, max_length=4)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]
