# Generated by Django 3.2.9 on 2022-01-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0025_alter_message_sent_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_text',
            field=models.TextField(max_length=919),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_name',
            field=models.CharField(max_length=12),
        ),
    ]
