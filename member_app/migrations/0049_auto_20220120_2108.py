# Generated by Django 3.2.9 on 2022-01-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0048_alter_member_is_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='done_foundation',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='done_maturity',
            field=models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='is_baptized',
            field=models.BooleanField(blank=True, choices=[(True, 'Baptized'), (False, 'Not Yet')], default=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_status',
            field=models.CharField(blank=True, choices=[('Member', 'Member'), ('New Member', 'New Member'), ('Guest', 'Guest'), ('Former Member', 'Former Member')], default='Member', max_length=25, null=True),
        ),
    ]