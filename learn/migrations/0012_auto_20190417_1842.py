# Generated by Django 2.1.7 on 2019-04-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0011_auto_20190417_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtopics_info',
            name='code_cpp',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='subtopics_info',
            name='code_py',
            field=models.TextField(blank=True, default=None),
        ),
    ]
