# Generated by Django 5.0.4 on 2024-06-12 16:02

import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclassname',
            name='file',
            field=models.FileField(upload_to='projects/'),
        ),
    ]
