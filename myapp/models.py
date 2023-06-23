from django.db import models


# Create your models here

class DrugList(models.Model):
    que1 = models.CharField(max_length=200, null=True, verbose_name='Медикамент: ')
    que2 = models.CharField(max_length=200, null=True, verbose_name='Исходная дозировка препарата: ')
    que3 = models.CharField(max_length=200, null=True, verbose_name='Способ введения: ')
    que4 = models.DateField(verbose_name='Дата начала приема: ')
    que5 = models.TimeField(verbose_name='Время приёма: ')
    que6 = models.IntegerField(null=1, verbose_name='На сколько дней назначено: ')
    que7 = models.CharField(max_length=200, null=True, verbose_name='Комментарий: ')
    objects = models.Manager()
    DoesNotExist = models.Manager

    def __repr__(self):
        return DrugList


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tblevents"




