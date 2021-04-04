from django.db import models
from django.contrib.auth.models import AbstractUser, User

from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class ProfileUserModel(models.Model):
    """"Модель профиля пользователя"""""
    area = (
        ('Шлифовка', 'Шлифовка'),
        ('Распиловка', 'Распиловка'),
        ('Пресс', 'Пресс'),
        ('Формовка', 'Формовка'),
        ('Клееварка', 'Клееварка'),
        ('Сушилка', 'Сушилка'),
        ('Стружечное', 'Стружечное'),
        ('Заточка', 'Заточка'),
        ('Дробилка', 'Дробилка'),
    )
    number_shift = (

        ('Смена 1', 'Смена 1'),
        ('Смена 2', 'Смена 2'),
        ('Смена 3', 'Смена 3'),
        ('Смена 4', 'Смена 4'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Владелец записи, пользователь")
    name_form1 = models.BooleanField("Толщина Шлифованой плиты", default=False, help_text='Участок - Шлифовка')
    name_form2 = models.BooleanField("Учёт шлифовальных материалов", default=False, help_text='Участок - Шлифовка')
    name_form3 = models.BooleanField("Толщина пакета шлифованной плиты", default=False, help_text='Участок - Шлифовка')
    name_form4 = models.BooleanField("Толщина пакета нешлифованой плиты", default=False, help_text='Участок - Распиловка')
    name_form5 = models.BooleanField("Измерение покоробленности", default=False, help_text='Участок - Распиловка')
    name_form6 = models.BooleanField("Учёт замены чернильной системы", default=False, help_text='Участок - Распиловка')
    name_form7 = models.BooleanField("Производственные параметры для пресовщика", default=False, help_text='Участок - Пресс')
    name_form8 = models.BooleanField("Расход природного газа и древесной пыли", default=False, help_text='Участок - Пресс')
    name_form9 = models.BooleanField("Толщина нешлифованой плиты", default=False, help_text='Участок - Пресс')
    name_form10 = models.BooleanField("Форма очистки лент преса", default=False, help_text='Участок - Пресс')
    name_form11 = models.BooleanField("Форма контроля рабочего состояния форсунок САП", default=False, help_text='Участок - Пресс')
    value2 = models.CharField(choices=number_shift, max_length=50, null=True, verbose_name='смена №')
    value3 = models.CharField(choices=area, max_length=500, null=True, verbose_name='Участок', help_text='дробилка, стружка. заточка, сушилка, клееварка, формовка, пресс, распиловка, шлифовка')


    def __str__(self):
        return ('автор  %s, смена : %s. участок : %s.' % (self.user, self.value2, self.value3))

    # def get_absolute_url(self):
    #     return f'/profile/{self.pk}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.user.id})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили для выбора Форм'
        ordering = ('-value2',)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """"создание профиля пользователя при регистрации"""""
    if created:
        ProfileUserModel.objects.create(user=instance, id=instance.id)


class Add_new_worker_shift(models.Model):
    #Добавить оператором ФИО нач. смены, оператора, водителя.
    Role = (
        ('Начальник смены','Начальник смены'),
        ('Оператор','Оператор'),
        ('Водитель','Водитель'),
        )
    fio = models.CharField(max_length=200, null=True)
    role_choices = models.CharField(max_length=200, null=True, choices=Role)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Добавить ФИО нач. смены, оперора, водителя'
        verbose_name_plural = 'Добавить ФИО оператором'