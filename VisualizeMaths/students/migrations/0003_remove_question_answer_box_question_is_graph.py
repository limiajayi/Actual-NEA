# Generated by Django 4.2.4 on 2024-01-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer_box',
        ),
        migrations.AddField(
            model_name='question',
            name='is_graph',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
