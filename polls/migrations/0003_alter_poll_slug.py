# Generated by Django 3.2.20 on 2023-07-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_sluf_poll_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.SlugField(max_length=256, unique=True),
        ),
    ]
