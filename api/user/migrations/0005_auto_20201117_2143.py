# Generated by Django 3.1.2 on 2020-11-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_customuser_paid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')], max_length=20, null=True),
        ),
    ]
