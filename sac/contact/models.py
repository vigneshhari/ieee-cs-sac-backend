from __future__ import unicode_literals

from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length = 500)
    phno = models.CharField(max_length = 20)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=10000)
    time = models.DateField()

    def __str__(self):
        return "Name = " + self.name + " Says " + self.message[:50]