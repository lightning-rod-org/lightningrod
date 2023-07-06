# Generated by Django 4.0.3 on 2023-07-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0022_parseinput_file_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='parseinput',
            name='p_output',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='parseinput',
            name='file_content',
            field=models.CharField(max_length=1500),
        ),
    ]
