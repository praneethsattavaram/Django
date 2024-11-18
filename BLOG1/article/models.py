from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    age = models.IntegerField(null=True, blank=True) 