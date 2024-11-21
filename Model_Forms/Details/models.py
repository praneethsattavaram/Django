from django.db import models

# Create your models here.

class LaptopDetails(models.Model):
    name = models.CharField(max_length=20)
    processor = models.CharField(max_length=20)
    memory = models.IntegerField()
    screen_size = models.IntegerField()
    
    def __str__(cls):
        return cls.name
    