from django.contrib import admin
from .models import Medicines, MedicinesType, Supplier, Client

# Register your models here.

@admin.register(Medicines)
class CarAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'description', 'price', 'instruction', 'medicines_type', 'supplier']
    list_filter = ['name', 'price', 'medicines_type']

@admin.register(MedicinesType)
class CarcassTypeAdmin(admin.ModelAdmin):
    list_display = ['designation']

@admin.register(Supplier)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['country', 'owner']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth','email', 'phone_number' ]
    list_filter = ['first_name', 'last_name', 'date_of_birth','email', 'phone_number' ]