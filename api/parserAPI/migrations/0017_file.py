# Generated by Django 4.0.3 on 2023-07-04 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0016_delete_file_parseinput_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
