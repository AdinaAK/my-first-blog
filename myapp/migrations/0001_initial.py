# Generated by Django 4.1.7 on 2023-05-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que1', models.CharField(max_length=200, null=True, verbose_name='Медикамент: ')),
                ('que2', models.CharField(max_length=200, null=True, verbose_name='Исходная дозировка препарата: ')),
                ('que3', models.CharField(max_length=200, null=True, verbose_name='Способ введения: ')),
                ('que4', models.DateField(verbose_name='Дата начала приема: ')),
                ('que5', models.TimeField(verbose_name='Время приёма: ')),
                ('que6', models.IntegerField(null=1, verbose_name='На сколько дней назначено: ')),
                ('que7', models.CharField(max_length=200, null=True, verbose_name='Комментарий: ')),
            ],
        ),
    ]