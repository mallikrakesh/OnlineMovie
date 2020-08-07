from django.shortcuts import render,redirect
import http.client
from django.contrib import messages
import json
from OnlineMovie.settings import onlinemovie_file
from App1.models import *
from App1.forms import *


# Create your views here.

def movieAdminLogin(request):
    return render(request,'adminlogin.html')

def movieAdminLoginPage(request):
    uname=request.POST.get('un')
    password=request.POST.get('pa')
    if uname == 'admin' and password == 'admin':
        return render(request,'admin_page.html')
    else:
        messages.error(request,'Invalid User')
        return redirect('admin_login')

def admin_home(request):
    return render(request, 'admin_page.html')

def add_movie(request):
    dict_data=json.loads(open("App1/raw/movies.json").read())
    # print(dict_data)
    movies_data=[x for x in dict_data['d']]
    print(movies_data)
    return render(request,'add_movie.html',{'data':movies_data})


def save_movie(request):
    data=request.GET.get('mdata')
    a = data.split(',')
    x = a[0]
    y = a[1]
    z = a[2]
    b = a[3]
    c = a[5]
    MovieAdmin(moviename=x, t_ype=y, rank=z, casting=b, release=c).save()
    messages.success(request,'Add Movie Successfully')
    return redirect("add_movie")


def view_movie(request):
    return render(request,'view_movie.html',{'data':MovieAdmin.objects.all()})


def delete_movie(request):
    mno=request.GET.get('no')
    MovieAdmin.objects.get(id=mno).delete()
    return redirect('add_movie')

#Customer Operation

def showIndex(request):
    return render(request,'index.html')


def loginPage(request):
    return render(request,'login_page.html',{'lf':LoginForm()})


def create_customer_account(request):
    return render(request,'create_account.html',{'cf':CustomerForm()})


def save_customer(request):
    un=request.POST.get('email')
    pa=request.POST.get('password')
    cf=CustomerForm(request.POST)
    if cf.is_valid():
        cf.save()
        LoginModel(email=un,password=pa).save()
        messages.success(request,'Registration Successful')
        return redirect('create_customer_account')
    else:
        return render(request, 'create_account.html', {'cf': CustomerForm()})


def login_customer(request):
    un = request.POST.get('email')
    pa = request.POST.get('password')
    try:
        LoginModel.objects.get(email=un,password=pa)
        return render(request,'customer_login.html',{'data':MovieAdmin.objects.all()})
    except LoginModel.DoesNotExist:
        messages.error(request,'Invalid Details')
        return redirect('login_page')


def searchaction(request):
    n = request.POST.get("s1")
    try:
        MovieAdmin.objects.get(moviename=n)
        a = MovieAdmin.objects.values('moviename')
        print(a)
        return render(request, "searchpage.html", {"data": a})
    except MovieAdmin.DoesNotExist:
        messages.error(request, "Not Found")
        return render(request, "searchpage.html")