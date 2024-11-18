from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    usn = models.CharField(max_length=10)
    mobile = models.IntegerField()
    course = models.TextField()
    
    def __str__(self):
        return self.name
    
    