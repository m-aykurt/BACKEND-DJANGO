from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=50, blank=True, null=True,default="No Name")