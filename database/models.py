from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email= models.EmailField(unique=True)