# Generated by Django 5.0.6 on 2024-06-04 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_date',
        ),
    ]
