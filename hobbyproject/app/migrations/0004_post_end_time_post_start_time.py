# Generated by Django 4.0.6 on 2022-07-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
