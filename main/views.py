from django.http import HttpResponse, HttpResponseRedirect
from account.models import ProfileUserModel
from .forms import *
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


menu = [{'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'plate'},
        {'title_place': "Шлифовка",'name_form':'Учёт шлифовальных материалов', 'url_name': 'about-me'},
        {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'},
        {'title_place': "Пресс",'name_form':'Форма контроля раб. состояния форсунок САП', 'url_name': 'about-me'},
        {'title_place': "Пресс",'name_form':'Форма очистки лент преса', 'url_name': 'about-me'},
        {'title_place': "Пресс",'name_form':'Толщина нешлифованой плиты', 'url_name': 'about-me'},
        {'title_place': "Пресс и Сушилка",'name_form':'Расход природного газа и древесной пыли', 'url_name': 'about-me'},
        {'title_place': "Пресс",'name_form':'Производственные параметры для пресовщика', 'url_name': 'about-me'},
        {'title_place': "Распиловка",'name_form':'Учёт замены чернильной системы', 'url_name': 'about-me'},
        {'title_place': "Распиловка",'name_form':'Измерение покоробленности', 'url_name': 'about-me'},
        {'title_place': "Распиловка",'name_form':'Толщина пакета нешлифованой плиты', 'url_name': 'about-me'}
]


def index(request):

    profile = ProfileUserModel.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'profile': profile,
    }

    return render(request, 'main/index.html', context=context)


class CustomSuccessMessageMixin:
    """" для появления записи о обновления поля или добавлении нового  подсвечивается редактированая запись"""""
    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class CustomFormValidMixin:

    def form_valid(self, form):
        """"Переопределение формы валидации для добавления автора в базу"""""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CustomGetFormUpdateMixin:

    def get_form_kwargs(self):
        """"Переопределяем метод для редактирования Только своей записи"""""
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class CustomPostDeleteMixin:

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


"""" Начало {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'plate'} """

class table_thickness_ground_plate_view(ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины плиты, тоже самое что и def add_table_thickness_ground_plate(request):"""""

    model = table_thickness_ground_plate_model
    template_name = 'main/plate.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина плиты'}


class create_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CreateView):
    """"Класс для создания новой записи с измерениями толщины плиты. Тоже самое что и def create(request):"""""
    model = table_thickness_ground_plate_model
    template_name = 'main/create_new_thickness_ground_plate.html'
    form_class = create_thickness_ground_plate_form
    success_url = reverse_lazy('plate')
    success_msg = 'Запись создана'
    extra_context = {'title':'Толщина плиты'}

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = table_thickness_ground_plate_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class update_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CustomGetFormUpdateMixin, UpdateView):
    """"#Класс для редактирования записи
     Тоже самое что и def update_table(request, pk):   """""

    model = table_thickness_ground_plate_model
    template_name = 'main/update.html'
    form_class = create_thickness_ground_plate_form
    success_url = reverse_lazy('plate')
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений толщины плиты'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)



class delete_view(LoginRequiredMixin, CustomPostDeleteMixin, DeleteView):
    model = table_thickness_ground_plate_model
    template_name = 'main/delete.html'
    success_url = reverse_lazy('plate')
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления плиты.'}


"""" Конец {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'plate'} """


"""" Начало {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'about-me'} """



class Pack_board_view(ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения пачки
    таблица измерений толщины пачки    """""

    model = Table_Pack_Board_Model
    template_name = 'main/pack_board.html'
    context_object_name = 'list_value'
    extra_context = {'title':'Толщина пачки шлифованой плиты'}


class Pack_board_create_view(LoginRequiredMixin, CustomSuccessMessageMixin,CustomFormValidMixin, CreateView):
    """"Класс для создания новой записи с измерениями пачки. """""
    model = Table_Pack_Board_Model
    template_name = 'main/create_new_pack_board.html'
    form_class = Pack_of_board_form
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись создана'
    extra_context = {'title': 'Форма    по    добавлению   значений   отшлифованой    пачки'}

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Table_Pack_Board_Model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Pack_board_update_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,CustomGetFormUpdateMixin, UpdateView):
    """"Класс для редактирования записи"""""

    model = Table_Pack_Board_Model
    template_name = 'main/pack_board_update.html'
    form_class = Pack_of_board_form
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Форма для редактирования значений толщины пачки'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class Pack_board_delete_view(LoginRequiredMixin, CustomPostDeleteMixin, DeleteView):
    model = Table_Pack_Board_Model
    template_name = 'main/delete.html'
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления значений толщины пачки.'}


"""" Конец {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'about-me'}, """



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