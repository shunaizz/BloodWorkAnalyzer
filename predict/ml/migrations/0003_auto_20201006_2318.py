# Generated by Django 3.1.1 on 2020-10-06 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20201006_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 23, 18, 7, 439526)),
        ),
    ]
