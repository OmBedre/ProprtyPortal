from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = PhoneNumberField()
    email = models.EmailField( max_length=254)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now,blank=True)



    def __str__(self):
        return self.name
    
    