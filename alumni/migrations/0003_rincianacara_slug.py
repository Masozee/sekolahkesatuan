# Generated by Django 2.1.5 on 2019-06-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0002_acara_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='rincianacara',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=140),
        ),
    ]
