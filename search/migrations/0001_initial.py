# Generated by Django 2.2.2 on 2020-01-08 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=51)),
                ('teacher', models.CharField(max_length=11)),
                ('capacity', models.IntegerField(default=0)),
                ('classroom', models.CharField(max_length=51)),
                ('supplement', models.TextField()),
                ('collage', models.CharField(max_length=51)),
                ('school', models.CharField(max_length=51)),
                ('lesson_id', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Class_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('interpretation', models.CharField(max_length=101)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Lesson')),
            ],
        ),
    ]