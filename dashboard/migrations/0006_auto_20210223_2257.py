# Generated by Django 3.1.6 on 2021-02-23 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210217_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='Model',
            new_name='model',
        ),
        migrations.AlterField(
            model_name='shoe',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 22, 57, 46, 139765)),
        ),
    ]
