# Generated by Django 4.2.2 on 2023-06-27 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0003_parseinput_p_output'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parseinput',
            name='time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
