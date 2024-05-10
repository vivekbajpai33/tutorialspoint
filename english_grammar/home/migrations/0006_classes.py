# Generated by Django 5.0.3 on 2024-04-23 02:31

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blogstory_contact_notification_studentquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video', models.FileField(null=True, upload_to='class_video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'mp4', 'webm', 'avi', 'mkv'])])),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.courses')),
            ],
        ),
    ]
