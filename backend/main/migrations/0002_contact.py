# Generated by Django 4.0.4 on 2022-04-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=166)),
                ('street', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('coutry', models.CharField(max_length=255)),
            ],
        ),
    ]
