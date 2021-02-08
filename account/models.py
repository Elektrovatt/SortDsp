from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


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