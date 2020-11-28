# Generated by Django 3.1.1 on 2020-11-22 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0016_auto_20201122_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardiomodel',
            old_name='alco',
            new_name='alcohol',
        ),
        migrations.RenameField(
            model_name='cardiomodel',
            old_name='gluc',
            new_name='glucose',
        ),
        migrations.AlterField(
            model_name='breastmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 10, 23, 14, 684933)),
        ),
        migrations.AlterField(
            model_name='cardiomodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 10, 23, 14, 684933)),
        ),
        migrations.AlterField(
            model_name='diabetesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 10, 23, 14, 683931)),
        ),
        migrations.AlterField(
            model_name='heartmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 10, 23, 14, 683931)),
        ),
    ]