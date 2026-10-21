from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)