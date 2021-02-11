from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import create_thickness_ground_plate_form
from .models import *
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages

class table_thickness_ground_plate_view(ListView):
    # Класс для отображения всех записей смена дата измерения плиты
    #таблица измерений толщины плиты, тоже самое что и def add_table_thickness_ground_plate(request):
    model = table_thickness_ground_plate_model
    template_name = 'main/plate.html'
    context_object_name = 'list_value'


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)



class create_view(CustomSuccessMessageMixin, CreateView):
    #Класс для создания новой записи с измерениями толщины плиты.
    #Тоже самое что и def create(request):
    model = table_thickness_ground_plate_model
    template_name = 'main/create_new_thickness_ground_plate.html'
    form_class = create_thickness_ground_plate_form
    success_url = reverse_lazy('plate')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] =  table_thickness_ground_plate_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)

class update_view(CustomSuccessMessageMixin, UpdateView):
    #Класс для редактирования записи
    # Тоже самое что и def update_table(request, pk):
    model = table_thickness_ground_plate_model
    template_name = 'main/create_new_thickness_ground_plate.html'
    form_class = create_thickness_ground_plate_form
    success_url = reverse_lazy('plate')
    success_msg = 'Запись успешно обнавлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] =  True
        return super().get_context_data(**kwargs)

class delete_view(DeleteView):
    model = table_thickness_ground_plate_model
    template_name = 'main/create_new_thickness_ground_plate.html'
    success_url = reverse_lazy('plate')
    success_msg = 'Запись удалена'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


# def delete(request,pk):
#     get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
#     get_plate.delete()
#     return redirect(reverse('plate'))

# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = create_thickness_ground_plate_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('plate')
#         else: 'Форма была не верной'
#     form = create_thickness_ground_plate_form()
#     context = {
#         'form': form,
#         'error': error
#                 }
#     return render(request, 'main/create_new_thickness_ground_plate.html', context)

# def add_table_thickness_ground_plate(request):
#   тоже самое что и class table_thickness_ground_plate_view(ListView):
#     list_value = Add_table_thickness_ground_plate.objects.all()
#     context = {
#     'list_value':list_value,
#        }
#     return render(request, 'main/plate.html', context)

# def update_table(request, pk):
#     get_plate = table_thickness_ground_plate_model.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = create_thickness_ground_plate_form(request.POST, instance = get_plate)
#         if form.is_valid():
#             form.save()
#             return redirect('plate')
#     template = 'main/update.html'
#     context = {
#             'get_plate': get_plate,
#             'update':True,
#             'form':create_thickness_ground_plate_form(instance = get_plate),
#     }
#     return render(request, template, context)