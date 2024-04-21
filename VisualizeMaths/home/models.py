from django.db import models #a class that defines the structure of databases
from django.contrib.auth.hashers import make_password #turns plain text passwords into a hash for databases

# Create your models here.
class StudentUser(models.Model):
    """A table containing the username, password and subjects for student users"""
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=250, null=True)
    maths = models.BooleanField(default=1, null=True)
    further_maths = models.BooleanField(null=True)

    def __str__(self):
        """Returns the usernames when viewing the table"""
        return self.username
    
    def save(self, *args, **kwargs):
      """Hashes passwords when users are being saved to the table"""
      self.password = make_password(self.password)
      super(StudentUser, self).save(*args, **kwargs)