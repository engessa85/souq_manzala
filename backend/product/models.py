from contextlib import nullcontext
from operator import mod
from tkinter.tix import Balloon
from django.db import models

# Create your models here.

class Persons(models.Model):
    idvalue = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(null = True,blank = True)

    def __str__(self):
        return self.first_name


class MainSlider(models.Model):
    productor_name = models.CharField(max_length=100)
    avatar = models.ImageField(null = True,blank = True)

    def __str__(self):
        return self.productor_name