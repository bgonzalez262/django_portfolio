from django.urls import path
from . import views

app_name = 'drinks'
urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/', views.name_search, name='search')
]