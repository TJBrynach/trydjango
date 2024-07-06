from django.db import models

# Create your models here.

#https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
class Product(models.Model):
    title       = models.CharField(max_length=120) 
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()