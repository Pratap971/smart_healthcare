# Generated by Django 3.0.2 on 2020-08-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Disease',
            field=models.CharField(default='', max_length=100),
        ),
    ]