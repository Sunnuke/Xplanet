# Generated by Django 2.2.4 on 2020-11-19 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_X', '0012_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='This human is a New Comer! ...or is just to lazy to leave a comment in their Bio!'),
        ),
    ]
