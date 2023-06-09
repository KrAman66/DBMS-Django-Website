# Generated by Django 3.1 on 2021-06-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('guardian_name', models.CharField(max_length=50)),
                ('standard', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=600)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('guardian_mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('english', models.IntegerField()),
                ('math', models.IntegerField()),
                ('science', models.IntegerField()),
                ('history', models.IntegerField()),
                ('geography', models.IntegerField()),
                ('total', models.FloatField()),
                ('grade', models.CharField(max_length=2)),
            ],
        ),
    ]
