# Generated by Django 3.1.2 on 2020-11-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20201108_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='mood',
            field=models.CharField(choices=[('CHILL', 'CHILL'), ('SAD', 'SAD'), ('HAPPY', 'HAPPY'), ('ANGRY', 'ANGRY'), ('MOTIVATIONAL', 'MOTIVATIONAL'), ('DEVOTIONAL', 'DEVOTIONAL'), ('CLASSICAL', 'CLASSICAL'), ('PARTY', 'PARTY'), ('ROMANTIC', 'ROMANTIC')], default='RANDOM', max_length=50),
        ),
    ]
