from django.urls import path
from . import views

app_name = 'xina'
urlpatterns = [
    path('', views.index, name='index'),  #Home
    path('login/', views.LoginPage, name='login'),  #signin Page
    path('signup/', views.SignUpPage, name='signup'),  #Signup Page
    path('logout/', views.logoutUser, name='logout'),  #Logout Page
    path('main/', views.mainPage, name='main'),  #Main Page
]