# Generated by Django 5.0.4 on 2024-06-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_alter_newclassname_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclassname',
            name='file',
            field=models.FileField(upload_to='projects/teacher'),
        ),
    ]
