# Generated by Django 5.0.4 on 2024-07-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paidBackendAPI', '0010_mvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='Point',
            field=models.IntegerField(default=0),
        ),
    ]