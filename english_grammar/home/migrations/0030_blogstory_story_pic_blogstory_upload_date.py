# Generated by Django 5.0.6 on 2024-06-14 07:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogstory',
            name='story_pic',
            field=models.ImageField(blank=True, null=True, upload_to='storypic/'),
        ),
        migrations.AddField(
            model_name='blogstory',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
