import django_filters
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from account.models import ProfileUserModel


class Thickness_board_model(models.Model):
    # from main.models import Thickness_board_model импорт для shell

    #добавить 8  измерений шлифованной плиты
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    # number_shift = models.ForeignKey(ProfileUserModel, on_delete=models.PROTECT, null=True, verbose_name='Номер смены')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # date_update=models.DateTimeField(auto_now=True, verbose_name='Дата Обновления')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')

    def __str__(self):
        return ('Смена №# %s, плита: %s, дата: %s. %s-%s-%s-%s-%s-%s-%s-%s' %(self.author, self.value0, self.date_created,
            self.value1,self.value2,self.value3,self.value4,self.value5,self.value6,self.value7,self.value8 ))

    def get_absolute_url(self):
         return f'/board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Толщина шлифованной плиты'
            ordering = ('-date_created',)


class Thickness_pack_board_model(models.Model):
    #добавить 22  измеренияпачки
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')
    value9 = models.CharField(max_length=5, null=True, verbose_name='Значение 9')
    value10 = models.CharField(max_length=5, null=True, verbose_name='Значение 10')
    value11 = models.CharField(max_length=5, null=True, verbose_name='Значение 11')
    value12 = models.CharField(max_length=5, null=True, verbose_name='Значение 12')
    value13 = models.CharField(max_length=5, null=True, verbose_name='Значение 13')
    value14 = models.CharField(max_length=5, null=True, verbose_name='Значение 14')
    value15 = models.CharField(max_length=5, null=True, verbose_name='Значение 15')
    value16 = models.CharField(max_length=5, null=True, verbose_name='Значение 16')
    value17 = models.CharField(max_length=5, null=True, verbose_name='Значение 17')
    value18 = models.CharField(max_length=5, null=True, verbose_name='Значение 18')
    value19 = models.CharField(max_length=5, null=True, verbose_name='Значение 19')
    value20 = models.CharField(max_length=5, null=True, verbose_name='Значение 20')
    value21 = models.CharField(max_length=5, null=True, verbose_name='Значение 21')
    value22 = models.CharField(max_length=5, null=True, verbose_name='Значение 22')

    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-pack-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Толщина шлифованной пачки'
            ordering = ('-date_created',)


class Thickness_unpolished_pack_board_model(models.Model):
    #добавить 22  измеренияпачки
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')
    value6 = models.CharField(max_length=5, null=True, verbose_name='Значение 6')
    value7 = models.CharField(max_length=5, null=True, verbose_name='Значение 7')
    value8 = models.CharField(max_length=5, null=True, verbose_name='Значение 8')
    value9 = models.CharField(max_length=5, null=True, verbose_name='Значение 9')
    value10 = models.CharField(max_length=5, null=True, verbose_name='Значение 10')
    value11 = models.CharField(max_length=5, null=True, verbose_name='Значение 11')
    value12 = models.CharField(max_length=5, null=True, verbose_name='Значение 12')
    value13 = models.CharField(max_length=5, null=True, verbose_name='Значение 13')
    value14 = models.CharField(max_length=5, null=True, verbose_name='Значение 14')
    value15 = models.CharField(max_length=5, null=True, verbose_name='Значение 15')
    value16 = models.CharField(max_length=5, null=True, verbose_name='Значение 16')
    value17 = models.CharField(max_length=5, null=True, verbose_name='Значение 17')
    value18 = models.CharField(max_length=5, null=True, verbose_name='Значение 18')
    value19 = models.CharField(max_length=5, null=True, verbose_name='Значение 19')
    value20 = models.CharField(max_length=5, null=True, verbose_name='Значение 20')
    value21 = models.CharField(max_length=5, null=True, verbose_name='Значение 21')
    value22 = models.CharField(max_length=5, null=True, verbose_name='Значение 22')

    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-unpolished-pack-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Распиловка - Толщина не шлифованой пачки'
            ordering = ('-date_created',)


class Thickness_unpolished_board_model(models.Model):
    #добавить 8  измерений нешлифованной плиты
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    value0 = models.CharField(max_length=2, null=True, verbose_name='Толщина плиты')
    value1 = models.CharField(max_length=5, null=True, verbose_name='Значение 1')
    value2 = models.CharField(max_length=5, null=True, verbose_name='Значение 2')
    value3 = models.CharField(max_length=5, null=True, verbose_name='Значение 3')
    value4 = models.CharField(max_length=5, null=True, verbose_name='Значение 4')
    value5 = models.CharField(max_length=5, null=True, verbose_name='Значение 5')


    def __str__(self):
        return ('Смена № %s, плита: %s, дата: %s.' %(self.author, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/thickness-unpolished-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Пресс - Толщина нешлифованой плиты'
            ordering = ('-date_created',)

class Number_tapes_model(models.Model):
    "Учёт шлифовальных материалов"
    Agg1 = (
        ('', ''),
        ('P 50', 'P 50'),
        ('P 80', 'P 80'),
        ('P 120', 'P 120'),
    )
    Agg2 = (
        ('', ''),
        ('Foam', 'Foam'),
        ('Pes', 'Pes'),
    )
    Agg3 = (
        ('', ''),
        ('Combi', 'Combi'),
        ('Polyster', 'Polyster'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата замены лент')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    number_1_1_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg1, verbose_name='Лента 1.1')
    number_1_1_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 1.1')
    value0 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 1.1')

    number_1_2_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg1,
                                          verbose_name='Лента 1.2')
    number_1_2_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 1.2')
    value1 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 1.2')

    number_2_1_choices = models.CharField(max_length=20,blank=True, null=True, choices=Agg1, verbose_name='Лента 2.1')
    number_2_1_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.1')
    liner_2_1_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg2, verbose_name='Вставка 2.1')
    value2 = models.CharField(max_length=20,blank=True, null=True,  verbose_name='Пробег ленты Agg 2.1')

    number_2_2_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg1, verbose_name='Лента 2.2')
    number_2_2_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.2')
    liner_2_2_choices = models.CharField(max_length=20,  blank=True, null=True,choices=Agg2, verbose_name='Вставка 2.2')
    value3 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 2.2')

    number_2_3_choices = models.CharField(max_length=20,  blank=True, null=True,choices=Agg1, verbose_name='Лента 2.3')
    number_2_3_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.3')
    liner_2_3_choices = models.CharField(max_length=20, blank=True, null=True,choices=Agg2, verbose_name='Вставка 2.3')
    value4 = models.CharField(max_length=20,blank=True, null=True,  verbose_name='Пробег ленты Agg 2.3')

    number_2_4_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg1, verbose_name='Лента 2.4')
    number_2_4_choices2 = models.CharField(max_length=20, blank=True, null=True, choices=Agg3,
                                           verbose_name='Тип ленты 2.4')
    liner_2_4_choices = models.CharField(max_length=20, blank=True, null=True, choices=Agg2, verbose_name='Вставка 2.4')
    value5 = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пробег ленты Agg 2.4')



    def __str__(self):
        return ('Смена № %s, дата: %s.' %(self.author, self.date_created))

    def get_absolute_url(self):
         return f'/number-tapes-liner/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Шлифвока - Учёт шлифовальных лент'
            ordering = ('-date_created',)


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Number_tapes_model
        fields = ['date_created']



class Lab_board_model(models.Model):
    """добавить лабораторную плиту"""
    Number_shift = (
        ('', ''),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец записи", blank=True, null=True)
    date_created = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата производства' )
    number_shift = models.CharField(max_length=1, choices=Number_shift, verbose_name='Смена (производства)№')
    number_path = models.CharField(max_length=1,choices=Number_shift, verbose_name='Номер партии')
    value0 = models.CharField(max_length=4,  verbose_name='Заказ')
    value1 = models.CharField(max_length=2, verbose_name='Толщина, мм')
    value2 = models.CharField(max_length=4, null=True, verbose_name='Длина, мм')
    value3 = models.CharField(max_length=1, null=True, verbose_name='Количество, шт.')
    value4 = models.CharField(max_length=30, null=True,blank=True, verbose_name='Комментарий')



    def __str__(self):
        return ('Смена производства № %s, заказ - %s, плита: %s - %s, дата производства: %s.'
                %(self.number_shift, self.value1,self.value1,self.value2, self.date_created))

    def get_absolute_url(self):
         return f'/lab-board/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Распиловка - Лабораторные образцы'
            ordering = ('-date_created',)