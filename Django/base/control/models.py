from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=10)
    college=models.CharField(max_length=3)


    
    
