from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=75, required=True)

    
    class Meta:  
        model = User 
        fields = ('email', 'first_name', 'last_name', 'username')