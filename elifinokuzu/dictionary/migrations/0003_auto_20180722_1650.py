# Generated by Django 2.0.7 on 2018-07-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_edge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='language',
            field=models.CharField(choices=[('tr', 'Turkish'), ('fr', 'French'), ('gr', 'German'), ('pl', 'Polish'), ('kr', 'Kurdish'), ('lt', 'Latin'), ('en', 'English'), ('es', 'Spanish'), ('ar', 'Arabic')], max_length=255),
        ),
    ]
