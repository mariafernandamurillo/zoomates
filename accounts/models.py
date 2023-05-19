from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=218)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role, 
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )