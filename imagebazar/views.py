from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import *


def show_about_page(request):
    return render(request, "about.html", {})


def show_home_page(request):
    images = Image.objects.all()
    cats = Category.objects.all()
    data = {
        'images': images,
        'cats': cats
    }
    return render(request, "home.html", data)


def show_category_page(request, cid):
    cat = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=cat)
    cats = Category.objects.all()
    data = {
        'images': images,
        'cats': cats,
        'catId': cid
    }
    return render(request, "home.html", data)
