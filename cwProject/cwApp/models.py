
from django.db import models


#function for dog

class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField (max_length=200)
    color = models.CharField (max_length=200)
    gender = models.CharField (max_length=200)
    #function for account
class Account(models.Model):
    username = models.CharField (max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField(default=0)