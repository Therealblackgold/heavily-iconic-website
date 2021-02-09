from django.db import models
from datetime import datetime 

# Create your models here.
class Service(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    description_1 = models.CharField(null=True, blank=True, max_length=300)
    price_1 = models.DecimalField(null=True, blank=True, max_digits=10000,decimal_places=2)
    price_date_1 = models.DateTimeField(default=datetime.now, blank=True)

    description_2 = models.CharField(null=True, blank=True, max_length=300)
    price_2 = models.DecimalField(null=True, blank=True, max_digits=10000,decimal_places=2)
    price_date_2 = models.DateTimeField(default=datetime.now, blank=True)

    description_3 = models.CharField(null=True, blank=True, max_length=300)
    price_3 = models.DecimalField(null=True, blank=True, max_digits=10000,decimal_places=2)
    price_date_3 = models.DateTimeField(default=datetime.now, blank=True)

    description_4 = models.CharField(null=True, blank=True, max_length=300)
    price_4 = models.DecimalField(null=True, blank=True, max_digits=10000,decimal_places=2)
    price_date_4 = models.DateTimeField(default=datetime.now, blank=True)

    description_5 = models.CharField(null=True, blank=True, max_length=300)
    price_5 = models.DecimalField(null=True, blank=True, max_digits=10000,decimal_places=2)
    price_date_5 = models.DateTimeField(default=datetime.now, blank=True) 





    def __str__(self):
        return self.title



   