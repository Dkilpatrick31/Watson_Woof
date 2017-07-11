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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

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

def update_dog(request, pk, template_name='request_form.html'):
   dog = get_object_or_404(Dog, pk=pk)
   form = DogForm(request.POST or None, instance=dog)
   if form.is_valid():
        form.save()
        messages.success(request, 'Request has been updated.')
        return redirect('/')
   return render(request, template_name, {'form': form})

def delete_dog(request, pk, template_name='dog_confirm_delete.html'):
   dog = get_object_or_404(dog, pk=pk)
   if request.method == 'POST':
        dog.delete()
        return redirect('/')
   return render(request, template_name, {'object': dog})

def about(request):
    dogs = Dog.objects.all()
    form = DogForm()
    return render(request, 'about.html', {'dogs':dogs, 'form':form})

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
