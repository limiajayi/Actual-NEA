from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class StudentUser(models.Model):
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=250, null=True)
    maths = models.BooleanField(default=1, null=True)
    further_maths = models.BooleanField(null=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
      self.password = make_password(self.password)
      super(StudentUser, self).save(*args, **kwargs)