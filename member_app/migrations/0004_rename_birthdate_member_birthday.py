# Generated by Django 3.2.9 on 2021-12-19 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0003_alter_member_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='birthdate',
            new_name='birthday',
        ),
    ]