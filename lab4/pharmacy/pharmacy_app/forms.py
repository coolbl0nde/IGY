from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import Medicines


def validate_age(value):
    today = date.today()
    age = today.year - value.year - int((today.month, today.day) < (value.month, value.day))
    if int(age) < 18:
        raise ValidationError("You must be over 18 years old")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))

    first_name = forms.CharField(label='first name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='last name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    date_birthday = forms.DateField(label='date of birth', widget=forms.DateInput(attrs={'class': 'form-input'}),
                                    validators=[validate_age])
    phone_number = forms.CharField(label='phone number', widget=forms.TextInput(attrs={'class': 'form-input'}),
                                   validators=[RegexValidator(
                                       regex=r'^(\+375 \(29\) [0-9]{3}-[0-9]{2}-[0-9]{2})$',
                                       message='Format +375 (29) XXX-XX-XX',
                                   )])
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = (
        'username', 'first_name', 'last_name', 'email', 'date_birthday', 'phone_number', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class MedicinesForm(forms.ModelForm):
    code = forms.CharField(label='code', widget=forms.TextInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    price = forms.IntegerField(label='price', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Medicines
        fields = ['code', 'name', 'instruction', 'description', 'price', 'medicines_type', 'supplier',
                  'photo']
