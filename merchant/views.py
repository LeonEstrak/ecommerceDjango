from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Item


class IndexView(generic.ListView):
    template_name = "merchant/index.html"
    context_object_name = "latest_item_list"

    def get_queryset(self):
        return Item.objects.order_by("entry_dateTime")


class DetailView(generic.DetailView):
    model = Item
    template_name = "merchant/itemDetails.html"


class CreateItemView(generic.CreateView):
    template_name = "merchant/addItem.html"
    model = Item
    fields = [
        "item_name",
        "item_price",
        "item_can_be_seen",
        "item_type",
        "item_profit_percentage",
        "item_image",
    ]


class UpdateItemView(generic.UpdateView):
    template_name = "merchant/addItem.html"
    model = Item
    fields = [
        "item_name",
        "item_price",
        "item_can_be_seen",
        "item_type",
        "item_profit_percentage",
        "item_image",
    ]


class DeleteItemView(generic.DeleteView):
    template_name = "merchant/deleteItem.html"
    model = Item
    success_url = reverse_lazy("merchant:index")
