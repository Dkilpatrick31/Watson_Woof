from django.shortcuts import render, redirect
from .models import Dog
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import DogForm, LoginForm, SignUpForm

def index(request):
    dogs = Dog.objects.all()
    form = DogForm()
    return render(request, 'index.html', {'dogs':dogs, 'form':form})

# def about(request):
#     return render(request, 'about.html', {'dogs':dogs})


# Create your views here.
dogs = [
    Dog('Buck', 500.00, 'male', 'labrador/golden retriever mixed', '8 years old'),
    Dog('Nahla', 0, 'female', 'maltipoo', '4 years old'),
    Dog('Gunnar', 20.00, 'male', 'dachshund', '3 years old')
]
