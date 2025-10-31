from django.urls import path
from . import views

app_name = 'xina'
urlpatterns = [
    path('', views.index, name='index'),  #Home
]