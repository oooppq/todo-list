# Generated by Django 4.0.6 on 2022-07-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_body_post_content_remove_post_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]