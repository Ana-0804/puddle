from django.shortcuts import render
from django.contrib import admin

from items.models import Category, Item

def index (request):
    item = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html',{
        "categories": categories,
        "items" : Item,
    })

def contact(request):
    return render(request, 'core/contact.html')

