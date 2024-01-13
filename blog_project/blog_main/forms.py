from django import forms
from django.forms import fields, widgets
from django.forms.models import model_to_dict
from .models import *


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password', 'mobile_no', 'address', 'City', 'State', 'Country', 'PinCode', 'Profile_Image')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'mobile_no': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'City': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'State': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Country': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'PinCode': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Profile_Image': forms.FileInput(attrs={
                'class': 'form-control'
            }),


        }