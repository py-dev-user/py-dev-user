from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    turn_on_block = True
    return render(request, 'main/index.html', {'turn_on_block': turn_on_block})
