from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control unicase-form-control text-input',
        'placeholder': 'Email Address',
        'id': 'id_email'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control unicase-form-control text-input',
        'placeholder': 'First Name',
        'id': 'id_first_name'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control unicase-form-control text-input',
        'placeholder': 'Phone Number',
        'id': 'id_phone'
    }))

    class Meta:
        model = CustomUser  # Use CustomUser instead of default User model
        fields = ['email', 'first_name', 'phone', 'password1', 'password2']
