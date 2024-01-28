from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    summary = models.TextField(max_length=2000)
    graduation = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    previous_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)