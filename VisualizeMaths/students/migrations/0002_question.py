# Generated by Django 4.2.4 on 2023-12-31 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, null=True)),
                ('answer', models.CharField(max_length=1000, null=True)),
                ('subject', models.CharField(choices=[('Maths', 'Maths'), ('Further Maths', 'Further Maths')], max_length=30, null=True)),
                ('topic', models.CharField(blank=True, choices=[('Quadratics', 'Quadratics'), ('Equations and Inequalities', 'Equations and Inequalities'), ('Graphs and Transformations', 'Graphs and Transformations'), ('Straight Line Graphs', 'Straight Line Graphs'), ('Circles', 'Circles'), ('Trigonometry', 'Trigonometry'), ('Differentiation', 'Differentiation'), ('Integration', 'Integration'), ('Exponentials and Logarithms', 'Exponentials and Logarithms'), ('2D Vectors', '2D Vectors'), ('Argand Diagrams', 'Argand Diagrams'), ('Volumes of Revolution', 'Volumes of Revolution'), ('Methods In Calculus', 'Methods In Calculus'), ('Matrices', 'Matrices'), ('3D Vectors', '3D Vectors'), ('Polar Coordinates', 'Polar Coordinates'), ('Hyperbolic Functions', 'Hyperbolic Functions')], max_length=100, null=True)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='questions/')),
                ('mark_scheme', models.ImageField(blank=True, null=True, upload_to='markschemes/')),
                ('answer_box', models.IntegerField(blank=True, null=True)),
                ('worked_solutions', models.ImageField(blank=True, null=True, upload_to='solutions/')),
            ],
        ),
    ]