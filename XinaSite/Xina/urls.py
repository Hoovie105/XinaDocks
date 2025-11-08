from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'xina'
urlpatterns = [
    path('', views.index, name='index'),  #Home
    path('login/', views.LoginPage, name='login'),  #signin Page
    path('signup/', views.SignUpPage, name='signup'),  #Signup Page
    path('logout/', views.logoutUser, name='logout'),  #Logout Page
    path('main/', views.mainPage, name='main'),  #Main Page
    path('Create/', views.Create, name='Create'),  #C
    path('read/<int:doc_id>/', views.read, name='read'),   #R
    path('update/<int:doc_id>/', views.update, name='update'),  #U
    path('delete/<int:doc_id>/', views.delete, name='delete'),  #D
    path('attachment/delete/<int:attachment_id>/', views.delete_attachment, name='delete_attachment'), # Delete Attachment
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)