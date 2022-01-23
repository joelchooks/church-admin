# Generated by Django 3.2.9 on 2022-01-02 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0007_alter_memberattendance_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberattendance',
            name='first_service',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='no_of_children',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='no_of_men',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='no_of_new_comers',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='no_of_new_converts',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='no_of_women',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='second_service',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='third_service',
        ),
        migrations.RemoveField(
            model_name='memberattendance',
            name='total',
        ),
        migrations.AddField(
            model_name='memberattendance',
            name='service_type',
            field=models.CharField(choices=[('Sunday Service', 'Sunday Service'), ('Tueday Healing & Deliverance', 'Tuesday Healing & Deliverance'), ('Wednesday Mid-Week Service', 'Wednesday Mid-Week Service'), ('Friday Worship & Wonders Night', 'Friday Worship & Wonders Night'), ('Others', 'Others')], default='Sunday Service', max_length=70),
        ),
        migrations.AlterField(
            model_name='memberattendance',
            name='service',
            field=models.CharField(choices=[('First Service', 'First Service'), ('Second Service', 'Second Service'), ('Third Service', 'Third Service'), ('Fourth Service', 'FourthS Service'), ('Fifth Service', 'Fifth Service')], default='First Service', max_length=50),
        ),
        migrations.CreateModel(
            name='ServiceCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_men', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_women', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_children', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_new_comers', models.PositiveIntegerField(blank=True, default=0)),
                ('no_of_new_converts', models.PositiveIntegerField(blank=True, default=0)),
                ('total', models.PositiveIntegerField(blank=True, default=0)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_app.memberattendance')),
            ],
        ),
    ]
