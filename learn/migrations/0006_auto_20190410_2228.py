# Generated by Django 2.1.7 on 2019-04-10 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_teacher_teacher_allowance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_allowance',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='teacher_allowance',
            name='teacher_id',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
        migrations.DeleteModel(
            name='teacher_allowance',
        ),
    ]
