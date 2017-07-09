# main_app/views.py
from django.shortcuts import render
from .models import Dog

def index(request):
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'dogs':dogs})

# Create your views here.




dogs = [
    Dog('Buck', 500.00, 'male', 'labrador/golden retriever mixed', '8 years old'),
    Dog('Nahla', 0, 'female', 'maltipoo', '4 years old'),
    Dog('Gunnar', 20.00, 'male', 'dachshund', '3 years old')
]
