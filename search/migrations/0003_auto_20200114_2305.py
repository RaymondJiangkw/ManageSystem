# Generated by Django 2.2.2 on 2020-01-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200108_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='score',
            field=models.CharField(default='1.0', max_length=5),
        ),
        migrations.AddField(
            model_name='lesson',
            name='weeks',
            field=models.CharField(default='第01-12周', max_length=51),
        ),
    ]
