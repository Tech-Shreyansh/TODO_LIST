from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class trial_class(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    classs = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.classs

class trial(models.Model):
    classs = models.ForeignKey(trial_class, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class trial_skill(models.Model):

    name = models.ForeignKey(trial, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill




