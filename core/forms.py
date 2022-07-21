from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "roll", "father", "city")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'father': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
