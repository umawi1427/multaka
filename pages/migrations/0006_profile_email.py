# Generated by Django 5.0.4 on 2024-05-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_profile_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
