# Generated by Django 2.1.5 on 2019-06-27 09:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0004_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='Isi',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
