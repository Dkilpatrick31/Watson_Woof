from django import forms
from models import Dog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class LoginForm(forms.Form):
#     """Login forms"""
#
#     username = forms.CharField(label="User Name", max_length=64)
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         if not user or not user.is_active:
#             raise forms.ValidationError("Username or Password incorrect.")
#         return self.cleaned_data
#
#     def login(self, request):
#         """Login Function """
#
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         return user
#
class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username = forms.CharField(label="User Name", max_length=64)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'value', 'gender', 'breed', 'age']
