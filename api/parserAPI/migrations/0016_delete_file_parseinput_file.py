# Generated by Django 4.0.3 on 2023-07-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0015_alter_parseinput_file_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AddField(
            model_name='parseinput',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
