from django.db import models
from django.contrib.auth.models import User

from __future__ import unicode_literals

from django.db import models



class User(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
    	return self.name
