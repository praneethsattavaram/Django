from django.db import models

# Create your models here.


class Recipe(models.Model):
    Title = models.CharField(max_length=100)
    Ingredients = models.TextField()
    Preparation_time = models.CharField(max_length=10)
    Instructions = models.TextField()
    
    def _str_(self):
        return self.Title
