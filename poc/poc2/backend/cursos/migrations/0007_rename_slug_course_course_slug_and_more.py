# Generated by Django 4.0.4 on 2022-06-16 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_courseposts_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='slug',
            new_name='course_slug',
        ),
        migrations.RenameField(
            model_name='courselesson',
            old_name='slug',
            new_name='lesson_slug',
        ),
    ]