# Generated by Django 5.0.6 on 2024-06-11 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_subject_created_subject_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='videothumb/'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='classvideo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'webm', 'avi', 'mkv'])]),
        ),
    ]