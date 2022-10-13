from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
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

def loginView(request):
    return render(request, 'main/login.html')