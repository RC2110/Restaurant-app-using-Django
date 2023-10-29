from django.contrib import admin
from .models import MenuApp

class FoodappAdmin(admin.ModelAdmin):
    list_display = ("menu", "description", "price")
    list_filter = ("status", "price")
    search_fields = ("menu", "description")

admin.site.register(MenuApp, FoodappAdmin)
