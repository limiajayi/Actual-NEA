from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #the url pointing to views.home which returns the home page
    path('login/', views.login, name='login'), #url pointing to login page
    path('signup/', views.signup, name='signup'), #url pointing to views.signup which returns the signup page
]
