# Generated by Django 4.0.3 on 2023-06-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0004_alter_parseinput_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='parseinput',
            name='ticket_number',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
    ]
