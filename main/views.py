from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import ItemModel, TagModel


def index(request):
    turn_on_block = True
    return render(request, 'main/index.html', {'turn_on_block': turn_on_block})


class ItemListView(ListView):
    model = ItemModel
    paginate_by = 5

    def get_queryset(self):
        try:
            tag = get_object_or_404(TagModel, tag=self.kwargs['tag_name'])
            return ItemModel.objects.filter(tag=tag.id)
        except KeyError as ex:
            return ItemModel.objects.filter(published=1)


class ItemDetailView(DetailView):
    model = ItemModel
