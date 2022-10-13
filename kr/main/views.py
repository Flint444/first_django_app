from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football',
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

class SignupView(View):
    def get(self, request):
        fm = SignUpForm()
        return render(request, 'main/signup.html', {'form':fm})

    def post(self, request):
        fm = SignUpForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('signup')
        else:
            return render(request, 'main/signup.html', {'form': fm})

class MyloginView(View):
    def get(self, request):
        fm = MyLoginForm()
        return render(request, 'main/login.html', {'form': fm})

    def post(self, request):
        fm = MyLoginForm(request, data=request.POST)

        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'main/login.html', {'form': fm})

        else:
            return render(request, 'main/login.html', {'form': fm})

class GetUsers(View):
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        return render(request, 'main/contacts.html', {'form':users})
