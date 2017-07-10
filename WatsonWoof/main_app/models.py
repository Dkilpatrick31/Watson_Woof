from django.db import models
from django.contrib.auth.models import User


class Dog(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    likes = models.IntegerField(default=0)

    # Figure out how to get these other classifications to work!

    # location = models.CharField(max_length=100)
    # childcompatability = models.CharField(max_length=100)
    # catcompatability = models.CharField(max_length=100)
    # dogcompatability = models.CharField(max_length=100)
    # description = models.CharField(max_length=100)

    def __str__(self):
    	return self.name
        return self.value
        return self.gender
        return self.breed
        return self.age
        return self.location
        return self.childcompatability
        return self.catcompatability
        return self.dogcompatability
        return self.description
