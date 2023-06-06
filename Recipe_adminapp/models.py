from django.db import models

# Create your models here.
class recipe(models.Model):
     recipe_name=models.CharField(max_length=10)
     recipe_image=models.ImageField(upload_to='pic',default='null.jpg')
     instruction=models.TextField(max_length=2000)
     ingredients=models.TextField(max_length=2000)
     