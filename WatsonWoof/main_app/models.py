# main_app/models.py
from django.db import models

def __str__(self):
	return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
# Create your models here.
