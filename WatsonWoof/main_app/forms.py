from django import forms
from .models import Dog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'value', 'gender', 'breed', 'age']

    # name = forms.CharField(label='Name', max_length=100)
    # value = forms.DecimalField(label='Value', max_digits=10, decimal_places=2)
    # gender = forms.CharField(label='Gender', max_length=100)
    # breed = forms.CharField(label='Breed', max_length=100)
    # age = forms.CharField(label='Age', max_length=100)
