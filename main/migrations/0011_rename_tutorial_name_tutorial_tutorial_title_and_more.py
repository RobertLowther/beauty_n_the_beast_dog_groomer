# Generated by Django 4.1 on 2022-08-10 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_name',
            new_name='tutorial_title',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 7, 38, 32, 865885), verbose_name='date published'),
        ),
    ]
