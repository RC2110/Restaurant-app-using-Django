from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('item/<int:pk>', views.MenuItemDetail.as_view(), name='detail') # <int:pk> to avaid pk error for dynamic urls.
]
