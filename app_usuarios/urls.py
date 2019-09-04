from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),    
    path('home_user/', views.home_user, name='home_user'),
    path('register/', views.register, name='register'),

]
