"""testdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from myapp import views

urlpatterns = [
    path("drugs/", views.indexx, name='drugs'),
    path("drugs/create/", views.create),
    path("drugs/edit/<int:id>/", views.edit),
    path("drugs/delete/<int:id>/", views.delete),
    path("admin/", admin.site.urls),
    path("home/", views.HomePage, name='home'),
    path("", views.LoginPage, name='login'),
    path("logout/", views.LogoutPage, name='logout'),
    path("about/", views.AboutPage, name='about'),
    path("account/", views.AccountPage, name='account'),
    path("signup/", views.SignupPage, name='signup'),
    path("calendar/", views.index, name='calendar'),
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('calculator/', views.calculator, name='calculator')



]