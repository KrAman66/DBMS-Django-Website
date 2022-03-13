# Generated by Django 3.1 on 2021-06-10 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_studentdetails_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentresult',
            name='roll',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student_result', serialize=False, to='web.studentdetails'),
        ),
    ]
