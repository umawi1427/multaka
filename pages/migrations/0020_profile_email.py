# Generated by Django 5.0.4 on 2024-05-03 21:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]