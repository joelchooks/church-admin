# Generated by Django 3.2.9 on 2022-01-02 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0005_auto_20220102_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberattendance',
            name='others',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='sunday_service',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='tuesday_h_d',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='wednesday_service',
        ),
        migrations.AddField(
            model_name='memberattendance',
            name='service',
            field=models.CharField(default='Sunday Service', max_length=70),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='first_service',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='no_of_children',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='no_of_men',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='no_of_new_comers',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='no_of_new_converts',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='no_of_women',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='second_service',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='third_service',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='total',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]