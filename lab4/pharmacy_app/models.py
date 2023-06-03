from django.db import models
from django.urls import reverse

# Create your models here.


class Medicines(models.Model):
    code = models.CharField(max_length = 20, help_text="Enter code")
    name = models.CharField(max_length=20, help_text="Enter name")
    instruction = models.TextField(help_text="Enter instruction")
    description = models.TextField(help_text="Enter description")
    price = models.IntegerField(help_text="Enter price")
    medicines_type = models.ForeignKey('CarcassType', on_delete=models.SET_NULL, null=True, help_text="Choose carcass type")
    supplier = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True, help_text="Choose producer")
    photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name


class MedicinesType(models.Model):
    designation = models.CharField(max_length=20, help_text="Enter type")

    def __str__(self):
        return self.designation


class Supplier(models.Model):
    country = models.CharField(max_length=20, help_text="Enter country")
    owner = models.CharField(max_length=20, help_text="Enter owner")

    def __str__(self):
        return f'{self.country}, {self.owner}'


class Client(models.Model):
    first_name = models.CharField(max_length=20, help_text='Enter first name')
    last_name = models.CharField(max_length=20, help_text='Enter last name')
    date_of_birth = models.DateField(help_text="Enter date of birth")
    email = models.EmailField(help_text="Enter email")
    phone_number = models.CharField(max_length=15, help_text='Enter phone number')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
