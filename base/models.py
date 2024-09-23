from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=300)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=300)
    contact = models.BigIntegerField(null = True)
    USERNAME_FIELD = 'email' #overriding username_field to make login with email instead of username
    REQUIRED_FIELDS = ['username']

class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    process = models.TextField()
    ingredients = models.TextField()
    picture = models.ImageField(upload_to='pictures/', null=True)

    def __str__(self):
        return self.name