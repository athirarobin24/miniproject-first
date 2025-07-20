from django import forms
from .models import Person

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'address', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }