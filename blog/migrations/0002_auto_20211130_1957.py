# Generated by Django 3.1.2 on 2021-11-30 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Comment',
        ),
    ]
