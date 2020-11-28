# Generated by Django 3.1.1 on 2020-11-21 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0013_auto_20201120_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breastmodel',
            name='concave',
        ),
        migrations.RemoveField(
            model_name='breastmodel',
            name='points_mean',
        ),
        migrations.RemoveField(
            model_name='breastmodel',
            name='points_se',
        ),
        migrations.RemoveField(
            model_name='breastmodel',
            name='points_worst',
        ),
        migrations.AddField(
            model_name='breastmodel',
            name='concave_points_mean',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breastmodel',
            name='concave_points_se',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breastmodel',
            name='concave_points_worst',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='breastmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 3, 56, 344419)),
        ),
        migrations.AlterField(
            model_name='cardiomodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 3, 56, 344419)),
        ),
        migrations.AlterField(
            model_name='diabetesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 3, 56, 342357)),
        ),
        migrations.AlterField(
            model_name='heartmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 18, 3, 56, 343399)),
        ),
    ]
