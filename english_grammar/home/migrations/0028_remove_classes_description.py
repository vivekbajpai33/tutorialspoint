# Generated by Django 5.0.6 on 2024-06-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_courses_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='description',
        ),
    ]
