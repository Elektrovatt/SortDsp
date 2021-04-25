from django.http import HttpResponse, HttpResponseRedirect
from account.models import ProfileUserModel
from .forms import *
from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *

def index(request):

    profile = ProfileUserModel.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        'profile': profile,
    }

    return render(request, 'main/index.html', context=context)




"""" Начало {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'board'} """

# {% for book in books|dictsort:"author.age" %}
#  * {{ book.title }} ({{ book.author.name }})
# {% endfor %}   попробовать выводить на главную страницу профиль...


class CustomThicknessBoardMixin:
    model = Thickness_board_model
    success_url = reverse_lazy('board')


class List_thickness_board_view(CustomThicknessBoardMixin, ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины плиты"""
    template_name = 'main/shlifovka/board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина плиты'}


class Create_thickness_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomThicknessBoardMixin, CreateView):
    """Класс для создания новой записи с измерениями толщины плиты."""
    template_name = 'main/shlifovka/create_new_board.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Толщина плиты'}
    form_class = Thickness_board_form

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Thickness_board_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_thickness_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomThicknessBoardMixin, CustomGetFormUpdateMixin, UpdateView):
    """Класс для редактирования записи"""
    form_class = Thickness_board_form
    template_name = 'main/shlifovka/board_update.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений толщины плиты'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class Delete_thickness_board_view(LoginRequiredMixin, CustomPostDeleteMixin, CustomThicknessBoardMixin, DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления плиты.'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'board'
        return context

"""" Конец {'title_place': "Шлифовка",'name_form':'Толщина Шлифованой плиты', 'url_name': 'board'} """


"""" Начало {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'} """


class List_thickness_pack_board_view(ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения пачки
    таблица измерений толщины пачки    """""

    model = Thickness_pack_board_model
    template_name = 'main/shlifovka/pack_board.html'
    context_object_name = 'list_value'
    extra_context = {'title':'Толщина пачки шлифованой плиты'}


class Create_thickness_pack_board_view(LoginRequiredMixin, CustomSuccessMessageMixin,CustomFormValidMixin, CreateView):
    """"Класс для создания новой записи с измерениями пачки. """""
    model = Thickness_pack_board_model
    template_name = 'main/shlifovka/create_new_pack_board.html'
    form_class = Thickness_pack_board_form
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись создана'
    extra_context = {'title': 'Форма    по    добавлению   значений   отшлифованой    пачки'}

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Thickness_pack_board_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_thickness_pack_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CustomGetFormUpdateMixin, UpdateView):
    """"Класс для редактирования записи"""""

    model = Thickness_pack_board_model
    template_name = 'main/shlifovka/pack_board_update.html'
    form_class = Thickness_pack_board_form
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Форма для редактирования значений толщины пачки'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class Delete_thickness_pack_board_view(LoginRequiredMixin, CustomPostDeleteMixin, DeleteView):
    model = Thickness_pack_board_model
    template_name = 'main/delete.html'
    success_url = reverse_lazy('pack-board')
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления значений толщины пачки.'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'pack-board'
        return context

"""" Конец {'title_place': "Шлифовка",'name_form':'Толщина пакета шлифованной плиты', 'url_name': 'pack-board'}, """

"""" Начало {'title_place': "Пресс",'name_form':'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'}, """


class List_thickness_unpolished_board_view(ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины плиты, тоже самое что и def add_table_thickness_ground_plate(request):"""""

    model = Thickness_unpolished_board_model
    template_name = 'main/press/list_unpolished_board.html.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина нешлифованой плиты'}


class Create_thickness_unpolished_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CreateView):
    """"Класс для создания новой записи с измерениями толщины плиты. Тоже самое что и def create(request):"""""

    model = Thickness_unpolished_board_model
    template_name = 'main/press/create_new_thickness_unpolished_board.html'
    form_class = Thickness_unpolished_board_form
    success_url = reverse_lazy('list-unpolished-board')
    success_msg = 'Запись создана'
    extra_context = {'title':'Толщина нешлифованой плиты'}

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Thickness_unpolished_board_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_thickness_unpolished_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CustomGetFormUpdateMixin, UpdateView):
    """"#Класс для редактирования записи    """""

    model = Thickness_unpolished_board_model
    template_name = 'main/press/update_unpolished_board.html'
    form_class = Thickness_unpolished_board_form
    success_url = reverse_lazy('list-unpolished-board')
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  толщины нешлифованой плиты'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class Delete_thickness_unpolished_board_view(LoginRequiredMixin, CustomPostDeleteMixin, DeleteView):
    model = Thickness_unpolished_board_model
    template_name = 'main/delete.html'
    success_url = reverse_lazy('list-unpolished-board')
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления значений нешлифованой плиты.'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-unpolished-board'
        return context

"""" Конец {'title_place': "Пресс",'name_form':'Толщина нешлифованой плиты', 'url_name': 'list-unpolished-board'}, """


"""" Начало {'title_place': "Распиловка",'name_form':'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'} """


class List_thickness_unpolished_pack_board_view(ListView):
    """" Класс для отображения всех записей. Cмена, дата измерения плиты
    таблица измерений толщины нешлифованой пачки"""""

    model = Thickness_unpolished_pack_board_model
    template_name = 'main/raspilovka/pack_unpolished_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Толщина пакета нешлифованой плиты'}


class Create_thickness_unpolished_pack_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CreateView):
    """"Класс для создания новой записи с измерениями толщины пакета нешлифованой плиты."""""

    model = Thickness_unpolished_pack_board_model
    template_name = 'main/raspilovka/create_new_pack_unpolished_board.html'
    form_class = Thickness_unpolished_pack_board_form
    success_url = reverse_lazy('list-unpolished-pack-board')
    success_msg = 'Запись создана'
    extra_context = {'title':'Толщина пакета нешлифованой плиты'}

    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Thickness_unpolished_pack_board_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_thickness_unpolished_pack_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin, CustomGetFormUpdateMixin, UpdateView):
    """"#Класс для редактирования записи значений толщины пакета нешлифованой плиты   """""

    model = Thickness_unpolished_pack_board_model
    template_name = 'main/raspilovka/pack_unpolished_board_update.html'
    form_class = Thickness_unpolished_pack_board_form
    success_url = reverse_lazy('list-unpolished-pack-board')
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений  толщины пакета нешлифованой плиты'}

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class Delete_thickness_unpolished_pack_board_view(LoginRequiredMixin, CustomPostDeleteMixin, DeleteView):
    model = Thickness_unpolished_pack_board_model
    template_name = 'main/delete.html'
    success_url = reverse_lazy('list-unpolished-pack-board')
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления значений пачки нешлифованой плиты.'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-unpolished-pack-board'
        return context

"""" Конец {'title_place': "Распиловка",'name_form':'Толщина пакета нешлифованой плиты', 'url_name': 'list-unpolished-pack-board'} """


"""" Начало {'title_place': "Шлифовка",'name_form':'Учёт шлифовальных материалов', 'url_name': 'number-tapes'} """



class CustomNumberTapesMixin:
    model = Number_tapes_model
    success_url = reverse_lazy('list-number-tapes')



class List_number_tapes_view(CustomNumberTapesMixin, ListView):
    template_name = 'main/shlifovka/number_tapes.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Шлифовальные ленты'}


class Create_number_tapes_view(LoginRequiredMixin, CustomSuccessMessageMixin,
                                  CustomFormValidMixin, CustomNumberTapesMixin, CreateView):

    form_class = Number_tapes_form
    template_name = 'main/shlifovka/create_new_number_tapes.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Шлифовальные ленты'}


    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Number_tapes_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_number_tapes_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomNumberTapesMixin, CustomGetFormUpdateMixin, UpdateView):

    form_class = Number_tapes_form
    template_name = 'main/shlifovka/create_new_number_tapes.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений пробега лент'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        context['menu'] = menu
        context['url'] = 'list-number-tapes'
        return context


        # context = super(BookListView, self).get_context_data(**kwargs)
        # # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        # context['some_data'] = 'This is just some data'
        # return context

class Delete_number_tapes_view(LoginRequiredMixin, CustomPostDeleteMixin, CustomNumberTapesMixin, DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-number-tapes'
        return context


""" Начало {'title_place': "Распиловка",'name_form':'Лабораторные образцы', 'url_name': 'list-lab-board'}"""


class CustomLabBoardMixin:
    model = Lab_board_model
    success_url = reverse_lazy('list-lab-board')


class List_lab_board_view(CustomLabBoardMixin, ListView):
    template_name = 'main/raspilovka/list_lab_board.html'
    context_object_name = 'list_value'
    extra_context = {'title': 'Лабораторные образцы'}


class Create_lab_board_view(LoginRequiredMixin, CustomSuccessMessageMixin,
                                  CustomFormValidMixin, CustomLabBoardMixin, CreateView):

    form_class = Lab_board_form
    template_name = 'main/raspilovka/create_new_lab_board.html'
    success_msg = 'Запись создана'
    extra_context = {'title':'Шлифовальные ленты'}


    def get_context_data(self, **kwargs):
        kwargs['list_articles'] = Lab_board_model.objects.all().order_by('-date_created')
        return super().get_context_data(**kwargs)


class Update_lab_board_view(LoginRequiredMixin, CustomSuccessMessageMixin, CustomFormValidMixin,
                                  CustomLabBoardMixin, CustomGetFormUpdateMixin, UpdateView):

    form_class = Lab_board_form
    template_name = 'main/raspilovka/create_new_lab_board.html'
    success_msg = 'Запись успешно обнавлена'
    extra_context = {'title': 'Изменение значений о лабораторном образце'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        context['menu'] = menu
        context['url'] = 'list-lab-board'
        return context


class Delete_lab_board_view(LoginRequiredMixin, CustomPostDeleteMixin, CustomLabBoardMixin, DeleteView):
    template_name = 'main/delete.html'
    success_msg = 'Запись удалена'
    extra_context = {'title': 'Форма для удаления записи лабораторного образца'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'list-lab-board'
        return context


"""" Конец {'title_place': "Распиловка",'name_form':'Лабораторные образцы', 'url_name': 'list-lab-board'} """




"""" Конец {'title_place': "Шлифовка",'name_form':'Учёт шлифовальных лент', 'url_name': 'number-tapes'} """
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