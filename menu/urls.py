from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    # path('a/(?P<pk>\d+)/', views.MenuItemDetail.as_view(), name='detail')
]
