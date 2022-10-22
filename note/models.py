from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    category = models.CharField(max_length=50,null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class topic(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    topic = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic

class description(models.Model):
    topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000)
    time = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    bookmark = models.IntegerField(default=0)
    image = models.ImageField(upload_to="note/img", height_field=None, width_field=None, max_length=100, default="")

    def __str__(self):
        return self.description[0:100]