# Generated by Django 3.1 on 2021-06-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classnotes',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='video_lectures',
            name='subject',
        ),
    ]