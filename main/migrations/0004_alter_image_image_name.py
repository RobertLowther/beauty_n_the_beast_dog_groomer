# Generated by Django 4.1 on 2022-08-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.FilePathField(verbose_name='gallery'),
        ),
    ]
