from django.db import models
from home.models import StudentUser

# Create your models here.
class MathsPoints(models.Model):
    """Stores the maths points in each maths topic for each user within StudentUser"""
    username = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, unique=True)
    quadratics = models.IntegerField(default=0, blank=True)
    equations_and_inequalities = models.IntegerField(default=0, blank=True)
    graphs_and_transformations = models.IntegerField(default=0, blank=True)
    straight_line_graphs = models.IntegerField(default=0, blank=True)
    circles = models.IntegerField(default=0, blank=True)
    trigonometry = models.IntegerField(default=0, blank=True)
    differentiation = models.IntegerField(default=0, blank=True)
    integration = models.IntegerField(default=0, blank=True)
    two_d_vectors = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.username)
    
class FurtherMathsPoints(models.Model):
    """Stores the further maths points in each further maths topic for users doing further maths within StudentUser"""
    username = models.OneToOneField(StudentUser, on_delete=models.CASCADE, null=True, unique=True)
    differentiation = models.IntegerField(default=0, blank=True)
    integration = models.IntegerField(default=0, blank=True)
    argand_diagrams = models.IntegerField(default=0, blank=True)
    volumes_of_revolution = models.IntegerField(default=0, blank=True)
    methods_in_calculus = models.IntegerField(default=0, blank=True)
    matrices = models.IntegerField(default=0, blank=True)
    polar_coordinates = models.IntegerField(default=0, blank=True)
    hyperbolic_functions = models.IntegerField(default=0, blank=True)
    three_d_vectors = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.username)
