from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)

