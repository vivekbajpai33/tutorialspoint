# Generated by Django 5.0.3 on 2024-06-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_classes_thumbnail_alter_classes_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='video_thumb'),
        ),
    ]
