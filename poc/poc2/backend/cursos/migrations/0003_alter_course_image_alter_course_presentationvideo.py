# Generated by Django 4.0.4 on 2022-06-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_course_image_alter_course_presentationvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='null', upload_to='./static/images/courses/images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='presentationVideo',
            field=models.FileField(default='null', upload_to='./static/images/courses/videos'),
        ),
    ]