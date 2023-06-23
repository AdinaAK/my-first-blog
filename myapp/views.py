from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.fields import json
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from .models import DrugList

def indexx(request):
    drugs = DrugList.objects.all()
    return render(request, 'indexx.html', {"drugs": drugs})

def create(request):
    if request.method == "POST":
        drugscr = DrugList()
        drugscr.que1 = request.POST.get("que1")
        drugscr.que2 = request.POST.get("que2")
        drugscr.que3 = request.POST.get("que3")
        drugscr.que4 = request.POST.get("que4")
        drugscr.que5 = request.POST.get("que5")
        drugscr.que6 = request.POST.get("que6")
        drugscr.que7 = request.POST.get("que7")
        drugscr.save()
        return HttpResponseRedirect("/drugs")


def edit(request, id):
    try:
        drugscr = DrugList.objects.get(id=id)

        if request.method == "POST":
            drugscr.que1 = request.POST.get("que1")
            drugscr.que2 = request.POST.get("que2")
            drugscr.que3 = request.POST.get("que3")
            drugscr.que4 = request.POST.get("que4")
            drugscr.que5 = request.POST.get("que5")
            drugscr.que6 = request.POST.get("que6")
            drugscr.que7 = request.POST.get("que7")
            drugscr.save()
            return HttpResponseRedirect("/drugs")
        else:
            return render(request, "edit.html", {"drugscr": drugscr})
    except DrugList.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        drugscr = DrugList.objects.get(id=id)
        drugscr.delete()
        return HttpResponseRedirect("/drugs")
    except DrugList.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")



@login_required(login_url='login')
def HomePage(request):
    return render(request, 'sidebar.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('User or Password is incorrect!')
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def AboutPage(request):
    return render(request, 'about.html')

def AccountPage(request):
    return render(request, 'account.html')


from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Events


# Create your views here.
def index(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, 'calendar.html', context)


def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)



def calculator(request):
    return render(request, 'calculator.html')

