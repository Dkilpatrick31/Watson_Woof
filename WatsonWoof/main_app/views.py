from django.shortcuts import render
from .models import Dog
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import DogForm, LoginForm

def index(request):
    dogs = Dog.objects.all()
    form = DogForm()
    return render(request, 'index.html', {'dogs':dogs})
    return render(request, 'index.html', {'dogs':dogs, 'form':form})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def dogprofile(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogprofile.html', {'dog': dog})

def post_dog(request):
    form = DogForm(request.POST)
    if form.is_valid():
        dog = form.save(commit = False)
        dog.user = request.user
        dog.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    dogs = Dog.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'dogs': dogs})

def like_dog(request):
    dog_id = request.GET.get('dog_id', None)

    likes = 0
    if (dog_id):
        dog = Dog.objects.get(id=int(dog_id))
        if dog is not None:
            likes = dog.likes + 1
            dog.likes = likes
            dog.save()
    return HttpResponse(likes)


# def about(request):
#     return render(request, 'about.html', {'dogs':dogs})


# Create your views here.
dogs = [
    Dog('Buck', 500.00, 'male', 'labrador/golden retriever mixed', '8 years old'),
    Dog('Nahla', 0, 'female', 'maltipoo', '4 years old'),
    Dog('Gunnar', 20.00, 'male', 'dachshund', '3 years old')
]
