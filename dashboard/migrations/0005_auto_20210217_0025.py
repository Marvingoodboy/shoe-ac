# Generated by Django 3.1.6 on 2021-02-16 22:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_auto_20210217_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 0, 25, 49, 41846)),
        ),
    ]
