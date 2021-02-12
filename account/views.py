from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView
# Create your views here.

class MyprojectLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main/index.html')

class RegisterUserView(CreateView):
    model = User
    template_name = 'account/register.html'
    form_class =  RegisterUserForm
    success_url = reverse_lazy('main/index.html')
    success_msg = 'Пользователь успешно создан'


def registerPage(request):
    context = {}
    return render(request, 'account/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)