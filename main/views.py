from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ItemModel


def index(request):
    turn_on_block = True
    return render(request, 'main/index.html', {'turn_on_block': turn_on_block})


class ItemListView(ListView):
    model = ItemModel
    queryset = ItemModel.objects.all().filter(published=1)


class ItemDetailView(DetailView):
    model = ItemModel
