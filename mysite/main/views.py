from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/base.html', {'title': 'Главная'})

def about(request):
    return render(request, 'main/about.html')


def categories(request):
    pass

def contacts(request):
    pass
