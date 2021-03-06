# Generated by Django 3.1.6 on 2021-02-16 22:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_auto_20210217_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='created_by',
            field=models.ForeignKey(default='auth.User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 0, 24, 51, 209151)),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='image',
            field=models.ImageField(default=None, upload_to='media'),
        ),
    ]
