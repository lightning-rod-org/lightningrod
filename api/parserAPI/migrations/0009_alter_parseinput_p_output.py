# Generated by Django 4.2.2 on 2023-07-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0008_parseinput_client_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parseinput',
            name='p_output',
            field=models.JSONField(null=True),
        ),
    ]