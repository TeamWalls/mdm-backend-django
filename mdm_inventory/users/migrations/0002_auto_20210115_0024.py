# Generated by Django 3.0.11 on 2021-01-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_supervisor',
            field=models.BooleanField(default=False, verbose_name='SuperVisor'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
