# Generated by Django 5.0.4 on 2024-06-21 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paidBackendAPI', '0005_videoview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('type', models.CharField(max_length=256)),
                ('careerB', models.DateField(default=datetime.date.today)),
                ('contrat', models.CharField(max_length=256)),
                ('contratDate', models.DateField(default=datetime.date.today)),
                ('contratEnCours', models.BooleanField()),
                ('contratRenouvelable', models.BooleanField()),
                ('typeOfWork', models.CharField(max_length=256)),
                ('money', models.IntegerField()),
                ('preveousMoney', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('idmission', models.IntegerField()),
                ('MissionName', models.CharField(max_length=256)),
                ('missionType', models.CharField(max_length=256)),
                ('MissionDate', models.DateField()),
                ('EndMissionDate', models.DateField()),
                ('ifMissionSuccesfully', models.BooleanField()),
                ('predicateReceiveMoney', models.IntegerField()),
            ],
        ),
    ]
