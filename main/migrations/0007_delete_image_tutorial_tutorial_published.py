# Generated by Django 4.1 on 2022-08-10 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_image_image_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 10, 7, 33, 24, 140642), verbose_name='date published'),
        ),
    ]
