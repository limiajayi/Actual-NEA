# Generated by Django 4.2.4 on 2024-02-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_mathspoints_exponents'),
    ]

    operations = [
        migrations.AddField(
            model_name='mathspoints',
            name='three_d_vectors',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]