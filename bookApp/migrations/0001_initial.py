# Generated by Django 3.1 on 2021-05-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('qty', models.IntegerField()),
                ('au_name', models.CharField(max_length=100)),
            ],
        ),
    ]
