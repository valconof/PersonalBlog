# Generated by Django 3.1.2 on 2021-12-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211130_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_information', models.CharField(max_length=50, verbose_name='текст информации')),
            ],
            options={
                'verbose_name': 'Информация админа',
                'verbose_name_plural': 'Информация админа',
            },
        ),
    ]
