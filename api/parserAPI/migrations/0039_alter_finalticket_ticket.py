# Generated by Django 4.0.3 on 2023-07-21 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parserAPI', '0038_alter_finalticket_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalticket',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='final_tick', to='parserAPI.ticket'),
        ),
    ]
