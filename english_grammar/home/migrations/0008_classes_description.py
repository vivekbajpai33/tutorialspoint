# Generated by Django 5.0.3 on 2024-05-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_notification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
