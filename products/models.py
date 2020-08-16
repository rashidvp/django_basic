from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)

class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class Form(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=2000)