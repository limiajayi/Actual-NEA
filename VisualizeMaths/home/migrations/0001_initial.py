# Generated by Django 4.2.4 on 2023-12-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True, unique=True)),
                ('password', models.CharField(max_length=250, null=True)),
                ('maths', models.BooleanField(default=1, null=True)),
                ('further_maths', models.BooleanField(null=True)),
            ],
        ),
    ]
