# Generated by Django 4.2.4 on 2024-02-12 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathspoints',
            name='exponents',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
