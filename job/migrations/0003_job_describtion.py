# Generated by Django 4.1.1 on 2022-09-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='describtion',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
