from django.shortcuts import render, redirect
from webAdmin.models import Goods

def index(request):
    allGoods = Goods.objects.all()
    context = {
        'title_head':'Home',
        'allGoods':allGoods,
    }
    
    return render(request, 'index.html', context)

def detailGoods(request, slugify):
    goods = Goods.objects.get(slugifyGoods = slugify)

    context = {
        'goods':goods
    }

    return render(request, "detailGoods.html", context)