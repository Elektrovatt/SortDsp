from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *
# Create your views here.


def registerPage(request):
    context = {}
    return render(request, 'account/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'account/login.html', context)