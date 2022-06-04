from django import forms
from django.forms import widgets
from .models import *


class CustomModelForm(forms.ModelForm):
  #we can change field property here also ex
  #name=forms.CharField(max_length=50)
  class Meta:
    model = User
    #This is for all the fields
    # fields = '__all__'
    fields = ['name', 'email', 'password']
    labels = {
        'name': 'Enter Name',
        'email': 'Enter email',
    }
    help_text = {
        'name': 'Enter your name here'
    }
    error_messages = {
        "name": {
            'required': "Name is required",
            'max_length': "Name length should be greater than 5 characters"
        },
        "email": {
            'required': "Email is required"
        }
    }
    widgets = {
        'password': forms.PasswordInput,
        'name': forms.TextInput(attrs={
            'class': 'name_class',
            'placeholder':'enter your name'
        })
    }
