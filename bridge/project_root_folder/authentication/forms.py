from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    fname = forms.CharField(max_length=30, required=True, help_text='Enter your first name')
    lname = forms.CharField(max_length=30, required=True, help_text='Enter your last name')
    email = forms.EmailField(max_length=254, required=True, help_text='Enter your email address')

    class Meta:
        model = User  # Assuming you have imported User model
        fields = UserCreationForm.Meta.fields + ('fname', 'lname', 'email')

