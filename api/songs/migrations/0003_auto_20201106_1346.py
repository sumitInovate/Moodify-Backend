# Generated by Django 3.1.2 on 2020-11-06 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20201106_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, help_text='Allowed_type - .mp3, .wav, .ogg', upload_to='audio/', validators=[django.core.validators.FileExtensionValidator(['.mp3', '.wav', '.ogg'])]),
        ),
    ]
