from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    # author_r=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=500)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
    # contact_id=models.AutoField(primary_key=True)
    # author_r=models.CharField(max_length=50)
class Post(models.Model):
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/images', blank=True, null=True)

    def __str__(self):
        return self.description[:50]  # Return first 50 characters of description as string representation
   

    
    

class Product(models.Model):
    # create media folder and setting .py me line 118 (three lines)
    
    product_id=models.AutoField
    product_name=models.CharField(max_length=100 )
    category=models.CharField(max_length=100,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images' ,default="")


    def __str__(self):
        return self.product_name


   

class Message(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text