# Generated by Django 3.0.2 on 2020-08-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20200807_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor_info',
            name='Doctor_id',
        ),
        migrations.AddField(
            model_name='doctor_info',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
