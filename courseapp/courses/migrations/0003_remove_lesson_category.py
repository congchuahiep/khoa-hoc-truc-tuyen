# Generated by Django 5.1.6 on 2025-02-28 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_category_course_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='category',
        ),
    ]
