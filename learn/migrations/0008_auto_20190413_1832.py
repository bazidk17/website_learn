# Generated by Django 2.1.7 on 2019-04-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_auto_20190410_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_picture',
            field=models.ImageField(upload_to='courses/imag/'),
        ),
        migrations.AlterField(
            model_name='subtopics_info',
            name='diagram',
            field=models.ImageField(upload_to='diagram_representation/imag/'),
        ),
    ]
