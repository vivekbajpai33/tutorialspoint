# Generated by Django 5.0.3 on 2024-06-06 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_classes_courses_alter_courses_subjectname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['subjectname']},
        ),
    ]
