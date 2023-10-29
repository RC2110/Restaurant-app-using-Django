from django.shortcuts import render
from django.views import generic
from .models import MenuApp, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = MenuApp.objects.order_by("date_added")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context
class MenuItemDetail(generic.DetailView):
    model = MenuApp
    template_name = "detail.html"




