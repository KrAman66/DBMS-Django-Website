# Generated by Django 3.1 on 2021-05-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='name',
            field=models.CharField(default=str, max_length=50),
            preserve_default=False,
        ),
    ]
