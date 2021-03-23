from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from account.models import ProfileUserModel


class table_thickness_ground_plate_model(models.Model):
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
        return ('Смена № %s, плита: %s, дата: %s.' %(self.number_shift, self.value0, self.date_created))

    def get_absolute_url(self):
         return f'/plate/{self.pk}'

    class Meta:
            verbose_name = 'поля'
            verbose_name_plural = 'Толщина плиты'
            ordering = ('-date_created',)

