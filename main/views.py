from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import create_thickness_ground_plate_form
from .models import *
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

# def add_table_thickness_ground_plate(request):
#   тоже самое что и class table_thickness_ground_plate_view(ListView):
#     list_value = Add_table_thickness_ground_plate.objects.all()
#     context = {
#     'list_value':list_value,
#        }
#     return render(request, 'main/plate.html', context)

class table_thickness_ground_plate_view(ListView):
    #таблица измерений толщины плиты
    model = table_thickness_ground_plate_model
    template_name = 'main/plate.html'
    context_object_name = 'list_value'


class create_view(ListView):
    model = table_thickness_ground_plate_model
    template_name = 'main/create_new_thickness_ground_plate.html'
    form_class = create_thickness_ground_plate_form
    success_url = reverse_lazy('main/create_new_thickness_ground_plate.html')


# class update_table(UpdateView):
#     model = table_thickness_ground_plate_model
#     template_name = 'main/update.html'
#     form_class = create_thickness_ground_plate_form


def update_table(request, pk):
    get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
    if request.method == 'POST':
        form = create_thickness_ground_plate_form(request.POST, instance = get_plate)
        if form.is_valid():
            form.save()
            return redirect('plate')
    template = 'main/update.html'
    context = {
            'get_plate': get_plate,
            'update':True,
            'form':create_thickness_ground_plate_form(instance = get_plate),
    }
    return render(request, template, context)

def create(request):
    error = ''
    if request.method == 'POST':
        form = create_thickness_ground_plate_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plate')
        else: 'Форма была не верной'
    form = create_thickness_ground_plate_form()
    context = {
        'form': form,
        'error': error
                }
    return render(request, 'main/create_new_thickness_ground_plate.html', context)


def delete(request,pk):
    get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
    get_plate.delete()
    return redirect(reverse('plate'))

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')