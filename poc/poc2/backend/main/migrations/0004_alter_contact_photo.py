# Generated by Django 4.0.4 on 2022-04-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.FileField(default='0', upload_to=''),
        ),
    ]