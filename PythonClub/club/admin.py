from django.db import models
from django.contrib.auth.models import User

class ProductType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='producttype'
        verbose_name_plural='producttypes'
