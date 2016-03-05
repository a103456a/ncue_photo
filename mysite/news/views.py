from django.shortcuts import render
from static.py.navbar_item import loadData


def home(request):
    return render(request, 'index.html', {
        'navItem': loadData()
    })
