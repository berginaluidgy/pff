# Generated by Django 5.0.4 on 2024-07-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paidBackendAPI', '0011_mission_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='missionbut',
            field=models.IntegerField(default=0),
        ),
    ]
