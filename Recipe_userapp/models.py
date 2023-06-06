from django.db import models

# Create your models here.
class contact(models.Model):
    name1=models.CharField(max_length=10)
    email1=models.EmailField()
    message1=models.CharField(max_length=1000)
class register(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=20)
