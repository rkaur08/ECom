# Generated by Django 2.2.3 on 2019-07-23 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location default', max_length=128),
        ),
    ]
