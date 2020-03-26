# Generated by Django 3.0.4 on 2020-03-26 07:23

import dblog.files
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dblog', '0011_auto_20200326_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='media/blog/images/'), upload_to=dblog.files.blog_image_upload_path, verbose_name='Cover Image'),
        ),
    ]