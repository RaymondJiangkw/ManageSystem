# Generated by Django 2.2.2 on 2020-01-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200114_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='time',
            field=models.CharField(default='星期一第1节', max_length=51),
        ),
        migrations.DeleteModel(
            name='Class_time',
        ),
    ]
