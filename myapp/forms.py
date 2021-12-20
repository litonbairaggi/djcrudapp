from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import UserModel

class UserForm(forms.ModelForm):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name Here'}), required=True, error_messages={'required':'Must Enter a Currect Name'})
    address = forms.CharField(label="Your address", widget=forms.Textarea({'class': 'form-control', 'placeholder':'Name Address', 'rows':3, 'cols':50}), required=True, error_messages={'required':'Must Enter a Currect Address'})
    class Meta:
        model = UserModel
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email Here'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Mobile Here'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'language': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }
        error_messages = {
            'gender': {'required': 'Must Select a Gender'},
            'email': {'required': 'Must Correct Email'},
        }