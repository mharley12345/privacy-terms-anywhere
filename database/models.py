from django.db import models
from .policies import Policy

import uuid


class Person(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email= models.EmailField(unique=True)
    password= models.CharField(max_length=20 ,default=None)
    uuid = models.UUIDField(default=uuid.uuid4,unique=True)


    def createUser(self):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = encrypt_password(password)
        self.save()


class SamplePolicys(models.Model):
    business_name= models.CharField(max_length=50)
    site_name = models.URLField()
    add_tracking = models.CharField(max_length=200,null=True,blank=True)
    add_payment_types = models.CharField(max_length=200,null=True,blank=True)
    add_information = models.CharField(max_length=200,null=True,blank=True)
    add_order_info = models.CharField(max_length=200,null=True,blank=True)
    add_device_info = models.CharField(max_length=200,null=True,blank=True)
    add_remarketing = models.CharField(max_length=200,null=True,blank=True)
    add_opt_out_links = models.CharField(max_length=200,null=True,blank=True)
    add_europe = models.BooleanField(default=False)
    add_age_restriction_age = models.IntegerField(null=True,blank=True)
    email = models.EmailField()
    street_address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()

    
    def TestPolicy(Field):
        return Policy()
    


    
    


    

