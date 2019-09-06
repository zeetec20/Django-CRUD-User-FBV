from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from .models import Goods
from .forms import (
    GoodsForm, 
    RegisterForm
) 

def index(request):
    context = {
        'title_head':'Admin',
    }

    return render(request, 'webAdmin/index.html', context)

def user(request):
    
    if user.is_authenticated:
        userStatus = 'login'
    else:
        userStatus = 'logout'    

    context = {
        'title_head':userStauserStatustus,
    }

    return render(request, 'webAdmin/user.html', context)

def login(request):
    context = {
        'message':'a'
    }

    if request.method == "POST":
        username_user = request.POST['username'];
        password_user = request.POST['password'];

        user = authenticate(request, username = username_user, password = password_user)

        print(user)
        if user is not None :
            dj_login(request, user)
            return redirect('index')
        else:
            return redirect('/webAdmin/login/?message')

    if "message" in request.GET:
        context['message'] = "Username atau Password anda salah"

    return render(request, 'webAdmin/login.html', context)  

def register(request):
    registerform = RegisterForm(request.POST or None)

    context = {
        'registerform':registerform
    }

    if request.method == "POST":
        if registerform.is_valid():
            print(registerform.cleaned_data)
            uname = registerform.cleaned_data['username']
            upass = registerform.cleaned_data['password']
            uemail = registerform.cleaned_data['email']
            User.objects.create_user(username = uname, password = upass, email = uemail)
            getUser = User.objects.get(username = uname)
            getUser.first_name = registerform.cleaned_data['firstname']
            getUser.last_name = registerform.cleaned_data['lastname']
            getUser.save()
            return redirect('index')

    return render(request, 'webAdmin/register.html', context)
    
def logout(request):
    dj_logout(request)

    if request.user.is_authenticated:
        pass
    else:
        return redirect('index')

    return render(request, 'webAdmin/logout.html')

def createGoods(request):
    goods = GoodsForm(request.POST, request.FILES or None)
    
    context = {
        'title_haed':'Create Goods',
        'title_page':'Memasukkan Barang Jual',
        'goods':goods,
    }

    if request.method == "POST":
        goods.save()
        if goods.is_valid():
            goods.save()
            return redirect('index')
        

    return render(request, 'webAdmin/createGoods.html', context)
    
def updateGoods(request, dynamicID):
    
    goods = Goods.objects.get(id = dynamicID)

    valueGoods = {
        'nameGoods' : goods.nameGoods,
        'decriptionGoods' : goods.descriptionGoods,
        'typeGoods' : goods.typeGoods,
        'conditionGoods' : goods.conditionGoods,
        'priceGoods' : goods.priceGoods,
        'imagesGoods' : goods.imagesGoods
    }
    
    goodsForm = GoodsForm(request.POST, initial=valueGoods, instance=goods)

    if request.method == "GET":
        goodsForm = GoodsForm(initial=valueGoods, instance=goods)
        context = {
            'title_head' : 'Update Barang',
            'goods' : goodsForm,
        }

    if request.method == "POST":
        goodsForm = GoodsForm(request.POST, request.FILES, instance=goods)
        context = {
            'title_head' : 'Update Barang',
            'goods' : goodsForm,
        }
        if goodsForm.is_valid():
            goodsForm.save()
            return redirect('index')

    return render(request, 'webAdmin/updateGoods.html', context)

def deleteGoods(request, dynamicID):
    goodsAll = Goods.objects.values_list()
    goods = Goods.objects.get(id = dynamicID)
    goods.delete()
    goodsID = []
    for a in goodsAll:
        goodsID.append(a[0])
    
    if dynamicID not in goodsID:
        return redirect(index)
    
    return render(request, 'webAdmin/createGoods.html')