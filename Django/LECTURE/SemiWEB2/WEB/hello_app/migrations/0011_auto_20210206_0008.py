# Generated by Django 3.1.6 on 2021-02-06 00:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_app', '0010_auto_20210206_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='regdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 0, 8, 42, 792914)),
        ),
    ]
