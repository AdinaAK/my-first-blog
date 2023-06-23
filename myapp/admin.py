from django.contrib import admin

# Register your models here.
from .models import DrugList, Events



admin.site.register(DrugList)
admin.site.register(Events)
