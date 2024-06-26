# Generated by Django 5.0.3 on 2024-05-16 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_delete_captcha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='courses',
            name='subject_code',
        ),
        migrations.RemoveField(
            model_name='courses',
            name='subject_name',
        ),
        migrations.AddField(
            model_name='courses',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='subject',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.subject'),
        ),
    ]
