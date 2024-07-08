from django.db import models
from django.urls import reverse
# Create your models here.
#https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
class Product(models.Model):
    title       = models.CharField(max_length=120) 
    description = models.TextField(blank=False, null=False)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True) 
    
    
    def get_absolute_url(self):
        return reverse("products:product_detail",kwargs={'id':self.id})