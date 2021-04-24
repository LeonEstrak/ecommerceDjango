from django.shortcuts import render
from django.views import generic
from .models import Item


class IndexView(generic.ListView):
    template_name = "merchant/index.html"
    context_object_name = "latest_item_list"

    def get_queryset(self):
        return Item.objects.order_by("entry_dateTime")


class DetailView(generic.DetailView):
    model = Item
    template_name = "merchant/itemDetails.html"